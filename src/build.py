#!/usr/bin/env python3
"""Builds the whole site into ../docs (or the folder given as the first argument).

Usage (from the repository root):  python3 src/build.py
Needs: Python 3.9+, and the packages `markdown` and `segno` (pip install markdown segno).
"""
import html, json, os, re, shutil, sys
import markdown
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docqa_tr import DOCQA_TR
from summaries import SUM
from sharh import SHARH, GLOSS, GLOSS_TR_SRC, BOOK
import sozluk, gate
import io, segno
SITE = 'https://tevhidim.com/'

ROOT = os.path.dirname(os.path.abspath(__file__))           # src/
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, '..', 'docs')
DECKS = f'{ROOT}/decks'
E = html.escape

# ------------------------------------------------------------------ data
POINTS = {'ar': ['الاعتقاد', 'الترك', 'البغض', 'التكفير', 'المعاداة'],
          'tr': ['İtikad', 'Terk', 'Buğz', 'Tekfir', 'Düşmanlık']}
ORD = {'ar': ['الأولى', 'الثانية', 'الثالثة', 'الرابعة', 'الخامسة'],
       'tr': ['Birinci', 'İkinci', 'Üçüncü', 'Dördüncü', 'Beşinci']}
LESSONS = [
    dict(n=1, live=True,
         ar='اعتقاد بطلان عبادة الطاغوت', tr='Tâğuta İbadetin Bâtıl Olduğuna İtikad',
         descAr='معنى الاعتقاد، والفرق بينه وبين المعرفة والقول والظن، ثم حقيقته وأدلته من الكتاب والسنة.',
         descTr='İtikadın anlamı; bilgi, söz ve zan ile farkı; hakikati ve Kitap ile Sünnet’ten delilleri.',
         verse='﴿فَمَنْ يَكْفُرْ بِالطَّاغُوتِ وَيُؤْمِنْ بِاللَّهِ فَقَدِ اسْتَمْسَكَ بِالْعُرْوَةِ الْوُثْقَى﴾',
         ref='البقرة: 256',
         verseTr='«Kim tâğutu inkâr edip Allah’a iman ederse, kopmayan sağlam bir kulpa yapışmıştır.» (Bakara, 256)',
         video='lesson1.mp4', videoTr='lesson1-tr.mp4', poster='poster1.jpg', posterTr='poster1-tr.jpg',
         sumAr='summary1-ar.jpg', sumTr='summary1-tr.jpg', deckAr='ar1', deckTr='tr1'),
    dict(n=2, live=True,
         ar='ترك عبادة الطاغوت', tr='Tâğuta İbadeti Terk Etmek',
         descAr='معنى الترك والاجتناب، وصور الترك وعلاقته بالاعتقاد، والفرق بين العبادة وما ليس عبادة، ثم الأدلة من الكتاب والسنة.',
         descTr='Terk ve ictinabın anlamı; terkin şekilleri ve itikadla ilişkisi; ibadet ile ibadet olmayanın farkı; ardından Kitap ve Sünnet’ten deliller.',
         verse='﴿وَالَّذِينَ اجْتَنَبُوا الطَّاغُوتَ أَنْ يَعْبُدُوهَا وَأَنَابُوا إِلَى اللَّهِ لَهُمُ الْبُشْرَىٰ﴾',
         ref='الزمر: 17',
         verseTr='«Tâğuta ibadet etmekten kaçınıp Allah’a yönelenlere müjde vardır.» (Zümer, 17)',
         video='lesson2.mp4', videoTr='lesson2-tr.mp4', poster='', posterTr='',
         sumAr='', sumTr='', deckAr='ar2', deckTr='tr2'),
    dict(n=3, live=True,
         ar='بغض الطاغوت وعبادته وأهله', tr='Tâğuta, İbadetine ve Ehline Buğz',
         descAr='معنى البغض، وما يتعلق به: عبادة غير الله والطاغوت وأهلها، وصوره، وعلاقته بالاعتقاد والترك، ثم الأدلة من الكتاب والسنة.',
         descTr='Buğzun anlamı; ilgili olduğu şeyler: Allah’tan başkasına ibadet, tâğut ve ehli; şekilleri, itikad ve terk ile ilişkisi; ardından Kitap ve Sünnet’ten deliller.',
         verse='﴿وَلَكِنَّ اللَّهَ حَبَّبَ إِلَيْكُمُ الْإِيمَانَ وَزَيَّنَهُ فِي قُلُوبِكُمْ وَكَرَّهَ إِلَيْكُمُ الْكُفْرَ وَالْفُسُوقَ وَالْعِصْيَانَ﴾',
         ref='الحجرات: 7',
         verseTr='«Fakat Allah size imanı sevdirdi, onu kalplerinizde süsledi; küfrü, fıskı ve isyanı size çirkin gösterdi.» (Hucurât, 7)',
         video='lesson3.mp4', videoTr='lesson3-tr.mp4', poster='', posterTr='',
         sumAr='', sumTr='', deckAr='ar3', deckTr='tr3'),
    dict(n=4, live=False, ar='تكفير أهلها', tr='Ehlini Tekfir Etmek'),
    dict(n=5, live=False, ar='معاداتهم', tr='Onlara Düşmanlık Etmek'),
]
for _L in LESSONS: _L.update(slug=f"l{_L['n']}", num=_L['n'], doc=f"lesson{_L['n']}", sk='taghut')

# «الفقه الميسّر» · كتاب الطهارة: one lesson per chapter (باب) of the book. Pages f1/ … ; internal number 100 + chapter.
FIQH = [
    dict(n=101, num=1, slug='f1', doc='fiqh1', sk='tahara', live=True,
         ar='أحكام الطهارة والمياه', tr='Taharet ve Su Hükümleri',
         descAr='معنى الفقه، وأهمية الطهارة وقسماها وتعريفها، وبأي ماء تحصل، وحكم ما خالطته نجاسة أو طاهر، والماء المستعمل، والأسآر.',
         descTr='Fıkhın anlamı; taharetin önemi, kısımları ve tanımı; hangi suyla olduğu; necaset veya temiz madde karışan su, kullanılmış su ve artık su.',
         verse='﴿وَأَنْزَلْنَا مِنَ السَّمَاءِ مَاءً طَهُورًا﴾',
         ref='الفرقان: 48',
         verseTr='«Gökten tertemiz bir su indirdik.» (Furkân, 48)',
         video='fiqh1.mp4', videoTr='fiqh1-tr.mp4', poster='poster-f1.jpg', posterTr='poster-f1-tr.jpg',
         deckAr='far1', deckTr='ftr1'),
    dict(n=102, num=2, slug='f2', sk='tahara', live=False, ar='الآنية', tr='Kaplar'),
    dict(n=103, num=3, slug='f3', sk='tahara', live=False, ar='قضاء الحاجة وآدابها', tr='Def-i Hacet ve Âdâbı'),
    dict(n=104, num=4, slug='f4', sk='tahara', live=False, ar='السواك وسنن الفطرة', tr='Misvak ve Fıtrat Sünnetleri'),
    dict(n=105, num=5, slug='f5', sk='tahara', live=False, ar='الوضوء', tr='Abdest'),
]
LIVE = [l for l in LESSONS if l['live']]
FIQH_LIVE = [l for l in FIQH if l['live']]
ALL_LIVE = LIVE + FIQH_LIVE

# what a section says about itself: its points/chapters, how a lesson is placed in it, its lead and quote
SECT = {
 'taghut': {
  'ar': dict(points=POINTS['ar'], ord=ORD['ar'], point='النقطة', of='من صفة الكفر بالطاغوت', short='صفة الكفر بالطاغوت',
             lead='خمسة دروس في قول الشيخ محمد بن عبد الوهاب رحمه الله في صفة الكفر بالطاغوت. لكل درس: فيديو، ودرس مكتوب، وعرض شرائح، وخريطة تفاعلية، وأسئلة وأجوبة، واختبار لقياس الفهم.',
             quote='«أن تعتقد بطلان عبادة غير الله، وتتركها، وتبغضها، وتكفّر أهلها، وتعاديهم»',
             quoteRef='الشيخ محمد بن عبد الوهاب رحمه الله، رسالة «معنى الطاغوت ورؤوس أنواعه»',
             pointsT='النقاط الخمس', pointsS='كل نقطة درس مستقل، تُضاف تباعًا. والروابط تبقى صالحة لكل الدروس.'),
  'tr': dict(points=POINTS['tr'], ord=ORD['tr'], point='husus', of='· Tâğutu inkârın keyfiyeti', short='Tâğutu İnkârın Keyfiyeti',
             lead='Şeyh Muhammed b. Abdülvehhab’ın (rahimehullah) tâğutu inkârın keyfiyeti hakkındaki sözü üzerine beş ders. Her ders için: video, yazılı ders, sunum, etkileşimli harita, soru-cevap ve anladığını ölçen bir test.',
             quote='«Allah’tan başkasına yapılan ibadetin bâtıl olduğuna inanman, onu terk etmen, ondan buğz etmen, ehlini tekfir etmen ve onlara düşmanlık etmendir.»',
             quoteRef='Şeyh Muhammed b. Abdülvehhab, «Ma‘ne’t-Tâğût ve Ruûsu Envâih» risalesi',
             pointsT='Beş husus', pointsS='Her husus ayrı bir derstir ve sırayla eklenir. Bağlantılar bütün dersler için geçerli kalır.'),
 },
 'tahara': {
  'ar': dict(points=['الطهارة والمياه', 'الآنية', 'قضاء الحاجة وآدابها', 'السواك وسنن الفطرة', 'الوضوء'],
             ord=['الأول', 'الثاني', 'الثالث', 'الرابع', 'الخامس'], point='الباب', of='من كتاب الطهارة', short='كتاب الطهارة',
             lead='أبواب كتاب الطهارة من «الفقه الميسّر في ضوء الكتاب والسنة»، بابًا بابًا. لكل درس: فيديو، ودرس مكتوب، وعرض شرائح، وخريطة تفاعلية، وأسئلة وأجوبة، واختبار لقياس الفهم.',
             quote='«مِفْتَاحُ الصَّلَاةِ الطُّهُورُ»', quoteRef='رواه أبو داود والترمذي وابن ماجه',
             pointsT='أبواب كتاب الطهارة', pointsS='كل باب درس مستقل، تُضاف تباعًا. والروابط تبقى صالحة لكل الدروس.'),
  'tr': dict(points=['Taharet ve sular', 'Kaplar', 'Def-i hacet ve âdâbı', 'Misvak ve fıtrat sünnetleri', 'Abdest'],
             ord=['Birinci', 'İkinci', 'Üçüncü', 'Dördüncü', 'Beşinci'], point='bölüm', of='· Taharet Kitabı', short='Taharet Kitabı',
             lead='«el-Fıkhu’l-Müyesser fî Dav’i’l-Kitâb ve’s-Sünne» kitabından Taharet Kitabı’nın bölümleri, bölüm bölüm. Her ders için: video, yazılı ders, sunum, etkileşimli harita, soru-cevap ve anladığını ölçen bir test.',
             quote='«Namazın anahtarı temizliktir.»', quoteRef='Ebû Dâvûd, Tirmizî ve İbn Mâce rivayet etmiştir',
             pointsT='Taharet Kitabı’nın bölümleri', pointsS='Her bölüm ayrı bir derstir ve sırayla eklenir. Bağlantılar bütün dersler için geçerli kalır.'),
 },
}

S = {
 'ar': dict(
    brand='وتواصوا بالحق', series='سلسلة صفة الكفر بالطاغوت', seriesShort='صفة الكفر بالطاغوت',
    eb='وتواصوا بالحق · دروس شرعية بإعداد جديد',
    lead='خمسة دروس في قول الشيخ محمد بن عبد الوهاب رحمه الله في صفة الكفر بالطاغوت. لكل درس: فيديو، ودرس مكتوب، وعرض شرائح، وخريطة تفاعلية، وأسئلة وأجوبة، واختبار لقياس الفهم.',
    quote='«أن تعتقد بطلان عبادة غير الله، وتتركها، وتبغضها، وتكفّر أهلها، وتعاديهم»',
    quoteRef='الشيخ محمد بن عبد الوهاب رحمه الله، رسالة «معنى الطاغوت ورؤوس أنواعه»',
    home='الرئيسية', lessons='الدروس', lesson='الدرس', point='النقطة', of='من صفة الكفر بالطاغوت',
    pointsT='النقاط الخمس', pointsS='كل نقطة درس مستقل، تُضاف تباعًا. والروابط تبقى صالحة لكل الدروس.',
    latestT='أحدث درس', latestS='ابدأ بالفيديو أو الدرس المكتوب، ثم راجع بالشرائح والخريطة، واختم بالأسئلة والاختبار.',
    listT='دروس القسم', listS='اضغط على الدرس لتفتح صفحته وكل أدواته.',
    open='افتح الدرس', soon='قريبًا', live='متاح',
    tText=('الدرس المكتوب', 'الشرح كاملًا بأدلته، للقراءة والطباعة'),
    tSlides=('عرض الشرائح', 'بطاقات الدرس شريحةً شريحة'),
    tMap=('الخريطة التفاعلية', 'سِر في الدرس فرعًا فرعًا'),
    tQA=('أسئلة وأجوبة', 'أسئلة المراجعة مع أجوبتها'),
    tQuiz=('اختبر فهمك', 'اختبار باختيارات متعددة وتصحيح فوري'),
    doneWhat=dict(text='الدرس المكتوب', slides='الشرائح', map='الخريطة', qa='الأسئلة والأجوبة', quiz='الاختبار', lesson='هذا الدرس'),
    doneOff='أنهيتُ {x}', doneOn='✓ أنهيتَ {x}', doneUndo='اضغط مرة أخرى للتراجع', doneHint='عندما تنتهي من كل أدوات الدرس، اضغط هنا لتسجّل أنك أتممته.',
    progReset='مسح تقدّمي المحفوظ على هذا الجهاز', install='ثبّت الموقع على جوالك كتطبيق',
    iosT='تثبيت الموقع على الآيفون',
    iosIntro='على iPhone وiPad يتم التثبيت من Safari بثلاث خطوات:',
    ios1='اضغط زر المشاركة في شريط Safari.',
    ios2='انزل في القائمة واختر «إضافة إلى الشاشة الرئيسية».',
    ios3='اضغط «إضافة»، وستجد الموقع بأيقونته بين تطبيقاتك: يفتح بملء الشاشة ويعمل بلا إنترنت.',
    iosSafari='إن كان الموقع مفتوحًا في متصفح آخر فافتحه في Safari أولًا.',
    themeDark='الوضع الليلي', themeLight='الوضع النهاري',
    fsDown='تصغير الخط', fsUp='تكبير الخط', fsLabel='حجم الخط', tShare=('صورة للمشاركة', 'صورة الدرس لواتساب وتيليجرام، فيها رمز يفتحه'),
    tSum=('ملخص الدرس للطباعة', 'صفحة واحدة برمز QR يفتح الدرس'),
    tSharh=('متن الكتاب ومعاني كلماته', 'نص الكتاب فقرةً فقرة؛ اضغط على الكلمة يظهر معناها'),
    sharhSub='نص الكتاب بحروفه فقرةً فقرة، ومعاني كلماته الغريبة',
    sharhHint='الكلمات التي تحتها نقاط: اضغط عليها ليظهر معناها ومصدره.',
    glHint='الكلمات التي تحتها نقاط: اضغط عليها ليظهر معناها.',
    sharhSrc='النص من {b}؛ والرقم فوق كل فقرة: الجزء/ الصفحة.',
    sharhFn='حواشي الكتاب', sharhGl='معاني الكلمات', sharhGlSrc='المصدر', sharhLbl='الشرح', sharhTr='',
    chipSum='الملخص', sumPrint='اطبع', sumPdf='تنزيل PDF', sumImg='تنزيل صورة',
    sumHelp='مقاس A4. امسح الرمز بكاميرا الجوال لتفتح صفحة الدرس.',
    sumFootT='صفحة الدرس: الفيديو والدرس المكتوب والشرائح والخريطة والاختبار',
    sumFoot='امسح الرمز لتفتح صفحة الدرس وأدواته كلها:',
    tVideo=('فيديو الدرس', 'شاهد الدرس كاملًا'),
    chipText='المكتوب', chipSlides='الشرائح', chipMap='الخريطة', chipQA='سؤال وجواب', chipQuiz='الاختبار',
    toolsT='أدوات الدرس', pathT='طريقة المذاكرة المقترحة',
    path=['شاهد الفيديو أو اقرأ الدرس المكتوب.', 'راجع البطاقات والخريطة التفاعلية.', 'أجب عن أسئلة المراجعة قبل أن تكشف الجواب.', 'اختبر فهمك، ثم احفظ العبارة الجامعة.'],
    prev='الدرس السابق', next='الدرس التالي',
    noVideo='فيديو هذا الدرس يُضاف قريبًا',
    wipBadge='قيد الإعداد',
    wipNote='فيديو هذا الدرس قيد الإعداد، ويُضاف قريبًا إن شاء الله. وبقية الدرس جاهزة الآن، فابدأ بها:',
    tzSoon='التشويقة تُضاف قريبًا',
    tzT='دروسٌ أوضح، وأقرب، وأيسر', tzD='نرفع جودة دروسنا بتجهيزات جديدة تيسّر التعلّم. شاهد التشويقة القصيرة وشاركها.',
    foot='وتواصوا بالحق · نسأل الله العلم النافع والعمل الصالح.',
    sumNote='صورة الملخص للطباعة والمشاركة.', download='تنزيل الصورة',
    toc='محتويات الدرس', tocShow='محتويات الدرس',
    textSub='درس تفصيلي للطالب، بأدلته من الكتاب والسنة.',
    textEnd='بعد القراءة: راجع نفسك بالأسئلة والأجوبة، ثم اختبر فهمك.',
    qaT='أسئلة وأجوبة', qaS='فكّر في الجواب أولًا، ثم اضغط «أظهر الجواب» لتقارن.',
    qaHint='طريقة المراجعة: اقرأ السؤال، وأجب في نفسك أو بصوت مسموع، ثم اكشف الجواب. ومع «صح أو خطأ» علّل جوابك ولا تكتفِ بكلمة.',
    qaAll='أظهر كل الأجوبة', qaShow='أظهر الجواب', qaCount='{n} سؤالًا',
    qaG1='أسئلة المراجعة', qaG2='أسئلة الدرس المكتوب', qaExtra='سؤال إضافي', tf='صح أو خطأ',
    quizT='اختبر فهمك', quizS='اختر الجواب الصحيح، وستظهر لك العلّة بعد كل سؤال.',
    retry='أعد الاختبار', backLesson='رجوع إلى صفحة الدرس', toQA='راجع الأسئلة والأجوبة', wrongT='أسئلة تحتاج مراجعة',
    slidesT='عرض الشرائح', grid='كل الشرائح', fs='ملء الشاشة', prevS='السابق', nextS='التالي',
    rotate='أدر الهاتف أفقيًا لعرض أوضح',
    textOnlyAr='', mapLang='', skip='تخطَّ إلى المحتوى',
 ),
 'tr': dict(
    brand='Ve Tevâsav bi’l-Hak', series='Tâğutu İnkârın Keyfiyeti Serisi', seriesShort='Tâğutu inkârın keyfiyeti',
    eb='Ve Tevâsav bi’l-Hak · Yeni bir hazırlıkla şer’î dersler',
    lead='Şeyh Muhammed b. Abdülvehhab’ın (rahimehullah) tâğutu inkârın keyfiyeti hakkındaki sözü üzerine beş ders. Her ders için: video, yazılı ders, sunum, etkileşimli harita, soru-cevap ve anladığını ölçen bir test.',
    quote='«Allah’tan başkasına yapılan ibadetin bâtıl olduğuna inanman, onu terk etmen, ondan buğz etmen, ehlini tekfir etmen ve onlara düşmanlık etmendir.»',
    quoteRef='Şeyh Muhammed b. Abdülvehhab, «Ma‘ne’t-Tâğût ve Ruûsu Envâih» risalesi',
    home='Ana sayfa', lessons='Dersler', lesson='Ders', point='husus', of='· Tâğutu inkârın keyfiyeti',
    pointsT='Beş husus', pointsS='Her husus ayrı bir derstir ve sırayla eklenir. Bağlantılar bütün dersler için geçerli kalır.',
    latestT='En son ders', latestS='Videoyla başlayın, sunum ve haritayla tekrar edin, soru-cevap ve testle bitirin.',
    listT='Bölümün dersleri', listS='Dersin sayfasını ve bütün araçlarını açmak için tıklayın.',
    open='Dersi aç', soon='Yakında', live='Yayında',
    tText=('Yazılı ders', 'Delilleriyle tam açıklama; okumak ve basmak için'),
    tSlides=('Sunum', 'Dersin slaytları tek tek'),
    tMap=('Etkileşimli harita', 'Dersi dal dal izleyin'),
    tQA=('Soru-cevap', 'Tekrar soruları ve cevapları'),
    tQuiz=('Kendini dene', 'Çoktan seçmeli test, anında düzeltme'),
    doneWhat=dict(text='Yazılı dersi', slides='Sunumu', map='Haritayı', qa='Soru-cevabı', quiz='Testi', lesson='Bu dersi'),
    doneOff='{x} bitirdim', doneOn='✓ {x} bitirdiniz', doneUndo='Geri almak için tekrar dokunun', doneHint='Dersin bütün araçlarını bitirdiğinizde, dersi tamamladığınızı kaydetmek için buraya dokunun.',
    progReset='Bu cihazda kayıtlı ilerlememi sil', install='Siteyi telefonunuza uygulama olarak yükleyin',
    iosT='iPhone’a yükleme',
    iosIntro='iPhone ve iPad’de yükleme Safari’den üç adımla yapılır:',
    ios1='Safari’nin Paylaş düğmesine dokunun.',
    ios2='Listeden «Ana Ekrana Ekle»yi seçin.',
    ios3='«Ekle»ye dokunun; site simgesiyle uygulamalarınız arasına eklenir, tam ekran açılır ve internetsiz çalışır.',
    iosSafari='Site başka bir tarayıcıda açıksa önce Safari’de açın.',
    themeDark='Gece modu', themeLight='Gündüz modu',
    fsDown='Yazıyı küçült', fsUp='Yazıyı büyüt', fsLabel='Yazı boyutu', tShare=('Paylaşım görseli', 'WhatsApp ve Telegram için dersi açan QR kodlu görsel'),
    tSum=('Yazdırılabilir ders özeti', 'Dersi açan QR kodlu tek sayfa'),
    tSharh=('Kitabın metni ve kelime anlamları', 'Arapça metin paragraf paragraf, Türkçe anlamıyla; kelimeye dokununca anlamı çıkar'),
    sharhSub='Kitabın Arapça metni harfiyen, paragraf paragraf; altında Türkçe anlamı ve garip kelimelerin anlamları',
    sharhHint='Altı noktalı kelimelere dokunun: anlamı ve kaynağı görünür.',
    glHint='Altı noktalı kelimelere dokunun: anlamı görünür.',
    sharhSrc='Metin {b} adlı eserdendir; her paragrafın üstündeki numara: cilt/ sayfa.',
    sharhFn='Kitabın dipnotları (Arapça)', sharhGl='Kelimelerin anlamları', sharhGlSrc='Kaynak', sharhLbl='Şerh', sharhTr='Türkçe anlamı',
    chipSum='Özet', sumPrint='Yazdır', sumPdf='PDF indir', sumImg='Görsel indir',
    sumHelp='A4 boyutunda. Ders sayfasını açmak için kodu telefon kamerasıyla okutun.',
    sumFootT='Ders sayfası: video, yazılı ders, sunum, harita ve test',
    sumFoot='Dersin sayfasını ve bütün araçlarını açmak için kodu okutun:',
    tVideo=('Ders videosu', 'Dersin tamamını izleyin'),
    chipText='Yazılı', chipSlides='Sunum', chipMap='Harita', chipQA='Soru-cevap', chipQuiz='Test',
    toolsT='Dersin araçları', pathT='Önerilen çalışma yolu',
    path=['Videoyu izleyin ya da yazılı dersi okuyun.', 'Sunumu ve etkileşimli haritayı tekrar edin.', 'Cevabı açmadan önce tekrar sorularını cevaplayın.', 'Kendinizi sınayın, ardından özet ifadeyi ezberleyin.'],
    prev='Önceki ders', next='Sonraki ders',
    noVideo='Bu dersin videosu yakında eklenecek',
    wipBadge='Hazırlanıyor',
    wipNote='Bu dersin videosu hazırlanıyor; inşallah yakında eklenecek. Dersin geri kalanı şimdiden hazır, onunla başlayabilirsiniz:',
    tzSoon='Tanıtım videosu yakında eklenecek',
    tzT='Daha net, daha yakın, daha kolay dersler', tzD='Öğrenmeyi kolaylaştıran yeni hazırlıklarla derslerimizin kalitesini yükseltiyoruz. Kısa tanıtımı izleyin ve paylaşın.',
    foot='Ve Tevâsav bi’l-Hak · Allah’tan faydalı ilim ve salih amel dileriz.',
    sumNote='Basmak ve paylaşmak için özet görseli.', download='Görseli indir',
    toc='İçindekiler', tocShow='İçindekiler',
    textSub='Öğrenci için ayrıntılı ders; Kitap ve Sünnet’ten delilleriyle.',
    textEnd='Okuduktan sonra: soru-cevapla kendinizi gözden geçirin, ardından anladığınızı sınayın.',
    qaT='Soru-cevap', qaS='Önce cevabı düşünün, sonra karşılaştırmak için «Cevabı göster»e basın.',
    qaHint='Tekrar yöntemi: Soruyu okuyun, içinizden ya da sesli cevaplayın, sonra cevabı açın. «Doğru mu, yanlış mı?» sorularında tek kelimeyle yetinmeyip gerekçe gösterin.',
    qaAll='Bütün cevapları göster', qaShow='Cevabı göster', qaCount='{n} soru',
    qaG1='Tekrar soruları', qaG2='Yazılı dersin soruları', qaExtra='Ek soru', tf='Doğru mu, yanlış mı?',
    quizT='Kendini dene', quizS='Doğru cevabı seçin; her sorudan sonra gerekçesi gösterilir.',
    retry='Testi tekrarla', backLesson='Ders sayfasına dön', toQA='Soru-cevaba bak', wrongT='Tekrar edilmesi gereken sorular',
    slidesT='Sunum', grid='Bütün slaytlar', fs='Tam ekran', prevS='Önceki', nextS='Sonraki',
    rotate='Daha net görmek için telefonu yatay çevirin',
    skip='İçeriğe geç',
 ),
}
DIG = lambda lang, n: ''.join('٠١٢٣٤٥٦٧٨٩'[int(c)] if c.isdigit() else c for c in str(n)) if lang == 'ar' else str(n)

