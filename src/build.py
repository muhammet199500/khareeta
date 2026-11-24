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
import io, segno
SITE = 'https://muhammet199500.github.io/khareeta/'

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
    dict(n=3, live=False, ar='بغض عبادة الطاغوت', tr='Tâğuta İbadete Buğz Etmek'),
    dict(n=4, live=False, ar='تكفير أهلها', tr='Ehlini Tekfir Etmek'),
    dict(n=5, live=False, ar='معاداتهم', tr='Onlara Düşmanlık Etmek'),
]
LIVE = [l for l in LESSONS if l['live']]

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
    iosHint='على iPhone: اضغط زر المشاركة ثم «إضافة إلى الشاشة الرئيسية» ليصير الموقع تطبيقًا يعمل بلا إنترنت.',
    fsDown='تصغير الخط', fsUp='تكبير الخط', fsLabel='حجم الخط', tShare=('صورة للمشاركة', 'صورة الدرس لواتساب وتيليجرام، فيها رمز يفتحه'),
    tSum=('ملخص الدرس للطباعة', 'صفحة واحدة برمز QR يفتح الدرس'),
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
    iosHint='iPhone’da: Paylaş düğmesine, ardından «Ana Ekrana Ekle»ye dokunun; site internetsiz de çalışan bir uygulama olur.',
    fsDown='Yazıyı küçült', fsUp='Yazıyı büyüt', fsLabel='Yazı boyutu', tShare=('Paylaşım görseli', 'WhatsApp ve Telegram için dersi açan QR kodlu görsel'),
    tSum=('Yazdırılabilir ders özeti', 'Dersi açan QR kodlu tek sayfa'),
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
         ar='حقيقة لا إله إلا الله', tr='Lâ ilâhe illallah’ın Hakikati', byAr='', byTr='',
         sections=[
            dict(key='taghut', ar='صفة الكفر بالطاغوت', tr='Tâğutu İnkârın Keyfiyeti', lessons=LESSONS),
            dict(key='shurut', ar='شروط لا إله إلا الله', tr='Lâ ilâhe illallah’ın Şartları', lessons=[]),
            dict(key='arkan', ar='أركان التوحيد', tr='Tevhidin Rükünleri', lessons=[]),
            dict(key='nawaqid', ar='نواقض التوحيد', tr='Tevhidin Nâkızları', lessons=[]),
         ]),
    dict(slug='tawhid', cat='aqeedah', status='prep', ar='شرح كتاب التوحيد', tr='Kitâbu’t-Tevhîd Şerhi',
         byAr='للشيخ محمد بن عبد الوهاب رحمه الله', byTr='Şeyh Muhammed b. Abdülvehhab'),
    dict(slug='fiqh-muyassar', cat='fiqh', status='prep', ar='الفقه الميسر', tr='el-Fıkhu’l-Müyesser', byAr='', byTr=''),
    dict(slug='usul-thalatha', cat='aqeedah', status='prep', ar='الأصول الثلاثة', tr='Üç Esas (el-Usûlu’s-Selâse)',
         byAr='للشيخ محمد بن عبد الوهاب رحمه الله', byTr='Şeyh Muhammed b. Abdülvehhab'),
    dict(slug='riyad', cat='hadith', status='soon', ar='رياض الصالحين', tr='Riyâzu’s-Sâlihîn',
         byAr='للإمام النووي رحمه الله', byTr='İmam Nevevî'),
    dict(slug='wajeez', cat='aqeedah', status='soon', ar='شرح كتاب الوجيز في عقيدة السلف', tr='el-Vecîz fî Akîdeti’s-Selef Şerhi', byAr='', byTr=''),
]
MAIN = SERIES[0]                      # the series the current lessons belong to
MAIN_PAGE = MAIN['page']

def ar_count(n, one, two, few, many):
    """Arabic counted noun: ١ درس واحد، درسان، ٣ دروس، ١١ درسًا"""
    if n == 1: return one
    if n == 2: return two
    if 3 <= n <= 10: return f'{DIG("ar", n)} {few}'
    return f'{DIG("ar", n)} {many}'