# ------------------------------------------------------------------ the library: all series
# A series has sections; a section has lessons. Only «حقيقة لا إله إلا الله» has lessons so far:
# its section «صفة الكفر بالطاغوت» holds LESSONS (pages l1/ … l5/ stay where they are, so old links keep working).
# status: 'live' (has lessons) · 'prep' (being prepared) · 'soon' (coming later). To add a series, add a dict here.
CATS = [('aqeedah', 'العقيدة', 'Akide'), ('fiqh', 'الفقه', 'Fıkıh'), ('hadith', 'الحديث', 'Hadis')]
SERIES = [
    dict(slug='la-ilaha', cat='aqeedah', status='live', page='la-ilaha.html',
         ar='حقيقة لا إله إلا الله', tr='Lâ ilâhe illallah’ın Hakikati', byAr='', byTr='', quizAll=True,
         sections=[
            dict(key='taghut', ar='صفة الكفر بالطاغوت', tr='Tâğutu İnkârın Keyfiyeti', lessons=LESSONS),
            dict(key='shurut', ar='شروط لا إله إلا الله', tr='Lâ ilâhe illallah’ın Şartları', lessons=[]),
            dict(key='arkan', ar='أركان التوحيد', tr='Tevhidin Rükünleri', lessons=[]),
            dict(key='nawaqid', ar='نواقض التوحيد', tr='Tevhidin Nâkızları', lessons=[]),
         ]),
    dict(slug='tawhid', cat='aqeedah', status='prep', ar='شرح كتاب التوحيد', tr='Kitâbu’t-Tevhîd Şerhi',
         byAr='للشيخ محمد بن عبد الوهاب رحمه الله', byTr='Şeyh Muhammed b. Abdülvehhab'),
    dict(slug='fiqh-muyassar', cat='fiqh', status='live', page='fiqh-muyassar.html',
         ar='الفقه الميسّر', tr='el-Fıkhu’l-Müyesser', byAr='إعداد نخبة من العلماء', byTr='Bir grup âlimin hazırladığı',
         leadAr='سلسلة في فقه العبادات على كتاب «الفقه الميسّر في ضوء الكتاب والسنة»: الطهارة، والصلاة، والزكاة، والصيام، بالأدلة من غير تعقيد. لكل درس: فيديو، ودرس مكتوب، وعرض شرائح، وخريطة تفاعلية، وأسئلة وأجوبة، واختبار.',
         leadTr='«el-Fıkhu’l-Müyesser fî Dav’i’l-Kitâb ve’s-Sünne» kitabı üzerine ibadet fıkhı serisi: taharet, namaz, zekât ve oruç; delilleriyle ve sade bir dille. Her derste: video, yazılı ders, sunum, etkileşimli harita, soru-cevap ve test.',
         quoteAr='«مَنْ يُرِدِ اللَّهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّينِ»',
         quoteTr='<span class="ar" lang="ar" dir="rtl">«مَنْ يُرِدِ اللَّهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّينِ»</span>',
         mealTr='«Allah kime hayır dilerse onu dinde fakih kılar.» (Buhârî, Müslim)',
         sections=[
            dict(key='tahara', ar='كتاب الطهارة', tr='Taharet Kitabı', lessons=FIQH),
            dict(key='salah', ar='كتاب الصلاة', tr='Namaz Kitabı', lessons=[]),
            dict(key='zakah', ar='كتاب الزكاة', tr='Zekât Kitabı', lessons=[]),
            dict(key='siyam', ar='كتاب الصيام', tr='Oruç Kitabı', lessons=[]),
         ]),
    dict(slug='usul-thalatha', cat='aqeedah', status='prep', ar='الأصول الثلاثة', tr='Üç Esas (el-Usûlu’s-Selâse)',
         byAr='للشيخ محمد بن عبد الوهاب رحمه الله', byTr='Şeyh Muhammed b. Abdülvehhab'),
    dict(slug='riyad', cat='hadith', status='soon', ar='رياض الصالحين', tr='Riyâzu’s-Sâlihîn',
         byAr='للإمام النووي رحمه الله', byTr='İmam Nevevî'),
    dict(slug='wajeez', cat='aqeedah', status='soon', ar='شرح كتاب الوجيز في عقيدة السلف', tr='el-Vecîz fî Akîdeti’s-Selef Şerhi', byAr='', byTr=''),
]
MAIN = SERIES[0]                      # the series of the first lessons (la-ilaha.html)
MAIN_PAGE = MAIN['page']

def where_of(L):
    """(series, section) a lesson belongs to"""
    for x in SERIES:
        for sec in x.get('sections', []):
            if any(l is L for l in sec['lessons']): return x, sec
    raise KeyError(L['ar'])

def sect_live(L):
    """the published lessons of the lesson's own section, in order"""
    return [l for l in where_of(L)[1]['lessons'] if l['live']]

def ar_count(n, one, two, few, many):
    """Arabic counted noun: ١ درس واحد، درسان، ٣ دروس، ١١ درسًا"""
    if n == 1: return one
    if n == 2: return two
    if 3 <= n <= 10: return f'{DIG("ar", n)} {few}'
    return f'{DIG("ar", n)} {many}'

LIB = {
 'ar': dict(title='مكتبة الدروس', nav='السلاسل',
    lead='دروس في العقيدة والفقه والحديث، مكتوبة ومرئية، مع أسئلة واختبار.',
    soonT='قريبًا إن شاء الله',
    search='ابحث في الدروس: كلمة أو عبارة…', noResult='لا نتائج. جرّب كلمة أخرى.',
    inT='نتائج داخل الدروس', inMore='عرض نتائج أكثر', inCount='{n} موضعًا',
    contT='تابع من حيث توقفت', contB='أكمِل',
    seriesT='السلاسل', seriesS='اختر سلسلة لتفتح صفحتها ودروسها.', all='الكل',
    st=dict(live='متاحة', prep='قيد الإعداد الآن', soon='قريبًا إن شاء الله'), stMeta=dict(prep='قيد الإعداد', soon='تبدأ قريبًا'),
    open='افتح السلسلة', latestT='أحدث الدروس', latestS='آخر ما نُشر من السلاسل.', openL='افتح الدرس',
    sectionsT='أقسام السلسلة', sectionsS='تُضاف الأقسام والدروس تباعًا.', sectionSoon='قريبًا',
    sLead='سلسلة في معنى كلمة التوحيد وما يحققها وما ينقضها: صفة الكفر بالطاغوت، وشروط لا إله إلا الله، وأركان التوحيد، ونواقض التوحيد. لكل درس: فيديو، ودرس مكتوب، وعرض شرائح، وخريطة تفاعلية، وأسئلة وأجوبة، واختبار.',
    sQuote='﴿فَاعْلَمْ أَنَّهُ لَا إِلَٰهَ إِلَّا اللَّهُ﴾', sQuoteMeal='',
    section='قسم', toSection='إلى القسم',
 ),
 'tr': dict(title='Ders Kütüphanesi', nav='Seriler',
    lead='Akide, fıkıh ve hadis dersleri: yazılı ve görüntülü, sorular ve testle.',
    soonT='Yakında inşallah',
    search='Derslerde ara: kelime veya ifade…', noResult='Sonuç yok. Başka bir kelime deneyin.',
    inT='Derslerin içinden sonuçlar', inMore='Daha fazla sonuç göster', inCount='{n} yer',
    contT='Kaldığın yerden devam et', contB='Devam et',
    seriesT='Seriler', seriesS='Sayfasını ve derslerini açmak için bir seri seçin.', all='Tümü',
    st=dict(live='Yayında', prep='Şu an hazırlanıyor', soon='İnşallah yakında'), stMeta=dict(prep='Hazırlanıyor', soon='Yakında başlıyor'),
    open='Seriyi aç', latestT='Son dersler', latestS='Serilerden en son yayınlananlar.', openL='Dersi aç',
    sectionsT='Serinin bölümleri', sectionsS='Bölümler ve dersler sırayla eklenir.', sectionSoon='Yakında',
    sLead='Tevhid kelimesinin anlamı, onu gerçekleştiren ve bozan şeyler üzerine bir seri: tâğutu inkârın keyfiyeti, lâ ilâhe illallah’ın şartları, tevhidin rükünleri ve tevhidin nâkızları. Her derste: video, yazılı ders, sunum, etkileşimli harita, soru-cevap ve test.',
    sQuote='<span class="ar" lang="ar" dir="rtl">﴿فَاعْلَمْ أَنَّهُ لَا إِلَٰهَ إِلَّا اللَّهُ﴾</span>', sQuoteMeal='«Bil ki Allah’tan başka hiçbir ilah yoktur.» (Muhammed, 19)',
    section='Bölüm', toSection='Bölüme git',
 ),
}

def lessons_count(lang, n):
    return ar_count(n, 'درس واحد', 'درسان', 'دروس', 'درسًا') if lang == 'ar' else f'{n} ders'

def published(lang, n):
    if lang == 'ar': return ar_count(n, 'درس واحد منشور', 'درسان منشوران', 'دروس منشورة', 'درسًا منشورًا')
    return f'{n} ders yayında'

def sections_count(lang, n):
    return ar_count(n, 'قسم واحد', 'قسمان', 'أقسام', 'قسمًا') if lang == 'ar' else f'{n} bölüm'

FONTS = {
 'ar': 'https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Naskh+Arabic:wght@400..700&family=Reem+Kufi:wght@400..700&display=swap',
 'tr': 'https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=EB+Garamond:wght@500..700&family=Source+Sans+3:wght@400..700&display=swap',
}
ORN = ''  # backgrounds of .hero/.phead are drawn in CSS (glow + fine dots)
I = {
 'text': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 21.5A2.5 2.5 0 0 1 6.5 19H20v3H6.5"/><path d="M9 7h7M9 11h5"/></svg>',
 'slides': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M12 16v4M8 20h8"/></svg>',
 'map': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="3"/><circle cx="4" cy="5" r="2"/><circle cx="20" cy="5" r="2"/><circle cx="4" cy="19" r="2"/><circle cx="20" cy="19" r="2"/><path d="M6 6l3.5 4M18 6l-3.5 4M6 18l3.5-4M18 18l-3.5-4"/></svg>',
 'qa': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.8 7L4 20l1.1-4.6A8 8 0 1 1 21 12z"/><path d="M9.6 9.3a2.5 2.5 0 0 1 4.8.9c0 1.6-2.4 2.1-2.4 3.3M12 16.5h.01"/></svg>',
 'quiz': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/></svg>',
 'sum': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/></svg>',
 'share': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg>',
 'video': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9l5 3-5 3z" fill="currentColor"/></svg>',
}

# ------------------------------------------------------------------ helpers
PRELOAD = {'ar': ['noto-naskh-arabic-arabic-wght-normal.woff2', 'reem-kufi-arabic-wght-normal.woff2'],
           'tr': ['source-sans-3-latin-wght-normal.woff2', 'eb-garamond-latin-wght-normal.woff2']}
def preload(lang, u):
    return '\n'.join(f'<link rel="preload" href="{u}assets/fonts/{f}" as="font" type="font/woff2" crossorigin>' for f in PRELOAD[lang])

def up(depth): return '../' * depth

def og_tags(lang, title, desc, image=None):
    img, w, h = (SITE + 'media/' + image, 1080, 1080) if image else (SITE + 'media/og.jpg', 1200, 630)
    return f'''<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{E(S[lang]['brand'])}">
<meta property="og:locale" content="{'ar_AR' if lang == 'ar' else 'tr_TR'}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="{w}">
<meta property="og:image:height" content="{h}">
<meta name="twitter:card" content="{'summary' if image else 'summary_large_image'}">'''

def app_tags(lang, root):
    """Installable app (manifest) and offline support (service worker) for every page."""
    man = f'{root}manifest.webmanifest' if lang == 'ar' else f'{root}tr/manifest.webmanifest'
    return f'''<link rel="manifest" href="{man}">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{E(S[lang]['brand'])}">
<script>if ('serviceWorker' in navigator) addEventListener('load', () => navigator.serviceWorker.register('{root}sw.js').catch(() => {{}}));</script>'''

# applies the student's saved day/night choice before first paint, so the page never flashes the other scheme
THEME_BOOT = "<script>try{var t=localStorage.getItem('wt.theme');if(t==='dark'||t==='light')document.documentElement.dataset.theme=t}catch(e){}</script>"

THEME_I = ('<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
           '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>')

def theme_btn(lang):
    s = S[lang]
    return f'<button class="tbtn" id="themeBtn" type="button" aria-label="{E(s["themeDark"])}" title="{E(s["themeDark"])}" data-dark="{E(s["themeDark"])}" data-light="{E(s["themeLight"])}">{THEME_I}</button>'

def head(lang, title, depth, desc='', extra='', image=None):
    d = 'rtl' if lang == 'ar' else 'ltr'
    u = up(depth)
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{THEME_BOOT}
{gate.tags(lang, u)}
<title>{E(title)}</title>
<meta name="description" content="{E(desc or S[lang]['lead'])}">
{og_tags(lang, title, desc or S[lang]['lead'], image)}
<meta name="theme-color" content="#0F2E2A">
{app_tags(lang, u)}
<link rel="icon" href="{u}media/logo.webp" type="image/webp">
<link rel="apple-touch-icon" href="{u}media/apple-touch-icon.png">
{preload(lang, u)}
<link rel="stylesheet" href="{u}assets/fonts.css">
<link rel="stylesheet" href="{u}assets/site.css">{extra}
</head>
<body tabindex="-1">
<a class="skip" href="#main">{S[lang]['skip']}</a>
'''

def bar(lang, depth, other):
    """other: href to the same page in the other language (relative to this page)."""
    s, u = S[lang], up(depth)
    olang = 'tr' if lang == 'ar' else 'ar'
    olabel = 'Türkçe' if lang == 'ar' else 'العربية'
    return f'''<header class="bar"><div class="wrap">
  <a class="brand" href="{home_of(lang, depth)}"><img src="{root_up(lang, depth)}media/logo.webp" alt="{E(s['brand'])}"><span>{E(s['brand'])}</span></a>
  <nav aria-label="{E(s['home'])}"><a class="hide-s" href="{home_of(lang, depth)}">{E(s['home'])}</a><a class="hide-s" href="{home_of(lang, depth)}#series">{E(LIB[lang]['nav'])}</a>{tasks_link(lang, depth)}{theme_btn(lang)}<a class="lang" lang="{olang}" hreflang="{olang}" href="{other}">{olabel}</a></nav>
</div></header>
'''

TASK_I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="3"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>'

def tasks_link(lang, depth):
    if not HAS_TASKS: return ''
    return f'<a class="tasks-nav" href="{home_of(lang, depth)[:-len("index.html")]}tasks.html">{TASK_I}{E(TS[lang]["nav"])}</a>'

def root_up(lang, depth):
    return up(depth)

def home_of(lang, depth):
    return up(depth - (1 if lang == 'tr' else 0)) + 'index.html'

def series_of(lang, depth):
    """link to the page of the series the current lessons belong to"""
    return up(depth - (1 if lang == 'tr' else 0)) + MAIN_PAGE

def footer(lang, depth):
    s, u = S[lang], up(depth)
    return f'''<footer><div class="wrap"><div class="f1"><img src="{u}media/logo.webp" alt=""><span>{E(s['foot'])}</span></div><span class="flinks"><a href="{home_of(lang, depth)}">{E(LIB[lang]['title'])}</a><a href="{home_of(lang, depth)[:-len('index.html')]}privacy.html">{'سياسة الخصوصية' if lang == 'ar' else 'Gizlilik Politikası'}</a></span></div><div class="wrap app-cta" id="appCta" hidden><button class="btn line" id="installBtn" type="button" hidden>{E(s['install'])}</button><button class="btn line" id="iosBtn" type="button" hidden>{E(s['install'])}</button></div>{ios_dialog(lang)}</footer>
'''

IOS_I = dict(
    share='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 14V3M8.5 6.5 12 3l3.5 3.5"/><path d="M5 10v9a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-9"/></svg>',
    add='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M12 9v6M9 12h6"/></svg>',
    ok='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>')

def ios_dialog(lang):
    """Illustrated add-to-home-screen steps for iPhone/iPad, opened from the footer install button."""
    s = S[lang]
    steps = ''.join(f'<li><span class="ic">{IOS_I[i]}</span><span>{E(s[k])}</span></li>'
                    for i, k in (('share', 'ios1'), ('add', 'ios2'), ('ok', 'ios3')))
    return f'''<dialog id="iosDlg" aria-labelledby="iosDlgT">
  <div class="dbar"><span id="iosDlgT">{E(s['iosT'])}</span><button id="iosDlgX" aria-label="×">×</button></div>
  <div class="ios-in"><p>{E(s['iosIntro'])}</p><ol class="ios-steps">{steps}</ol><p class="ios-note">{E(s['iosSafari'])}</p></div>
</dialog>
'''

def dialog(lang):
    s = S[lang]
    return f'''<dialog id="dlg" aria-labelledby="dlgT">
  <div class="dbar"><span id="dlgT"></span><button id="dlgX" aria-label="×">×</button></div>
  <img id="dlgImg" alt="">
  <p class="dnote"><span>{E(s['sumNote'])}</span><a class="btn line" id="dlgDl" href="#" download>{E(s['download'])}</a></p>
</dialog>
'''

def done_btn(lang, n, k, cls='donebtn'):
    """A button the student presses to record that they finished a tool (or the whole lesson)."""
    s = S[lang]; x = s['doneWhat'][k]
    off, on = s['doneOff'].format(x=x), s['doneOn'].format(x=x)
    return f'<button class="{cls}" type="button" data-done="{n}:{k}" data-off="{E(off)}" data-on="{E(on)}" title="{E(s["doneUndo"])}" aria-pressed="false">{E(off)}</button>'

def fs_ctl(lang):
    s = S[lang]; a = 'أ' if lang == 'ar' else 'A'
    return f'<div class="fs-ctl" role="group" aria-label="{E(s["fsLabel"])}"><button type="button" data-fs="-1" aria-label="{E(s["fsDown"])}" title="{E(s["fsDown"])}">{a}<small>−</small></button><button type="button" data-fs="1" aria-label="{E(s["fsUp"])}" title="{E(s["fsUp"])}">{a}<small>+</small></button></div>'

def tool(icon, label, href, primary=False, data_img=None, title=None):
    b, sm = label
    cls = 'tool' + (' primary' if primary else '')
    if data_img:
        return f'<button class="{cls}" data-img="{data_img}" data-title="{E(title or b)}"><span class="ic">{I[icon]}</span><span><b>{E(b)}</b><small>{E(sm)}</small></span></button>'
    return f'<a class="{cls}" href="{href}"><span class="ic">{I[icon]}</span><span><b>{E(b)}</b><small>{E(sm)}</small></span></a>'

def ayahify(h):
    return re.sub(r'(﴿[^﴾]*﴾)', r'<span class="ayah" lang="ar">\1</span>', h)

def arabify(h):
    """In Turkish pages: mark quoted Arabic (hadith, sayings) so it gets an Arabic font and direction."""
    return re.sub(r'«([^«»<]*[\u0600-\u06FF][^«»<]*)»', r'<span class="ar" lang="ar" dir="rtl">«\1»</span>', h)

def lesson_base(lang, depth):
    """path from a page at `depth` to the lesson folders of this language"""
    return up(depth)

def player(lang, L, prefix):
    s = S[lang]
    v = L.get('videoTr' if lang == 'tr' else 'video')
    p = L.get('posterTr' if lang == 'tr' else 'poster') or ''
    poster = f' poster="{prefix}media/{p}"' if p else ''
    if v and not os.path.exists(os.path.join(OUT, 'media', v)):
        # video not uploaded yet: say so plainly from the first moment, and point to what is ready
        bg = f' style="background-image:url(\'{prefix}media/{p}\')"' if p else ''
        return (f'<div class="wip"><div class="wipart"{bg} role="img" aria-label="{E(s["noVideo"])}"><span class="wipbadge">{E(s["wipBadge"])}</span></div>'
                f'<p class="wipnote">{E(s["wipNote"])}</p><div class="wipgo"><a class="btn" href="text.html">{E(s["tText"][0])}</a>'
                f'<a class="btn ghost" href="slides.html">{E(s["tSlides"][0])}</a></div></div>')
    return f'''<div class="player" data-logo="{prefix}media/logo.webp" data-soon="{E(s['noVideo'])}"><video controls preload="none" playsinline{poster} data-check><source src="{prefix}media/{v}" type="video/mp4"></video></div>'''

# ------------------------------------------------------------------ Q&A data
def deck_qa(deck):
    order = json.load(open(f'{DECKS}/{deck}/deck.json'))['order']
    out = []
    for sid in order:
        if not sid.startswith('review'): continue
        t = open(f'{DECKS}/{deck}/slides/{sid}.html', encoding='utf-8').read()
        tf = 'صح أو خطأ' in t or 'Doğru mu' in t
        for q, a in re.findall(r'<p class="q">(.*?)</p><p class="a fragment">(.*?)</p>', t, re.S):
            out.append(dict(q=q.strip(), a=a.strip(), tf=tf))
    return out

EXTRA = {
 'ar2': [dict(q='ما الدرس العملي الذي نأخذه من قصة أصحاب الكهف في هذا الباب؟', a='الثبات على الترك ولو كان المسلم في قلة، وعدم الاغترار بكثرة المخالفين.', tf=False, extra=True),
         dict(q='الخوف الطبيعي من حيوان مفترس عبادة.', a='خطأ؛ لأنه خوف طبيعي لا تعبدي.', tf=True, extra=True)],
 'tr2': [dict(q='Ashâb-ı Kehf kıssasından bu konuda hangi amelî dersi çıkarırız?', a='Müslüman azınlıkta olsa da Allah’tan başkasına ibadeti terkte sebat etmek ve muhaliflerin çokluğuna aldanmamak.', tf=False, extra=True),
         dict(q='Yırtıcı bir hayvandan duyulan tabii korku ibadettir.', a='Yanlış; çünkü tabii bir korkudur, ibadet korkusu değildir.', tf=True, extra=True)],
}

# questions of the written lesson, with answers drawn from the lesson text
DOCQA = {
 1: [
  ('عرّف الطاغوت لغة، واذكر تعريف ابن القيم له.', 'الطاغوت في اللغة مشتق من الطغيان، وهو مجاوزة الحد. وعرّفه ابن القيم رحمه الله بقوله: «الطاغوت ما تجاوز به العبد حدّه من معبود أو متبوع أو مطاع».', False),
  ('ما معنى الاعتقاد؟ ولماذا لا تكفي المعرفة الذهنية؟', 'الاعتقاد: الجزم والتصديق القلبي بشيء، بحيث يستقر في القلب ويطمئن إليه. ولا تكفي المعرفة الذهنية وحدها لأنها قد تجتمع مع الجحود؛ فقد عرف فرعون وقومه الحق ولم يؤمنوا به: ﴿وَجَحَدُوا بِهَا وَاسْتَيْقَنَتْهَا أَنْفُسُهُمْ ظُلْمًا وَعُلُوًّا﴾ [النمل: 14].', False),
  ('اذكر المعاني الثلاثة التي يتضمنها اعتقاد بطلان عبادة الطاغوت.', '١) اعتقاد استحقاق الله وحده للعبادة. ٢) اعتقاد بطلان كل عبادة صُرفت لغير الله. ٣) اعتقاد أن غير الله لا يستحق شيئًا من العبادة، مهما بلغت منزلته أو صلاحه.', False),
  ('استدل بآيتين على هذه النقطة مع بيان وجه الدلالة.', 'من ذلك: ﴿ذَٰلِكَ بِأَنَّ اللَّهَ هُوَ الْحَقُّ وَأَنَّ مَا يَدْعُونَ مِنْ دُونِهِ هُوَ الْبَاطِلُ﴾ [الحج: 62]، ووجه الدلالة أن الله قابل بين الحق والباطل: فهو الحق، وما يُدعى من دونه هو الباطل. و﴿وَلَقَدْ بَعَثْنَا فِي كُلِّ أُمَّةٍ رَسُولًا أَنِ اعْبُدُوا اللَّهَ وَاجْتَنِبُوا الطَّاغُوتَ﴾ [النحل: 36]، ووجه الدلالة أن الله جمع بين الأمر بعبادته والأمر باجتناب الطاغوت، وجعل ذلك دعوة جميع الرسل.', False),
  ('ما ركنا «لا إله إلا الله»؟ وما صلة كل منهما بآية البقرة؟', 'النفي «لا إله»: نفي استحقاق العبادة عن كل ما سوى الله، ويقابل الكفر بالطاغوت. والإثبات «إلا الله»: إثبات استحقاق العبادة لله وحده، ويقابل الإيمان بالله. وهما ما في قوله تعالى: ﴿فَمَنْ يَكْفُرْ بِالطَّاغُوتِ وَيُؤْمِنْ بِاللَّهِ﴾ [البقرة: 256].', False),
  ('لماذا قُدِّم الكفر بالطاغوت على الإيمان بالله في آية البقرة؟', 'لأن القلب لا يصفو للتوحيد حتى يتخلّى عن الباطل، وهذا ما يسميه العلماء: التخلية قبل التحلية.', False),
  ('رجل ترك عبادة القبور لأن أهل بلده لا يفعلونها، لا لأنه يعتقد بطلانها. ما الخلل في حاله؟', 'تركه قائم على العادة والبيئة لا على اعتقاد في القلب؛ فإذا تغيرت الظروف رجع إليها. والمطلوب أن يعتقد بطلانها؛ لأن القلب أصل والجوارح تبع.', False),
  ('كيف تجمع بين اعتقاد بطلان عبادة عيسى عليه السلام وبين محبته وتعظيمه نبيًّا كريمًا؟', 'بالتفريق بين بطلان العبادة والحكم على المعبود: فعبادته من دون الله باطلة، وهو نبي كريم بريء ممن عبده: ﴿مَا قُلْتُ لَهُمْ إِلَّا مَا أَمَرْتَنِي بِهِ أَنِ اعْبُدُوا اللَّهَ رَبِّي وَرَبَّكُمْ﴾ [المائدة: 117]. فنحبه ونعظمه نبيًّا، ولا نصرف له شيئًا من العبادة.', False),
  ('يكفي في الكفر بالطاغوت أن يترك الإنسان عبادته بجوارحه.', 'خطأ؛ فلا بد أن يكون في القلب اعتقاد ببطلانها، لأن الترك بلا اعتقاد قد يكون لعادة أو بيئة أو خوف من الناس.', True),
  ('كل من عُبد من دون الله فهو طاغوت راضٍ بعبادته.', 'خطأ؛ فقد يُعبد نبي أو ملك أو عبد صالح وهو بريء من ذلك، كعيسى عليه السلام، والملائكة الذين يتبرؤون ممن عبدهم: ﴿قَالُوا سُبْحَانَكَ أَنْتَ وَلِيُّنَا مِنْ دُونِهِمْ﴾ [سبأ: 41].', True),
  ('انتشار عبادةٍ ما بين الناس دليل على صحتها.', 'خطأ؛ فالمعيار هو الحق الذي جاء به الوحي، لا كثرة الفاعلين ولا شيوع العادة. وقد ذمّ الله من احتج بذلك: ﴿إِنَّا وَجَدْنَا آبَاءَنَا عَلَى أُمَّةٍ وَإِنَّا عَلَى آثَارِهِمْ مُقْتَدُونَ﴾ [الزخرف: 23].', True),
 ],
 2: [
  ('ما معنى الترك لغة؟ وما الفرق بينه وبين الاجتناب؟', 'الترك: مفارقة الشيء والتخلّي عنه. والاجتناب من «الجانب»: أن تكون في جانب والشيء في جانب آخر؛ فهو أبلغ من مجرد الترك، إذ يتضمن ترك الفعل والابتعاد عن وسائله ومواضعه.', False),
  ('اذكر الصور الأربع لترك عبادة الطاغوت.', '١) ترك صرف العبادة لغير الله. ٢) ترك المشاركة فيها مع أهلها. ٣) اجتناب الوسائل والذرائع المفضية إليها. ٤) الثبات على الترك.', False),
  ('استدل بآية الزمر على هذه النقطة، وبيّن وجه الدلالة.', '﴿وَالَّذِينَ اجْتَنَبُوا الطَّاغُوتَ أَنْ يَعْبُدُوهَا وَأَنَابُوا إِلَى اللَّهِ لَهُمُ الْبُشْرَىٰ﴾ [الزمر: 17]. وجه الدلالة: بيّنت أن المراد باجتناب الطاغوت ترك عبادتها، وقرنت الترك بالإنابة إلى الله فاجتمع النفي والإثبات، ووعدت أهل ذلك بالبشرى.', False),
  ('ما وجه الدلالة من حديث النذر ببُوَانة؟', 'لم يأذن النبي ﷺ بالذبح لله في ذلك المكان حتى تأكد أنه لم يكن موضعًا لعبادة وثن ولا لعيد من أعيادهم؛ فهو أصل في اجتناب مواضع عبادة غير الله ووسائلها. فإذا كان هذا في ذبح يُراد به الله، فكيف بمن يذبح لغير الله؟', False),
  ('ما مقتضى النفي في «لا إله إلا الله» في العمل؟', 'ترك عبادة غير الله. أما مقتضاه في القلب فاعتقاد بطلانها.', False),
  ('لماذا جاء الترك بعد الاعتقاد في ترتيب النقاط؟', 'لأن الاعتقاد أصل والترك ثمرته وبرهانه؛ فمن اعتقد بطلان شيء لزمه أن يتركه، ومن زعم أنه يعتقد بطلان عبادة غير الله ثم هو يفعلها ففعله يكذّب قوله.', False),
  ('رجل يقول إنه يعتقد بطلان الذبح لغير الله، لكنه يشارك فيه مجاملةً لأهله. ما الخلل في حاله؟', 'هذا اعتقاد بلا ترك، وفعله ينقض قوله؛ لأن الاعتقاد الجازم يوجب العمل بمقتضاه، ولا يستقيم أن يجزم القلب ببطلان شيء ثم تباشره الجوارح مختارة.', False),
  ('ما الدرس العملي الذي نأخذه من قصة أصحاب الكهف في هذا الباب؟', 'الثبات على الترك ولو كان المسلم في قلة، وعدم الاغترار بكثرة المخالفين؛ فقد تركوا ما يعبده قومهم من دون الله واستثنوا الله وحده.', False),
  ('من لم يعبد غير الله قط فقد حقق الكفر بالطاغوت ولو لم يعتقد بطلانها.', 'خطأ؛ فهذا ترك بلا اعتقاد، ترك عادة لا ترك عبادة، وهو معرّض للزوال متى تغيرت البيئة.', True),
  ('الاجتناب أبلغ من مجرد الترك.', 'صح؛ لأنه يتضمن ترك الفعل والابتعاد عن وسائله ومواضعه.', True),
 ],
 3: [
  ('ما معنى البغض لغة؟ وما معنى البغضاء؟', 'البغض ضد الحب، والبغضاء شدة البغض. قال الجوهري: «البُغْضُ: ضدُّ الحبِّ... والبَغْضاءُ: شدّة البُغْضِ» [الصحاح]. ومنه: ﴿وَبَدَا بَيْنَنَا وَبَيْنَكُمُ الْعَدَاوَةُ وَالْبَغْضَاءُ أَبَدًا﴾ [الممتحنة: 4].', False),
  ('ما الأمور الثلاثة التي يتعلق بها البغض في هذه النقطة؟', '١) عبادة غير الله: الشرك وكل عبادة تُصرف لغير الله. ٢) الطاغوت: كل ما عُبد من دون الله وهو راضٍ، وكل من دعا إلى عبادة نفسه أو جاوز حدّه بما هو من حق الله. ٣) أهلها: أهل عبادة غير الله، من أجل شركهم وكفرهم، ولو كانوا أقرب قريب.', False),
  ('اذكر رؤوس الطواغيت الخمسة كما ذكرها الشيخ محمد بن عبد الوهاب.', 'قال رحمه الله في «ثلاثة الأصول»: «والطواغيت كثيرون، ورؤوسهم خمسة: إبليس لعنه الله، ومن عُبد وهو راضٍ، ومن دعا الناس إلى عبادة نفسه، ومن ادعى شيئًا من علم الغيب، ومن حكم بغير ما أنزل الله».', False),
  ('استدل بآية الممتحنة على بغض أهل الشرك، وبيّن وجه الدلالة.', '﴿قَدْ كَانَتْ لَكُمْ أُسْوَةٌ حَسَنَةٌ فِي إِبْرَاهِيمَ وَالَّذِينَ مَعَهُ إِذْ قَالُوا لِقَوْمِهِمْ إِنَّا بُرَآءُ مِنْكُمْ وَمِمَّا تَعْبُدُونَ مِنْ دُونِ اللَّهِ كَفَرْنَا بِكُمْ وَبَدَا بَيْنَنَا وَبَيْنَكُمُ الْعَدَاوَةُ وَالْبَغْضَاءُ أَبَدًا حَتَّى تُؤْمِنُوا بِاللَّهِ وَحْدَهُ﴾ [الممتحنة: 4]. وجه الدلالة: تبرأ إبراهيم عليه السلام والذين معه من قومهم ومما يعبدون من دون الله، وأعلنوا البغضاء بينهم وبين قومهم المشركين، وجعل الله ذلك أسوة حسنة للمؤمنين، وغاية هذا البغض ﴿حَتَّى تُؤْمِنُوا بِاللَّهِ وَحْدَهُ﴾.', False),
  ('ما وجه الدلالة من آية المجادلة على هذه النقطة؟', '﴿لَا تَجِدُ قَوْمًا يُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ يُوَادُّونَ مَنْ حَادَّ اللَّهَ وَرَسُولَهُ وَلَوْ كَانُوا آبَاءَهُمْ أَوْ أَبْنَاءَهُمْ أَوْ إِخْوَانَهُمْ أَوْ عَشِيرَتَهُمْ﴾ [المجادلة: 22]. نفى الله الإيمان عمّن يوادّ من حادّ الله ورسوله ولو كان من أقرب الناس إليه. والمودة محبة القلب، فدلّ على أن المؤمن لا يحب أهل الشرك، بل يبغضهم في الله.', False),
  ('لماذا لا يكفي الاعتقاد والترك دون البغض؟', 'لأن القلب لا يكفي فيه أن يعلم ويصدّق، بل لا بد أن يحب ما يحبه الله ويبغض ما يبغضه الله. فمن ترك بلا بغض فقلبه يميل إلى عبادة غير الله أو يحب أهلها، وهذا خلل في الكفر بالطاغوت. ومن اعتقد بلا بغض لم يحقق هذه النقطة؛ والمسلم لا يكون محايدًا بين التوحيد والشرك، ولا بين أهل التوحيد وأهل الشرك.', False),
  ('هل يُبغض عيسى عليه السلام لأن النصارى عبدوه؟ ولماذا؟', 'لا؛ لأن من عُبد من دون الله وهو غير راضٍ بذلك، كعيسى عليه السلام والملائكة والصالحين، فليس طاغوتًا ولا يُبغض، بل يُحب ويُتولّى؛ والمبغوض عبادتهم من دون الله. قال عيسى عليه السلام: ﴿مَا قُلْتُ لَهُمْ إِلَّا مَا أَمَرْتَنِي بِهِ أَنِ اعْبُدُوا اللَّهَ رَبِّي وَرَبَّكُمْ﴾ [المائدة: 117].', False),
  ('رجل يحب قريبه المشرك ويوادّه على ما هو عليه. ما الخلل في حاله؟', 'لم يبغض أهل الشرك في الله، والله نفى الإيمان عمّن يوادّ من حادّ الله ورسوله ولو كانوا آباءهم أو أبناءهم أو إخوانهم أو عشيرتهم [المجادلة: 22]. والمطلوب أن يبغض ما عليه قريبه من الشرك، ولا يوادّه عليه، ولا تحمله القرابة على الرضا بشركه.', False),
  ('يكفي المسلمَ أن يعلم بطلان عبادة غير الله، ولو لم يبغضها ولم يبغض أهلها.', 'خطأ؛ فهذا اعتقاد بلا بغض، ومن كان كذلك لم يحقق هذه النقطة. والمطلوب أن يبغضها ويبغض الطاغوت وأهله في الله.', True),
  ('كل من عُبد من دون الله يُبغض، ولو كان غير راضٍ بعبادته.', 'خطأ؛ فمن عُبد وهو غير راضٍ، كعيسى عليه السلام والملائكة والصالحين، لا يُبغض؛ والمبغوض عبادتهم من دون الله، لا هم [المائدة: 117].', True),
  ('البغض في الله من استكمال الإيمان.', 'صح؛ قال رسول الله ﷺ: «مَنْ أَحَبَّ لِلَّهِ، وَأَبْغَضَ لِلَّهِ، وَأَعْطَى لِلَّهِ، وَمَنَعَ لِلَّهِ، فَقَدِ اسْتَكْمَلَ الْإِيمَانَ» رواه أبو داود.', True),
 ],
 101: [
  ('ما معنى الفقه لغة واصطلاحًا؟', 'الفقه لغةً: الفهم، ومنه: ﴿مَا نَفْقَهُ كَثِيرًا مِمَّا تَقُولُ﴾ [هود: 91]. واصطلاحًا: العلم بالأحكام الشرعية العملية المكتسبة من أدلتها التفصيلية.', False),
  ('ما قسما الطهارة؟ وأيهما أهم؟', 'طهارة معنوية: طهارة القلب من الشرك والمعاصي وكل ما ران عليه، وطهارة حسية: طهارة البدن والثوب والمكان. والمعنوية أهم، ولا تتحقق طهارة البدن مع وجود نجس الشرك: ﴿إِنَّمَا الْمُشْرِكُونَ نَجَسٌ﴾ [التوبة: 28].', False),
  ('عرّف الطهارة اصطلاحًا، وفرّق بين الحدث والخبث.', 'الطهارة: ارتفاع الحدث وزوال الخبث. والحدث وصف قائم بالبدن يمنع من الصلاة ونحوها، ويرتفع بالوضوء أو الغسل. والخبث هو النجاسة، وتكون في البدن والثوب والمكان، وتزول بإزالتها.', False),
  ('ما الماء الطهور؟ اذكر أربعة أمثلة له.', 'الطاهر في نفسه، المطهِّر لغيره، الباقي على خلقته. ومن أمثلته: المطر، وذوب الثلج، وماء الأنهار، وماء البحار.', False),
  ('ما حدّ الماء الكثير؟ وما دليله؟', 'ما بلغ قلّتين فأكثر، والقلّتان نحو 160.5 لترًا. ودليله حديث ابن عمر رضي الله عنهما: «إِذَا بَلَغَ الْمَاءُ قُلَّتَيْنِ لَمْ يَحْمِلِ الْخَبَثَ».', False),
  ('لماذا لا تحصل الطهارة بالعصير وإن كان طاهرًا؟ استدل بآية.', 'لأن الله قال: ﴿فَلَمْ تَجِدُوا مَاءً فَتَيَمَّمُوا صَعِيدًا طَيِّبًا﴾ [المائدة: 6]؛ فلو كانت الطهارة تحصل بمائع غير الماء لأُرشد إليه من عدم الماء، ولم يُنقل إلى التراب.', False),
  ('كيف يدل حديث غسل ابنة النبي ﷺ على حكم الماء الذي خالطه طاهر؟', 'أمر ﷺ بغسلها «بِمَاءٍ وَسِدْرٍ»، والسدر طاهر يخالط الماء، فدلّ على أن الماء الذي خالطه طاهر ولم يغلب عليه باقٍ على طهوريته.', False),
  ('ما الحكمة من طهارة سؤر الهرة كما جاء في الحديث؟', 'رفع الحرج والمشقة؛ لأنها من الطوّافين على الناس في بيوتهم ويشق التحرز منها: «إِنَّهَا لَيْسَتْ بِنَجَسٍ، إِنَّمَا هِيَ مِنَ الطَّوَّافِينَ عَلَيْكُمْ وَالطَّوَّافَاتِ».', False),
  ('الماء المستعمل في الوضوء لا يجوز التطهر به مرة أخرى.', 'خطأ؛ هو طاهر مطهِّر على الصحيح ما لم يتغيّر، فقد كادوا يقتتلون على وَضوئه ﷺ، وصبّ وَضوءه على جابر، و«إِنَّ الْمُؤْمِنَ لَا يَنْجُسُ».', True),
  ('سؤر الحائض طاهر.', 'صح؛ لأن سؤر الآدمي طاهر، ومنه الجنب والحائض، و«إِنَّ الْمُؤْمِنَ لَا يَنْجُسُ» رواه مسلم.', True),
  ('الماء الكثير إذا غيّرت النجاسة لونه يبقى طهورًا لكثرته.', 'خطأ؛ ما تغيّر أحد أوصافه بالنجاسة نجس بالإجماع، قليلًا كان أو كثيرًا.', True),
 ],
}

def qa_cards(lang, items, start=1):
    s = S[lang]
    out = []
    fx = (lambda h: arabify(ayahify(h))) if lang == 'tr' else ayahify
    for k, it in enumerate(items):
        n = DIG(lang, start + k)
        tag = ''
        if it.get('extra'): tag += f'<span class="tf">{E(s["qaExtra"])}</span> '
        if it.get('tf'): tag += f'<span class="tf">{E(s["tf"])}</span>'
        out.append(f'''<li class="qcard"><span class="qn">{n}</span><div>{tag}<p class="qq">{fx(it["q"])}</p></div><button class="rev" type="button" aria-expanded="false">{E(s["qaShow"])}</button><p class="qa-a">{fx(it["a"])}</p></li>''')
    return '\n'.join(out)

# ------------------------------------------------------------------ pages
def page_series(lang, X=None):
    """page of a live series: its sections, then the section that has lessons, with its lessons"""
    X = X or MAIN; PAGE = X['page']; SEC = next(sec for sec in X['sections'] if sec['lessons']); LS = SEC['lessons']
    s = S[lang]; depth = 0 if lang == 'ar' else 1; u = up(depth); sx = SECT[SEC['key']][lang]
    other = f'tr/{PAGE}' if lang == 'ar' else f'../{PAGE}'
    lb = LIB[lang]
    latest = [L for L in LS if L['live']][-1]
    pts = []
    for i, p in enumerate(sx['points']):
        L = LS[i]
        inner = f'<span class="k">{E(sx["point"]) + " " + E(sx["ord"][i]) if lang == "ar" else E(sx["ord"][i]) + " " + E(sx["point"])}</span><span class="t">{E(p)}</span>'
        if L['live']:
            pts.append(f'<li class="live"><a href="{L["slug"]}/index.html">{inner}</a></li>')
        else:
            pts.append(f'<li>{inner}<span class="m">{E(s["soon"])}</span></li>')
    rows = []
    for L in LS:
        n = DIG(lang, L['num'])
        if L['live']:
            b = f'{L["slug"]}/'
            chips = []
            chips.append((I['text'], s['chipText'], f'{b}text.html'))
            chips += [(I['slides'], s['chipSlides'], f'{b}slides.html'), (I['map'], s['chipMap'], f'map.html#l{L["n"]}'), (I['qa'], s['chipQA'], f'{b}qa.html'), (I['quiz'], s['chipQuiz'], f'{b}quiz.html')]
            if (L['n'], lang) in SUM: chips.append((I['sum'], s['chipSum'], f'{b}summary.html'))
            ch = ''.join(f'<a class="chip" href="{h}">{ic}{E(t)}</a>' for ic, t, h in chips)
            rows.append(f'''<li class="lrow live"><span class="n">{n}</span><div><h3><a href="{b}index.html">{E(L[lang])}</a></h3><p>{E(L["descAr"] if lang == "ar" else L["descTr"])}</p><div class="chips">{ch}</div><p class="lprog" data-lesson="{L['n']}" hidden></p></div><a class="pill" href="{b}index.html">{E(s["open"])}</a></li>''')
        else:
            rows.append(f'''<li class="lrow"><span class="n">{n}</span><div><h3>{E(L[lang])}</h3><p>{E(s["lesson"])} {n}</p></div><span class="pill">{E(s["soon"])}</span></li>''')
    b = f'{latest["slug"]}/'
    meal = f'<p class="meal">{E(latest["verseTr"])}</p>' if lang == 'tr' else ''
    secs = []
    for sec in X['sections']:
        ls = sec['lessons']; live = [L for L in ls if L['live']]
        meta = f'{lessons_count(lang, len(ls))} · {published(lang, len(live))}' if ls else lb['sectionSoon']
        inner = f'<span class="k">{E(lb["section"])}</span><span class="t">{E(sec[lang])}</span><span class="m">{E(meta)}</span>'
        secs.append(f'<li class="live"><a href="#{sec["key"]}">{inner}</a></li>' if live else f'<li>{inner}</li>')
    cat = dict((c, ar if lang == 'ar' else tr) for c, ar, tr in CATS)[X['cat']]
    slead = X.get('leadAr' if lang == 'ar' else 'leadTr') or lb['sLead']
    squote = X.get('quoteAr' if lang == 'ar' else 'quoteTr') or lb['sQuote']
    smeal_t = (X.get('mealTr', '') if lang == 'tr' else '') if 'quoteAr' in X else lb['sQuoteMeal']
    smeal = f'<p class="smeal">{E(smeal_t)}</p>' if smeal_t else ''
    tools2 = (tool('quiz', (QALL[lang]['btn'], QALL[lang]['btnS']), 'quiz-all.html') if X.get('quizAll') else '') + tool('qa', (CARDS[lang]['title'], CARDS[lang]['sub']), 'cards.html')
    return head(lang, f'{X[lang]} · {s["brand"]}', depth, slead) + bar(lang, depth, other) + f'''<main id="main">