LIB = {
 'ar': dict(title='مكتبة الدروس', nav='السلاسل',
    lead='سلاسل علمية في العقيدة والفقه والحديث. لكل درس: فيديو، ودرس مكتوب، وعرض شرائح، وخريطة تفاعلية، وأسئلة وأجوبة، واختبار.',
    search='ابحث عن سلسلة أو درس…', noResult='لا نتائج. جرّب كلمة أخرى.',
    contT='تابع من حيث توقفت', contB='أكمِل',
    seriesT='السلاسل', seriesS='اختر سلسلة لتفتح صفحتها ودروسها.', all='الكل',
    st=dict(live='متاحة', prep='قيد الإعداد', soon='قريبًا'), stMeta=dict(prep='قيد الإعداد', soon='تبدأ قريبًا'),
    open='افتح السلسلة', latestT='أحدث الدروس', latestS='آخر ما نُشر من السلاسل.', openL='افتح الدرس',
    sectionsT='أقسام السلسلة', sectionsS='تُضاف الأقسام والدروس تباعًا.', sectionSoon='قريبًا',
    sLead='سلسلة في معنى كلمة التوحيد وما يحققها وما ينقضها: صفة الكفر بالطاغوت، وشروط لا إله إلا الله، وأركان التوحيد، ونواقض التوحيد. لكل درس: فيديو، ودرس مكتوب، وعرض شرائح، وخريطة تفاعلية، وأسئلة وأجوبة، واختبار.',
    sQuote='﴿فَاعْلَمْ أَنَّهُ لَا إِلَٰهَ إِلَّا اللَّهُ﴾', sQuoteMeal='',
    section='قسم', toSection='إلى القسم',
 ),
 'tr': dict(title='Ders Kütüphanesi', nav='Seriler',
    lead='Akide, fıkıh ve hadis alanında ilmî seriler. Her derste: video, yazılı ders, sunum, etkileşimli harita, soru-cevap ve test.',
    search='Seri veya ders ara…', noResult='Sonuç yok. Başka bir kelime deneyin.',
    contT='Kaldığın yerden devam et', contB='Devam et',
    seriesT='Seriler', seriesS='Sayfasını ve derslerini açmak için bir seri seçin.', all='Tümü',
    st=dict(live='Yayında', prep='Hazırlanıyor', soon='Yakında'), stMeta=dict(prep='Hazırlanıyor', soon='Yakında başlıyor'),
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

def head(lang, title, depth, desc='', extra='', image=None):
    d = 'rtl' if lang == 'ar' else 'ltr'
    u = up(depth)
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
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
<body>
<a class="skip" href="#main">{S[lang]['skip']}</a>
'''

def bar(lang, depth, other):
    """other: href to the same page in the other language (relative to this page)."""
    s, u = S[lang], up(depth)
    olang = 'tr' if lang == 'ar' else 'ar'
    olabel = 'Türkçe' if lang == 'ar' else 'العربية'
    return f'''<header class="bar"><div class="wrap">
  <a class="brand" href="{home_of(lang, depth)}"><img src="{root_up(lang, depth)}media/logo.webp" alt="{E(s['brand'])}"><span>{E(s['brand'])}</span></a>
  <nav aria-label="{E(s['home'])}"><a class="hide-s" href="{home_of(lang, depth)}">{E(s['home'])}</a><a class="hide-s" href="{home_of(lang, depth)}#series">{E(LIB[lang]['nav'])}</a><a class="lang" lang="{olang}" hreflang="{olang}" href="{other}">{olabel}</a></nav>
</div></header>
'''

def root_up(lang, depth):
    return up(depth)

def home_of(lang, depth):
    return up(depth - (1 if lang == 'tr' else 0)) + 'index.html'

def series_of(lang, depth):
    """link to the page of the series the current lessons belong to"""
    return up(depth - (1 if lang == 'tr' else 0)) + MAIN_PAGE

def footer(lang, depth):
    s, u = S[lang], up(depth)
    return f'''<footer><div class="wrap"><div class="f1"><img src="{u}media/logo.webp" alt=""><span>{E(s['foot'])}</span></div><a href="{home_of(lang, depth)}">{E(LIB[lang]['title'])}</a></div><div class="wrap app-cta" id="appCta" hidden><button class="btn line" id="installBtn" type="button" hidden>{E(s['install'])}</button><span id="iosHint" hidden>{E(s['iosHint'])}</span></div></footer>
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
  ('ترك عبادة الطاغوت يعني ترك التعامل المباح مع غير المسلمين.', 'خطأ؛ فالمطلوب ترك العبادة المصروفة لغير الله وما يفضي إليها، لا ترك البرّ والتعامل المباح: ﴿لَا يَنْهَاكُمُ اللَّهُ عَنِ الَّذِينَ لَمْ يُقَاتِلُوكُمْ فِي الدِّينِ ... أَنْ تَبَرُّوهُمْ وَتُقْسِطُوا إِلَيْهِمْ﴾ [الممتحنة: 8].', True),
  ('الاجتناب أبلغ من مجرد الترك.', 'صح؛ لأنه يتضمن ترك الفعل والابتعاد عن وسائله ومواضعه.', True),
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
def page_series(lang):
    """page of the series «حقيقة لا إله إلا الله»: its sections, then the section «صفة الكفر بالطاغوت» with its lessons"""
    s = S[lang]; depth = 0 if lang == 'ar' else 1; u = up(depth)
    other = f'tr/{MAIN_PAGE}' if lang == 'ar' else f'../{MAIN_PAGE}'
    lb = LIB[lang]
    latest = LIVE[-1]
    pts = []
    for i, p in enumerate(POINTS[lang]):
        L = LESSONS[i]
        inner = f'<span class="k">{E(s["point"]) + " " + E(ORD[lang][i]) if lang == "ar" else E(ORD[lang][i]) + " " + E(s["point"])}</span><span class="t">{E(p)}</span>'
        if L['live']:
            pts.append(f'<li class="live"><a href="l{L["n"]}/index.html">{inner}</a></li>')
        else:
            pts.append(f'<li>{inner}</li>')
    rows = []
    for L in LESSONS:
        n = DIG(lang, L['n'])
        if L['live']:
            b = f'l{L["n"]}/'
            chips = []
            chips.append((I['text'], s['chipText'], f'{b}text.html'))
            chips += [(I['slides'], s['chipSlides'], f'{b}slides.html'), (I['map'], s['chipMap'], f'map.html#l{L["n"]}'), (I['qa'], s['chipQA'], f'{b}qa.html'), (I['quiz'], s['chipQuiz'], f'{b}quiz.html')]
            if (L['n'], lang) in SUM: chips.append((I['sum'], s['chipSum'], f'{b}summary.html'))
            ch = ''.join(f'<a class="chip" href="{h}">{ic}{E(t)}</a>' for ic, t, h in chips)
            rows.append(f'''<li class="lrow live"><span class="n">{n}</span><div><h3><a href="{b}index.html">{E(L[lang])}</a></h3><p>{E(L["descAr"] if lang == "ar" else L["descTr"])}</p><div class="chips">{ch}</div><p class="lprog" data-lesson="{L['n']}" hidden></p></div><a class="pill" href="{b}index.html">{E(s["open"])}</a></li>''')
        else:
            rows.append(f'''<li class="lrow"><span class="n">{n}</span><div><h3>{E(L[lang])}</h3><p>{E(s["lesson"])} {n}</p></div><span class="pill">{E(s["soon"])}</span></li>''')
    b = f'l{latest["n"]}/'
    tools = [tool('text', s['tText'], f'{b}text.html', True),
             tool('slides', s['tSlides'], f'{b}slides.html'), tool('map', s['tMap'], f'map.html#l{latest["n"]}'),
             tool('qa', s['tQA'], f'{b}qa.html'), tool('quiz', s['tQuiz'], f'{b}quiz.html')]
    if (latest['n'], lang) in SUM: tools.append(tool('sum', s['tSum'], f'{b}summary.html'))
    meal = f'<p class="meal">{E(latest["verseTr"])}</p>' if lang == 'tr' else ''
    secs = []
    for sec in MAIN['sections']:
        ls = sec['lessons']; live = [L for L in ls if L['live']]
        meta = f'{lessons_count(lang, len(ls))} · {published(lang, len(live))}' if ls else lb['sectionSoon']
        inner = f'<span class="k">{E(lb["section"])}</span><span class="t">{E(sec[lang])}</span><span class="m">{E(meta)}</span>'
        secs.append(f'<li class="live"><a href="#{sec["key"]}">{inner}</a></li>' if live else f'<li>{inner}</li>')
    cat = dict((c, ar if lang == 'ar' else tr) for c, ar, tr in CATS)[MAIN['cat']]
    smeal = f'<p class="smeal">{E(lb["sQuoteMeal"])}</p>' if lb['sQuoteMeal'] else ''
    return head(lang, f'{MAIN[lang]} · {s["brand"]}', depth, lb['sLead']) + bar(lang, depth, other) + f'''<main id="main">
<section class="hero">{ORN}<div class="wrap"><div class="in">
  <div class="emblem"><img src="{u}media/logo.webp" alt="{E(s['brand'])}"></div>
  <div><nav class="crumbs hero-crumbs" aria-label="breadcrumb"><a href="index.html">{E(s['home'])}</a><span class="sep">›</span><a href="index.html#series">{E(cat)}</a></nav><h1>{E(MAIN[lang])}</h1><p class="lead">{E(lb['sLead'])}</p>
  <p class="quote">{lb['sQuote']}</p>{smeal}</div>
</div></div></section>

<section class="band"><div class="wrap">
  <h2>{E(lb['sectionsT'])}</h2><p class="sub">{E(lb['sectionsS'])}</p>
  <ol class="points secs">{''.join(secs)}</ol>
</div></section>

<section class="band tight sect" id="taghut"><div class="wrap">
  <div class="secthead"><p class="eb">{E(lb['section'])}</p><h2>{E(s['seriesShort'] if lang == 'ar' else MAIN['sections'][0]['tr'])}</h2><p class="sub">{E(s['lead'])}</p>
  <p class="squote">{E(s['quote'])}<small>{E(s['quoteRef'])}</small></p></div>
  <h3 class="h3s">{E(s['pointsT'])}</h3><p class="sub">{E(s['pointsS'])}</p>
  <ol class="points">{''.join(pts)}</ol>
<h3 class="h3s">{E(s['latestT'])}</h3><p class="sub">{E(s['latestS'])}</p>
  <article class="open">
    {player(lang, latest, u)}
    <div>
      <span class="num">{E(s['lesson'])} {DIG(lang, latest['n'])}</span>
      <h3><a href="{b}index.html">{E(latest[lang])}</a></h3>
      <p>{E(latest['descAr'] if lang == 'ar' else latest['descTr'])}</p>
      <p class="verse" lang="ar" dir="rtl">{E(latest['verse'])}</p>{meal}
      <div class="tools">{''.join(tools)}</div>
    </div>
  </article>
  <h3 class="h3s" id="lessons">{E(s['listT'])}</h3><p class="sub">{E(s['listS'])}</p>
  <ol class="list">{''.join(rows)}</ol>
  <p class="reset-wrap"><button class="linkbtn" id="progReset" type="button" hidden>{E(s['progReset'])}</button></p>
</div></section>

</main>
''' + footer(lang, depth) + f'<script src="{u}assets/site.js"></script>\n</body>\n</html>\n'

SEARCH_I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'

def page_library(lang):
    """home page: every series, with search, category filter, «continue where you stopped» and the latest lessons"""
    s, lb = S[lang], LIB[lang]; depth = 0 if lang == 'ar' else 1; u = up(depth)
    other = 'tr/index.html' if lang == 'ar' else '../index.html'
    catname = dict((c, ar if lang == 'ar' else tr) for c, ar, tr in CATS)
    counts = {c: sum(1 for x in SERIES if x['cat'] == c) for c, _, _ in CATS}
    cats = f'<li><button type="button" class="on" data-cat="">{E(lb["all"])}<span>{DIG(lang, len(SERIES))}</span></button></li>'
    cats += ''.join(f'<li><button type="button" data-cat="{c}">{E(catname[c])}<span>{DIG(lang, counts[c])}</span></button></li>' for c, _, _ in CATS if counts[c])
    cards = []
    for x in SERIES:
        by = x['byAr'] if lang == 'ar' else x['byTr']
        q = ' '.join([x['ar'], x['tr'], by, catname[x['cat']]] + [sec['ar'] + ' ' + sec['tr'] for sec in x.get('sections', [])])
        if x['status'] == 'live':
            secs = x['sections']; allL = [L for sec in secs for L in sec['lessons']]; live = [L for L in allL if L['live']]
            names = ' · '.join(sec[lang] for sec in secs)
            q += ' ' + ' '.join(L['ar'] + ' ' + L['tr'] for L in live)
            body = f'''<p class="sec">{I['text']}<span>{E(names)}</span></p><p class="meta">{E(sections_count(lang, len(secs)))} · {E(published(lang, len(live)))}</p>
<p class="sprog" data-lessons="{','.join(str(L['n']) for L in live)}" hidden></p>
<div class="ft"><span class="spill">{E(lb['st']['live'])}</span><a class="go" href="{x['page']}">{E(lb['open'])} <span aria-hidden="true">{'←' if lang == 'ar' else '→'}</span></a></div>'''
            title = f'<a href="{x["page"]}">{E(x[lang])}</a>'
        else:
            body = f'<div class="ft"><span class="spill {x["status"]}">{E(lb["st"][x["status"]])}</span></div>'
            title = E(x[lang])
        cards.append(f'''<li class="scard {x['cat']} {x['status']}" data-cat="{x['cat']}" data-q="{E(q)}"><div class="cover"><p class="tag">{E(catname[x['cat']])}</p><h3>{title}</h3>{f'<p class="by">{E(by)}</p>' if by else ''}</div>
<div class="bd">{body}</div></li>''')
    # latest lessons, newest first, from every live series
    rows, cont = [], {}
    for x in SERIES:
        for sec in x.get('sections', []):
            for L in sec['lessons']:
                if not L['live']: continue
                where = f'{x[lang]} · {sec[lang]}'
                cont[L['n']] = dict(t=f'{s["lesson"]} {DIG(lang, L["n"])}: {L[lang]}', w=where)
                rows.append(f'''<li class="lrow live" data-q="{E(L['ar'] + ' ' + L['tr'] + ' ' + x['ar'] + ' ' + x['tr'] + ' ' + sec['ar'] + ' ' + sec['tr'])}"><span class="n">{DIG(lang, L['n'])}</span><div><p class="where">{E(where)}</p><h3><a href="l{L['n']}/index.html">{E(L[lang])}</a></h3><p class="lprog" data-lesson="{L['n']}" hidden></p></div><a class="pill" href="l{L['n']}/index.html">{E(lb['openL'])}</a></li>''')
    rows.reverse()
    redirect = f'''<script>{{ const h = location.hash, m = /^#l(\\d+)$/.exec(h); if (m) location.replace('map.html' + h); else if (h === '#lessons') location.replace('{MAIN_PAGE}#lessons'); }}</script>'''
    data = json.dumps(cont, ensure_ascii=False).replace('</', '<\\/')
    return head(lang, f'{s["brand"]} · {lb["title"]}', depth, lb['lead']) + redirect + bar(lang, depth, other) + f'''<main id="main" class="lib">
<section class="hero">{ORN}<div class="wrap"><div class="in">
  <div class="emblem"><img src="{u}media/logo.webp" alt="{E(s['brand'])}"></div>
  <div><p class="eb">{E(s['eb'])}</p><h1>{E(lb['title'])}</h1><p class="lead">{E(lb['lead'])}</p>
  <label class="srch">{SEARCH_I}<input id="libQ" type="search" placeholder="{E(lb['search'])}" aria-label="{E(lb['search'])}" autocomplete="off"></label></div>
</div></div></section>

<section class="band" id="contBand" hidden><div class="wrap">
  <h2>{E(lb['contT'])}</h2>
  <div class="cont"><span class="ic">{I['text']}</span><div><p class="where" id="contW"></p><h3 id="contT"></h3><p class="lprog" id="contP" hidden></p></div><a class="btn" id="contA" href="#">{E(lb['contB'])}</a></div>
</div></section>

<section class="band" id="series"><div class="wrap">
  <h2>{E(lb['seriesT'])}</h2><p class="sub">{E(lb['seriesS'])}</p>
  <ul class="cats" aria-label="{E(lb['seriesT'])}">{cats}</ul>
  <ul class="sgrid">{''.join(cards)}</ul>
  <p class="noresult" id="noResult" hidden>{E(lb['noResult'])}</p>
</div></section>

<section class="band tight" id="latest"><div class="wrap">
  <h2>{E(lb['latestT'])}</h2><p class="sub">{E(lb['latestS'])}</p>
  <ol class="list">{''.join(rows)}</ol>
</div></section>

<section class="band tight"><div class="wrap">
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
    n = L['n']
    return dict(
        home='../index.html',
        text='text.html',
        slides='slides.html', qa='qa.html', quiz='quiz.html', hub='index.html',
        map=f'../map.html#l{n}',
        media='../media/' if lang == 'ar' else '../../media/',
        assets='../assets/' if lang == 'ar' else '../../assets/',
        other=lambda page: (f'../tr/l{n}/{page}' if lang == 'ar' else f'../../l{n}/{page}'),
    )

def phead(lang, L, title, sub, crumbs_extra=None):
    s = S[lang]
    eb = f'{s["lesson"]} {DIG(lang, L["n"])} · ' + (f'{s["point"]} {ORD[lang][L["n"]-1]} {s["of"]}' if lang == 'ar' else f'{ORD[lang][L["n"]-1]} {s["point"]} {s["of"]}')
    cr = f'<a href="../index.html">{E(s["home"])}</a><span class="sep">›</span><a href="../{MAIN_PAGE}#taghut">{E(MAIN[lang])}</a><span class="sep">›</span>'
    if crumbs_extra:
        cr += f'<a href="index.html">{E(s["lesson"])} {DIG(lang, L["n"])}</a><span class="sep">›</span><span>{E(crumbs_extra)}</span>'
    else:
        cr += f'<span>{E(s["lesson"])} {DIG(lang, L["n"])}</span>'
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
    if (L['n'], lang) in SUM:
        tools.append(tool('sum', s['tSum'], 'summary.html'))
    sh = share_img(lang, L)
    if sh:
        tools.append(tool('share', s['tShare'], f'{P["media"]}{sh}').replace('<a class="tool" href=', '<a class="tool" download href=', 1))
    meal = f'<p class="meal">{E(L["verseTr"])}</p>' if lang == 'tr' else ''
    path = ''.join(f'<li>{E(x)}</li>' for x in s['path'])
    idx = LIVE.index(L)
    pager = ''
    if idx > 0:
        pv = LIVE[idx-1]; pager += f'<a href="../l{pv["n"]}/index.html"><small>{E(s["prev"])}</small><b>{E(pv[lang])}</b></a>'
    if idx < len(LIVE) - 1:
        nx = LIVE[idx+1]; pager += f'<a class="nx" href="../l{nx["n"]}/index.html"><small>{E(s["next"])}</small><b>{E(nx[lang])}</b></a>'
    return head(lang, f'{L[lang]} · {s["series"]}', depth, L['descAr'] if lang == 'ar' else L['descTr'], image=share_img(lang, L)) + bar(lang, depth, P['other']('index.html')) + '<main id="main">\n' + phead(lang, L, L[lang], L['descAr'] if lang == 'ar' else L['descTr']) + f'''
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

def page_text(lang, L):
    s = S[lang]; P = lesson_paths(lang, L); n = L['n']; depth = 1 if lang == 'ar' else 2
    md = open(f'{ROOT}/content/lesson{n}-{lang}.md', encoding='utf-8').read()
    body = markdown.markdown(md, extensions=['tables', 'sane_lists'])
    body = re.sub(r'<table>', '<div class="tbl"><table>', body); body = body.replace('</table>', '</table></div>')
    toc = []; c = [0]
    def hid(m):
        c[0] += 1; tag, txt = m.group(1), m.group(2)
        i = f's{c[0]}'
        if tag == 'h2': toc.append((i, re.sub('<[^>]+>', '', txt)))
        return f'<{tag} id="{i}">{txt}</{tag}>'
    body = re.sub(r'<(h[23])>(.*?)</\1>', hid, body)
    body = ayahify(body)
    if lang == 'tr': body = arabify(body)
    tocl = ''.join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, t in toc)
    return head(lang, f'{L[lang]} · {s["tText"][0]}', depth, L['descAr'] if lang == 'ar' else L['descTr'], image=share_img(lang, L)) + bar(lang, depth, P['other']('text.html')) + f'<main id="main" data-lesson="{n}" data-page="text">\n' + phead(lang, L, L[lang], s['textSub'], s['tText'][0]) + f'''
<section class="band"><div class="wrap"><div class="doc">
  <article class="prose">{fs_ctl(lang)}{body}
    <div class="endcta"><p>{E(s['textEnd'])}</p><div style="display:flex;gap:8px;flex-wrap:wrap">{done_btn(lang, n, 'text')}<a class="btn" href="qa.html">{E(s['tQA'][0])}</a><a class="btn ghost" href="quiz.html">{E(s['tQuiz'][0])}</a></div></div>
  </article>
  <aside class="toc"><details open><summary>{E(s['toc'])} <span aria-hidden="true">▾</span></summary><ol>{tocl}</ol></details></aside>
</div></div></section>
</main>
''' + footer(lang, depth) + '''<script>if (innerWidth < 960) document.querySelector('.toc details').open = false;</script>''' + f'<script src="{P["assets"]}site.js"></script>\n</body>\n</html>\n'

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
<body>
<div class="sv" data-lesson="{L['n']}">
  <div class="sv-top">
    <div class="g"><a href="index.html" aria-label="{E(s['backLesson'])}"><span aria-hidden="true">{'→' if lang == 'ar' else '←'}</span> <span class="lbl">{E(s['lesson'])} {DIG(lang, L['n'])}</span></a><img src="{P['media']}logo.webp" alt=""></div>
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
    return f'share-l{L["n"]}-{lang}.jpg' if os.path.exists(f'{ROOT}/media/share-l{L["n"]}-{lang}.jpg') else None

def lesson_url(lang, L):
    return SITE + ('' if lang == 'ar' else 'tr/') + f'l{L["n"]}/'

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
    base = f'summary-l{n}-{lang}'
    return head(lang, f'{s["tSum"][0]} · {L[lang]}', depth, L['descAr'] if lang == 'ar' else L['descTr'], extra=f'\n<link rel="stylesheet" href="{P["assets"]}summary.css">', image=share_img(lang, L)) + bar(lang, depth, P['other']('summary.html')) + '<main id="main">\n' + phead(lang, L, s['tSum'][0], L[lang], s['tSum'][0]) + f'''
<section class="band sum-band"><div class="wrap">
  <div class="sum-tools"><button class="btn" type="button" onclick="print()">{E(s['sumPrint'])}</button><a class="btn line" href="{P['media']}{base}.pdf" download>{E(s['sumPdf'])}</a><a class="btn line" href="{P['media']}{base}.jpg" download>{E(s['sumImg'])}</a><p class="note">{E(s['sumHelp'])}</p></div>
  <div class="sheet-wrap" id="sheetWrap">{sheet(lang, L, P['media'])}</div>
</div></section>
</main>
''' + footer(lang, depth) + """<script>
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
        t = t.replace('<title>خريطة دروس صفة الكفر بالطاغوت</title>', '<title>الخريطة التفاعلية · صفة الكفر بالطاغوت</title>\n' + og_tags('ar', 'الخريطة التفاعلية · صفة الكفر بالطاغوت', S['ar']['lead']) + '\n<link rel="icon" href="media/logo.webp" type="image/webp">\n<meta name="theme-color" content="#0F2E2A">\n' + app_tags('ar', ''))
    else:
        t = t.replace('data-base="../" href="../"', 'data-base="../map.html" href="../map.html"')
        home, more, quizL, allL, resetL, homeL, pinch = MAIN_PAGE, 'Diğer', 'Kendini dene', 'Haritanın tamamı', 'Baştan', 'Seri sayfası', 'Dalları okumak için iki parmakla yakınlaştırın'
        t = t.replace('<title>Tâğutu İnkârın Keyfiyeti · Ders Haritası</title>', '<title>Tâğutu İnkârın Keyfiyeti · Ders Haritası</title>\n' + og_tags('tr', 'Tâğutu İnkârın Keyfiyeti · Ders Haritası', S['tr']['lead']) + '\n<link rel="icon" href="../media/logo.webp" type="image/webp">\n<meta name="theme-color" content="#0F2E2A">\n' + app_tags('tr', '../'))
    # brand → link home
    t = re.sub(r'<div id="brand">(.*?)</div></div>', lambda m: f'<a id="brand" href="{home}" title="{homeL}">{m.group(1)}</a></div>', t, count=1, flags=re.S)
    css = f'''
/* site integration + phone fixes */
html[lang=ar] body {{ word-spacing: .14em; }}
.ov .acts button.mapdone {{ background: transparent; color: #8FE0B5; border-color: #3F8F6A; }}
.ov .acts button.mapdone.on {{ background: #3F8F6A; color: #fff; }}
#brand {{ pointer-events: auto; text-decoration: none; }}
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
  #top {{ background: linear-gradient(var(--parch) 72%, rgba(244,238,225,0)); height: 66px; }}
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
  /* progress: the lesson's map counts as seen once the student starts it (kept on this device only) */
  const db = document.querySelector('#close .mapdone');
  if (db) {
    const K = 'wt.progress.v1', rd = () => { try { return JSON.parse(localStorage.getItem(K)) || {}; } catch (e) { return {}; } };
    const paintDone = () => { const on = !!(rd()[LI + 1] || {}).map; db.textContent = on ? db.dataset.on.replace('{x}', db.dataset.x) : db.dataset.off.replace('{x}', db.dataset.x); db.classList.toggle('on', on); db.setAttribute('aria-pressed', on); };
    db.onclick = () => { const o = rd(), l = o[LI + 1] = o[LI + 1] || {}; if (l.map) delete l.map; else l.map = 1; try { localStorage.setItem(K, JSON.stringify(o)); } catch (e) {} paintDone(); };
    paintDone();
  }
'''
    t = t.replace("  $('jamiaText').textContent = L.jamia;", js + "\n  $('jamiaText').textContent = L.jamia;", 1)
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
    keep_media = {'logo.webp', 'icon-192.png', 'apple-touch-icon.png', 'poster1.jpg', 'poster1-tr.jpg', 'poster-teaser.jpg'}
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

def page_404():
    h = head('ar', 'الصفحة غير موجودة · Sayfa bulunamadı', 0).replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="/khareeta/">')
    return h + bar('ar', 0, 'tr/index.html') + f'''<main id="main">
<section class="phead">{ORN}<div class="wrap">
  <p class="eb">٤٠٤</p><h1>الصفحة غير موجودة</h1><p>ربما تغيّر الرابط. ابدأ من الصفحة الرئيسية لتجد الدرس الذي تبحث عنه.</p>
  <p lang="tr" dir="ltr" style="font-family:'Source Sans 3',sans-serif">Sayfa bulunamadı. Aradığınız dersi bulmak için ana sayfadan başlayın.</p>
</div></section>
<section class="band"><div class="wrap" style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="index.html">الصفحة الرئيسية</a><a class="btn ghost" lang="tr" href="tr/index.html">Ana sayfa</a></div></section>
</main>
''' + footer('ar', 0) + '</body>\n</html>\n'

# ------------------------------------------------------------------ write
def w(path, text):
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
    w(MAIN_PAGE, page_series('ar')); w('tr/' + MAIN_PAGE, page_series('tr'))
    for L in LIVE:
        n = L['n']
        for lang, pre in (('ar', ''), ('tr', 'tr/')):
            w(f'{pre}l{n}/index.html', page_hub(lang, L))
            w(f'{pre}l{n}/slides.html', page_slides(lang, L))
            w(f'{pre}l{n}/qa.html', page_qa(lang, L))
            w(f'{pre}l{n}/quiz.html', page_quiz(lang, L))
            if (n, lang) in SUM: w(f'{pre}l{n}/summary.html', page_summary(lang, L))
            w(f'{pre}l{n}/text.html', page_text(lang, L))
    w('404.html', page_404())
    write_app_files()
    w('.nojekyll', '')
    print('built', OUT)

if __name__ == '__main__':
    build()