<section class="hero">{ORN}<div class="wrap"><div class="in">
  <div class="emblem"><img src="{u}media/logo.webp" alt="{E(s['brand'])}"></div>
  <div><nav class="crumbs hero-crumbs" aria-label="breadcrumb"><a href="index.html">{E(s['home'])}</a><span class="sep">›</span><a href="index.html#series">{E(cat)}</a></nav><h1>{E(X[lang])}</h1><p class="lead">{E(slead)}</p>
  <p class="quote">{squote}</p>{smeal}</div>
</div></div></section>

<section class="band"><div class="wrap">
  <h2>{E(lb['sectionsT'])}</h2><p class="sub">{E(lb['sectionsS'])}</p>
  <ol class="points secs">{''.join(secs)}</ol>
</div></section>

<section class="band tight sect" id="{SEC['key']}"><div class="wrap">
  <div class="secthead"><p class="eb">{E(lb['section'])}</p><h2>{E(sx['short'])}</h2><p class="sub">{E(sx['lead'])}</p>
  <p class="squote">{E(sx['quote'])}<small>{E(sx['quoteRef'])}</small></p></div>
  <h3 class="h3s">{E(sx['pointsT'])}</h3><p class="sub">{E(sx['pointsS'])}</p>
  <ol class="points">{''.join(pts)}</ol>
<h3 class="h3s">{E(s['latestT'])}</h3><p class="sub">{E(s['latestS'])}</p>
  <article class="open brief">
    <div>
      <span class="num">{E(s['lesson'])} {DIG(lang, latest['num'])}</span>
      <h3><a href="{b}index.html">{E(latest[lang])}</a></h3>
      <p>{E(latest['descAr'] if lang == 'ar' else latest['descTr'])}</p>
      <p class="verse" lang="ar" dir="rtl">{E(latest['verse'])}</p>{meal}
      <a class="btn" href="{b}index.html">{E(s['open'])} <span aria-hidden="true">{'←' if lang == 'ar' else '→'}</span></a>
    </div>
  </article>
  <h3 class="h3s" id="lessons">{E(s['listT'])}</h3><p class="sub">{E(s['listS'])}</p>
  <ol class="list">{''.join(rows)}</ol>
  <div class="tools grid" style="margin-top:18px">
    {tools2}
  </div>
  <p class="reset-wrap"><button class="linkbtn" id="progReset" type="button" hidden>{E(s['progReset'])}</button></p>
</div></section>

</main>
''' + footer(lang, depth) + f'<script src="{u}assets/site.js"></script>\n</body>\n</html>\n'

# ------------------------------------------------------------------ weekly tasks (daily task + reminders)
# src/tasks.json holds the weeks; each day: date (YYYY-MM-DD), ar, tr, and an optional href to a page of the site.
# The reminder service lives in remind/worker.js (Cloudflare); it reads docs/tasks.json from the live site.
REMIND_URL = 'https://khareeta.wtawasaw.workers.dev'
TASKS = json.load(open(f'{ROOT}/tasks.json', encoding='utf-8'))
HAS_TASKS = any(w.get('days') for w in TASKS.get('weeks', []))
TS = {
 'ar': dict(nav='الواجبات', title='واجبات الأسبوع',
    sub='واجب صغير كل يوم. اضغط «أنهيتُ» حين تنتهي منه، ويصلك تذكير كل ساعتين نهارًا حتى تضغطه.',
    backHome='الرجوع إلى الصفحة الرئيسية', today='واجب اليوم', week='واجب الأسبوع', openWeek='افتح الواجب', all='كل واجبات الأسبوع', none='لا واجب اليوم.',
    empty='لم تُنشر واجبات هذا الأسبوع بعد.', open='افتح', doneOff='أنهيتُ الواجب', doneOn='✓ أنهيتَ الواجب',
    rT='التذكير بالواجب', rOn='🔔 فعّل التذكير', askQ='هل تريد أن نذكّرك بواجب الغد؟', askNo='لا، شكرًا', rOff='أوقف التذكير', rIsOn='✓ التذكير مفعّل على هذا الجهاز.',
    rHelp='يصلك إشعار كل ساعتين من ١٠ صباحًا إلى ١٠ ليلًا، ويتوقف في اليوم الذي تضغط فيه «أنهيتُ».',
    rIos='على iPhone: ثبّت الموقع أولًا (زر المشاركة ← «إضافة إلى الشاشة الرئيسية»)، ثم افتحه من الشاشة الرئيسية واضغط «فعّل التذكير».',
    rNo='متصفحك لا يدعم الإشعارات. جرّب Chrome على Android، أو ثبّت الموقع على iPhone.',
    rDenied='الإشعارات ممنوعة لهذا الموقع في إعدادات المتصفح. اسمح بها ثم أعد المحاولة.',
    rErr='تعذّر تفعيل التذكير الآن. تأكد من الاتصال بالإنترنت وحاول مرة أخرى.',
    nTitle='واجب اليوم · وتواصوا بالحق', nDone='أنهيتُ',
    goalT='هدف الواجب', stepsT='طريقة التنفيذ', trackT='متابعة اليوم', tSeg='أتممتُ المقطع', tKept='تركتُ السب والشتم',
    yes='نعم', no='لا', why='سبب الإخفاق إن وقع', whyPh='اكتب السبب باختصار…', counterT='عدد الألفاظ اليوم',
    cmp='يوم الاثنين: {a} · اليوم: {b}', todayTag='اليوم', pledgeT='تعهّد', pledgeOn='✓ تعهّدتُ', pledgeOff='أتعهّد',
    notePh='اكتب هنا…', private='ما تكتبه هنا يُحفظ على جهازك فقط، ولا يراه أحد إلا إذا أرسلته أنت.',
    sendT='أرسِل واجبك للمعلّم', sendTab='أرسِل الواجب', missed='واجب {d} لم يُسجَّل بعد', missedBtn='سجّله الآن', sendHelp='يتحوّل واجب الأسبوع كاملًا إلى ملف PDF باسمك، ترسله للمعلّم بواتساب أو تيليجرام.',
    nameL='اسمك', namePh='اكتب اسمك', sendBtn='أرسِل واجبي', saveBtn='حفظ الملف', noName='اكتب اسمك أولًا.',
    imgDone='أنهى الواجب', imgNot='لم يُنهِ', imgNA='—', imgName='الاسم', imgWeek='من {a} إلى {b}', imgFile='واجبي',
    progDone='أنجزتَ {a} من {b}', progStart='يبدأ {d}', progAll='✓ أنجزتَ واجب الأسبوع كله'),
 'tr': dict(nav='Ödevler', title='Haftanın ödevleri',
    sub='Her gün küçük bir ödev. Bitirdiğinizde «Bitirdim»e dokunun; dokunana kadar gündüz iki saatte bir hatırlatma gelir.',
    backHome='Ana sayfaya dön', today='Bugünün ödevi', week='Haftanın ödevi', openWeek='Ödevi aç', all='Haftanın bütün ödevleri', none='Bugün ödev yok.',
    empty='Bu haftanın ödevleri henüz yayımlanmadı.', open='Aç', doneOff='Ödevi bitirdim', doneOn='✓ Ödevi bitirdiniz',
    rT='Ödev hatırlatması', rOn='🔔 Hatırlatmayı aç', askQ='Yarının ödevini sana hatırlatalım mı?', askNo='Hayır, teşekkürler', rOff='Hatırlatmayı kapat', rIsOn='✓ Bu cihazda hatırlatma açık.',
    rHelp='Sabah 10’dan gece 10’a kadar iki saatte bir bildirim gelir; «Bitirdim»e dokunduğunuz gün durur.',
    rIos='iPhone’da: Önce siteyi yükleyin (Paylaş ← «Ana Ekrana Ekle»), sonra ana ekrandan açıp «Hatırlatmayı aç»a dokunun.',
    rNo='Tarayıcınız bildirimleri desteklemiyor. Android’de Chrome’u deneyin ya da iPhone’da siteyi yükleyin.',
    rDenied='Bu site için bildirimler tarayıcı ayarlarında engellenmiş. İzin verip yeniden deneyin.',
    rErr='Hatırlatma şu an açılamadı. İnternet bağlantınızı kontrol edip yeniden deneyin.',
    nTitle='Bugünün ödevi · Ve Tevâsav bi’l-Hak', nDone='Bitirdim',
    goalT='Ödevin amacı', stepsT='Nasıl uygulanır', trackT='Günün takibi', tSeg='Bölümü bitirdim', tKept='Sövmeyi ve hakareti bıraktım',
    yes='Evet', no='Hayır', why='Aksama olduysa sebebi', whyPh='Sebebi kısaca yaz…', counterT='Bugünkü söz sayısı',
    cmp='Pazartesi: {a} · Bugün: {b}', todayTag='Bugün', pledgeT='Söz', pledgeOn='✓ Söz verdim', pledgeOff='Söz veriyorum',
    notePh='Buraya yaz…', private='Buraya yazdıkların yalnızca cihazında saklanır; sen göndermedikçe kimse görmez.',
    sendT='Ödevini hocana gönder', sendTab='Ödevi gönder', missed='{d} ödevi henüz kaydedilmedi', missedBtn='Şimdi kaydet', sendHelp='Haftanın ödevinin tamamı adınla bir PDF dosyasına dönüşür; onu WhatsApp ya da Telegram ile hocana gönderirsin.',
    nameL='Adın', namePh='Adını yaz', sendBtn='Ödevimi gönder', saveBtn='Dosyayı kaydet', noName='Önce adını yaz.',
    imgDone='Ödevi bitirdi', imgNot='Bitirmedi', imgNA='—', imgName='Ad', imgWeek='{a} – {b}', imgFile='odevim',
    progDone='{b} günden {a} tamamlandı', progStart='Başlangıç: {d}', progAll='✓ Haftanın bütün ödevlerini bitirdiniz'),
}
TS_KEYS = ['doneOff', 'doneOn', 'none', 'empty', 'open', 'rOn', 'rOff', 'rIsOn', 'rHelp', 'rIos', 'rNo', 'rDenied', 'rErr', 'nTitle', 'nDone']

def tasks_attrs(lang):
    t = TS[lang]
    return f'data-remind="{REMIND_URL}" data-tasks="{up(0 if lang == "ar" else 1)}tasks.json" data-ts="{E(json.dumps(t, ensure_ascii=False))}"'

def page_tasks(lang):
    s, t = S[lang], TS[lang]; depth = 0 if lang == 'ar' else 1; u = up(depth)
    other = 'tr/tasks.html' if lang == 'ar' else '../tasks.html'
    crumbs = f'<a href="index.html">{E(s["home"])}</a><span class="sep">›</span><span>{E(t["title"])}</span>'
    back = ('→ ' if lang == 'ar' else '← ') + E(t['backHome'])
    return head(lang, f'{t["title"]} · {s["brand"]}', depth, t['sub']) + bar(lang, depth, other) + f'''<main id="main" class="tasks-page" {tasks_attrs(lang)}>
<section class="phead">{ORN}<div class="wrap">
  <nav class="crumbs" aria-label="breadcrumb">{crumbs}</nav>
  <h1>{E(t['title'])}</h1><p>{E(t['sub'])}</p>
  <a class="btn ghost back" href="index.html">{back}</a>
</div></section>
<section class="band"><div class="wrap">
  <div class="wksk" id="wkSk" aria-hidden="true"></div>
  <div id="wkIntro"></div>
  <div class="rcard" data-rcard="page" hidden></div>
  <div id="wkHead"></div>
  <ol class="tlist" id="taskList"></ol>
  <div id="wkFinal"></div>
  <p class="tprivate">{E(t['private'])}</p>
  <p class="noresult" id="taskEmpty" hidden>{E(t['empty'])}</p>
  <p class="backrow"><a class="btn back2" href="index.html">{back}</a></p>
</div></section>
</main>
''' + footer(lang, depth) + f'<script src="{u}assets/site.js"></script>\n</body>\n</html>\n'

def today_band(lang):
    """card on the home page with today's task (filled by site.js); only when tasks are published"""
    if not HAS_TASKS: return ''
    t = TS[lang]
    return f'''<section class="band" id="todayBand" hidden {tasks_attrs(lang)}><div class="wrap">
  <div class="today"><span class="ic">{I['quiz']}</span><div><p class="where" id="todayWhere">{E(t['today'])}</p><p class="tseg" id="todaySeg"></p><p class="ttext" id="todayText"></p><a class="btn tgo" href="tasks.html">{E(t['all'])}</a></div><button class="donebtn" type="button" id="todayDone"></button></div>
  <div class="rcard" data-rcard="home" hidden></div>
</div></section>
'''

SEARCH_I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'

def page_library(lang):
    """home page: every series, with search, category filter, «continue where you stopped» and the latest lessons"""
    s, lb = S[lang], LIB[lang]; depth = 0 if lang == 'ar' else 1; u = up(depth)
    other = 'tr/index.html' if lang == 'ar' else '../index.html'
    catname = dict((c, ar if lang == 'ar' else tr) for c, ar, tr in CATS)
    counts = {c: sum(1 for x in SERIES if x['cat'] == c) for c, _, _ in CATS}
    cats = f'<li><button type="button" class="on" data-cat="">{E(lb["all"])}<span>{DIG(lang, len(SERIES))}</span></button></li>'
    cats += ''.join(f'<li><button type="button" data-cat="{c}">{E(catname[c])}<span>{DIG(lang, counts[c])}</span></button></li>' for c, _, _ in CATS if counts[c])
    cards, soon = [], []
    for x in SERIES:
        by = x['byAr'] if lang == 'ar' else x['byTr']
        q = ' '.join([x['ar'], x['tr'], by, catname[x['cat']]] + [sec['ar'] + ' ' + sec['tr'] for sec in x.get('sections', [])])
        if x['status'] == 'live':
            secs = x['sections']; allL = [L for sec in secs for L in sec['lessons']]; live = [L for L in allL if L['live']]
            names = ' · '.join(sec[lang] for sec in secs)
            q += ' ' + ' '.join(L['ar'] + ' ' + L['tr'] for L in live)
            body = f'''<p class="sec">{I['text']}<span>{E(names)}</span></p><p class="meta">{E(sections_count(lang, len(secs)))} · {E(published(lang, len(live)))}</p>
<p class="sprog" data-lessons="{','.join(str(L['n']) for L in live)}" hidden></p>
<div class="ft"><a class="go" href="{x['page']}">{E(lb['open'])} <span aria-hidden="true">{'←' if lang == 'ar' else '→'}</span></a></div>'''
            title = f'<a href="{x["page"]}">{E(x[lang])}</a>'
        else:
            # not available yet: one short card (title + state), so the student reaches the lessons sooner
            cards.append(f'''<li class="scard mini {x['cat']} {x['status']}" data-cat="{x['cat']}" data-q="{E(q)}"><div class="cover"><div class="top"><p class="tag">{E(catname[x['cat']])}</p><span class="spill {x["status"]}">{E(lb["st"][x["status"]])}</span></div><h3>{E(x[lang])}</h3>{f'<p class="by">{E(by)}</p>' if by else ''}</div></li>''')
            continue
        cards.append(f'''<li class="scard {x['cat']} {x['status']}" data-cat="{x['cat']}" data-q="{E(q)}"><div class="cover"><p class="tag">{E(catname[x['cat']])}</p><h3>{title}</h3>{f'<p class="by">{E(by)}</p>' if by else ''}</div>
<div class="bd">{body}</div></li>''')
    # latest lessons, newest first, from every live series
    rows, cont = [], {}
    for x in SERIES:
        for sec in x.get('sections', []):
            for L in sec['lessons']:
                if not L['live']: continue
                where = f'{x[lang]} · {sec[lang]}'
                cont[L['n']] = dict(t=f'{s["lesson"]} {DIG(lang, L["num"])}: {L[lang]}', w=where)
                rows.append(f'''<li class="lrow live" data-q="{E(L['ar'] + ' ' + L['tr'] + ' ' + x['ar'] + ' ' + x['tr'] + ' ' + sec['ar'] + ' ' + sec['tr'])}"><div><p class="where">{E(where)} · {E(s['lesson'])} {DIG(lang, L['num'])}</p><h3><a href="{L['slug']}/index.html">{E(L[lang])}</a></h3><p class="lprog" data-lesson="{L['n']}" hidden></p></div><a class="pill" href="{L['slug']}/index.html">{E(lb['openL'])}</a></li>''')
    rows.reverse(); rows = rows[:5]
    redirect = f'''<script>{{ const h = location.hash, m = /^#l(\\d+)$/.exec(h); if (m) location.replace('map.html' + h); else if (h === '#lessons') location.replace('{MAIN_PAGE}#lessons'); }}</script>'''
    data = json.dumps(cont, ensure_ascii=False).replace('</', '<\\/')
    return head(lang, f'{s["brand"]} · {lb["title"]}', depth, lb['lead']) + redirect + bar(lang, depth, other) + f'''<main id="main" class="lib">
<section class="hero">{ORN}<div class="wrap"><div class="in">
  <div class="emblem"><img src="{u}media/logo.webp" alt="{E(s['brand'])}"></div>
  <div><p class="eb">{E(s['eb'])}</p><h1>{E(lb['title'])}</h1><p class="lead">{E(lb['lead'])}</p>
  <label class="srch">{SEARCH_I}<input id="libQ" type="search" placeholder="{E(lb['search'])}" aria-label="{E(lb['search'])}" autocomplete="off"></label></div>
</div></div></section>

{today_band(lang)}<section class="band tight" id="cardBand" data-due="{E(CARDS[lang]['homeDue'])}" data-none="{E(CARDS[lang]['homeNone'])}" hidden><div class="wrap">
  <div class="cont cardcont"><span class="ic">{I['quiz']}</span><div><p class="where">{E(CARDS[lang]['homeT'])}</p><h3 id="cardMsg"></h3></div><a class="btn" href="cards.html">{E(CARDS[lang]['homeB'])}</a></div>
</div></section>

<section class="band" id="contBand" hidden><div class="wrap">
  <h2>{E(lb['contT'])}</h2>
  <div class="cont"><span class="ic">{I['text']}</span><div><p class="where" id="contW"></p><h3 id="contT"></h3><p class="lprog" id="contP" hidden></p></div><a class="btn" id="contA" href="#">{E(lb['contB'])}</a></div>
</div></section>

<section class="band tight" id="latest"><div class="wrap">
  <h2>{E(lb['latestT'])}</h2>
  <ol class="list">{''.join(rows)}</ol>
</div></section>

<section class="band tight" id="inBand" hidden><div class="wrap">
  <h2>{E(lb['inT'])}</h2><p class="sub" id="inCount"></p>
  <ol class="hits" id="inHits"></ol>
  <p><button class="btn line" id="inMore" type="button" hidden>{E(lb['inMore'])}</button></p>
</div></section>

<section class="band" id="series"><div class="wrap">
  <h2>{E(lb['seriesT'])}</h2>
  <ul class="cats" aria-label="{E(lb['seriesT'])}">{cats}</ul>
  <ul class="sgrid">{''.join(cards)}</ul>
  <p class="noresult" id="noResult" hidden>{E(lb['noResult'])}</p>
</div></section>

<section class="band tight" id="teaserBand"><div class="wrap">
  <div class="teaser">
    <div class="vbox player" data-soon="{E(s['tzSoon'])}" data-logo="{u}media/logo.webp"><video controls preload="metadata" playsinline poster="{u}media/poster-teaser.jpg" data-check><source src="{u}media/teaser.mp4" type="video/mp4"></video></div>
    <div><h2>{E(s['tzT'])}</h2><p>{E(s['tzD'])}</p></div>
  </div>
</div></section>
</main>
<script type="application/json" id="libData">{data}</script>
''' + footer(lang, depth) + f'<script src="{u}assets/site.js"></script>\n</body>\n</html>\n'

def lesson_paths(lang, L):
    """relative links from a lesson folder page (l1/x.html or tr/l1/x.html)"""
    n, sl = L['n'], L['slug']
    return dict(
        home='../index.html',
        text='text.html',
        slides='slides.html', qa='qa.html', quiz='quiz.html', hub='index.html',
        map=f'../map.html#l{n}',
        media='../media/' if lang == 'ar' else '../../media/',
        assets='../assets/' if lang == 'ar' else '../../assets/',
        other=lambda page: (f'../tr/{sl}/{page}' if lang == 'ar' else f'../../{sl}/{page}'),
    )

def phead(lang, L, title, sub, crumbs_extra=None):
    s = S[lang]; X, SEC = where_of(L); sx = SECT[L['sk']][lang]; k = L['num']
    eb = f'{s["lesson"]} {DIG(lang, k)} · ' + (f'{sx["point"]} {sx["ord"][k-1]} {sx["of"]}' if lang == 'ar' else f'{sx["ord"][k-1]} {sx["point"]} {sx["of"]}')
    cr = f'<a href="../index.html">{E(s["home"])}</a><span class="sep">›</span><a href="../{X["page"]}#{SEC["key"]}">{E(X[lang])}</a><span class="sep">›</span>'
    if crumbs_extra:
        cr += f'<a href="index.html">{E(s["lesson"])} {DIG(lang, k)}</a><span class="sep">›</span><span>{E(crumbs_extra)}</span>'
    else:
        cr += f'<span>{E(s["lesson"])} {DIG(lang, k)}</span>'
    return f'''<section class="phead">{ORN}<div class="wrap">
  <nav class="crumbs" aria-label="breadcrumb">{cr}</nav>
  <p class="eb">{E(eb)}</p><h1>{E(title)}</h1>{f'<p>{E(sub)}</p>' if sub else ''}
</div></section>
'''

def page_hub(lang, L):
    s = S[lang]; P = lesson_paths(lang, L); depth = 1 if lang == 'ar' else 2
    n = L['n']
    tools = []
    tools.append(tool('text', s['tText'], P['text'], True))
    tools += [tool('slides', s['tSlides'], P['slides']), tool('map', s['tMap'], P['map']), tool('qa', s['tQA'], P['qa']), tool('quiz', s['tQuiz'], P['quiz'])]
    if L['n'] in SHARH:
        tools.insert(1, tool('text', s['tSharh'], 'sharh.html'))
    if (L['n'], lang) in SUM:
        tools.append(tool('sum', s['tSum'], 'summary.html'))
    sh = share_img(lang, L)
    if sh:
        tools.append(tool('share', s['tShare'], f'{P["media"]}{sh}').replace('<a class="tool" href=', '<a class="tool" download href=', 1))
    meal = f'<p class="meal">{E(L["verseTr"])}</p>' if lang == 'tr' else ''
    path = ''.join(f'<li>{E(x)}</li>' for x in s['path'])
    SL = sect_live(L); idx = SL.index(L); X, SEC = where_of(L)
    pager = ''
    if idx > 0:
        pv = SL[idx-1]; pager += f'<a href="../{pv["slug"]}/index.html"><small>{E(s["prev"])}</small><b>{E(pv[lang])}</b></a>'
    if idx < len(SL) - 1:
        nx = SL[idx+1]; pager += f'<a class="nx" href="../{nx["slug"]}/index.html"><small>{E(s["next"])}</small><b>{E(nx[lang])}</b></a>'
    return head(lang, f'{L[lang]} · {SEC[lang]} · {X[lang]}', depth, L['descAr'] if lang == 'ar' else L['descTr'], image=share_img(lang, L)) + bar(lang, depth, P['other']('index.html')) + '<main id="main">\n' + phead(lang, L, L[lang], L['descAr'] if lang == 'ar' else L['descTr']) + f'''
<section class="band"><div class="wrap">
  <article class="open">
    {player(lang, L, P['media'][:-6])}
    <div>
      <p class="verse" lang="ar" dir="rtl">{E(L['verse'])}</p>{meal}
      <h3 style="font-size:20px;margin-top:4px">{E(s['pathT'])}</h3>
      <ol class="prose" style="font-size:16.5px;line-height:1.8;margin:0;padding-inline-start:1.3em">{path}</ol>
    </div>
  </article>
</div></section>

<section class="band tight"><div class="wrap">
  <h2>{E(s['toolsT'])}</h2>
  <p class="prog" data-lesson="{n}" hidden></p>
  <div class="tools grid">{''.join(tools)}</div>
  <div class="lesson-done"><p>{E(s['doneHint'])}</p>{done_btn(lang, n, 'lesson', 'donebtn big')}</div>
</div></section>
{f'<section class="band tight"><div class="wrap"><nav class="pager">{pager}</nav></div></section>' if pager else ''}
</main>
''' + footer(lang, depth) + dialog(lang) + f'<script src="{P["assets"]}site.js"></script>\n</body>\n</html>\n'


_YES, _NO = {'نعم', 'Evet'}, {'لا', 'Hayır'}

def tables_to_cards(body):
    """Tables read badly on a phone, so every lesson table becomes cards (decided with the author):
       - a comparison table (empty top-left cell, 2+ things compared) → one card per compared thing;
       - a table whose last column is only yes/no → a short list with ✓ / ✗;
       - any other table → one card per row, titled by its first cell.
       Decision tables are written by hand in the lesson as <ol class="flow"> question steps."""
    def conv(m):
        t = m.group(1)
        head = [c.strip() for c in re.findall(r'<th[^>]*>(.*?)</th>', t, re.S)]
        rows = [[c.strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)] for r in re.findall(r'<tr>(.*?)</tr>', t, re.S)]
        rows = [r for r in rows if r]
        n = len(head)
        if not rows or n < 2: return m.group(0)
        last = {re.sub('<[^>]+>', '', r[-1]).strip() for r in rows}
        if n >= 3 and last <= (_YES | _NO):
            li = ''.join(f'<li><span class="ic {"yes" if re.sub("<[^>]+>", "", r[-1]).strip() in _YES else "no"}" aria-hidden="true">'
                         f'{"✓" if re.sub("<[^>]+>", "", r[-1]).strip() in _YES else "✗"}</span><span><strong>{re.sub("</?strong>", "", r[0])}</strong>: '
                         + '، '.join(r[1:-1]) + f' <span class="vlh">({head[-1]} {r[-1]})</span></span></li>' for r in rows)
            return f'<ul class="vl">{li}</ul>'
        if not re.sub('<[^>]+>', '', head[0]).strip() and n >= 3:
            cards = ''.join(f'<div class="cc"><h4>{head[j]}</h4><dl>' + ''.join(f'<dt>{re.sub("</?strong>", "", r[0])}</dt><dd>{r[j]}</dd>' for r in rows) + '</dl></div>' for j in range(1, n))
            return f'<div class="cmp">{cards}</div>'
        out = []
        for r in rows:
            title = re.sub('</?strong>', '', r[0])
            if n == 2: inner = f'<p>{r[1]}</p>'
            else: inner = '<dl>' + ''.join(f'<dt>{head[j]}</dt><dd>{r[j]}</dd>' for j in range(1, n)) + '</dl>'
            out.append(f'<div class="rc"><h4>{title}</h4>{inner}</div>')
        return f'<div class="rcs">{"".join(out)}</div>'
    return re.sub(r'<div class="tbl"><table>(.*?)</table></div>', conv, body, flags=re.S)

def lesson_doc(lang, L):
    """The written lesson: markdown → (html body, its table of contents).
       Used by the lesson page and by the search index, so both always see the same headings and ids."""
    md = open(f'{ROOT}/content/{L["doc"]}-{lang}.md', encoding='utf-8').read()
    body = markdown.markdown(md, extensions=['tables', 'sane_lists'])
    body = re.sub(r'<table>', '<div class="tbl"><table>', body); body = body.replace('</table>', '</table></div>')
    body = tables_to_cards(body)
    toc = []; c = [0]
    def hid(m):
        c[0] += 1; tag, txt = m.group(1), m.group(2)
        i = f's{c[0]}'
        if tag == 'h2': toc.append((i, re.sub('<[^>]+>', '', txt)))
        return f'<{tag} id="{i}">{txt}</{tag}>'
    body = re.sub(r'<(h[23])>(.*?)</\1>', hid, body)
    body = ayahify(body)
    if lang == 'tr': body = arabify(body)
    return body, toc

def plain(h):
    """html → the words in it, one space between them (for the search index)"""
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()

def search_index(lang):
    """What the search on the home page looks in: every section of every written lesson, and every question.
       Each entry: [lesson number, where it is, link, text]. The file is saved for offline use with the rest."""
    out = []
    for L in ALL_LIVE:
        n, sl = L['n'], L['slug']
        body, _ = lesson_doc(lang, L)
        # split the lesson at its main headings: one entry per section, linking to that heading
        parts = re.split(r'<h2 id="(s\d+)">(.*?)</h2>', body)
        for k in range(1, len(parts), 3):
            sid, hd, txt = parts[k], plain(parts[k + 1]), plain(parts[k + 2])
            if txt: out.append([n, hd, f'{sl}/text.html#{sid}', txt])
        DQ = DOCQA if lang == 'ar' else DOCQA_TR
        for q, a, _tf in DQ.get(n, []):
            out.append([n, S[lang]['qaT'], f'{sl}/qa.html', plain(q) + ' — ' + plain(a)])
    return out


_HAR = '[ً-ْٰـ]*'
def _ar_re(word):
    L = [('[اأإآ]' if ch in 'اأإآ' else re.escape(ch)) for ch in word]   # alif/hamza forms match each other
    return '(?<![ء-ي])(?:[وفبلك]' + _HAR + ')?' + _HAR.join(L) + _HAR + '(?![ء-ي])'
_GL_TR = re.compile('|'.join(f'(?P<{t["k"]}>(?<!\\w){t["re"]})' for t in sozluk.TR))
_GL_AR = [(re.compile(_ar_re(w)), k, None) for w, k in sozluk.AR] + [(re.compile(_ar_re(f)), t['k'], t.get('docs')) for t in sozluk.AR_TERMS for f in t['forms']]
_AR_T = {t['k']: t for t in sozluk.AR_TERMS}

def gloss_mark(body, lang, doc=''):
    """Mark the first occurrence, in each h2 section, of every glossary word (sozluk.py).
       Returns (html, {key: popup data}). Headings, links, buttons and Qur'an text are left alone."""
    used_all = {}; parts = re.split(r'(<[^>]+>)', body); skip = 0; seen = set(); out = []
    for part in parts:
        if part.startswith('<'):
            m = re.match(r'<(/?)(h[1-4]|a|button|summary)\b', part)
            if m: skip += -1 if m.group(1) else 1
            if re.match(r'<h2\b', part): seen = set()
            out.append(part); continue
        if skip or not part.strip(): out.append(part); continue
        segs = re.split(r'(﴿[^﴾]*﴾)', part); res = []
        for seg in segs:
            if seg.startswith('﴿'): res.append(seg); continue
            if lang == 'tr':
                def rep(m):
                    k = m.lastgroup
                    if k in seen: return m.group(0)
                    seen.add(k); used_all[k] = 1
                    return f'<button type="button" class="gl" data-k="{k}" aria-expanded="false">{m.group(0)}</button>'
                res.append(_GL_TR.sub(rep, seg))
            else:
                for rx, k, only in _GL_AR:
                    if k in seen or (only and doc not in only): continue
                    m = rx.search(seg)
                    if m and not re.search(r'<button[^>]*>[^<]*$', seg[:m.start()]):
                        seen.add(k); used_all[k] = 1
                        seg = seg[:m.start()] + f'<button type="button" class="gl" data-k="{k}" aria-expanded="false">{m.group(0)}</button>' + seg[m.end():]
                res.append(seg)
        out.append(''.join(res))
    html = ''.join(out)
    data = {}
    if lang == 'tr':
        T = {t['k']: t for t in sozluk.TR}
        for k in used_all: data[k] = dict(w=T[k]['w'], m=T[k]['m'], **({'src': T[k]['src']} if T[k].get('src') else {}))
    else:
        for k in used_all:
            if k in _AR_T: t = _AR_T[k]; data[k] = dict(w=t['w'], m=t['m'], **({'src': t['src']} if t.get('src') else {}))
            else: g = GLOSS[k]; data[k] = dict(w=g['w'], m=g['ar'], src=g['src'])
    return html, data

def page_text(lang, L):
    s = S[lang]; P = lesson_paths(lang, L); n = L['n']; depth = 1 if lang == 'ar' else 2
    body, toc = lesson_doc(lang, L)
    body, gdata = gloss_mark(body, lang, L['doc'])
    gl = (f'<p class="hint">{E(s["glHint"])}</p>' if gdata else '')
    gjs = (f'<script type="application/json" id="glData">' + json.dumps(gdata, ensure_ascii=False).replace('</', '<\\/') + '</script>' + SHARH_JS) if gdata else ''
    tocl = ''.join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, t in toc)
    return head(lang, f'{L[lang]} · {s["tText"][0]}', depth, L['descAr'] if lang == 'ar' else L['descTr'], extra=('\n' + GL_CSS) if gdata else '', image=share_img(lang, L)) + bar(lang, depth, P['other']('text.html')) + f'<main id="main" data-lesson="{n}" data-page="text">\n' + phead(lang, L, L[lang], s['textSub'], s['tText'][0]) + f'''
<section class="band"><div class="wrap"><div class="doc">
  <article class="prose">{fs_ctl(lang)}{gl}{body}
    <div class="endcta"><p>{E(s['textEnd'])}</p><div style="display:flex;gap:8px;flex-wrap:wrap">{done_btn(lang, n, 'text')}<a class="btn" href="qa.html">{E(s['tQA'][0])}</a><a class="btn ghost" href="quiz.html">{E(s['tQuiz'][0])}</a></div></div>
  </article>
  <aside class="toc"><details open><summary>{E(s['toc'])} <span aria-hidden="true">▾</span></summary><ol>{tocl}</ol></details></aside>
</div></div></section>
{gjs}
</main>
''' + footer(lang, depth) + '''<script>if (innerWidth < 960) document.querySelector('.toc details').open = false;</script>''' + f'<script src="{P["assets"]}site.js"></script>\n</body>\n</html>\n'

SHARH_CSS = """<style>
.sh-src{font-size:.88em;color:var(--muted);margin:0 0 6px}
.sh-p{margin:18px 0 26px}
.matn{background:var(--parch2);border:1px solid var(--line);border-radius:14px;padding:16px 20px;font-family:var(--af);font-size:1.14em;line-height:1.95;color:var(--ink);direction:rtl;text-align:right}
.matn .pg{display:block;font-family:var(--uf);font-size:.68em;color:var(--gold);margin-bottom:4px}
.matn .ayah{font-size:1.04em}
.sh-tr{margin:10px 4px 0;line-height:1.8}
.sh-tr small{display:block;font-family:var(--uf);font-weight:700;color:var(--gold);font-size:.78em;margin-bottom:2px}
.gl{all:unset;cursor:pointer;color:inherit;border-bottom:2px dotted var(--goldl);padding:0 1px 1px;border-radius:3px}
.gl:hover,.gl.on,.gl:focus-visible{background:rgba(217,178,106,.22)}
.glpop{position:absolute;z-index:30;max-width:320px;background:var(--band);color:var(--onband);font:500 15px/1.75 var(--uf);padding:10px 14px;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.25);border:1px solid var(--goldl)}
.glpop b{color:var(--goldl);display:block;font-family:var(--af);font-size:1.15em;margin-bottom:2px}
.glpop .ar2{display:block;font-family:var(--af);direction:rtl;text-align:right;opacity:.85;margin-top:4px}
.glpop small{display:block;color:var(--onband3);font-size:.8em;margin-top:6px}
.sh-fn{margin:8px 4px 0;font-size:.9em}
.sh-fn summary{cursor:pointer;color:var(--gold);font-family:var(--uf);font-weight:600}
.sh-fn ol{list-style:none;margin:6px 0 0;padding:0;font-family:var(--af);direction:rtl;text-align:right;line-height:1.9;color:var(--body)}
.sh-note{margin:8px 4px 0;padding:8px 12px;border-inline-start:3px solid var(--goldl);background:rgba(217,178,106,.1);border-radius:6px;font-size:.92em}
.sh-sharh{margin:12px 4px 0}
.sh-sharh .lbl{font-family:var(--uf);font-weight:700;color:var(--gold)}
.sh-audio{width:100%;margin-top:10px}
.sh-gl dt{font-family:var(--af);font-size:1.15em;color:var(--ink);margin-top:12px;font-weight:700}
.sh-gl dd{margin:2px 0 0}
.sh-gl dd small{color:var(--muted)}
</style>"""

SHARH_JS = r"""<script>(function(){var G=JSON.parse(document.getElementById('glData').textContent),pop=null,cur=null;
function close(){if(pop)pop.remove();pop=null;if(cur){cur.classList.remove('on');cur.setAttribute('aria-expanded','false')}cur=null}
document.addEventListener('click',function(e){var b=e.target.closest('.gl');if(!b){if(!e.target.closest('.glpop'))close();return}
if(cur===b){close();return}close();var g=G[b.dataset.k];if(!g)return;cur=b;b.classList.add('on');b.setAttribute('aria-expanded','true');
pop=document.createElement('div');pop.className='glpop';pop.setAttribute('role','status');
var t=document.createElement('b');t.textContent=g.w;pop.appendChild(t);pop.appendChild(document.createTextNode(g.m));
if(g.ar){var a=document.createElement('span');a.className='ar2';a.lang='ar';a.textContent=g.ar;pop.appendChild(a)}
if(g.src){var sm=document.createElement('small');sm.textContent=g.src;pop.appendChild(sm)}document.body.appendChild(pop);
var r=b.getBoundingClientRect(),w=Math.min(320,innerWidth-24);pop.style.maxWidth=w+'px';
var x=r.left+r.width/2-pop.offsetWidth/2+scrollX;x=Math.max(12+scrollX,Math.min(x,innerWidth-pop.offsetWidth-12+scrollX));
pop.style.left=x+'px';pop.style.top=(r.bottom+8+scrollY)+'px'});
addEventListener('keydown',function(e){if(e.key==='Escape')close()});addEventListener('resize',close)})();</script>"""

GL_CSS = '<style>' + '\n'.join(l for l in SHARH_CSS.splitlines() if l.startswith(('.gl', '.glpop'))) + '</style>'

def sharh_inline(t):
    return re.sub(r'\[\[([^|\]]+)\|(\w+)\]\]', lambda m: f'<button type="button" class="gl" data-k="{m.group(2)}" aria-expanded="false">{m.group(1)}</button>', t)

def page_sharh(lang, L):
    """The book's text paragraph by paragraph (sharh.py), with tap-a-word meanings."""
    s = S[lang]; P = lesson_paths(lang, L); depth = 1 if lang == 'ar' else 2; n = L['n']
    out = []; used = []
    for sec in SHARH[n]:
        if lang == 'ar': out.append(f'<h2>{E(sec["ar"])}</h2>')
        else: out.append(f'<h2>{E(sec["tr"])}</h2><p class="ar" lang="ar" dir="rtl" style="margin:-6px 0 8px;color:var(--muted)">{E(sec["ar"])}</p>')
        for p in sec['paras']:
            used += re.findall(r'\|(\w+)\]\]', p['ar'])
            h = f'<div class="sh-p"><div class="matn" lang="ar" dir="rtl"><span class="pg">({E(p["pg"])})</span>{ayahify(sharh_inline(p["ar"]))}</div>'
            if lang == 'tr': h += f'<p class="sh-tr"><small>{E(s["sharhTr"])}</small>{E(p["tr"])}</p>'
            if p.get('note'): h += f'<p class="sh-note">{E(p["note"][lang])}</p>'
            if p.get('sharh') and p['sharh'].get(lang):
                h += f'<div class="sh-sharh"><span class="lbl">{E(s["sharhLbl"])}:</span>{ayahify(markdown.markdown(p["sharh"][lang]))}</div>'
            if p.get('audio') and p['audio'].get(lang):
                h += f'<audio class="sh-audio" controls preload="none" src="{P["media"]}{p["audio"][lang]}"></audio>'
            if p['fn']:
                h += f'<details class="sh-fn"><summary>{E(s["sharhFn"])}</summary><ol>' + ''.join(f'<li>{E(x)}</li>' for x in p['fn']) + '</ol></details>'
            out.append(h + '</div>')
    gdata = {}
    for k in dict.fromkeys(used):
        g = GLOSS[k]
        gdata[k] = dict(w=g['w'], m=g['ar'], src=g['src']) if lang == 'ar' else dict(w=g['w'], m=g['tr'], ar=g['ar'], src=GLOSS_TR_SRC.get(g['src'], g['src']))
    gl = ''.join(f'<dt lang="ar">{E(d["w"])}</dt><dd>{E(d["m"])}' + (f'<br><span class="ar" lang="ar" dir="rtl">{E(d["ar"])}</span>' if lang == 'tr' else '') + f' <small>({E(s["sharhGlSrc"])}: {E(d["src"])})</small></dd>' for d in gdata.values())
    data = json.dumps(gdata, ensure_ascii=False).replace('</', '<\\/')
    top = head(lang, f'{L[lang]} · {s["tSharh"][0]}', depth, L['descAr'] if lang == 'ar' else L['descTr'], extra='\n' + SHARH_CSS, image=share_img(lang, L)) + bar(lang, depth, P['other']('sharh.html'))
    top += f'<main id="main" data-lesson="{n}" data-page="sharh">\n' + phead(lang, L, L[lang], s['sharhSub'], s['tSharh'][0])
    body = f'''
<section class="band"><div class="wrap narrow">
  <article class="prose">{fs_ctl(lang)}
    <p class="sh-src">{E(s['sharhSrc'].format(b=BOOK[lang]))}</p>
    <p class="hint">{E(s['sharhHint'])}</p>
    {''.join(out)}
    <h2>{E(s['sharhGl'])}</h2>
    <dl class="sh-gl">{gl}</dl>
    <div class="endcta"><p>{E(L[lang])}</p><div style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn" href="text.html">{E(s['tText'][0])}</a><a class="btn ghost" href="index.html">{E(s['backLesson'])}</a></div></div>
  </article>
</div></section>
<script type="application/json" id="glData">{data}</script>
{SHARH_JS}
</main>
'''
    return top + body + footer(lang, depth) + f'<script src="{P["assets"]}site.js"></script>\n</body>\n</html>\n'

def page_qa(lang, L):
    s = S[lang]; P = lesson_paths(lang, L); depth = 1 if lang == 'ar' else 2
    deck = L['deckAr'] if lang == 'ar' else L['deckTr']
    g1 = deck_qa(deck) + EXTRA.get(deck, [])
    total = len(g1)
    groups = f'<section class="qgroup"><h2>{E(s["qaG1"])}</h2><ol class="qlist">{qa_cards(lang, g1)}</ol></section>'
    DQ = DOCQA if lang == 'ar' else DOCQA_TR
    if L['n'] in DQ:
        g2 = [dict(q=q, a=a, tf=tf) for q, a, tf in DQ[L['n']]]
        total += len(g2)
        groups += f'<section class="qgroup"><h2>{E(s["qaG2"])}</h2><ol class="qlist">{qa_cards(lang, g2, len(g1) + 1)}</ol></section>'
    return head(lang, f'{s["qaT"]} · {L[lang]}', depth, image=share_img(lang, L)) + bar(lang, depth, P['other']('qa.html')) + f'<main id="main" data-lesson="{L["n"]}" data-page="qa">\n' + phead(lang, L, s['qaT'], f'{L[lang]} · ' + s['qaS'], s['qaT']) + f'''
<section class="band"><div class="wrap narrow">
  <p class="hint">{E(s['qaHint'])}</p>
  <div class="qa-tools">{fs_ctl(lang)}<span class="count">{E(s['qaCount'].format(n=DIG(lang, total)))}</span><button class="btn line" id="qaAll" type="button">{E(s['qaAll'])}</button></div>
  {groups}
  <div class="endcta"><p>{E(L[lang])}</p><div style="display:flex;gap:8px;flex-wrap:wrap">{done_btn(lang, L['n'], 'qa')}<a class="btn" href="quiz.html">{E(s['tQuiz'][0])}</a><a class="btn ghost" href="index.html">{E(s['backLesson'])}</a></div></div>
</div></section>
</main>
''' + footer(lang, depth) + f'<script src="{P["assets"]}site.js"></script>\n</body>\n</html>\n'

def page_quiz(lang, L):
    s = S[lang]; P = lesson_paths(lang, L); depth = 1 if lang == 'ar' else 2
    data = '../data.js' if lang == 'ar' else '../data_tr.js'
    return head(lang, f'{s["quizT"]} · {L[lang]}', depth, image=share_img(lang, L)) + bar(lang, depth, P['other']('quiz.html')) + f'<main id="main" data-lesson="{L["n"]}" data-page="quiz">\n' + phead(lang, L, s['quizT'], f'{L[lang]} · ' + s['quizS'], s['quizT']) + f'''
<section class="band"><div class="wrap narrow">
  <div class="quiz" id="quiz" data-lesson="{L['n']}" aria-live="polite">
    <div id="qcard">
      <p class="qprog"><span id="qprog"></span><span id="qscoreNow"></span></p>
      <div class="bar2"><i id="qbar"></i></div>
      <p class="qtext" id="qtext"></p>
      <div class="qopts" id="qopts"></div>
      <div class="qfb" id="qfb"></div>
      <div class="acts"><button class="btn" id="qnext" hidden></button></div>
    </div>
    <div id="qres" hidden>
      <svg class="ring" id="qring" viewBox="0 0 120 120" aria-hidden="true"></svg>
      <p class="score" id="qscore"></p>
      <p id="qmsg" style="color:var(--mint);margin:0"></p>
      <p id="qwrongT" style="margin:18px 0 0;font-family:var(--hf);color:var(--goldl)">{E(s['wrongT'])}</p>
      <ul class="review" id="qwrong"></ul>
      <div class="acts">{done_btn(lang, L['n'], 'quiz')}<button class="btn" id="qretry">{E(s['retry'])}</button><a class="btn ghost" href="qa.html">{E(s['toQA'])}</a><a class="btn ghost" href="index.html">{E(s['backLesson'])}</a></div>
    </div>
  </div>
</div></section>
</main>
''' + footer(lang, depth) + f'<script src="{data}"></script>\n<script src="{P["assets"]}site.js"></script>\n</body>\n</html>\n'

def page_slides(lang, L):
    s = S[lang]; P = lesson_paths(lang, L); depth = 1 if lang == 'ar' else 2
    deck = L['deckAr'] if lang == 'ar' else L['deckTr']
    dj = json.load(open(f'{DECKS}/{deck}/deck.json'))
    secs = []
    for sid in dj['order']:
        t = open(f'{DECKS}/{deck}/slides/{sid}.html', encoding='utf-8').read().strip()
        t = re.sub(r'src="/_blob/[0-9a-f]+"', f'src="{P["media"]}logo.webp"', t)
        t = re.sub(r'<aside>.*?</aside>', '', t, flags=re.S)
        t = t.replace('>تنبيه للمعلم<', '>تنبيه<').replace('>Öğretmene not<', '>Not<')
        secs.append(t)
    hf = "'IBM Plex Sans Arabic', Tahoma, sans-serif" if lang == 'ar' else "'Source Sans 3', Arial, sans-serif"
    bf = "'IBM Plex Sans Arabic', Tahoma, sans-serif" if lang == 'ar' else "'Source Sans 3', Arial, sans-serif"
    d = 'rtl' if lang == 'ar' else 'ltr'
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(s['slidesT'])} · {E(L[lang])}</title>
{og_tags(lang, s['slidesT'] + ' · ' + L[lang], L['descAr'] if lang == 'ar' else L['descTr'], share_img(lang, L))}
<meta name="theme-color" content="#0F2E2A">
{app_tags(lang, P['assets'][:-7])}
<link rel="icon" href="{P['media']}logo.webp" type="image/webp">
{preload(lang, P['assets'][:-7])}
<link rel="stylesheet" href="{P['assets']}fonts.css">
<link rel="stylesheet" href="{P['assets']}deck-{lang}.css">
<style>:root {{ --sv-hf: {hf}; --sv-bf: {bf}; }}</style>
<link rel="stylesheet" href="{P['assets']}slides.css">
</head>
<body tabindex="-1">
<div class="sv" data-lesson="{L['n']}">
  <div class="sv-top">
    <div class="g"><a href="index.html" aria-label="{E(s['backLesson'])}"><span aria-hidden="true">{'→' if lang == 'ar' else '←'}</span> <span class="lbl">{E(s['lesson'])} {DIG(lang, L['num'])}</span></a><img src="{P['media']}logo.webp" alt=""></div>
    <div class="t">{E(L[lang])}</div>
    <div class="g"><button id="svGridBtn" aria-pressed="false" aria-label="{E(s['grid'])}"><span aria-hidden="true">▦</span> <span class="lbl">{E(s['grid'])}</span></button><button id="svFs" aria-label="{E(s['fs'])}"><span aria-hidden="true">⛶</span> <span class="lbl">{E(s['fs'])}</span></button><a lang="{'tr' if lang == 'ar' else 'ar'}" href="{P['other']('slides.html')}">{'TR' if lang == 'ar' else 'AR'}</a></div>
  </div>
  <div class="sv-stage" id="svStage">
    <div class="sv-canvas" id="svCanvas">
{chr(10).join(secs)}
    </div>
    <div class="sv-frag" id="svFrag" hidden></div>
    <div class="sv-hint" id="svHint">{E(s['rotate'])}</div>
    <div class="sv-grid" id="svGrid" hidden></div>
    <div class="sv-prog"><i id="svBar"></i></div>
  </div>
  <div class="sv-bot">
    <button id="svPrev">{E(s['prevS'])}</button>
    <span class="cnt" id="svCnt"></span>
    <button id="svNext" class="nx">{E(s['nextS'])}</button>
    {done_btn(lang, L['n'], 'slides', 'sv-done')}
  </div>
</div>
<script src="{P['assets']}slides.js"></script>
</body>
</html>
'''

# ------------------------------------------------------------------ printable summary
def share_img(lang, L):
    return f'share-{L["slug"]}-{lang}.jpg' if os.path.exists(f'{ROOT}/media/share-{L["slug"]}-{lang}.jpg') else None

def lesson_url(lang, L):
    return SITE + ('' if lang == 'ar' else 'tr/') + f'{L["slug"]}/'

def sheet(lang, L, media):
    s = S[lang]; d = SUM[(L['n'], lang)]
    fx = (lambda h: arabify(ayahify(h))) if lang == 'tr' else ayahify
    cards = []
    for k, b in enumerate(d['blocks']):
        h = f'<h3><span class="n">{DIG(lang, k + 1)}</span>{E(b["t"])}</h3>'
        for x in b.get('p', []): h += f'<p>{fx(x)}</p>'
        if 'bullets' in b: h += '<ul>' + ''.join(f'<li>{fx(x)}</li>' for x in b['bullets']) + '</ul>'
        if 'table' in b: h += '<table>' + ''.join(f'<tr><td>{fx(a)}</td><td>{fx(c)}</td></tr>' for a, c in b['table']) + '</table>'
        if 'chips' in b:
            h += '<div class="chips">' + (f'<span class="lbl">{E(b["chipsLabel"])}</span>' if b.get('chipsLabel') else '') + ''.join(
                f'<span class="chip2{" on" if b.get("on") == i else ""}">{E(c)}</span>' for i, c in enumerate(b['chips'])) + '</div>'
        if 'note' in b: h += f'<p class="sh-note">{fx(b["note"])}</p>'
        cards.append(f'<section class="card{" wide" if b.get("wide") else ""}">{h}</section>')
    url = lesson_url(lang, L)
    qr = segno.make(url, error='m').svg_inline(dark='#0F2E2A', border=0, omitsize=True)
    return f'''<article class="sheet" id="sheet" lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
  <header class="sh-head"><img src="{media}logo.webp" alt="{E(s['brand'])}"><div><p class="sh-eb">{E(d['eb'])}</p><h2 class="sh-title">{E(L[lang])}</h2><p class="sh-sub">{E(d['sub'])}</p></div></header>
  <div class="sh-body">
    <div class="sh-grid">{''.join(cards)}</div>
    <section class="jam"><h4>{E(d['jamiaT'])}</h4><p>{E(d['jamia'])}</p></section>
    <footer class="sh-foot"><div class="qr" role="img" aria-label="QR: {E(url)}">{qr}</div><div><h4>{E(s['sumFootT'])}</h4><p>{E(s['sumFoot'])} <span class="url">{E(url.replace('https://', ''))}</span></p><p class="src">{E(d['src'])}</p></div></footer>
  </div>
</article>'''

def page_summary(lang, L):
    s = S[lang]; P = lesson_paths(lang, L); depth = 1 if lang == 'ar' else 2; n = L['n']
    base = f'summary-{L["slug"]}-{lang}'
    return head(lang, f'{s["tSum"][0]} · {L[lang]}', depth, L['descAr'] if lang == 'ar' else L['descTr'], extra=f'\n<link rel="stylesheet" href="{P["assets"]}summary.css">', image=share_img(lang, L)) + bar(lang, depth, P['other']('summary.html')) + '<main id="main">\n' + phead(lang, L, s['tSum'][0], L[lang], s['tSum'][0]) + f'''
<section class="band sum-band"><div class="wrap">
  <div class="sum-tools"><button class="btn" type="button" onclick="print()">{E(s['sumPrint'])}</button><a class="btn line" href="{P['media']}{base}.pdf" download>{E(s['sumPdf'])}</a><a class="btn line" href="{P['media']}{base}.jpg" download>{E(s['sumImg'])}</a><p class="note">{E(s['sumHelp'])}</p></div>
  <div class="sheet-wrap" id="sheetWrap">{sheet(lang, L, P['media'])}</div>
</div></section>
</main>
''' + footer(lang, depth) + f'<script src="{P["assets"]}site.js"></script>\n' + """<script>
(() => { const w = document.getElementById('sheetWrap'), sh = document.getElementById('sheet');
  const fit = () => { const z = Math.min(1, w.clientWidth / 794); sh.style.zoom = z; };
  fit(); addEventListener('resize', fit); })();
</script>
</body>
</html>
"""

# ------------------------------------------------------------------ map pages
def page_map(lang):
    src = f'{ROOT}/maps/map-{lang}.html'
    t = open(src, encoding='utf-8').read()
    logo = 'media/logo.webp' if lang == 'ar' else '../media/logo.webp'
    t = t.replace('src="" data-logo=""', f'src="{logo}"')
    t = t.replace('src="" data-wm=""', f'src="{logo}"')
    fu = '' if lang == 'ar' else '../'
    t = re.sub(r'<link rel="preconnect" href="https://fonts.googleapis.com">\n?', '', t)
    t = re.sub(r'<link rel="preconnect" href="https://fonts.gstatic.com"[^>]*>\n?', '', t)
    t = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/[^"]*">', f'{preload(lang, fu)}\n<link rel="stylesheet" href="{fu}assets/fonts.css">', t)
    assert 'googleapis' not in t
    t = t.replace('<script src="logo.js"></script>\n', '').replace('<script src="../logo.js"></script>\n', '')
    s_ = S[lang]
    mb = f'<button class="mapdone" type="button" data-off="{E(s_["doneOff"])}" data-on="{E(s_["doneOn"])}" data-x="{E(s_["doneWhat"]["map"])}" title="{E(s_["doneUndo"])}"></button>'
    t = re.sub(r'(<div id="close" class="ov">.*?<div class="acts">)', lambda m: m.group(1) + mb, t, count=1, flags=re.S)
    assert 'class="mapdone"' in t
    if lang == 'ar':
        t = t.replace('data-base="tr/" href="tr/"', 'data-base="tr/map.html" href="tr/map.html"')
        home, more, quizL, allL, resetL, homeL, pinch = MAIN_PAGE, 'المزيد', 'اختبر فهمك', 'الخريطة كاملة', 'من البداية', 'صفحة السلسلة', 'كبّر بإصبعين لقراءة الفروع'
        t = t.replace('<title>خريطة دروس صفة الكفر بالطاغوت</title>', '<title>الخريطة التفاعلية · صفة الكفر بالطاغوت · حقيقة لا إله إلا الله</title>\n' + og_tags('ar', 'الخريطة التفاعلية · صفة الكفر بالطاغوت · حقيقة لا إله إلا الله', S['ar']['lead']) + '\n<link rel="icon" href="media/logo.webp" type="image/webp">\n<meta name="theme-color" content="#0F2E2A">\n' + app_tags('ar', ''))
    else:
        t = t.replace('data-base="../" href="../"', 'data-base="../map.html" href="../map.html"')
        home, more, quizL, allL, resetL, homeL, pinch = MAIN_PAGE, 'Diğer', 'Kendini dene', 'Haritanın tamamı', 'Baştan', 'Seri sayfası', 'Dalları okumak için iki parmakla yakınlaştırın'
        t = t.replace('<title>Tâğutu İnkârın Keyfiyeti · Ders Haritası</title>', '<title>Ders Haritası · Tâğutu İnkârın Keyfiyeti · Lâ ilâhe illallah’ın Hakikati</title>\n' + og_tags('tr', 'Ders Haritası · Tâğutu İnkârın Keyfiyeti · Lâ ilâhe illallah’ın Hakikati', S['tr']['lead']) + '\n<link rel="icon" href="../media/logo.webp" type="image/webp">\n<meta name="theme-color" content="#0F2E2A">\n' + app_tags('tr', '../'))
    # brand → link home
    t = re.sub(r'<div id="brand">(.*?)</div></div>', lambda m: f'<a id="brand" href="{home}" title="{homeL}">{m.group(1)}</a></div>', t, count=1, flags=re.S)
    css = f'''
/* site integration + phone fixes */
html[lang=ar] body {{ word-spacing: .14em; }}
.ov .acts button.mapdone {{ background: transparent; color: #8FE0B5; border-color: #3F8F6A; }}
.ov .acts button.mapdone.on {{ background: #3F8F6A; color: #fff; }}
#brand {{ pointer-events: auto; text-decoration: none; }}
.tasksl {{ pointer-events: auto; display: inline-flex; align-items: center; gap: 6px; min-height: 38px; padding: 0 14px; border-radius: 30px; background: #D9B26A; color: #0F2E2A; font-weight: 700; font-size: 14.5px; text-decoration: none; white-space: nowrap; }}
.tasksl svg {{ width: 17px; height: 17px; }}
.tasksl:hover {{ background: #E6C483; }}
@media (max-width: 760px) {{ .tasksl {{ padding: 0 10px; min-height: 36px; }} .tasksl span {{ display: none; }} .tasksl svg {{ width: 20px; height: 20px; }} }}
#brand:hover span {{ color: var(--ink); }}
#bar .m-only {{ display: none; }}
#moreMenu {{ position: fixed; bottom: 76px; left: 50%; transform: translateX(-50%); z-index: 6; background: rgba(15,46,42,.98); border-radius: 18px; padding: 8px; display: grid; gap: 4px; min-width: 220px; box-shadow: 0 14px 40px rgba(15,46,42,.4); }}
#moreMenu button, #moreMenu a {{ min-height: 46px; border: 0; border-radius: 12px; background: transparent; color: #F7F3EA; padding: 0 16px; text-align: start; font-family: var(--qxf); font-size: 16px; text-decoration: none; display: flex; align-items: center; }}
#moreMenu button:hover, #moreMenu a:hover {{ background: rgba(255,255,255,.1); }}
#toast {{ position: fixed; top: 70px; left: 50%; transform: translateX(-50%); z-index: 6; background: rgba(15,46,42,.95); color: #F7F3EA; border: 1px solid var(--goldl); border-radius: 30px; padding: 8px 18px; font-size: 14px; white-space: nowrap; pointer-events: none; transition: opacity .4s; }}
.ov .acts a.home {{ min-height: 48px; border-radius: 30px; padding: 0 22px; border: 2px solid rgba(217,178,106,.5); color: #F7F3EA; display: inline-flex; align-items: center; text-decoration: none; font-family: var(--qxf); font-size: 17px; }}
@media (max-width: 760px) {{
  #tools {{ display: none; }}
  #bar .m-only {{ display: inline-flex; align-items: center; justify-content: center; font-size: 22px; padding: 0 14px; }}
  #top {{ background: linear-gradient(var(--parch) 72%, rgba(244,238,225,0)); height: calc(66px + env(safe-area-inset-top)); }}
  #brand img {{ width: 40px; height: 40px; }}
}}
</style>'''
    t = t.replace('</style>', css, 1)
    t = t.replace('<button id="reset" class="opt">', f'<button id="more" class="m-only" aria-haspopup="true" aria-expanded="false" aria-label="{more}">⋯</button>\n  <button id="reset" class="opt">', 1)
    t = t.replace('<div id="prog"></div>', f'''<div id="prog"></div>
<div id="moreMenu" hidden><button data-m="quizb">{quizL}</button><button data-m="all">{allL}</button><button data-m="reset">{resetL}</button><a href="{home}">{homeL}</a></div>
<div id="toast" hidden>{pinch}</div>''', 1)
    # home link on the intro overlay
    t = re.sub(r'(<div class="acts"><button id="start">.*?</button><button id="explore" class="ghost">.*?</button>)', lambda m: m.group(1) + f'<a class="home" href="{home}">{homeL}</a>', t, count=1)
    js = '''
  /* ---------- phone: more menu + pinch hint ---------- */
  const mm = $('moreMenu'), mb = $('more');
  mb.onclick = e => { e.stopPropagation(); mm.hidden = !mm.hidden; mb.setAttribute('aria-expanded', !mm.hidden); };
  mm.querySelectorAll('[data-m]').forEach(b => b.onclick = () => { mm.hidden = true; mb.setAttribute('aria-expanded', false); $(b.dataset.m).click(); });
  addEventListener('click', e => { if (!mm.hidden && !e.target.closest('#moreMenu')) { mm.hidden = true; mb.setAttribute('aria-expanded', false); } });
  let tt; const toast = () => { if (!narrow()) return; const t = $('toast'); t.hidden = false; t.style.opacity = 1; clearTimeout(tt); tt = setTimeout(() => { t.style.opacity = 0; setTimeout(() => { t.hidden = true; }, 400); }, 3200); };
  $('all').addEventListener('click', toast); $('explore').addEventListener('click', toast);
  if (L.home) document.querySelectorAll('#brand, #moreMenu a, .ov .acts a.home').forEach(a => { a.href = L.home; });
  /* progress: the lesson's map counts as seen once the student starts it (kept on this device only) */
  const db = document.querySelector('#close .mapdone');
  if (db) {
    const K = 'wt.progress.v1', rd = () => { try { return JSON.parse(localStorage.getItem(K)) || {}; } catch (e) { return {}; } };
    const paintDone = () => { const on = !!(rd()[L.n] || {}).map; db.textContent = on ? db.dataset.on.replace('{x}', db.dataset.x) : db.dataset.off.replace('{x}', db.dataset.x); db.classList.toggle('on', on); db.setAttribute('aria-pressed', on); };
    db.onclick = () => { const o = rd(), l = o[L.n] = o[L.n] || {}; if (l.map) delete l.map; else l.map = 1; try { localStorage.setItem(K, JSON.stringify(o)); } catch (e) {} paintDone(); };
    paintDone();
  }
'''
    t = t.replace("  $('jamiaText').textContent = L.jamia;", js + "\n  $('jamiaText').textContent = L.jamia;", 1)
    if HAS_TASKS:   # the gold «tasks» button, as on every other page
        tl = f'<a class="tasksl" href="tasks.html" aria-label="{E(TS[lang]["nav"])}" title="{E(TS[lang]["nav"])}">{TASK_I}<span>{E(TS[lang]["nav"])}</span></a>'
        t = t.replace('<div id="crumb"></div></div><a id="brand"', tl + '<div id="crumb"></div></div><a id="brand"', 1)
        assert 'class="tasksl"' in t, 'map tasks button failed'
    assert 'id="more"' in t and 'moreMenu' in t and 'class="home"' in t and 'id="brand" href' in t, 'map patch failed'
    return t

def write_app_files():
    """manifest for each language, and the service worker with the list of files saved for offline use."""
    import hashlib
    for lang, pre in (('ar', ''), ('tr', 'tr/')):
        s = S[lang]
        icons = '../media/' if lang == 'tr' else 'media/'
        man = {
            'id': './', 'name': f"{s['brand']} · {LIB[lang]['title']}", 'short_name': s['brand'],
            'description': LIB[lang]['lead'], 'lang': lang, 'dir': 'rtl' if lang == 'ar' else 'ltr',
            'start_url': './', 'scope': '../' if lang == 'tr' else './', 'display': 'standalone',
            'background_color': '#0F2E2A', 'theme_color': '#0F2E2A',
            'icons': [
                {'src': icons + 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                {'src': icons + 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
                {'src': icons + 'icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'},
            ],
        }
        w(pre + 'manifest.webmanifest', json.dumps(man, ensure_ascii=False, indent=1))
    keep_media = {'logo.webp', 'icon-192.png', 'apple-touch-icon.png', 'poster1.jpg', 'poster1-tr.jpg', 'poster-f1.jpg', 'poster-f1-tr.jpg', 'poster-teaser.jpg'}
    files = []
    for dp, dn, fn in os.walk(OUT):
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), OUT).replace(os.sep, '/')
            if rel.startswith('media/') and rel[6:] not in keep_media: continue
            if rel in ('sw.js', '404.html', '.nojekyll') or rel.startswith('.'): continue
            files.append(rel)
    files.sort()
    h = hashlib.sha1()
    for rel in files: h.update(rel.encode()); h.update(open(os.path.join(OUT, rel), 'rb').read())
    urls = ['./'] + [f[:-len('index.html')] if f.endswith('/index.html') else f for f in files if f != 'index.html']
    urls += [f for f in files if f.endswith('/index.html')]
    sw = open(f'{ROOT}/sw_template.js', encoding='utf-8').read()
    w('sw.js', sw.replace('__VERSION__', h.hexdigest()[:12]).replace('__PRECACHE__', json.dumps(urls, ensure_ascii=False, indent=1)))

from privacy import PRIVACY, UPDATED as PRIV_UPDATED

def page_privacy(lang):
    s, P = S[lang], PRIVACY[lang]; depth = 0 if lang == 'ar' else 1; u = up(depth)
    other = 'tr/privacy.html' if lang == 'ar' else '../privacy.html'
    body = ''.join(f'<h2>{E(h)}</h2>' + ''.join(f'<p>{E(x)}</p>' for x in paras) for h, paras in P['body'])
    return head(lang, f'{P["title"]} · {s["brand"]}', depth, P['sub']) + bar(lang, depth, other) + f'''<main id="main">
<section class="phead">{ORN}<div class="wrap">
  <nav class="crumbs" aria-label="breadcrumb"><a href="index.html">{E(s['home'])}</a><span class="sep">›</span><span>{E(P['title'])}</span></nav>
  <h1>{E(P['title'])}</h1><p>{E(P['sub'])}</p>
</div></section>
<section class="band"><div class="wrap"><article class="prose policy">
  <p class="upd">{E(P['updated'])}: {E(PRIV_UPDATED[lang])}</p>
  {body}
</article></div></section>
</main>
''' + footer(lang, depth) + f'<script src="{u}assets/site.js"></script>\n</body>\n</html>\n'

def page_404():
    h = head('ar', 'الصفحة غير موجودة · Sayfa bulunamadı', 0).replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="/">')
    return h + bar('ar', 0, 'tr/index.html') + f'''<main id="main">
<section class="phead">{ORN}<div class="wrap">
  <p class="eb">٤٠٤</p><h1>الصفحة غير موجودة</h1><p>ربما تغيّر الرابط. ابدأ من الصفحة الرئيسية لتجد الدرس الذي تبحث عنه.</p>
  <p lang="tr" dir="ltr" style="font-family:'Source Sans 3',sans-serif">Sayfa bulunamadı. Aradığınız dersi bulmak için ana sayfadan başlayın.</p>
</div></section>
<section class="band"><div class="wrap" style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="index.html">الصفحة الرئيسية</a><a class="btn ghost" lang="tr" href="tr/index.html">Ana sayfa</a></div></section>
</main>
''' + footer('ar', 0) + '</body>\n</html>\n'

# ------------------------------------------------------------------ memory cards, and the section's whole-quiz
# بطاقات الحفظ: كل بطاقة سؤال ووجهه الآخر جوابه. ما يذكره الطالب يبتعد موعده، وما ينساه يعود قريبًا.
# المواعيد تُحفظ على جهاز الطالب وحده (كبقية تقدّمه)، والبطاقات تُبنى من أسئلة المراجعة ومن العبارة الجامعة لكل درس.
CARDS = {
 'ar': dict(nav='بطاقات الحفظ', title='بطاقات الحفظ',
    sub='بطاقات تعود إليك على فترات متباعدة حتى يرسخ المحفوظ: ما أتقنتَه يبتعد موعده، وما نسيتَه يعود قريبًا.',
    show='أظهر الجواب', ok='أذكرها', again='لم أذكرها', left='بقي {n}',
    doneT='انتهت بطاقات اليوم', doneS='أحسنت. البطاقات تعود في مواعيدها، فعُد غدًا.',
    noneT='لا بطاقات مستحقة اليوم', noneS='كل بطاقاتك في مواعيد لاحقة. ويمكنك أن تراجع قبل الموعد إن شئت.',
    ahead='راجع قبل الموعد', restart='ابدأ من جديد',
    statNew='جديدة', statLearn='قيد الحفظ', statKnown='راسخة',
    jamiaTag='العبارة الجامعة', jamiaQ='ما العبارة الجامعة لهذا الدرس؟', qaTag='سؤال مراجعة',
    homeT='بطاقات المراجعة', homeDue='عندك {n} مستحقة اليوم', homeNone='لا بطاقات مستحقة اليوم',
    homeB='ابدأ المراجعة', backHome='الرجوع إلى الصفحة الرئيسية',
    priv='مواعيد بطاقاتك تُحفظ على هذا الجهاز وحده: لا حساب، ولا إرسال لأي بيانات.'),
 'tr': dict(nav='Ezber kartları', title='Ezber kartları',
    sub='Kartlar giderek artan aralıklarla geri döner: iyi bildiğin uzaklaşır, unuttuğun yakında tekrar gelir.',
    show='Cevabı göster', ok='Biliyorum', again='Bilmiyorum', left='{n} kaldı',
    doneT='Bugünün kartları bitti', doneS='Tebrikler. Kartlar vakti gelince döner; yarın tekrar uğrayın.',
    noneT='Bugün vakti gelen kart yok', noneS='Bütün kartlarınız ileri bir tarihte. İsterseniz vaktinden önce de çalışabilirsiniz.',
    ahead='Vaktinden önce çalış', restart='Yeniden başla',
    statNew='yeni', statLearn='öğreniliyor', statKnown='pekişti',
    jamiaTag='Toparlayıcı ifade', jamiaQ='Bu dersin toparlayıcı ifadesi nedir?', qaTag='Tekrar sorusu',
    homeT='Tekrar kartları', homeDue='Bugün {n} kart sizi bekliyor', homeNone='Bugün vakti gelen kart yok',
    homeB='Tekrara başla', backHome='Ana sayfaya dön',
    priv='Kart tarihleriniz yalnızca bu cihazda saklanır: hesap yok, hiçbir veri gönderilmez.'),
}
QALL = {
 'ar': dict(nav='اختبار القسم', title='اختبار القسم الجامع',
    sub='أسئلة مخلوطة من كل دروس القسم المنشورة، تكشف ما رسخ منها وما يحتاج إعادة.',
    btn='اختبار القسم الجامع', btnS='أسئلة من كل الدروس مخلوطة', backHome='الرجوع إلى الصفحة الرئيسية'),
 'tr': dict(nav='Bölüm testi', title='Bölümün genel testi',
    sub='Bölümün yayımlanmış bütün derslerinden karışık sorular: neyin pekiştiğini, neyin tekrara muhtaç olduğunu gösterir.',
    btn='Bölümün genel testi', btnS='Bütün derslerden karışık sorular', backHome='Ana sayfaya dön'),
}

def card_data(lang):
    """The cards built at build time: the review questions of every published lesson.
       The lesson's gathering sentence is added in the page itself, from the map's data file."""
    DQ = DOCQA if lang == 'ar' else DOCQA_TR
    fx = (lambda h: arabify(ayahify(h))) if lang == 'tr' else ayahify
    out = []
    for L in ALL_LIVE:
        n = L['n']
        for k, (q, a, _tf) in enumerate(DQ.get(n, [])):
            out.append(dict(id=f'q{n}-{k}', n=n, q=fx(q), a=fx(a)))
    return out

def page_cards(lang):
    s, c = S[lang], CARDS[lang]; depth = 0 if lang == 'ar' else 1
    other = 'tr/cards.html' if lang == 'ar' else '../cards.html'
    data = json.dumps(dict(cards=card_data(lang),
                           lessons={L['n']: f'{s["lesson"]} {DIG(lang, L["num"])}: {L[lang]}' for L in ALL_LIVE},
                           t=c), ensure_ascii=False).replace('</', '<\\/')
    crumbs = f'<a href="index.html">{E(s["home"])}</a><span class="sep">›</span><span>{E(c["title"])}</span>'
    back = ('→ ' if lang == 'ar' else '← ') + E(c['backHome'])
    return head(lang, f'{c["title"]} · {s["brand"]}', depth, c['sub']) + bar(lang, depth, other) + f'''<main id="main">
<section class="phead">{ORN}<div class="wrap">
  <nav class="crumbs" aria-label="breadcrumb">{crumbs}</nav>
  <h1>{E(c['title'])}</h1><p>{E(c['sub'])}</p>
  <a class="btn ghost back" href="index.html">{back}</a>
</div></section>
<section class="band"><div class="wrap narrow">
  <p class="cstat" id="cStat" hidden></p>
  <div class="quiz" id="cards" aria-live="polite">
    <div id="cBox" hidden>
      <p class="qprog"><span id="cProg"></span><span id="cLeft"></span></p>
      <div class="bar2"><i id="cBar"></i></div>
      <p class="ctag" id="cTag"></p>
      <p class="qtext" id="cQ"></p>
      <div class="ca" id="cA" hidden></div>
      <div class="acts">
        <button class="btn" id="cShow" type="button">{E(c['show'])}</button>
        <button class="btn" id="cOk" type="button" hidden>✓ {E(c['ok'])}</button>
        <button class="btn ghost" id="cAgain" type="button" hidden>↻ {E(c['again'])}</button>
      </div>
    </div>
    <div id="cDone" hidden>
      <p class="score" id="cDoneT"></p>
      <p id="cDoneS" style="color:var(--mint);margin:0 0 4px"></p>
      <div class="acts"><button class="btn" id="cAhead" type="button" hidden>{E(c['ahead'])}</button><a class="btn ghost" href="index.html">{E(c['backHome'])}</a></div>
    </div>
  </div>
  <p class="note" style="margin-top:14px">{E(c['priv'])}</p>
</div></section>
</main>
<script type="application/json" id="cardData">{data}</script>
''' + footer(lang, depth) + f'<script src="{"data.js" if lang == "ar" else "data_tr.js"}"></script>\n<script src="{up(depth)}assets/site.js"></script>\n</body>\n</html>\n'

def page_quiz_all(lang):
    s, qa = S[lang], QALL[lang]; depth = 0 if lang == 'ar' else 1
    other = 'tr/quiz-all.html' if lang == 'ar' else '../quiz-all.html'
    crumbs = f'<a href="index.html">{E(s["home"])}</a><span class="sep">›</span><a href="{MAIN_PAGE}#taghut">{E(MAIN[lang])}</a><span class="sep">›</span><span>{E(qa["title"])}</span>'
    back = ('→ ' if lang == 'ar' else '← ') + E(qa['backHome'])
    return head(lang, f'{qa["title"]} · {s["brand"]}', depth, qa['sub']) + bar(lang, depth, other) + f'''<main id="main">
<section class="phead">{ORN}<div class="wrap">
  <nav class="crumbs" aria-label="breadcrumb">{crumbs}</nav>
  <h1>{E(qa['title'])}</h1><p>{E(qa['sub'])}</p>
  <a class="btn ghost back" href="{MAIN_PAGE}#lessons">{back}</a>
</div></section>
<section class="band"><div class="wrap narrow">
  <div class="quiz" id="quiz" data-lesson="all" data-count="15" aria-live="polite">
    <div id="qcard">
      <p class="qprog"><span id="qprog"></span><span id="qscoreNow"></span></p>
      <div class="bar2"><i id="qbar"></i></div>
      <p class="qtext" id="qtext"></p>
      <div class="qopts" id="qopts"></div>
      <div class="qfb" id="qfb"></div>
      <div class="acts"><button class="btn" id="qnext" hidden></button></div>
    </div>
    <div id="qres" hidden>
      <svg class="ring" id="qring" viewBox="0 0 120 120" aria-hidden="true"></svg>
      <p class="score" id="qscore"></p>
      <p id="qmsg" style="color:var(--mint);margin:0"></p>
      <p id="qwrongT" style="margin:18px 0 0;font-family:var(--hf);color:var(--goldl)">{E(s['wrongT'])}</p>
      <ul class="review" id="qwrong"></ul>
      <div class="acts"><button class="btn" id="qretry">{E(s['retry'])}</button><a class="btn ghost" href="{MAIN_PAGE}#lessons">{E(qa['backHome'])}</a></div>
    </div>
  </div>
</div></section>
</main>
''' + footer(lang, depth) + f'<script src="{"data.js" if lang == "ar" else "data_tr.js"}"></script>\n<script src="{up(depth)}assets/site.js"></script>\n</body>\n</html>\n'

# بصمة SHA-256 لمفتاح توقيع تطبيق Google Play، مثل '14:6D:E9:...' — تُستخرج كما في guide/android-play.md
PLAY_SHA256 = ''

# ------------------------------------------------------------------ write
# Cloudflare Web Analytics: visit counts for the teacher only; no cookies, no tracking of individual students
ANALYTICS = '<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{"token": "dda53286faab4be6aca43215f29dc4b7"}\'></script>'

# switching language replaces the page instead of adding one, so «back» leaves the page
# instead of bouncing between its Arabic and Turkish versions
LANG_SWAP = """<script id="langSwap">document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a.lang[hreflang]');if(!a||e.defaultPrevented||e.button||e.ctrlKey||e.metaKey||e.shiftKey||e.altKey)return;e.preventDefault();location.replace(a.href)});</script>"""

def w(path, text):
    if path.endswith('.html'):
        if gate.START not in text and '</head>' in text:   # pages with their own template (slides, map)
            text = text.replace('</head>', gate.tags('tr' if path.startswith('tr/') else 'ar', '../' * path.count('/')) + '\n</head>', 1)
        text = gate.strip_if_free(path, text)
        if '</body>' in text and 'id="langSwap"' not in text:
            text = text.replace('</body>', LANG_SWAP + '\n</body>', 1)
    if path.endswith('.html') and '</head>' in text and 'cloudflareinsights' not in text:
        text = text.replace('</head>', ANALYTICS + '\n</head>', 1)
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)

def build():
    # Clean the output, but keep docs/media: videos uploaded there directly are not in src/.
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        if name == 'media': continue
        p = os.path.join(OUT, name)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    shutil.copytree(f'{ROOT}/assets', f'{OUT}/assets')
    shutil.copy(f'{DECKS}/ar1/deck.css', f'{OUT}/assets/deck-ar.css')
    shutil.copy(f'{DECKS}/tr1/deck.css', f'{OUT}/assets/deck-tr.css')
    shutil.copytree(f'{ROOT}/media', f'{OUT}/media', dirs_exist_ok=True)
    w('data.js', open(f'{ROOT}/maps/data.js', encoding='utf-8').read().replace('tag: "تنبيه للمعلم"', 'tag: "تنبيه"'))
    os.makedirs(f'{OUT}/tr', exist_ok=True)
    w('tr/data_tr.js', open(f'{ROOT}/maps/data_tr.js', encoding='utf-8').read().replace('tag: "Öğretmene not"', 'tag: "Not"'))
    w('map.html', page_map('ar')); w('tr/map.html', page_map('tr'))
    w('index.html', page_library('ar')); w('tr/index.html', page_library('tr'))
    for X in SERIES:
        if X['status'] == 'live': w(X['page'], page_series('ar', X)); w('tr/' + X['page'], page_series('tr', X))
    w('tasks.html', page_tasks('ar')); w('tr/tasks.html', page_tasks('tr'))
    w('privacy.html', page_privacy('ar')); w('tr/privacy.html', page_privacy('tr'))
    w('cards.html', page_cards('ar')); w('tr/cards.html', page_cards('tr'))
    w('quiz-all.html', page_quiz_all('ar')); w('tr/quiz-all.html', page_quiz_all('tr'))
    shutil.copy(f'{ROOT}/tasks.json', f'{OUT}/tasks.json')
    for L in ALL_LIVE:
        n, sl = L['n'], L['slug']
        for lang, pre in (('ar', ''), ('tr', 'tr/')):
            w(f'{pre}{sl}/index.html', page_hub(lang, L))
            w(f'{pre}{sl}/slides.html', page_slides(lang, L))
            w(f'{pre}{sl}/qa.html', page_qa(lang, L))
            w(f'{pre}{sl}/quiz.html', page_quiz(lang, L))
            if (n, lang) in SUM: w(f'{pre}{sl}/summary.html', page_summary(lang, L))
            w(f'{pre}{sl}/text.html', page_text(lang, L))
            if n in SHARH: w(f'{pre}{sl}/sharh.html', page_sharh(lang, L))
    w('404.html', page_404())
    # what the home-page search looks in; saved for offline use like the rest of the site
    w('search.json', json.dumps(search_index('ar'), ensure_ascii=False))
    w('tr/search.json', json.dumps(search_index('tr'), ensure_ascii=False))
    write_app_files()
    w('.nojekyll', '')
    # custom domain for GitHub Pages, and files for search engines
    w('CNAME', 'tevhidim.com\n')
    # تطبيق Google Play: بعد إنشاء مفتاح التوقيع (الدليل في guide/android-play.md) توضع بصمته في PLAY_SHA256
    # فيُنشر الملف الذي يثبت أن التطبيق لهذا الموقع، ويفتح التطبيق بلا شريط متصفح
    if PLAY_SHA256:
        w('.well-known/assetlinks.json', '[{"relation": ["delegate_permission/common.handle_all_urls"], '
          '"target": {"namespace": "android_app", "package_name": "com.tevhidim.app", '
          '"sha256_cert_fingerprints": ["' + PLAY_SHA256 + '"]}}]\n')
    pages = sorted(os.path.relpath(os.path.join(dp, f), OUT).replace(os.sep, '/') for dp, dn, fn in os.walk(OUT) for f in fn if f.endswith('.html') and f not in ('404.html',) and not f.startswith('_'))
    urls = ''.join(f'  <url><loc>{SITE}{p[:-10] if p.endswith("index.html") else p}</loc></url>\n' for p in pages)
    w('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    w('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
    print('built', OUT)

if __name__ == '__main__':
    build()
