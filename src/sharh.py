# صفحة «الشرح» لكل درس: متن الكتاب فقرةً فقرة كما هو، وفي كل فقرة كلمات يُضغط عليها فيظهر معناها.
#
# كيف تُكتب الفقرة:
#   ar      نص الكتاب بحروفه. الكلمة المشروحة تُكتب هكذا: [[الكلمة|المفتاح]] والمفتاح من GLOSS بالأسفل.
#   tr      ترجمة الفقرة إلى التركية (تظهر في الصفحة التركية تحت المتن العربي).
#   fn      حواشي الكتاب على الفقرة، بحروفها.
#   note    تنبيه منّا على الحاشية إن لزم (ar, tr).
#   sharh   شرح الفقرة (ar, tr): يُضاف لاحقًا. يُكتب Markdown بسيطًا، ويظهر تحت المتن إن وُجد.
#   audio   ملف الشرح الصوتي في media/ (ar, tr): يُضاف لاحقًا، ويظهر مشغّل تحت المتن إن وُجد.
#
# مصادر معاني الكلمات مذكورة مع كل كلمة؛ ولا تُضاف كلمة بلا مصدر.

BOOK = dict(
    ar='«الفقه الميسّر في ضوء الكتاب والسنة»، تأليف مجموعة من العلماء',
    tr='«el-Fıkhu’l-Müyesser fî Dav’i’l-Kitâbi ve’s-Sünne» (bir âlimler heyeti)',
)

GLOSS = {
 'fiqh': dict(w='نَفْقَهُ',
   ar='من الفقه، وهو في اللغة: الفهم. أي: ما نفهم.',
   tr='Fıkıh kökündendir; fıkıh sözlükte «anlamak»tır. Yani: anlamıyoruz.',
   src='الكتاب نفسه (المقدمة/ ١٨)'),
 'ran': dict(w='ران',
   ar='من الرَّيْن، وأصل الرَّين: الطَّبْع والتغطية؛ ومنه قوله تعالى: ﴿كَلَّا بَلْ رَانَ عَلَى قُلُوبِهِمْ﴾ أي: طبع وختم.',
   tr='«Reyn» kökündendir; aslı mühürlemek ve örtmektir. ﴿كَلَّا بَلْ رَانَ عَلَى قُلُوبِهِمْ﴾ âyetinde de bu anlamdadır: kalpleri mühürledi, örttü.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٢٩١)'),
 'hadath': dict(w='الحَدَث',
   ar='وصف قائم بالبدن يمنع من الصلاة ونحوها مما يشترط له الطهارة. وهو نوعان: أصغر يرتفع بالوضوء، وأكبر يرتفع بالغسل.',
   tr='Bedende bulunan ve namaz gibi taharet şartı olan şeylere engel olan bir vasıf. İki türlüdür: abdestle kalkan küçük hades ve gusülle kalkan büyük hades.',
   src='حاشية الكتاب (١/ ١)'),
 'khabath': dict(w='الخَبَث',
   ar='النجاسة.',
   tr='Necaset (pislik).',
   src='حاشية الكتاب (١/ ١)'),
 'nadh': dict(w='نَضْحه',
   ar='النَّضْح: رَشُّ الماء.',
   tr='Nadh: su serpmek.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (١/ ١٣٤)'),
 'said': dict(w='صَعِيدًا',
   ar='اختلف أهل التأويل فيه: فقيل: الأرض الملساء التي لا نبات فيها، وقيل: التراب، وقيل: وجه الأرض.',
   tr='Müfessirler farklı söylemiştir: bitki bitmeyen düz yer; toprak; yeryüzü.',
   src='ابن جرير الطبري، «جامع البيان» (ت. التركي ٧/ ٨١–٨٢)'),
 'qulla': dict(w='قُلَّتين',
   ar='القُلّة هي الجرّة، جمعها قُلَل وقِلال. والقلّتان خمس قِرَب تقريبًا.',
   tr='Kulle: büyük testi; çoğulu kulel ve kılâl. İki kulle yaklaşık beş kırbadır.',
   src='حاشية الكتاب (١/ ٣)'),
 'ushnan': dict(w='الأُشْنان',
   ar='معرَّب، وهو حَمْض تُغسل به الأيدي، ويقال له بالعربية: الحُرْض، ويقال بكسر الألف أيضًا.',
   tr='Arapçaya başka dilden geçmiş bir kelimedir: çorak ve tuzlu yerlerde yetişen otlardan (hamd) bir bitki; elleri yıkamada kullanılır. Arapçada «hurd» da denir.',
   src='حاشية الكتاب (١/ ٣)'),
 'sidr': dict(w='السِّدْر',
   ar='شجر النَّبْق، واحدته سِدْرة.',
   tr='Nebk ağacı (bir tür hünnap ağacı); tekili sidre.',
   src='ابن سيده، «المحكم والمحيط الأعظم» (٨/ ٤٤٥)'),
 'tawr': dict(w='الأَتْوار',
   ar='جمع تَوْر، وهو: إناء يُشرب فيه.',
   tr='«Tevr»in çoğulu: içinden su içilen bir kap.',
   src='حاشية الكتاب (١/ ٤)'),
 'jafna': dict(w='الجِفان',
   ar='واحدتها: جَفْنة، وهي كالقَصْعة.',
   tr='Tekili «cefne»: büyük ve geniş bir kap, çanak gibi.',
   src='حاشية الكتاب (١/ ٤)'),
 'tawwaf': dict(w='الطَّوَّافين',
   ar='الطائف: الخادم الذي يخدمك برفق وعناية، والطوّاف: فعّال منه؛ شبّهها بالخادم الذي يطوف على مولاه ويدور حوله.',
   tr='«Tâif»: sana yumuşaklık ve özenle hizmet eden hizmetçi; «tavvâf» bunun mübalağalı hâlidir. Kediyi, efendisinin etrafında dolaşan hizmetçiye benzetmiştir.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٣/ ١٤٢)'),
 'walagh': dict(w='وَلَغ',
   ar='شرب منه بلسانه.',
   tr='Diliyle ondan içti (yaladı).',
   src='حاشية الكتاب (١/ ٥)'),
 'rijs': dict(w='رِجْسٌ',
   ar='الرِّجس: القَذَر، وقد يُعبَّر به عن الحرام والفعل القبيح والعذاب واللعنة.',
   tr='Rics: pislik; bazen haram, çirkin iş, azap ve lanet için de kullanılır.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٢٠٠)'),
}

GLOSS_TR_SRC = {
 'الكتاب نفسه (المقدمة/ ١٨)': 'Kitabın kendisi (Mukaddime/ 18)',
 'حاشية الكتاب (١/ ١)': 'Kitabın dipnotu (1/ 1)',
 'حاشية الكتاب (١/ ٣)': 'Kitabın dipnotu (1/ 3)',
 'حاشية الكتاب (١/ ٤)': 'Kitabın dipnotu (1/ 4)',
 'حاشية الكتاب (١/ ٥)': 'Kitabın dipnotu (1/ 5)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٢٩١)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (2/ 291)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (١/ ١٣٤)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (1/ 134)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٣/ ١٤٢)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (3/ 142)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٢٠٠)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (2/ 200)',
 'ابن جرير الطبري، «جامع البيان» (ت. التركي ٧/ ٨١–٨٢)': 'Taberî, Câmiu’l-Beyân (Türkî tahkiki 7/ 81–82)',
 'ابن سيده، «المحكم والمحيط الأعظم» (٨/ ٤٤٥)': 'İbn Sîde, el-Muhkem (8/ 445)',
}

def P(ar, tr, pg, fn=None, note=None):
    return dict(ar=ar, tr=tr, pg=pg, fn=fn or [], note=note, sharh=None, audio=None)

SHARH = {
 101: [
  dict(ar='التمهيد: معنى الفقه، ومصادره، وموضوعه، وثمرته، وفضله', tr='Giriş: Fıkhın anlamı, kaynakları, konusu, faydası ve fazileti', paras=[
   P('الفقه في اللغة: الفهم. ومنه قول الله تعالى عن قوم شعيب: ﴿... مَا [[نَفْقَهُ|fiqh]] كَثِيرًا مِمَّا تَقُولُ ...﴾ [هود: ٩١]. وقوله عز وجل: ﴿... وَلَكِنْ لَا تَفْقَهُونَ تَسْبِيحَهُمْ ...﴾ [الإسراء: ٤٤].',
     'Fıkıh sözlükte «anlamak»tır. Allah Teâlâ’nın Şuayb’ın kavmi hakkındaki şu sözü bundandır: «…Söylediklerinin çoğunu anlamıyoruz…» [Hûd, 91]. Yine Allah’ın şu sözü: «…fakat siz onların tesbihlerini anlamazsınız…» [İsrâ, 44].',
     'المقدمة/ ١٨'),
   P('والفقه في الاصطلاح: العلم بالأحكام الشرعية العملية المكتسبة من أدلتها التفصيلية. وقد يطلق الفقه على الأحكام نفسها.',
     'Fıkıh ıstılahta: ayrıntılı delillerinden elde edilen amelî şer’î hükümleri bilmektir. Fıkıh kelimesi bazen bu hükümlerin kendisi için de kullanılır.',
     'المقدمة/ ١٨'),
   P('مصادر الفقه «الأساسية»: ١- القرآن الكريم. ٢- السنة المطهرة. ٣- الإجماع. ٤- القياس.',
     'Fıkhın «temel» kaynakları: 1- Kur’ân-ı Kerîm. 2- Temiz Sünnet. 3- İcmâ. 4- Kıyas.',
     'المقدمة/ ١٨'),
   P('موضوع الفقه: أفعال المكلفين من العباد على نحوٍ عام وشامل، فهو يتناول علاقات الإنسان مع ربه، ومع نفسه، ومع مجتمعه. ويتناول الأحكام العملية، وما يصدر عن المكلف من أقوال، وأفعال، وعقود وتصرفات. وهي على نوعين: الأول: أحكام العبادات: من صلاة، وصيام، وحج، ونحوها. الثاني: أحكام المعاملات: من عقود، وتصرفات، وعقوبات، وجنايات، وضمانات وغيرها مما يقصد به تنظيم علاقات الناس بعضهم مع بعض.',
     'Fıkhın konusu: kulların içinden mükellef olanların fiilleridir; genel ve kapsayıcı bir şekilde. İnsanın Rabbiyle, kendisiyle ve toplumuyla ilişkilerini ele alır. Amelî hükümleri ve mükelleften sadır olan sözleri, fiilleri, akitleri ve tasarrufları kapsar. Bunlar iki türlüdür: Birincisi, ibadet hükümleri: namaz, oruç, hac ve benzerleri. İkincisi, muamelât hükümleri: akitler, tasarruflar, cezalar, cinayetler, tazminatlar ve insanların birbirleriyle ilişkilerini düzenlemeyi amaçlayan diğer hükümler.',
     'المقدمة/ ١٨–١٩'),
   P('وهذه الأحكام يمكن حصرها فيما يلي: ١- أحكام الأسرة من بدء تكوينها إلى نهايتها. وتشمل: أحكام الزواج، والطلاق، والنسب، والنفقة، والميراث ونحوها. ٢- أحكام المعاملات المالية (المدنية): وهي المتعلقة بمعاملات الأفراد، ومبادلاتهم من: بيع، وإجارة، وشركة ونحوها. ٣- الأحكام الجنائية: وهي التي تتعلق بما يصدر عن المكلف من جرائم وتعديات، وما يستحقه عليها من عقوبات. ٤- أحكام المرافعات والقضاء: وهي المتعلقة بالقضاء في الخصومات، والدعوى، وطرق الإثبات ونحوها. ٥- الأحكام الدولية: وهي التي تتعلق بتنظيم علاقة الدولة الإسلامية بغيرها من الدول في السلم والحرب، وعلاقة غير المسلمين المواطنين بالدولة. وتشمل الجهاد والمعاهدات.',
     'Bu hükümler şöyle sınırlandırılabilir: 1- Ailenin kuruluşundan sonuna kadar aile hükümleri: evlilik, boşanma, nesep, nafaka, miras ve benzerleri. 2- Malî (medenî) muamele hükümleri: fertlerin alım-satım, kira, ortaklık gibi muamele ve değişimleriyle ilgili hükümler. 3- Cezaî hükümler: mükelleften sadır olan suç ve tecavüzler ile bunlara karşılık hak ettiği cezalar. 4- Yargılama ve kaza hükümleri: davalar, iddialar ve ispat yolları gibi. 5- Devletler arası hükümler: İslam devletinin barışta ve savaşta diğer devletlerle ilişkisini ve gayrimüslim vatandaşların devletle ilişkisini düzenleyen hükümler; cihad ve antlaşmaları da kapsar.',
     'المقدمة/ ١٩'),
   P('ثمرة علم الفقه: معرفة الفقه، والعمل به، تثمر صلاح المكلف، وصحة عبادته، واستقامة سلوكه. وإذا صلح العبد صلح المجتمع، وصارت النتيجة في الدنيا السعادة والعيش الرغد، وفي الأخرى رضوان الله وجنته.',
     'Fıkıh ilminin faydası: Fıkhı bilmek ve onunla amel etmek; kişinin düzelmesini, ibadetinin sahih olmasını ve davranışının doğru olmasını sağlar. Kul düzelince toplum da düzelir; sonuç dünyada mutluluk ve bolluk içinde yaşamak, ahirette ise Allah’ın rızası ve cennetidir.',
     'المقدمة/ ١٩'),
   P('فضل الفقه في الدين والحث على طلبه وتحصيله: إن التفقه في الدين من أفضل الأعمال، ومن أطيب الخصال. وقد دلت النصوص من الكتاب والسنة على فضله، والحث عليه. منها: قوله تعالى: ﴿وَمَا كَانَ الْمُؤْمِنُونَ لِيَنْفِرُوا كَافَّةً فَلَوْلَا نَفَرَ مِنْ كُلِّ فِرْقَةٍ مِنْهُمْ طَائِفَةٌ لِيَتَفَقَّهُوا فِي الدِّينِ وَلِيُنْذِرُوا قَوْمَهُمْ إِذَا رَجَعُوا إِلَيْهِمْ لَعَلَّهُمْ يَحْذَرُونَ﴾ [التوبة: ١٢٢]. وقوله ﷺ: «من يرد الله به خيرًا يفقهه في الدين» (١).',
     'Dinde fıkhın fazileti ve onu öğrenmeye teşvik: Dinde derin anlayış sahibi olmak amellerin en faziletlilerinden ve hasletlerin en güzellerindendir. Kitap ve Sünnet’in nasları onun faziletine ve ona teşvike delalet eder. Bunlardan biri Allah Teâlâ’nın şu sözüdür: «Müminlerin hepsinin birden savaşa çıkması doğru değildir. Her topluluktan bir grubun dinde derin bilgi edinmek ve döndüklerinde kavimlerini uyarmak için ayrılması gerekmez miydi? Umulur ki sakınırlar.» [Tevbe, 122]. Ve Nebî’nin (sallallâhu aleyhi ve sellem) şu sözü: «Allah kime hayır dilerse onu dinde derin anlayış sahibi kılar.» (1)',
     'المقدمة/ ١٩', fn=['(١) رواه البخاري برقم (٧١)، ومسلم برقم (١٠٣٧).']),
   P('فقد رتب النبي ﷺ الخير كله على الفقه في الدين، وهذا مما يدل على أهميته، وعظم شأنه وعلوّ منزلته. وقوله ﷺ: «الناس معادن خيارهم في الجاهلية خيارهم في الإسلام إذا فقهوا» (١). فالفقه في الدين منزلته في الإسلام عظيمة، ودرجته في الثواب كبيرة؛ لأن المسلم إذا تفقه في أمور دينه، وعرف ما له، وما عليه من حقوق وواجبات، يعبد ربه على علم وبصيرة، ويُوَفَّق للخير والسعادة في الدنيا والآخرة.',
     'Nebî (sallallâhu aleyhi ve sellem) hayrın tamamını dinde fıkha bağlamıştır; bu, onun önemine, şanının büyüklüğüne ve makamının yüceliğine delalet eder. Yine şu sözü: «İnsanlar madenler gibidir; cahiliyede en hayırlı olanları, dini anladıklarında İslam’da da en hayırlılarıdır.» (1) Dinde fıkhın İslam’daki yeri büyük, sevaptaki derecesi yüksektir; çünkü Müslüman dininin işlerinde anlayış sahibi olur, lehine ve aleyhine olan hakları ve vazifeleri bilirse Rabbine ilim ve basiret üzere ibadet eder; dünyada ve ahirette hayra ve mutluluğa muvaffak kılınır.',
     'المقدمة/ ١٩–٢٠', fn=['(١) رواه البخاري برقم (٣٣٨٣) واللفظ له، ومسلم برقم (٢٦٣٨).']),
  ]),
  dict(ar='المسألة الأولى: التعريف بالطهارة، وبيان أهميتها، وأقسامها', tr='Birinci mesele: Taharetin tanımı, önemi ve kısımları', paras=[
   P('١- أهمية الطهارة وأقسامها: الطهارة هي مفتاح الصلاة، وآكد شروطها، والشرط لابد أن يتقدم على المشروط.',
     '1- Taharetin önemi ve kısımları: Taharet namazın anahtarı ve şartlarının en kuvvetlisidir; şart ise şartlı olandan önce gelmek zorundadır.',
     '١/ ١'),
   P('والطهارة على قسمين: القسم الأول: طهارة معنوية وهي طهارة القلب من الشرك والمعاصي وكل ما [[ران|ran]] عليه، وهي أهم من طهارة البدن، ولا يمكن أن تتحقق طهارة البدن مع وجود نجس الشرك كما قال تعالى: ﴿إِنَّمَا الْمُشْرِكُونَ نَجَسٌ﴾ [التوبة: ٢٨]. القسم الثاني: الطهارة الحسية، وسيأتي تفصيل القول فيها في الأسطر التالية.',
     'Taharet iki kısımdır: Birinci kısım manevî taharettir: kalbin şirkten, günahlardan ve onu kirleten her şeyden temizlenmesidir. Bu, beden temizliğinden daha önemlidir; şirk necaseti varken beden temizliği gerçekleşemez. Allah Teâlâ şöyle buyurur: «Müşrikler ancak bir necasettir.» [Tevbe, 28]. İkinci kısım maddî taharettir; ayrıntısı ileriki satırlarda gelecektir.',
     '١/ ١'),
   P('٢- تعريفها: وهي في اللغة: النظافة، والنزاهة من الأقذار. وفي الاصطلاح: رفع [[الحَدَث|hadath]]، وزوال [[الخَبَث|khabath]] (١).',
     '2- Tanımı: Sözlükte temizlik ve pisliklerden uzak olmaktır. Istılahta ise hadesi kaldırmak ve necaseti gidermektir. (1)',
     '١/ ١', fn=['(١) الحَدَثُ: هو وصف قائم بالبدن يمنع من الصلاة ونحوها مما يشترط له الطهارة. وهو نوعان: حدث أصغر؛ وهو الذي يقوم بأعضاء الوضوء كالخارج من السبيلين من بول وغائط، ويرتفع هذا بالوضوء، وحدث أكبر؛ وهو الذي يقوم بالبدن كله، كالجنابة، وهذا يرتفع بالغسل. وعلى هذا فطهارة الحدث: كبرى؛ وهي الغسل، وصغرى، وهي الوضوء، وبدل منهما عند تعذرهما؛ وهو التيمم. انظر: الشرح الممتع (١/ ١٩)، الفقه الإسلامي وأدلته (١/ ٢٣٨). والخبث: النجاسة، وسيأتي بيانها.']),
   P('والمراد بارتفاع الحدث: إزالة الوصف المانع من الصلاة باستعمال الماء في جميع البدن، إن كان الحدث أكبر، وإن كان حدثًا أصغر يكفي مروره على أعضاء الوضوء بنية، وإن فقد الماء أو عجز عنه استعمل ما ينوب عنه، وهو التراب، على الصفة المأمور بها شرعًا. وسيأتي ذكرها إن شاء الله في باب التيمم.',
     'Hadesin kalkmasından maksat, namaza engel olan vasfı gidermektir: hades büyükse bütün bedende su kullanarak; küçükse suyun niyetle abdest organlarından geçmesi yeterlidir. Su bulunmaz veya kullanılamazsa onun yerine geçen şey, yani toprak, şer’an emredilen şekilde kullanılır. İnşallah teyemmüm bölümünde zikredilecektir.',
     '١/ ١'),
   P('والمراد بزوال الخبث: أي: زوال النجاسة من البدن والثوب والمكان. فالطهارة الحسية على نوعين: طهارة حدث وتختص بالبدن، وطهارة خبث، وتكون في البدن، والثوب، والمكان. والحدث على نوعين: حدث أصغر، وهو ما يجب به الوضوء، وحدث أكبر، وهو ما يجب به الغسل. والخبث على ثلاثة أنواع: خبث يجب غسله، وخبث يجب [[نضحه|nadh]]، وخبث يجب مسحه.',
     'Necasetin giderilmesinden maksat, necasetin bedenden, elbiseden ve mekândan giderilmesidir. Buna göre maddî taharet iki türlüdür: bedene mahsus olan hades tahareti ve beden, elbise ve mekânda olan necasetten taharet. Hades iki türlüdür: abdesti gerektiren küçük hades ve guslü gerektiren büyük hades. Necaset ise üç türlüdür: yıkanması gereken, üzerine su serpilmesi gereken ve silinmesi gereken.',
     '١/ ١–٢'),
  ]),
  dict(ar='المسألة الثانية: الماء الذي تحصل به الطهارة', tr='İkinci mesele: Taharetin gerçekleştiği su', paras=[
   P('الطهارة تحتاج إلى شيء يتطهر به، يزال به النجس ويرفع به الحدث وهو الماء، والماء الذي تحصل به الطهارة هو الماء الطَّهُور، وهو: الطاهر في ذاته المطهر لغيره، وهو الباقي على أصل خلقته، أي: على صفته التي خلق عليها، سواء كان نازلًا من السماء: كالمطر وذوب الثلوج والبَرَد، أو جاريًا في الأرض: كماء الأنهار والعيون والآبار والبحار.',
     'Taharet, kendisiyle temizlenilecek; necasetin giderileceği ve hadesin kaldırılacağı bir şeye muhtaçtır; o da sudur. Taharetin gerçekleştiği su «tahûr» sudur: kendisi temiz, başkasını temizleyici olan; yaratılışındaki asıl hâli, yani yaratıldığı vasıf üzere kalan sudur. İster gökten inmiş olsun: yağmur, eriyen kar ve dolu gibi; ister yerde akıyor olsun: nehir, pınar, kuyu ve deniz suyu gibi.',
     '١/ ٢'),
   P('لقوله تعالى: ﴿وَيُنَزِّلُ عَلَيْكُمْ مِنَ السَّمَاءِ مَاءً لِيُطَهِّرَكُمْ بِهِ﴾ [الأنفال: ١١]. ولقوله تعالى: ﴿وَأَنْزَلْنَا مِنَ السَّمَاءِ مَاءً طَهُورًا﴾ [الفرقان: ٤٨]. ولقول النبي ﷺ: «اللهم اغسلني من خطاياي بالماء والثلج والبرد» (١). ولقوله ﷺ عن ماء البحر: «هو الطهور ماؤه، الحِلُّ ميتته» (٢).',
     'Delili Allah Teâlâ’nın şu sözleridir: «Sizi onunla temizlemek için üzerinize gökten su indiriyordu.» [Enfâl, 11] ve «Gökten tertemiz bir su indirdik.» [Furkân, 48]. Nebî’nin (sallallâhu aleyhi ve sellem) şu sözü: «Allah’ım! Beni hatalarımdan su, kar ve dolu ile yıka.» (1) Ve deniz suyu hakkındaki şu sözü: «Onun suyu temizleyicidir, ölüsü helaldir.» (2)',
     '١/ ٢', fn=['(١) أخرجه البخاري برقم (٧٤٤)، ومسلم برقم (٥٩٨).', '(٢) أخرجه أبو داود برقم (٨٣)، والترمذي برقم (٦٩)، والنسائي برقم (٥٩)، وابن ماجه برقم (٣٢٤٦)، قال الترمذي: حديث حسن صحيح. وصححه الألباني (صحيح سنن النسائي برقم ٥٨).']),
   P('ولا تحصل الطهارة بماء غير الماء كالخل والبنزين والعصير والليمون، وما شابه ذلك؛ لقوله تعالى: ﴿فَلَمْ تَجِدُوا مَاءً فَتَيَمَّمُوا [[صَعِيدًا|said]] طَيِّبًا﴾ [المائدة: ٦] فلو كانت الطهارة تحصل بماء غير الماء لنقل عادم الماء إليه، ولم ينقل إلى التراب.',
     'Sirke, benzin, meyve suyu, limon ve benzeri su dışındaki sıvılarla taharet gerçekleşmez. Delil Allah Teâlâ’nın şu sözüdür: «Su bulamazsanız temiz bir toprakla teyemmüm edin.» [Mâide, 6]. Eğer taharet su dışındaki bir sıvıyla gerçekleşseydi, suyu bulamayan kimse ona yönlendirilirdi; toprağa yönlendirilmezdi.',
     '١/ ٢'),
  ]),
  dict(ar='المسألة الثالثة: الماء إذا خالطته نجاسة', tr='Üçüncü mesele: Necaset karışan su', paras=[
   P('الماء إذا خالطته نجاسة فغيَّرت أحد أوصافه الثلاثة -ريحه، أو طعمه، أو لونه- فهو نجس بالإجماع لا يجوز استعماله، فلا يرفع الحدث، ولا يزيل الخبث -سواء كان كثيرًا أو قليلًا- أما إن خالطته النجاسة ولم تغير أحد أوصافه: فإن كان كثيرًا لم ينجس وتحصل الطهارة به، وأما إن كان قليلًا فينجس، ولا تحصل الطهارة به. وحدُّ الماء الكثير ما بلغ [[قُلَّتين|qulla]] (١) فأكثر، والقليل ما دون ذلك.',
     'Suya necaset karışır ve üç vasfından birini —kokusunu, tadını veya rengini— değiştirirse icmâ ile necistir; kullanılması caiz değildir: hadesi kaldırmaz, necaseti gidermez; ister çok olsun ister az. Necaset karışır da vasıflarından hiçbirini değiştirmezse: su çoksa necis olmaz ve onunla taharet gerçekleşir; azsa necis olur ve onunla taharet gerçekleşmez. Çok suyun sınırı iki kulle (1) ve fazlasıdır; az su ise bundan aşağısıdır.',
     '١/ ٢–٣', fn=['(١) القلة هي الجرة، جمعها قُلل وقلال. وهي تساوي ما يقارب ٩٣.٠٧٥ صاعًا = ١٦٠.٥ لترًا من الماء، والقلتان خمس قرب تقريبًا.']),
   P('والدليل على ذلك حديث أبي سعيد الخدري رضي الله عنه قال: قال رسول الله ﷺ: «إن الماء طهور لا ينجسه شيء» (٢)، وحديث ابن عمر رضي الله عنهما أن رسول الله ﷺ قال: «إذا بلغ الماء قلتين لم يحمل الخبث» (٣).',
     'Bunun delili Ebû Saîd el-Hudrî’nin (radıyallâhu anh) hadisidir: Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Su temizleyicidir; onu hiçbir şey necis kılmaz.» (2) Ve İbn Ömer’in (radıyallâhu anhümâ) hadisi: Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Su iki kulleye ulaşınca pisliği taşımaz.» (3)',
     '١/ ٣', fn=['(٢) أخرجه أحمد في مسنده (٣/ ١٥)، وأبو داود في كتاب الطهارة باب ما جاء في بئر بضاعة، برقم (٦١)، والنسائي في كتاب المياه برقم (٢٧٧)، والترمذي في كتاب الطهارة، باب أن الماء لا ينجسه شيء برقم (٦٦) وقال: حديث حسن. وصححه الألباني في الإرواء (١/ ٤٥).',
       '(٣) أخرجه أحمد برقم (٢/ ٢٧)، وأبو داود في كتاب الطهارة باب ما ينجس الماء برقم (٦٣)، والترمذي في كتاب الطهارة باب أن الماء لا ينجسه شيء برقم (٦٧)، والنسائي كتاب الطهارة برقم (٥٢)، وابن ماجه كتاب الطهارة باب مقدار الماء الذي لا ينجس برقم (٥١٧) ولفظه: إذا كان الماء قلتين لم ينجسه شيء، وصححه الألباني في الإرواء (١/ ٤٥).'],
     note=dict(ar='تنبيه على الحاشية (٢): حديث بئر بضاعة في «سنن أبي داود» برقم (٦٦)، أما رقم (٦١) فهو حديث «مفتاح الصلاة الطهور».',
               tr='(2) numaralı dipnot hakkında: Budâa kuyusu hadisi Ebû Dâvûd’un Sünen’inde 66 numaradadır; 61 numara ise «Namazın anahtarı temizliktir» hadisidir.')),
  ]),
  dict(ar='المسألة الرابعة: الماء إذا خالطه طاهر', tr='Dördüncü mesele: Temiz bir madde karışan su', paras=[
   P('الماء إذا خالطته مادة طاهرة، كأوراق الأشجار أو الصابون أو [[الأُشْنان|ushnan]] (٤) أو [[السِّدْر|sidr]] أو غير ذلك من المواد الطاهرة، ولم يغلب ذلك المخالط عليه، فالصحيح أنه طهور يجوز التطهر به من الحدث والنجاسة، لأن الله سبحانه وتعالى قال: ﴿وَإِنْ كُنْتُمْ مَرْضَى أَوْ عَلَى سَفَرٍ أَوْ جَاءَ أَحَدٌ مِنْكُمْ مِنَ الْغَائِطِ أَوْ لَامَسْتُمُ النِّسَاءَ فَلَمْ تَجِدُوا مَاءً فَتَيَمَّمُوا صَعِيدًا طَيِّبًا فَامْسَحُوا بِوُجُوهِكُمْ وَأَيْدِيكُمْ﴾ [النساء: ٤٣].',
     'Suya ağaç yaprakları, sabun, üşnan (4), sidr veya bunlar dışındaki temiz maddelerden biri karışır ve karışan şey suya galip gelmezse, doğru olan görüşe göre su tahûrdur; onunla hadesten ve necasetten temizlenmek caizdir. Çünkü Allah Sübhânehû ve Teâlâ şöyle buyurmuştur: «Eğer hasta veya yolculukta iseniz ya da biriniz ayakyolundan gelmişse yahut kadınlara dokunmuşsanız ve su bulamamışsanız, temiz bir toprakla teyemmüm edin; yüzlerinize ve ellerinize sürün.» [Nisâ, 43]',
     '١/ ٣', fn=['(٤) معرَّب، وهو حمض تغسل به الأيدي، ويقال له بالعربية: الحُرْضُ، ويقال بكسر الألف أيضًا.']),
   P('فلفظ الماء في الآية نكرة في سياق النفي، فيعم كل ماء. لا فرق بين الماء الخالص والمخلوط.',
     'Âyetteki «su» lafzı olumsuzluk bağlamında nekre olarak gelmiştir; dolayısıyla her suyu kapsar. Saf su ile karışık su arasında fark yoktur.',
     '١/ ٣'),
   P('ولقوله ﷺ للنسوة اللاتي قمن بتجهيز ابنته: «اغسلنها ثلاثًا أو خمسًا، أو أكثر من ذلك إن رأيتن، بماء وسدر، واجعلن في الآخرة كافورًا، أو شيئًا من كافور» (٥).',
     'Bir de Nebî’nin (sallallâhu aleyhi ve sellem), kızını (vefatında) hazırlayan kadınlara söylediği şu söz: «Onu üç, beş ya da gerekli görürseniz daha fazla, su ve sidr ile yıkayın; sonuncusuna kâfur ya da biraz kâfur katın.» (5)',
     '١/ ٣', fn=['(٥) متفق عليه: أخرجه البخاري برقم (١٢٥٣، ١٢٥٨، ١٢٥٩، وغيرها)، ومسلم برقم (٩٣٩).']),
  ]),
  dict(ar='المسألة الخامسة: حكم الماء المستعمل في الطهارة', tr='Beşinci mesele: Taharette kullanılmış suyun hükmü', paras=[
   P('الماء المستعمل في الطهارة -كالماء المنفصل عن أعضاء المتوضئ والمغتسل- طاهر مطهر لغيره على الصحيح، يرفع الحدث ويزيل النجس، ما دام أنه لم يتغير منه أحد الأوصاف الثلاثة: الرائحة والطعم واللون.',
     'Taharette kullanılmış su —abdest alan ve gusleden kimsenin organlarından ayrılan su gibi— doğru olan görüşe göre temiz ve başkasını temizleyicidir; üç vasfından biri, yani kokusu, tadı ve rengi değişmediği sürece hadesi kaldırır ve necaseti giderir.',
     '١/ ٤'),
   P('ودليل طهارته: «أن النبي ﷺ كان إذا توضأ كادوا يقتتلون على وضوئه» (١)، ولأنه ﷺ صبَّ على جابر من وضوئه إذ كان مريضًا (٢). ولو كان نجسًا لم يجز فعل ذلك، ولأن النبي ﷺ وأصحابه ونساءه كانوا يتوضؤون في الأقداح و[[الأَتْوار|tawr]] (٣)، ويغتسلون في [[الجِفان|jafna]] (٤)، ومثل هذا لا يَسْلَم من رشاش يقع في الماء من المُستَعْمِل، ولقوله ﷺ لأبي هريرة وقد كان جنبًا: «إن المؤمن لا ينجس» (٥). وإذا كان كذلك فإن الماء لا يفقد طهوريته بمجرد مماسته له.',
     'Temiz olduğunun delili: «Nebî (sallallâhu aleyhi ve sellem) abdest aldığında, abdest suyu için neredeyse birbirleriyle çekişirlerdi.» (1) Ayrıca o, hasta olduğu sırada Câbir’in üzerine abdest suyundan dökmüştür (2); necis olsaydı bunu yapmak caiz olmazdı. Yine Nebî (sallallâhu aleyhi ve sellem), ashabı ve hanımları kadehlerde ve tevrlerde (3) abdest alır, cefnelerde (4) gusl ederlerdi; böyle bir durumda kullanan kimseden suya sıçrayan damlalardan kaçınılamaz. Bir de cünüp olduğu hâlde Ebû Hureyre’ye söylediği şu söz: «Mümin necis olmaz.» (5) Durum böyle olunca su, sadece mümine dokunmakla tahûrluğunu kaybetmez.',
     '١/ ٤', fn=['(١) رواه البخاري برقم (١٨٩).', '(٢) أخرجه البخاري برقم (٥٦٥١)، ومسلم برقم (١٦١٦).', '(٣) جمع تَوْر، وهو: إناء يشرب فيه.', '(٤) واحدتها: جَفنَة، وهي كالقصعة.', '(٥) رواه مسلم برقم (٣٧١).']),
  ]),
  dict(ar='المسألة السادسة: أسآر الآدميين وبهيمة الأنعام', tr='Altıncı mesele: İnsanların ve hayvanların artık suyu', paras=[
   P('السُّؤر: هو ما بقي في الإناء بعد شرب الشارب منه، فالآدمي طاهر، وسؤره طاهر، سواء كان مسلمًا أو كافرًا، وكذلك الجنب والحائض، وقد ثبت أن رسول الله ﷺ قال: «المؤمن لا ينجس» (٦). وعن عائشة: أنها كانت تشرب من الإناء وهي حائض، فيأخذه رسول الله ﷺ، فيضع فاه على موضع فيها (٧).',
     'Sür’ (artık su): İçen kimsenin içtikten sonra kapta kalan sudur. İnsan temizdir, artığı da temizdir; Müslüman olsun kâfir olsun. Cünüp ve hayızlı da böyledir. Rasûlullah’ın (sallallâhu aleyhi ve sellem) «Mümin necis olmaz» buyurduğu sabittir (6). Âişe’den (radıyallâhu anhâ): Kendisi hayızlı iken kaptan içerdi; Rasûlullah (sallallâhu aleyhi ve sellem) kabı alır, ağzını onun ağzının değdiği yere koyardı (7).',
     '١/ ٤', fn=['(٦) رواه مسلم برقم (٣٧١).', '(٧) رواه مسلم برقم (٣٠٠).']),
   P('وقد أجمع العلماء على طهارة سؤر ما يؤكل لحمه من بهيمة الأنعام وغيرها.',
     'Âlimler, eti yenen hayvanların —davar ve diğerlerinin— artığının temiz olduğunda icmâ etmiştir.',
     '١/ ٤'),
   P('أما ما لا يؤكل لحمه كالسباع والحمر وغيرها فالصحيح: أن سؤرها طاهر، ولا يؤثر في الماء، وبخاصة إذا كان الماء كثيرًا. أما إذا كان الماء قليلًا وتغيَّر بسبب شربها منه، فإنه ينجس.',
     'Yırtıcılar, eşekler ve benzerleri gibi eti yenmeyen hayvanlara gelince, doğru olan görüş şudur: Artıkları temizdir ve suya etki etmez; özellikle su çoksa. Su az olur da onların içmesi sebebiyle değişirse necis olur.',
     '١/ ٤–٥'),
   P('ودليل ذلك: الحديث السابق، وفيه: أنه ﷺ سُئل عن الماء، وما ينوبه من الدواب والسباع، فقال: «إذا بلغ الماء قلتين لم يحمل الخبث»، وقوله ﷺ في الهرة وقد شربت من الإناء: «إنها ليست بنجس، إنما هي من [[الطَّوَّافين|tawwaf]] عليكم والطوافات» (١)، ولأنه يشق التحرز منها في الغالب. فلو قلنا بنجاسة سؤرها، ووجوب غسل الأشياء، لكان في ذلك مشقة، وهي مرفوعة عن هذه الأمة.',
     'Delili önceki hadistir; onda Nebî’ye (sallallâhu aleyhi ve sellem) su ve ona uğrayan hayvanlarla yırtıcılar sorulmuş, o da «Su iki kulleye ulaşınca pisliği taşımaz» buyurmuştur. Bir de kaptan içen kedi hakkındaki şu sözü: «O necis değildir; o, aranızda dolaşan erkek ve dişilerdendir.» (1) Ayrıca çoğu zaman ondan sakınmak zordur. Artığının necis olduğunu ve eşyaların yıkanmasının gerektiğini söyleseydik bunda meşakkat olurdu; meşakkat ise bu ümmetten kaldırılmıştır.',
     '١/ ٥', fn=['(١) أخرجه أحمد برقم (٥/ ٢٩٦) وأبو داود في كتاب الطهارة باب سؤر الهرة برقم (٧٥)، والترمذي في كتاب الطهارة باب ما جاء في سؤر الهرة برقم (٩٢) وقال: حديث حسن صحيح، وصححه الألباني (الإرواء رقم ٢٣).']),
   P('أما سؤر الكلب فإنه نجس، وكذلك الخنزير. أما الكلب: فعن أبي هريرة رضي الله عنه أن رسول الله ﷺ قال: «طهور إناء أحدكم إذا [[وَلَغ|walagh]] (٢) فيه الكلب، أن يغسله سبع مرات، أولاهن بالتراب» (٣). وأما الخنزير: فلنجاسته، وخبثه، وقذارته، قال الله تعالى: ﴿فَإِنَّهُ [[رِجْسٌ|rijs]]﴾ [الأنعام: ١٤٥].',
     'Köpeğin artığına gelince necistir; domuzunki de öyledir. Köpek hakkında Ebû Hureyre’den (radıyallâhu anh): Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Birinizin kabına köpek ağzını daldırırsa (2) onun temizlenmesi, ilki toprakla olmak üzere yedi kez yıkanmasıdır.» (3) Domuz ise necis, habis ve pis olduğu içindir. Allah Teâlâ şöyle buyurur: «…çünkü o pistir.» [En’âm, 145]',
     '١/ ٥', fn=['(٢) وَلَغَ: شرب منه بلسانه.', '(٣) رواه البخاري (١٧٢)، ومسلم برقم (٢٧٩) - ٩١، واللفظ لمسلم.']),
  ]),
 ],
}


# ------------------------------------------------------------------ الدرس الثاني: الآنية (الباب الثاني، ١/ ٦–٨)
# sharh: شرحنا للفقرة، على طريقة الشرح المعتمد في المجلس (سؤال، ثم معنى الكلمات، ثم العلّة والمثال)، بعبارتنا،
# ويليه «شرح الحواشي» إن كان للفقرة حواشٍ.

GLOSS.update({
 'sihaf': dict(w='صِحافها',
   ar='الصَّحْفة: إناء كالقَصْعة المبسوطة ونحوها، وجمعها صِحاف.',
   tr='Sahfe: yayvan çanak gibi bir kap; çoğulu sıhâf.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٣/ ١٣)'),
 'jarjar': dict(w='يُجَرْجِرُ',
   ar='أي: يُحدِر فيها نار جهنم؛ فجعل الشرب والجَرْع جَرْجَرةً، وهي صوت وقوع الماء في الجوف.',
   tr='Yani karnına cehennem ateşini indirir. İçmeyi ve yudumlamayı «cercere» diye anlatmıştır; bu, suyun karına düşerken çıkardığı sestir.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (١/ ٢٥٥)'),
 'mumawwah': dict(w='المُمَوَّه',
   ar='المطليّ.',
   tr='Kaplanmış, yaldızlanmış.',
   src='حاشية الكتاب (١/ ٦)'),
 'tadbib': dict(w='المُضَبَّب',
   ar='التضبيب: هو وصل الإناء المكسور بالحديد ونحوه.',
   tr='Tazbîb: kırılan kabı demir ve benzeri bir şeyle birleştirmek (yamamak).',
   src='حاشية الكتاب (١/ ٦)'),
 'shab': dict(w='الشَّعْب',
   ar='أي: مكان الصَّدْع والشَّقّ الذي فيه.',
   tr='Yani kaptaki çatlağın ve yarığın yeri.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٤٧٧)'),
 'mazada': dict(w='مَزَادة',
   ar='قربة كبيرة يزاد فيها جلد من غيرها.',
   tr='Başka bir deri eklenerek büyütülmüş büyük su tulumu.',
   src='حاشية الكتاب (١/ ٧)'),
 'ihala': dict(w='إهالَة سَنِخَة',
   ar='الإهالة: الشحم والزيت. والسنخة: المتغيرة الريح.',
   tr='İhâle: iç yağı ve sıvı yağ. Sanıha: kokusu değişmiş.',
   src='حاشية الكتاب (١/ ٧)'),
 'ihab': dict(w='إهاب',
   ar='الإهاب: الجلد قبل أن يدبغ.',
   tr='İhâb: tabaklanmadan önceki deri.',
   src='حاشية الكتاب (١/ ٧)'),
 'dhakat': dict(w='الذكاة',
   ar='التذكية: الذبح والنحر؛ يقال: ذكّيت الشاة تذكية، والاسم: الذكاة، والمذبوح: ذكيّ.',
   tr='Tezkiye: boğazlamak ve (deveyi) nahretmek, yani şer’î kesim. «Zekât» bunun ismidir; kesilen hayvana «zekî» denir.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ١٦٤)'),
 'qaraz': dict(w='القَرَظ',
   ar='ورق السَّلَم، يُدبغ به.',
   tr='Selem ağacının yaprağı; deri onunla tabaklanır.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٤/ ٤٣)'),
})

GLOSS_TR_SRC.update({
 'حاشية الكتاب (١/ ٦)': 'Kitabın dipnotu (1/ 6)',
 'حاشية الكتاب (١/ ٧)': 'Kitabın dipnotu (1/ 7)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٣/ ١٣)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (3/ 13)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (١/ ٢٥٥)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (1/ 255)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٤٧٧)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (2/ 477)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ١٦٤)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (2/ 164)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٤/ ٤٣)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (4/ 43)',
})

def PS(ar, tr, pg, sh_ar, sh_tr, fn=None, note=None):
    p = P(ar, tr, pg, fn=fn, note=note)
    p['sharh'] = {'ar': sh_ar, 'tr': sh_tr}
    return p

SHARH[102] = [
 dict(ar='الباب الثاني: في الآنية', tr='İkinci bölüm: Kaplar', paras=[
  PS('الآنية: هي الأوعية التي يحفظ فيها الماء وغيره، سواء كانت من الحديد أو من غيره. والأصل فيها الإباحة؛ لقوله تعالى: ﴿هُوَ الَّذِي خَلَقَ لَكُمْ مَا فِي الْأَرْضِ جَمِيعًا﴾ [البقرة: ٢٩].',
     'Kaplar: İçinde su ve başka şeylerin saklandığı kaplardır; demirden olsun veya başka bir maddeden. Kaplarda asıl olan mubahlıktır. Çünkü Allah Teâlâ şöyle buyurur: «Yeryüzünde ne varsa hepsini sizin için yaratan O’dur.» [Bakara, 29]',
     '١/ ٦',
     'لماذا يأتي باب الآنية بعد باب المياه؟ لأن الماء لا يُحفظ ولا يُحمل إلا في إناء، فبعد أن عرفنا الماء الذي نتطهّر به، نعرف الوعاء الذي نحفظه فيه ونتوضأ منه.\n\n'
     '**الآنية** جمع إناء: الكأس، والقدر، والإبريق، والقربة، والطبق، وكل ما يُحفظ فيه شيء. ولا فرق بين أن يكون من حديد أو نحاس أو زجاج أو خشب أو غيرها.\n\n'
     '**والأصل فيها الإباحة:** أي أن الإناء حلال حتى يأتي دليل يمنع منه. ووجه الاستدلال بالآية أن الله ذكر خلق ما في الأرض لنا في مقام الامتنان، ولا يمتنّ الله على عباده بشيء محرّم عليهم.',
     'Kaplar bölümü neden sulardan sonra gelir? Çünkü su ancak bir kapta saklanır ve taşınır. Temizlendiğimiz suyu öğrendikten sonra, onu sakladığımız ve ondan abdest aldığımız kabı öğreniriz.\n\n'
     '**Âniye** (kaplar), «inâ»nın çoğuludur: bardak, tencere, ibrik, kırba, tabak ve içinde bir şey saklanan her şey. Demirden, bakırdan, camdan, tahtadan veya başka bir maddeden olması fark etmez.\n\n'
     '**Asıl olan mubahlıktır:** Kap, onu yasaklayan bir delil gelinceye kadar helâldir. Âyetten delil yönü şudur: Allah, yeryüzündekileri bizim için yarattığını bir nimet olarak hatırlatır; Allah kullarına haram kıldığı bir şeyi nimet olarak saymaz.'),
 ]),
 dict(ar='المسألة الأولى: استعمال آنية الذهب والفضة وغيرهما في الطهارة', tr='Birinci mesele: Altın, gümüş ve diğer kapların taharette kullanılması', paras=[
  PS('يجوز استعمال جميع الأواني في الأكل والشرب وسائر الاستعمال، إذا كانت طاهرة مباحة، ولو كانت ثمينة، لبقائها على الأصل وهو الإباحة،',
     'Temiz ve mubah olduğu sürece bütün kapların yemede, içmede ve diğer bütün kullanımlarda kullanılması caizdir; değerli olsalar bile. Çünkü asıl hâl olan mubahlık üzere kalırlar.',
     '١/ ٦',
     'السؤال الذي تجيب عنه المسألة: **هل يجوز أن يتوضأ الإنسان من إناء ذهب أو فضة أو غيرهما؟**\n\n'
     'بدأ الكتاب بالقاعدة العامة قبل الاستثناء: كل إناء يجوز استعماله بشرطين: أن يكون **طاهرًا** (فلا يكون نجسًا كجلد ميتة لم يُدبغ)، وأن يكون **مباحًا** (فلا يكون مغصوبًا ونحوه). ولا يمنع منه أنه **ثمين**: فالإناء من الكريستال أو الحجر الكريم يُستعمل، لأن الغلاء وحده ليس دليلًا على التحريم.',
     'Meselenin cevap verdiği soru: **İnsan altın, gümüş veya başka bir kaptan abdest alabilir mi?**\n\n'
     'Kitap istisnadan önce genel kaideyle başlar: Her kap iki şartla kullanılabilir: **temiz** olması (tabaklanmamış ölü hayvan derisi gibi necis olmaması) ve **mubah** olması (gasp edilmiş vb. olmaması). **Değerli** olması ise engel değildir: Kristal veya kıymetli taştan bir kap kullanılır; çünkü pahalılık tek başına haramlığa delil değildir.'),
  PS('ما عدا آنية الذهب والفضة، فإنه يحرم الأكل والشرب فيهما خاصة، دون سائر الاستعمال؛ لقوله ﷺ: (لا تشربوا في آنية الذهب والفضة ولا تأكلوا في [[صحافها|sihaf]] فإنها لهم في الدنيا ولكم في الآخرة) (١)، وقوله ﷺ: (الذي يشرب في آنية الفضة إنما [[يجرجر|jarjar]] في بطنه نار جهنم) (٢)',
     'Altın ve gümüş kaplar bunun dışındadır: Onlarda yalnızca yemek ve içmek haramdır, diğer kullanımlar haram değildir. Çünkü Nebî (sallallâhu aleyhi ve sellem) şöyle buyurmuştur: «Altın ve gümüş kaplarda içmeyin, tabaklarında yemeyin; çünkü bunlar dünyada onlar içindir, ahirette ise sizin içindir.» (1) Yine şöyle buyurmuştur: «Gümüş kapta içen kimse, karnına ancak cehennem ateşini gürüldeterek indirir.» (2)',
     '١/ ٦',
     'هذا هو **الاستثناء** من القاعدة، وهو محدود بأمرين: **المعدن** (الذهب والفضة)، و**الفعل** (الأكل والشرب).\n\n'
     'وفي الحديث الأول **علّة** النهي: «فَإِنَّهَا لَهُمْ فِي الدُّنْيَا»، أي للكفار الذين يتنعّمون بها في دنياهم، «وَلَكُمْ فِي الْآخِرَةِ»، فهي من نعيم الجنة المدّخر للمؤمنين. وفي الحديث الثاني **وعيد** شديد: من شرب في آنية الفضة فكأنما يصبّ في بطنه نار جهنم. وتحريم الأكل والشرب فيهما محلّ إجماع، نقله ابن عبد البر في «الاستذكار» (٨/ ٣٥٠).\n\n'
     '**شرح الحواشي:** (١) الحديث في الصحيحين من حديث حذيفة رضي الله عنه. (٢) والثاني فيهما من حديث أم سلمة رضي الله عنها.',
     'Bu, kaidenin **istisnasıdır** ve iki şeyle sınırlıdır: **maden** (altın ve gümüş) ve **fiil** (yemek ve içmek).\n\n'
     'Birinci hadiste yasağın **gerekçesi** vardır: «Bunlar dünyada onlar içindir», yani dünyada bunlarla nimetlenen kâfirler içindir; «ahirette ise sizin içindir», yani müminler için saklanmış cennet nimetlerindendir. İkinci hadiste ağır bir **tehdit** vardır: Gümüş kapta içen, karnına cehennem ateşi döker gibidir. Bu ikisinde yemenin ve içmenin haram olduğunda icmâ vardır; İbn Abdilber bunu el-İstizkâr’da (8/ 350) nakletmiştir.\n\n'
     '**Dipnotların şerhi:** (1) Hadis Buhârî ve Müslim’de Huzeyfe’den (radıyallâhu anh) rivayet edilmiştir. (2) İkincisi yine ikisinde Ümmü Seleme’den (radıyallâhu anhâ) rivayet edilmiştir.',
     fn=['(١) رواه البخاري برقم (٥٤٢٦)، ومسلم برقم (٢٠٦٧).', '(٢) رواه البخاري برقم (٥٦٣٤)، ومسلم برقم (٢٠٦٥).']),
  PS('فهذا نصٌ على تحريم الأكل والشرب دون سائر الاستعمال، فدل على جواز استعمالها في الطهارة.',
     'Bu, diğer kullanımları değil, yemeyi ve içmeyi haram kılan bir nastır. Bu da onların taharette kullanılmasının caiz olduğunu gösterir.',
     '١/ ٦',
     'هنا **وجه الدلالة**: النبي ﷺ ذكر الأكل والشرب بعينهما، ولم يقل: «لا تستعملوا». فما سواهما يبقى على الأصل الذي تقرّر في أول الباب، وهو الإباحة. والوضوء والغسل ليسا أكلًا ولا شربًا، **فيجوز أن يتوضأ المسلم من إبريق فضة**.\n\n'
     'وفي هذا درس في الفقه: **نقف عند حدود النص**، فلا نوسّع التحريم إلى ما لم يذكره، ولا نضيّقه عمّا ذكره.',
     'İşte **delil yönü**: Nebî (sallallâhu aleyhi ve sellem) yemeyi ve içmeyi açıkça zikretmiş, «kullanmayın» dememiştir. Bunların dışındaki kullanımlar, bölümün başında belirlenen asıl üzere, yani mubahlık üzere kalır. Abdest ve gusül ne yemektir ne içmektir; **dolayısıyla Müslüman gümüş bir ibrikten abdest alabilir.**\n\n'
     'Burada bir fıkıh dersi vardır: **Nassın sınırında dururuz**; haramlığı nassın zikretmediğine genişletmeyiz, zikrettiğinden de daraltmayız.'),
  PS('والنهي عام يتناول الإناء الخالص، أو [[المُمَوَّه|mumawwah]] (٣) بالذهب أو الفضة، أو الذي فيه شيء من الذهب والفضة.',
     'Yasak geneldir: saf kabı, altın veya gümüşle kaplanmış (3) kabı ve içinde biraz altın veya gümüş bulunan kabı kapsar.',
     '١/ ٦',
     'ما الذي يدخل في النهي؟ ثلاثة أنواع:\n\n'
     '1. **الخالص:** الإناء المصنوع كلّه من ذهب أو فضة.\n'
     '2. **المموَّه:** إناء من معدن آخر طُلي بالذهب أو الفضة، ككأس طُليت حافّته بماء الذهب.\n'
     '3. **ما فيه شيء منهما:** إناء دخل فيه شيء من الذهب أو الفضة.\n\n'
     'فاختار الكتاب أن النهي **عام** في هذه الأنواع كلها، لأنها كلها يصدق عليها أنها آنية ذهب أو فضة. ويُستثنى من الثالث ما تأتي في المسألة التالية: الضبّة اليسيرة من الفضة.\n\n'
     '**شرح الحواشي:** (٣) المموَّه هو المطليّ؛ أي أن الطلاء وحده كافٍ لدخوله في النهي، ولو كان أصل الإناء من غير الذهب والفضة.',
     'Yasağa hangi kaplar girer? Üç çeşit:\n\n'
     '1. **Saf olan:** Tamamı altından veya gümüşten yapılmış kap.\n'
     '2. **Kaplanmış olan:** Başka bir madenden yapılıp altın veya gümüşle kaplanmış kap; kenarı altın yaldızla kaplanmış bir bardak gibi.\n'
     '3. **İçinde biraz bulunan:** İçine biraz altın veya gümüş girmiş kap.\n\n'
     'Kitap, yasağın bu çeşitlerin hepsinde **genel** olduğunu tercih etmiştir; çünkü hepsine altın veya gümüş kap denir. Üçüncüsünden, bir sonraki meselede gelecek olan az gümüş yama müstesnadır.\n\n'
     '**Dipnotların şerhi:** (3) Mumeveh, kaplanmış demektir; yani kabın aslı altın ve gümüşten olmasa bile, kaplama tek başına onu yasağa sokmaya yeter.',
     fn=['(٣) المُمَوَّه: المطليّ.']),
 ]),
 dict(ar='المسألة الثانية: حكم استعمال الإناء المُضَبَّب بالذهب والفضة', tr='İkinci mesele: Altın ve gümüşle yamanmış kabı kullanmanın hükmü', paras=[
  PS('إن كانت [[الضبة|tadbib]] (٤) من الذهب حرم استعمال الإناء مطلقاً؛ لدخوله تحت عموم النص،',
     'Yama (4) altındansa kabın kullanılması her durumda haramdır; çünkü nassın genel hükmüne girer.',
     '١/ ٦',
     'صورة المسألة: إناء من خشب أو نحاس أو غيرهما **انكسر**، فوُصل موضع الكسر ولُحِم بقطعة من معدن. هذه القطعة تسمّى **الضبّة**. فإن كانت من حديد أو نحاس فلا إشكال. **فإن كانت من ذهب أو فضة، فما الحكم؟**\n\n'
     '**الذهب:** يحرم استعمال الإناء **مطلقًا**، قليلًا كان الذهب أو كثيرًا؛ لأن الإناء صار مما «فيه شيء من الذهب»، فدخل في عموم النهي الذي تقدّم.\n\n'
     '**شرح الحواشي:** (٤) التضبيب هو الوصل: يكون الإناء مكسورًا فيُوصل بالحديد ونحوه؛ فالكلام هنا في **إصلاح** الإناء، لا في زخرفته.',
     'Meselenin sureti: Tahtadan, bakırdan veya başka bir şeyden yapılmış bir kap **kırılmış**, kırık yeri bir maden parçasıyla birleştirilip kaynatılmıştır. Bu parçaya **dabbe (yama)** denir. Demirden veya bakırdan olursa sorun yoktur. **Altından veya gümüşten olursa hüküm nedir?**\n\n'
     '**Altın:** Altın az olsun çok olsun, kabın kullanılması **her durumda** haramdır; çünkü kap «içinde biraz altın bulunan» kaplardan olmuş ve önceki genel yasağa girmiştir.\n\n'
     '**Dipnotların şerhi:** (4) Tazbîb birleştirmektir: Kap kırık olur ve demir benzeri bir şeyle birleştirilir. Burada söz konusu olan kabın **onarılmasıdır**, süslenmesi değil.',
     fn=['(٤) التضبيب: هو وصل الإناء المكسور بالحديد ونحوه.']),
  PS('أما إن كانت الضبة من الفضة وهي يسيرة فإنه يجوز استعمال الإناء؛ لحديث أنس ﵁ قال: (انكسر قدح رسول الله ﷺ فاتخذ مكان [[الشعْب|shab]] سلسلة من فضة) (٥).',
     'Yama gümüşten ve az ise kabın kullanılması caizdir. Çünkü Enes (radıyallâhu anh) şöyle demiştir: «Rasûlullah’ın (sallallâhu aleyhi ve sellem) kadehi kırıldı; çatlağın yerine gümüşten bir zincir yaptı.» (5)',
     '١/ ٦',
     '**الفضة:** يجوز استعمال الإناء بشرط أن تكون الفضة **يسيرة**. والدليل **فعل النبي ﷺ**: قدحه انشقّ، فرُبط موضع الشقّ بسلسلة صغيرة من فضة، وبقي يُستعمل.\n\n'
     'فلماذا فرّقنا بين الذهب والفضة؟ لأن الرخصة جاءت في الفضة اليسيرة وحدها، فبقي الذهب على عموم التحريم. وإن كانت الفضة **كثيرة** لم تدخل في الرخصة.\n\n'
     '**مثال:** قدح خشبي انشقّ فرُبط بشريط صغير من فضة: يُشرب فيه. ولو رُبط بشريط من ذهب: لا يُستعمل.\n\n'
     '**شرح الحواشي:** (٥) الحديث في صحيح البخاري، في الباب الذي جمع فيه ما ذُكر من درع النبي ﷺ وعصاه وسيفه وقدحه.',
     '**Gümüş:** Gümüş **az** olmak şartıyla kabın kullanılması caizdir. Delil, **Nebî’nin (sallallâhu aleyhi ve sellem) fiilidir**: Kadehi çatlamış, çatlak yeri küçük bir gümüş zincirle bağlanmış ve kullanılmaya devam etmiştir.\n\n'
     'Altın ile gümüş arasında neden ayrım yaptık? Çünkü ruhsat yalnızca az gümüş hakkında gelmiştir; altın genel haramlık üzere kalır. Gümüş **çok** olursa ruhsata girmez.\n\n'
     '**Örnek:** Çatlayan tahta bir kadeh küçük bir gümüş şeritle bağlanırsa onda içilir. Altın bir şeritle bağlanırsa kullanılmaz.\n\n'
     '**Dipnotların şerhi:** (5) Hadis, Buhârî’nin Sahîh’inde, Nebî’nin (sallallâhu aleyhi ve sellem) zırhı, asası, kılıcı ve kadehiyle ilgili rivayetleri topladığı babdadır.',
     fn=['(٥) رواه البخاري برقم (٣١٠٩).']),
 ]),
 dict(ar='المسألة الثالثة: آنية الكفار', tr='Üçüncü mesele: Kâfirlerin kapları', paras=[
  PS('الأصل في آنية الكفار الحل، إلا إذا عُلمت نجاستها، فإنه لا يجوز استعمالها إلا بعد غسلها؛ لحديث أبي ثعلبة الخشني قال: قلت يا رسول الله إنا بأرض قوم أهل كتاب، أفنأكل في آنيتهم؟ قال: (لا تأكلوا فيها إلا أن لا تجدوا غيرها فاغسلوها، ثم كلوا فيها) (١).',
     'Kâfirlerin kaplarında asıl olan helâlliktir. Ancak necaseti bilinirse, yıkandıktan sonra kullanılabilir. Çünkü Ebû Sa’lebe el-Huşenî şöyle demiştir: «Ey Allah’ın Rasûlü! Biz Ehl-i Kitap bir kavmin yurdundayız; onların kaplarında yiyelim mi?» Buyurdu ki: «Başkasını bulamazsanız hariç onlarda yemeyin; (bulamazsanız) onları yıkayın, sonra onlarda yiyin.» (1)',
     '١/ ٧',
     'الأصل في آنية الكفار **الحِلّ والطهارة**، كسائر الآنية. ويخرج عن هذا الأصل حالة واحدة: أن **تُعلم نجاستها**، فلا تُستعمل حتى تُغسل.\n\n'
     'ولماذا أمر النبي ﷺ أبا ثعلبة بالغسل؟ لأن أولئك القوم كانوا **يباشرون النجاسة في آنيتهم**: يطبخون فيها الخنزير، ويشربون فيها الخمر، كما جاء في رواية أبي داود. وفي الحديث أدب آخر: «لا تأكلوا فيها» ما دمتم تجدون غيرها؛ احتياطًا وبعدًا عمّا كانت فيه النجاسة. فإن لم تجدوا غيرها، فالغسل يكفي.\n\n'
     '**شرح الحواشي:** (١) الحديث في الصحيحين، ولفظه عندهما: «فَإِنْ وَجَدْتُمْ غَيْرَ آنِيَتِهِمْ فَلَا تَأْكُلُوا فِيهَا، وَإِنْ لَمْ تَجِدُوا فَاغْسِلُوهَا ثُمَّ كُلُوا فِيهَا»، والمعنى واحد.',
     'Kâfirlerin kaplarında asıl olan, diğer kaplar gibi **helâllik ve temizliktir**. Bu asıldan tek bir durumda çıkılır: **necasetinin bilinmesi**. O zaman yıkanmadan kullanılmaz.\n\n'
     'Nebî (sallallâhu aleyhi ve sellem) Ebû Sa’lebe’ye neden yıkamayı emretti? Çünkü o kavim **kaplarında necasetle uğraşıyordu**: Ebû Dâvûd’un rivayetinde geldiği gibi tencerelerinde domuz pişiriyor, kaplarında şarap içiyorlardı. Hadiste başka bir edep de vardır: Başkasını bulduğunuz sürece «onlarda yemeyin»; bu, ihtiyat ve necasetin bulunduğu şeyden uzak durmak içindir. Başkasını bulamazsanız yıkamak yeterlidir.\n\n'
     '**Dipnotların şerhi:** (1) Hadis Buhârî ve Müslim’dedir; ikisindeki lafzı şöyledir: «Onların kaplarından başkasını bulursanız onlarda yemeyin; bulamazsanız onları yıkayın, sonra onlarda yiyin.» Anlam aynıdır.',
     fn=['(١) رواه البخاري برقم (٥٤٧٨)، ومسلم برقم (١٩٣٠).']),
  PS('وأما إذا لم تُعلم نجاستها بأن يكون أهلها غير معروفين بمباشرة النجاسة، فإنه يجوز استعمالها؛ لأنه ثبت أن النبي ﷺ وأصحابه أخذوا الماء للوضوء من [[مَزَادة|mazada]] امرأة مشركة (٢)،',
     'Necaseti bilinmiyorsa, yani sahipleri necasetle uğraşmakla tanınmıyorsa, kullanılması caizdir. Çünkü Nebî’nin (sallallâhu aleyhi ve sellem) ve ashabının, müşrik bir kadının mezâdesinden (büyük su tulumundan) abdest için su aldıkları sabittir. (2)',
     '١/ ٧',
     'هذه هي الحالة الثانية: **لم تُعلم النجاسة**، فيبقى الإناء على الأصل: يجوز استعماله دون غسل.\n\n'
     'والدليل أن النبي ﷺ وأصحابه أخذوا الماء من قربة امرأة مشركة وتوضؤوا منه، ولم يسألوا عن قربتها ولم يغسلوها. ويُفهم من هذا أن المرأة لم تكن معروفة بمباشرة النجاسة في قربتها، فبقيت على الأصل.\n\n'
     'ويشهد لهذا حديث جابر رضي الله عنه: «كُنَّا نَغْزُو مَعَ رَسُولِ اللَّهِ ﷺ، فَنُصِيبُ مِنْ آنِيَةِ الْمُشْرِكِينَ وَأَسْقِيَتِهِمْ، فَنَسْتَمْتِعُ بِهَا، فَلَا يَعِيبُ ذَلِكَ عَلَيْهِمْ»، رواه أبو داود (٣٨٣٨).\n\n'
     '**كيف نجمع بين الدليلين؟** الغسل في حديث أبي ثعلبة لأن النجاسة **معلومة**، وترك الغسل في حديث المزادة لأنها **غير معلومة**. فلا تعارض بينهما.\n\n'
     '**شرح الحواشي:** (٢) الحديث في الصحيحين من حديث عمران بن حصين رضي الله عنه في قصة طويلة. و**المزادة** قربة كبيرة يُضاف إليها جلد آخر لتتّسع.',
     'Bu ikinci durumdur: **Necaset bilinmiyorsa** kap asıl hâli üzere kalır ve yıkamadan kullanılabilir.\n\n'
     'Delili, Nebî’nin (sallallâhu aleyhi ve sellem) ve ashabının müşrik bir kadının su tulumundan su alıp ondan abdest almalarıdır; tulumunu sormamış ve yıkamamışlardır. Buradan, kadının tulumunda necasetle uğraşmakla tanınmadığı, tulumun asıl hâli üzere kaldığı anlaşılır.\n\n'
     'Câbir’in (radıyallâhu anh) hadisi de buna şahittir: «Rasûlullah (sallallâhu aleyhi ve sellem) ile birlikte savaşırdık; müşriklerin kaplarından ve kırbalarından ele geçirip onlardan faydalanırdık; o da bunu ayıplamazdı.» Ebû Dâvûd (3838).\n\n'
     '**İki delil nasıl bağdaştırılır?** Ebû Sa’lebe hadisinde yıkama emredilmiştir; çünkü necaset **biliniyordu**. Mezâde hadisinde yıkanmamıştır; çünkü necaset **bilinmiyordu**. Dolayısıyla aralarında çelişki yoktur.\n\n'
     '**Dipnotların şerhi:** (2) Hadis, İmrân b. Husayn’ın (radıyallâhu anh) uzun bir kıssasıyla Buhârî ve Müslim’dedir. **Mezâde**, genişlemesi için başka bir deri eklenen büyük su tulumudur.',
     fn=['(٢) رواه البخاري في كتاب التيمم باب الصعيد الطيب رقم (٣٤٤) ومسلم كتاب المساجد باب قضاء الصلاة الفائتة برقم (٦٨٢)، والمزادة: قربة كبيرة يزاد فيها جلد من غيرها.']),
  PS('ولأن الله سبحانه قد أباح لنا طعام أهل الكتاب، وقد يقدِّمونه إلينا في أوانيهم، كما دعا غلام يهودي النبي ﷺ على خبز شعير و[[إهالَة سَنِخَة|ihala]] فأكل منها (٣).',
     'Ayrıca Allah Teâlâ bize Ehl-i Kitab’ın yemeğini helâl kılmıştır; onlar da onu bize kendi kaplarında sunabilirler. Nitekim Yahudi bir genç Nebî’yi (sallallâhu aleyhi ve sellem) arpa ekmeği ile kokusu değişmiş yağa davet etmiş, o da ondan yemiştir. (3)',
     '١/ ٧',
     'دليل ثالث على أن الأصل في آنيتهم الطهارة: أن الله أباح لنا طعام أهل الكتاب بقوله: ﴿وَطَعَامُ الَّذِينَ أُوتُوا الْكِتَابَ حِلٌّ لَكُمْ﴾ [المائدة: ٥]، ومعلوم أنهم يقدّمونه في أوانيهم. فلو كانت آنيتهم نجسة لما أُبيح لنا طعامهم بلا غسل.\n\n'
     'وفي قصة الغلام اليهودي **حسن خلق النبي ﷺ**: دعاه إلى طعام بسيط، خبز شعير وشحم قد تغيّرت رائحته، فأجاب دعوته وأكل منه.\n\n'
     '**شرح الحواشي:** (٣) الحديث رواه أحمد من حديث أنس رضي الله عنه، وصحّحه الألباني. و**الإهالة** الشحم أو الزيت، و**السَّنِخة** التي تغيّرت ريحها لطول بقائها.',
     'Kaplarında asıl olanın temizlik olduğuna üçüncü delil: Allah, «Kendilerine kitap verilenlerin yemeği size helâldir» [Mâide, 5] buyurarak Ehl-i Kitab’ın yemeğini bize helâl kılmıştır. Onların yemeği kendi kaplarında sundukları da bilinmektedir. Kapları necis olsaydı, yemekleri bize yıkamadan helâl kılınmazdı.\n\n'
     'Yahudi gencin kıssasında **Nebî’nin (sallallâhu aleyhi ve sellem) güzel ahlakı** vardır: Genç onu sade bir yemeğe, arpa ekmeği ve kokusu değişmiş yağa davet etmiş; o da davetine icabet edip ondan yemiştir.\n\n'
     '**Dipnotların şerhi:** (3) Hadisi Ahmed, Enes’ten (radıyallâhu anh) rivayet etmiş, Elbânî sahih kabul etmiştir. **İhâle** iç yağı veya sıvı yağdır; **sanıha** uzun süre kaldığı için kokusu değişmiş olandır.',
     fn=['(٣) أخرجه أحمد (٣/ ٢١٠، ٢١١). وصححه الألباني في الإرواء (١/ ٧١) والإهالة: الشحم والزيت. والسنخة: المتغيرة الريح.']),
 ]),
 dict(ar='المسألة الرابعة: الطهارة في الآنية المتخذة من جلود الميتة', tr='Dördüncü mesele: Ölü hayvan derisinden yapılan kaplarda taharet', paras=[
  PS('جلد الميتة إذا دبغ طهر وجاز استعماله لقوله ﷺ: (أيما [[إهاب|ihab]] (٤) دبغ فقد طهر) (٥).',
     'Ölü hayvanın derisi tabaklanınca temizlenir ve kullanılması caiz olur. Çünkü Nebî (sallallâhu aleyhi ve sellem) şöyle buyurmuştur: «Hangi deri (4) tabaklanırsa temizlenmiş olur.» (5)',
     '١/ ٧',
     'كانت القِرَب والدِّلاء والأوعية تُصنع من الجلود. فإذا ماتت شاة دون ذبح، هل يُنتفع بجلدها إناءً؟\n\n'
     '**الميتة** ما مات دون ذكاة شرعية، وهي نجسة. لكن جلدها إذا **دُبغ** طهُر. و**الدباغ** معالجة الجلد بمواد تمنع تعفّنه وتجفّفه، حتى يصلح للاستعمال.\n\n'
     '**شرح الحواشي:** (٤) **الإهاب** هو الجلد قبل أن يُدبغ. (٥) الحديث من رواية ابن عباس رضي الله عنهما.',
     'Kırbalar, kovalar ve kaplar deriden yapılırdı. Bir koyun kesilmeden ölürse, derisinden kap olarak faydalanılır mı?\n\n'
     '**Meyte**, şer’î kesim olmadan ölen hayvandır ve necistir. Ancak derisi **tabaklanınca** temizlenir. **Tabaklama**, deriyi kokuşmasını önleyen ve onu kurutan maddelerle işlemek, böylece kullanılır hâle getirmektir.\n\n'
     '**Dipnotların şerhi:** (4) **İhâb**, tabaklanmadan önceki deridir. (5) Hadis İbn Abbâs’ın (radıyallâhu anhümâ) rivayetidir.',
     fn=['(٤) الإهاب: الجلد قبل أن يدبغ.', '(٥) رواه الترمذي برقم (١٦٥٠)، ومسلم برقم (٣٦٦) بلفظ: (إذا دبغ الإهاب فقد طهر) من حديث ابن عباس.'],
     note=dict(ar='تنبيه على الحاشية (٥): الحديث في «جامع الترمذي» برقم (١٧٢٨) في الترقيم المشهور، وقال: حسن صحيح.',
               tr='(5) numaralı dipnot hakkında: Hadis, Tirmizî’nin Câmi’inde yaygın numaralandırmada 1728 numaradadır; Tirmizî «hasen sahih» demiştir.')),
  PS('ولأنه ﷺ مرّ على شاة ميتة فقال ﷺ: (هلَّا أخذوا إهابها فدبغوه فانتفعوا به)؟ فقالوا: إنها ميتة. قال: (فإنما حَرُمَ أكلُهَا) (٦).',
     'Ayrıca Nebî (sallallâhu aleyhi ve sellem) ölü bir koyunun yanından geçti ve şöyle buyurdu: «Derisini alıp tabaklasalar da ondan faydalansalar ya!» «O ölüdür» dediler. Buyurdu ki: «Onun yalnızca yenmesi haram kılındı.» (6)',
     '١/ ٧',
     'تأمّل جواب النبي ﷺ: الصحابة ظنّوا أن كون الشاة ميتة يمنع من كل انتفاع بها، فبيّن لهم أن الذي حرُم منها هو **الأكل**. أما الجلد، فإذا دُبغ صار طاهرًا يُنتفع به، **مع أنها ميتة غير مذبوحة**.\n\n'
     'وفي الحديث **حفظ المال وترك الإسراف**: فلا يُرمى ما يمكن الانتفاع به.\n\n'
     '**شرح الحواشي:** (٦) الحديث رواه مسلم، وفيه أن الشاة كانت لمولاة ميمونة رضي الله عنها، أُعطيتها من الصدقة.',
     'Nebî’nin (sallallâhu aleyhi ve sellem) cevabına dikkat edin: Sahâbe, koyunun ölü olmasının ondan her türlü faydalanmaya engel olduğunu sandılar. O da onlara bu hayvandan haram olanın **yenmesi** olduğunu açıkladı. Derisi ise tabaklanınca temiz olur ve ondan faydalanılır; **kesilmemiş, ölü bir hayvan olmasına rağmen**.\n\n'
     'Hadiste **malı korumak ve israfı terk etmek** de vardır: Faydalanılabilecek bir şey atılmaz.\n\n'
     '**Dipnotların şerhi:** (6) Hadisi Müslim rivayet etmiştir; koyun, Meymûne’nin (radıyallâhu anhâ) azatlı cariyesine sadakadan verilmiş bir koyundu.',
     fn=['(٦) رواه مسلم برقم (٣٦٣)، وابن ماجه برقم (٣٦١٠).']),
  PS('وهذا فيما إذا كانت الميتة مما تحلها [[الذكاة|dhakat]] وإلا فلا.',
     'Bu hüküm, ölü hayvan kesimin helâl kıldığı hayvanlardan ise geçerlidir; değilse geçerli değildir.',
     '١/ ٧',
     'هذا **الشرط** الذي تقوم عليه المسألة كلها. و**الذكاة** هي الذبح الشرعي الذي استوفى شروطه.\n\n'
     'فالسؤال: **لو ذُبح هذا الحيوان ذبحًا شرعيًّا، هل يحلّ أكله؟** إن كان الجواب نعم، كالشاة والبقرة والإبل، فجلده إذا مات يطهر بالدباغ. وإن كان الجواب لا، فلا يطهر جلده بالدباغ.',
     'Bütün meselenin dayandığı **şart** budur. **Zekât (tezkiye)**, şartlarını taşıyan şer’î kesimdir.\n\n'
     'Soru şudur: **Bu hayvan şer’î olarak kesilseydi eti yenir miydi?** Cevap evetse, koyun, sığır ve deve gibi, öldüğünde derisi tabaklanmakla temizlenir. Cevap hayırsa, derisi tabaklanmakla temizlenmez.'),
  PS('أما شعرها فهو طاهر -أي شعر الميتة المباحة الأكل في حال الحياة- وأما اللحم فإنه نجس، ومحرم أكله. لقوله تعالى: ﴿إِلَّا أَنْ يَكُونَ مَيْتَةً أَوْ دَمًا مَسْفُوحًا أَوْ لَحْمَ خِنْزِيرٍ فَإِنَّهُ [[رِجْسٌ|rijs]]﴾ [الأنعام: ١٤٥].',
     'Ölü hayvanın kılına gelince, o temizdir; yani hayattayken eti yenen hayvanın ölüsünün kılı. Eti ise necistir ve yenmesi haramdır. Çünkü Allah Teâlâ şöyle buyurur: «Ancak ölü hayvan, akıtılmış kan veya domuz eti olursa başka; çünkü bunlar pisliktir.» [En’âm, 145]',
     '١/ ٧',
     'فرّق الكتاب بين أجزاء الميتة المأكولة:\n\n'
     '- **الشعر** (ومثله الصوف والوبر): طاهر، ولو لم يُدبغ الجلد.\n'
     '- **اللحم:** نجس ومحرّم، بنصّ الآية: ﴿فَإِنَّهُ رِجْسٌ﴾، والرِّجس: النجس.\n\n'
     'وقيّد الكتاب الشعر بأن يكون من **الميتة المباحة الأكل في حياتها**، أي من الحيوان الذي يحلّ أكله لو ذُبح.',
     'Kitap, eti yenen ölü hayvanın parçaları arasında ayrım yapmıştır:\n\n'
     '- **Kıl** (yün ve tüy de böyledir): Deri tabaklanmasa bile temizdir.\n'
     '- **Et:** Âyetin nassıyla necis ve haramdır: «Çünkü bunlar pisliktir.» Rics, necis demektir.\n\n'
     'Kitap kılı, **hayattayken eti yenen ölü hayvanın** kılı olmakla kayıtlamıştır; yani kesilse eti helâl olan hayvanın.'),
  PS('ويحصل الدبغ بتنظيف الأذى والقذر الذي كان في الجلد، بواسطة مواد تضاف إلى الماء كالملح وغيره، أو بالنبات المعروف كـ[[القَرَظ|qaraz]] أو العرعر ونحوهما.',
     'Tabaklama, derideki eziyet verici şeylerin ve pisliklerin temizlenmesiyle olur; suya katılan tuz ve benzeri maddelerle ya da karaz veya ardıç gibi bilinen bitkilerle.',
     '١/ ٨',
     'كيف يكون الدباغ؟ المقصود أن يُزال ما في الجلد من رطوبات وقذر، حتى لا يتعفّن ويصلح للاستعمال. وذلك بأحد طريقين:\n\n'
     '1. **مواد تُضاف إلى الماء:** كالملح ونحوه.\n'
     '2. **نباتات معروفة بالدباغ:** كالقَرَظ، وهو ورق شجر السَّلَم، والعَرعَر.\n\n'
     'فليس الدباغ مجرّد تجفيف الجلد في الشمس، بل تنظيفه ومعالجته.',
     'Tabaklama nasıl olur? Amaç, deri kokuşmasın ve kullanılır hâle gelsin diye ondaki nemin ve pisliğin giderilmesidir. Bu iki yoldan biriyle olur:\n\n'
     '1. **Suya katılan maddeler:** tuz ve benzeri.\n'
     '2. **Tabaklamada bilinen bitkiler:** selem ağacının yaprağı olan karaz ve ardıç gibi.\n\n'
     'Yani tabaklama, deriyi sadece güneşte kurutmak değil; onu temizleyip işlemektir.'),
  PS('وأما ما لا تحله الذكاة فإنه لا يطهر، وعلى هذا فجلد الهرة وما دونها في الخلقة لا يطهر بالدبغ، ولو كان في حال الحياة طاهراً.',
     'Kesimin helâl kılmadığı hayvanın derisi ise temizlenmez. Buna göre kedinin ve yaratılışta ondan küçük olan hayvanların derisi, hayattayken temiz olsa bile tabaklanmakla temizlenmez.',
     '١/ ٨',
     'هنا تنبيه دقيق: **الهرّة طاهرة في حياتها**، وقد عرفنا في الدرس الأول أن سؤرها طاهر. فهل يطهر جلدها بالدباغ؟\n\n'
     '**لا.** لأن السؤال ليس: هل كان الحيوان طاهرًا وهو حيّ؟ بل: **هل يحلّ أكله إذا ذُبح؟** والهرّة لا تؤكل، فجلدها لا يطهر بالدباغ. ومثلها ما دونها في الخِلقة، أي ما كان أصغر منها من الحيوان الذي لا يُؤكل.',
     'Burada ince bir uyarı vardır: **Kedi hayattayken temizdir**; ilk derste artığının temiz olduğunu öğrendik. Peki derisi tabaklanmakla temizlenir mi?\n\n'
     '**Hayır.** Çünkü soru, «hayvan hayattayken temiz miydi?» değildir; soru, **«kesilse eti helâl olur mu?»** sorusudur. Kedi yenmez; bu yüzden derisi tabaklanmakla temizlenmez. Yaratılışta ondan küçük olan, yani ondan küçük ve eti yenmeyen hayvanlar da böyledir.'),
  PS('وجلد ما يحرم أكله ولو كان طاهراً في الحياة فإنه لا يطهر بالدباغ.',
     'Eti yenmesi haram olan hayvanın derisi, hayattayken temiz olsa bile tabaklanmakla temizlenmez.',
     '١/ ٨',
     'وهذه قاعدة الفقرة السابقة بعبارة عامة: **طهارة الحيوان في حياته لا تكفي**؛ فكل حيوان يحرم أكله لا يطهر جلده بالدباغ.',
     'Bu, önceki paragrafın kaidesinin genel ifadesidir: **Hayvanın hayattayken temiz olması yetmez**; eti haram olan her hayvanın derisi tabaklanmakla temizlenmez.'),
  PS('والخلاصة: أن كل حيوان مات، وهو من مأكول اللحم، فإنَّ جلده يطهر بالدباغ، وكل حيوان مات، وليس من مأكول اللحم، فإن جلده لا يطهر بالدباغ.',
     'Özet: Eti yenen her hayvan öldüğünde derisi tabaklanmakla temizlenir; eti yenmeyen her hayvan öldüğünde ise derisi tabaklanmakla temizlenmez.',
     '١/ ٨',
     'هذه **العبارة الجامعة** التي يحفظها الطالب من المسألة: **لا يطهر بالدباغ إلا جلد ما يحلّ أكله بالذكاة.**\n\n'
     '**مثال:** شاة ماتت في المزرعة، فدبغ صاحبها جلدها وجعله قِربة: يحفظ فيها الماء ويتوضأ منه، وصوفها طاهر. وقطّ مات فدُبغ جلده: لا يطهر.',
     'Öğrencinin bu meseleden ezberleyeceği **özet ifade** budur: **Tabaklanmakla ancak kesimle eti helâl olan hayvanın derisi temizlenir.**\n\n'
     '**Örnek:** Çiftlikte bir koyun ölse, sahibi derisini tabaklayıp ondan bir kırba yapsa, onda su saklar ve ondan abdest alır; yünü de temizdir. Ölen bir kedinin derisi tabaklansa da temizlenmez.'),
 ]),
]

# ------------------------------------------------------------------ الدرس الثالث: قضاء الحاجة وآدابها (الباب الثالث، ١/ ٩–١٢)
GLOSS.update({
 'idawa': dict(w='إداوة', ar='إناء صغير من جلد.', tr='Deriden küçük bir kap.', src='حاشية الكتاب (١/ ٩)'),
 'rajee': dict(w='رجيع', ar='العَذِرة والروث.', tr='Dışkı ve tezek.', src='حاشية الكتاب (١/ ٩)'),
 'khubth': dict(w='الخبث والخبائث',
   ar='الخُبُث بضم الباء جمع الخبيث، والخبائث جمع الخبيثة؛ يريد ذكور الشياطين وإناثهم.',
   tr='«Hubus» habîsin, «habâis» habîsenin çoğuludur; erkek ve dişi şeytanlar kastedilir.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٦)'),
 'baraz': dict(w='البراز', ar='البَراز بالفتح: اسم للفضاء الواسع، فكنَّوا به عن قضاء الغائط.', tr='Berâz: geniş açık arazi; ihtiyaç gidermek bununla kinaye yoluyla anlatılmıştır.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (١/ ١١٨)'),
 'rakid': dict(w='الراكد', ar='الساكن الذي لا يجري.', tr='Akmayan, durgun (su).', src='حاشية الكتاب (١/ ١١)'),
 'malaain': dict(w='الملاعن', ar='جمع مَلْعَنة، وهي الفَعْلة التي يُلعن بها فاعلها، كأنها مظنّة للّعن.', tr='«Mel’ane»nin çoğulu: yapanın lanetlenmesine sebep olan iş; lanet edilmeye yol açan yer.',
   src='ابن الأثير، «النهاية في غريب الحديث والأثر» (٤/ ٢٥٥)'),
})
GLOSS_TR_SRC.update({
 'حاشية الكتاب (١/ ٩)': 'Kitabın dipnotu (1/ 9)',
 'حاشية الكتاب (١/ ١١)': 'Kitabın dipnotu (1/ 11)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٢/ ٦)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (2/ 6)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (١/ ١١٨)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (1/ 118)',
 'ابن الأثير، «النهاية في غريب الحديث والأثر» (٤/ ٢٥٥)': 'İbnü’l-Esîr, en-Nihâye fî Garîbi’l-Hadîs (4/ 255)',
})

SHARH[103] = [
 dict(ar='المسألة الأولى: الاستنجاء والاستجمار وقيام أحدهما مقام الآخر', tr='Birinci mesele: İstincâ, isticmâr ve birinin diğerinin yerini tutması', paras=[
  PS('الاستنجاء: إزالة الخارج من السبيلين بالماء. والاستجمار: مسحه بطاهر مباح مُنْقِ كالحجر ونحوه.',
     'İstincâ: iki yoldan çıkanı su ile gidermektir. İsticmâr: onu taş gibi temiz, mubah ve temizleyici bir şeyle silmektir.',
     '١/ ٩',
     'لماذا يأتي هذا الباب بعد المياه والآنية؟ لأن أول ما يحتاج المسلم إلى تطهيره قبل الوضوء هو أثر ما يخرج منه. وفي الباب دليل على **شمول الشريعة**: فلم تترك حالًا من أحوال المسلم بلا أدب، حتى قضاء الحاجة. وهذا العلم ينفعك في السفر والرحلات وانقطاع الماء.\n\n'
     'وفرّق الكتاب بين لفظين: **الاستنجاء** يكون **بالماء**، و**الاستجمار** يكون بغير الماء، وأصله من الجِمار، أي الحجارة الصغيرة. **والسبيلان:** مخرج البول ومخرج الغائط.\n\n'
     'وما يُستجمر به له ثلاثة أوصاف: **طاهر**، فلا يكون نجسًا كالروث؛ و**مباح**، فلا يكون مغصوبًا ولا مما له حرمة؛ و**مُنْقٍ**، أي يزيل الأذى، فما لا يُنقي كالشيء الأملس لا يحصل به المقصود.',
     'Bu bölüm neden sulardan ve kaplardan sonra gelir? Çünkü Müslümanın abdestten önce ilk temizlemesi gereken şey, kendisinden çıkanın izidir. Bölüm **şeriatın kapsayıcılığını** gösterir: Müslümanın hiçbir hâlini, ihtiyaç gidermeyi bile edepsiz bırakmamıştır. Bu bilgi yolculukta, gezilerde ve suyun kesildiği durumlarda işinize yarar.\n\n'
     'Kitap iki kelimeyi ayırmıştır: **İstincâ su ile**, **isticmâr ise su dışındaki bir şeyle** olur; aslı «cimâr», yani küçük taşlardır. **İki yol:** idrar ve dışkının çıkış yerleri.\n\n'
     'İsticmârda kullanılan şeyin üç vasfı vardır: **temiz** olması (tezek gibi necis olmaması), **mubah** olması (gasp edilmiş veya saygınlığı olan bir şey olmaması) ve **temizleyici** olması, yani pisliği gidermesi; temizlemeyen kaygan bir şeyle amaç hâsıl olmaz.'),
  PS('ويجزئ أحدهما عن الآخر؛ لثبوت ذلك عن النبي ﷺ: فعن أنس ﵁ قال: (كان النبي ﷺ يدخل الخلاء، فأحمل أنا وغلام نحوي [[إداوة|idawa]] من ماء وعنزة، فيستنجي بالماء) (١). وعن عائشة ﵂، عن النبي ﷺ قال: (إذا ذهب أحدكم إلى الغائط، فليستطب بثلاثة أحجار، فإنها تُجزئ عنه) (٢). والجمع بينهما أفضل.',
     'Her biri diğerinin yerini tutar; çünkü bu, Nebî’den (sallallâhu aleyhi ve sellem) sabittir. Enes (radıyallâhu anh) şöyle demiştir: «Nebî (sallallâhu aleyhi ve sellem) tuvalete girerdi; ben ve benim yaşımda bir genç, içinde su bulunan küçük bir deri kap ve kısa bir mızrak taşırdık; o da su ile istincâ yapardı.» (1) Âişe’den (radıyallâhu anhâ), Nebî (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Biriniz ihtiyacını gidermeye gidince üç taşla temizlensin; bu ona yeter.» (2) İkisini birlikte yapmak daha faziletlidir.',
     '١/ ٩',
     'بعض الناس يظن أن الاستجمار لا يجوز إلا إذا لم يجد الماء، **وليس كذلك**: فكلٌّ منهما يجزئ عن الآخر، ولو مع وجود الماء؛ وهذا من تيسير الشريعة. فمن استجمر بالمناديل ثم توضأ وصلّى، فطهارته وصلاته صحيحتان.\n\n'
     'لكن **الماء أفضل** من الحجارة وحدها، لأنه يزيل عين النجاسة وأثرها، والحجارة تزيل العين وقد يبقى أثر يسير يُعفى عنه. **والجمع بينهما أفضل** من الكل: يبدأ بالحجارة أو المناديل، ثم يُتبعها الماء.\n\n'
     '**شرح الحواشي:** (١) الحديث في صحيح مسلم. و**الإداوة** إناء صغير من جلد يُحمل فيه الماء، و**العَنَزة** عصا قصيرة في طرفها حديدة. (٢) حديث عائشة أخرجه أحمد والدارقطني، وصحّح الدارقطني إسناده.',
     'Bazı insanlar, su bulunmadıkça isticmârın caiz olmadığını sanır; **böyle değildir**: Su bulunsa bile her biri diğerinin yerini tutar; bu, şeriatın kolaylığındandır. Peçeteyle isticmâr yapıp abdest alan ve namaz kılanın taharet ve namazı sahihtir.\n\n'
     'Ancak **su, yalnız taştan daha faziletlidir**; çünkü pisliğin hem kendisini hem izini giderir. Taş ise kendisini giderir, affedilen küçük bir iz kalabilir. **İkisini birlikte yapmak** ise hepsinden faziletlidir: önce taş veya peçeteyle başlanır, sonra su kullanılır.\n\n'
     '**Dipnotların şerhi:** (1) Hadis Müslim’in Sahîh’indedir. **İdâve**, su taşınan deriden küçük kaptır; **aneze**, ucunda demir bulunan kısa bir değnektir. (2) Âişe hadisini Ahmed ve Dârekutnî rivayet etmiş, Dârekutnî isnadını sahih saymıştır.',
     fn=['(١) رواه مسلم برقم (٢٧١)، والإداوة: إناء صغير من جلد.', '(٢) أخرجه أحمد (٦/ ١٠٨)، والدارقطني برقم (١٤٤) وقال: إسناد صحيح.']),
  PS('والاستجمار يحصل بالحجارة أو ما يقوم مقامها من كل طاهر مُنْقِ مباح، كمناديل الورق والخشب ونحو ذلك؛ لأن النبي ﷺ كان يستجمر بالحجارة فيلحق بها ما يماثلها في الإنقاء. ولا يجزئ في الاستجمار أقل من ثلاث مسحات؛ لحديث سلمان ﵁: (نهانا -يعني النبي ﷺ - أن نستنجي باليمين، وأن نستنجي بأقل من ثلاثة أحجار، وأن نستنجي بـ[[رجيع|rajee]] أو عظم) (٣).',
     'İsticmâr taşlarla veya onların yerini tutan temiz, temizleyici ve mubah her şeyle olur: kâğıt peçete, tahta ve benzeri gibi. Çünkü Nebî (sallallâhu aleyhi ve sellem) taşla isticmâr yapardı; temizlemede ona benzeyen şeyler de ona katılır. İsticmârda üç silmeden azı yetmez. Selmân’ın (radıyallâhu anh) hadisi buna delildir: «(Nebî) bizi sağ elle istincâ yapmaktan, üç taştan azıyla istincâ yapmaktan ve tezek ya da kemikle istincâ yapmaktan nehyetti.» (3)',
     '١/ ٩',
     'العلّة في الحجارة **الإنقاء**، فكل ما يُنقي مثلها يقوم مقامها: المناديل، والخشب، ونحوها.\n\n'
     'وأُضيف إلى الشروط السابقة شرط مهم: **ألا يكون له حرمة**. فلا يُستجمر بورق الجرائد والكتب، لأنها قد تحمل آيات أو أحاديث أو أسماء فيها اسم الله، كعبد الله وعبد الرحمن؛ ولا يُستجمر بالطعام.\n\n'
     '**وأقل الاستجمار ثلاث مسحات**، ولو نظف المحلّ بأقل منها. وحديث سلمان جمع ثلاثة أحكام: لا يُستنجى باليمين، ولا بأقل من ثلاثة أحجار، ولا برجيع أو عظم.\n\n'
     '**شرح الحواشي:** (٣) الحديث في صحيح مسلم. و**الرجيع** العَذِرة والروث، سُمّي رجيعًا لأنه رجع عن حاله الأولى.',
     'Taştaki gerekçe **temizlemesidir**; onun gibi temizleyen her şey onun yerini tutar: peçete, tahta ve benzerleri.\n\n'
     'Önceki şartlara önemli bir şart eklenir: **saygınlığı olmaması**. Gazete ve kitap kâğıtlarıyla isticmâr yapılmaz; çünkü içinde âyetler, hadisler veya Abdullah, Abdurrahman gibi Allah’ın adı geçen isimler bulunabilir. Yiyecekle de isticmâr yapılmaz.\n\n'
     '**İsticmârın en azı üç silmedir**; yer daha azıyla temizlense bile. Selmân hadisi üç hükmü toplamıştır: sağ elle, üç taştan azıyla, tezek veya kemikle istincâ yapılmaz.\n\n'
     '**Dipnotların şerhi:** (3) Hadis Müslim’in Sahîh’indedir. **Recî’** dışkı ve tezektir; ilk hâlinden döndüğü için böyle adlandırılmıştır.',
     fn=['(٣) رواه مسلم برقم (٢٦٢)، والرجيع: العَذرَةُ والروْثُ.']),
 ]),
 dict(ar='المسألة الثانية: استقبال القبلة واستدبارها حال قضاء الحاجة', tr='İkinci mesele: İhtiyaç giderirken kıbleye yönelmek ve sırt dönmek', paras=[
  PS('لا يجوز استقبال القبلة ولا استدبارها حال قضاء الحاجة في الصحراء بلا حائل؛ لحديث أبي أيوب الأنصاري ﵁: قال رسول الله ﷺ: (إذا أتيتم الغائط فلا تستقبلوا القبلة، ولا تستدبروها، ولكن شَرِّقوا أو غَرِّبوا) قال أبو أيوب: فقدمنا الشام، فوجدنا مراحيض قد بُنيت نحو الكعبة، فننحرف عنها، ونستغفر الله (٤).',
     'Açık arazide engel olmadan ihtiyaç giderirken kıbleye yönelmek de sırt dönmek de caiz değildir. Ebû Eyyûb el-Ensârî’nin (radıyallâhu anh) hadisi buna delildir: Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «İhtiyacınızı gidermeye vardığınızda kıbleye yönelmeyin, sırtınızı da dönmeyin; doğuya veya batıya dönün.» Ebû Eyyûb dedi ki: «Şam’a geldik, Kâbe’ye doğru yapılmış tuvaletler bulduk; onlardan yönümüzü çevirir ve Allah’tan bağışlanma dilerdik.» (4)',
     '١/ ٩',
     'تأمّل القيود في الحكم، فكل قيد له معنى: **في الصحراء**، و**بلا حائل**. فإذا اجتمعا حرُم الاستقبال والاستدبار.\n\n'
     'و**«شرّقوا أو غرّبوا»** خطاب لأهل المدينة، لأن الكعبة عندهم جهة الجنوب؛ فإذا اتجهوا شرقًا أو غربًا لم يستقبلوها ولم يستدبروها. أما من كانت القبلة عنده في الشرق، فإنه يتجه جنوبًا أو شمالًا.\n\n'
     'وفي فعل أبي أيوب أدب جميل: كان ينحرف عن القبلة ما استطاع، ويستغفر الله.\n\n'
     '**شرح الحواشي:** (٤) الحديث متفق عليه.',
     'Hükümdeki kayıtlara dikkat edin; her kaydın bir anlamı vardır: **açık arazide** ve **engelsiz**. İkisi bir araya gelince kıbleye yönelmek ve sırt dönmek haram olur.\n\n'
     '**«Doğuya veya batıya dönün»** sözü Medine halkına hitaptır; çünkü onlara göre Kâbe güney yönündedir. Doğuya veya batıya döndüklerinde ona ne yönelmiş ne de sırt dönmüş olurlar. Kıblesi doğuda olan kimse ise güneye veya kuzeye döner.\n\n'
     'Ebû Eyyûb’un fiilinde güzel bir edep vardır: Gücü yettiğince kıbleden yönünü çevirir ve Allah’tan bağışlanma dilerdi.\n\n'
     '**Dipnotların şerhi:** (4) Hadis Buhârî ve Müslim’dedir.',
     fn=['(٤) رواه البخاري في كتاب الوضوء برقم (١٤٤)، ومسلم برقم (٢٦٤).']),
  PS('أما إن كان في بنيان، أو كان بينه وبين القبلة شيء يستره، فلا بأس بذلك؛ لحديث ابن عمر ﵄: (أنه رأى رسول الله ﷺ يبول في بيته مستقبل الشام مستدبر الكعبة) (١)، ولحديث مروان الأصغر قال: (أناخ ابن عمر بعيره مستقبل القبلة، ثم جلس يبول إليه، فقلت: أبا عبد الرحمن، أليس قد نُهي عن هذا؟ قال: بلى إنما نهي عن هذا في الفضاء، أما إذا كان بينك وبين القبلة شيء يسترك فلا بأس) (٢). والأفضل ترك ذلك حتى في البنيان، والله أعلم.',
     'Binada olursa veya kıble ile arasında onu örten bir şey bulunursa sakıncası yoktur. İbn Ömer’in (radıyallâhu anhümâ) hadisi buna delildir: «Rasûlullah’ı (sallallâhu aleyhi ve sellem) evinde, yüzü Şam’a, sırtı Kâbe’ye dönük olarak küçük abdestini yaparken gördü.» (1) Mervân’ın hadisi de öyledir: «İbn Ömer devesini kıbleye doğru çöktürdü, sonra ona doğru oturup küçük abdestini yaptı. “Ey Ebû Abdirrahman, bundan nehyedilmedi mi?” dedim. Dedi ki: “Evet; ama bundan yalnızca açık arazide nehyedildi. Seninle kıble arasında seni örten bir şey varsa sakıncası yoktur.”» (2) Binada bile bunu terk etmek daha faziletlidir. Allah en iyisini bilir.',
     '١/ ١٠',
     'هذه الحالة الثانية: **في البنيان، أو خلف حائل**، فلا بأس. والدليل فعل النبي ﷺ في بيته، وفهم ابن عمر رضي الله عنهما للنهي: إنما هو في الفضاء.\n\n'
     '**كيف نجمع بين الحديثين؟** حديث أبي أيوب في الفضاء بلا حائل، وحديث ابن عمر في البنيان؛ فلا تعارض.\n\n'
     'ثم قال الكتاب: **والأفضل ترك ذلك حتى في البنيان**؛ احتياطًا وتعظيمًا للقبلة. فإن شقّ عليه ذلك، كحمّام بُني إلى جهة القبلة، فلا حرج.\n\n'
     '**شرح الحواشي:** (١) حديث ابن عمر متفق عليه. (٢) أثر ابن عمر رواه أبو داود والدارقطني والحاكم، وصحّحه جماعة من الأئمة، وحسّنه ابن حجر والألباني.',
     'Bu ikinci durumdur: **binada veya bir engelin arkasında** sakınca yoktur. Delili, Nebî’nin (sallallâhu aleyhi ve sellem) evindeki fiili ve İbn Ömer’in (radıyallâhu anhümâ) yasağı anlayışıdır: Yasak yalnızca açık araziyle ilgilidir.\n\n'
     '**İki hadisi nasıl bağdaştırırız?** Ebû Eyyûb hadisi engelsiz açık arazi, İbn Ömer hadisi bina hakkındadır; çelişki yoktur.\n\n'
     'Sonra kitap şöyle der: **Binada bile bunu terk etmek daha faziletlidir**; ihtiyat ve kıbleye saygı için. Kıbleye doğru yapılmış bir tuvalet gibi zorluk varsa günah yoktur.\n\n'
     '**Dipnotların şerhi:** (1) İbn Ömer hadisi Buhârî ve Müslim’dedir. (2) İbn Ömer’in bu sözünü Ebû Dâvûd, Dârekutnî ve Hâkim rivayet etmiş; bir grup imam sahih, İbn Hacer ve Elbânî hasen saymıştır.',
     fn=['(١) رواه البخاري برقم (١٤٨)، ومسلم برقم (٢٦٦).', '(٢) رواه أبو داود برقم (١١)، والدارقطني برقم (١٥٨)، والحاكم (١/ ١٥٤). وصححه الدارقطني، والحاكم ووافقه الذهبي، وحَسنه الحافظ ابن حجر، والحازمي، والألباني (انظر: الإرواء برقم ٦١).'],
     note=dict(ar='تنبيه: الراوي في المصادر «مروان الأصفر»، بالفاء.', tr='Not: Kaynaklarda râvinin adı «Mervân el-Asfar»dır.')),
 ]),
 dict(ar='المسألة الثالثة: ما يسن فعله لداخل الخلاء', tr='Üçüncü mesele: Tuvalete giren kimse için sünnet olanlar', paras=[
  PS('يسن لداخل الخلاء قول: "بسم الله اللهم إني أعوذ بك من [[الخبث والخبائث|khubth]]". وعند الانتهاء والخروج: "غفرانك". وتقديم رجله اليسرى عند الدخول واليمنى عند الخروج، وأن لا يكشف عورته حتى يدنو من الأرض. وإذا كان في الفضاء يستحب له الإبعاد والاستتار حتى لا يُرى.',
     'Tuvalete giren kimsenin şöyle demesi sünnettir: «Allah’ın adıyla. Allah’ım! Erkek ve dişi şeytanlardan sana sığınırım.» İşini bitirip çıkarken: «Bağışlamanı dilerim.» Girerken sol ayağını, çıkarken sağ ayağını öne alması ve yere yaklaşmadan avret yerini açmaması da sünnettir. Açık arazide ise görünmeyecek şekilde uzaklaşması ve örtünmesi müstehaptır.',
     '١/ ١٠',
     'هذه **خمس سنن** يحفظها الطالب: البسملة والاستعاذة عند الدخول، و«غفرانك» عند الخروج، واليسرى دخولًا واليمنى خروجًا، وألا يكشف عورته حتى يدنو من الأرض، والإبعاد والاستتار في الفضاء.\n\n'
     '**لاحظ الترتيب:** هنا يبدأ بالبسملة ثم الاستعاذة، بخلاف القراءة التي يبدأ فيها بالاستعاذة ثم البسملة.\n\n'
     '**ولماذا اليسرى عند الدخول؟** لأن اليمنى تُقدَّم لما هو شريف كالمسجد، واليسرى لما سواه.',
     'Öğrencinin ezberleyeceği **beş sünnet** budur: girerken besmele ve istiâze, çıkarken «gufrâneke», girerken sol ve çıkarken sağ ayak, yere yaklaşmadan avret yerini açmamak, açık arazide uzaklaşmak ve örtünmek.\n\n'
     '**Sıraya dikkat edin:** Burada önce besmele, sonra istiâze gelir; Kur’ân okurken ise önce istiâze, sonra besmele gelir.\n\n'
     '**Girerken neden sol ayak?** Çünkü mescit gibi şerefli yerlere sağ, diğerlerine sol ayakla girilir.'),
  PS('وأدلة ذلك كله: حديث جابر ﵁ قال: (خرجنا مع رسول الله ﷺ في سفر وكان رسول الله ﷺ لا يأتي [[البراز|baraz]] حتى يتغيب فلا يُرى) (٣). وحديث علي ﵁ قال: قال رسول الله ﷺ: (ستر ما بين الجن وعورات بني آدم إذا دخل الخلاء، أن يقول: بسم الله) (٤). وحديث أنس ﵁: كان النبي ﷺ إذا دخل الخلاء قال: (اللهم إني أعوذ بك من الخبث والخبائث) (٥).',
     'Bunların hepsinin delilleri şunlardır: Câbir’in (radıyallâhu anh) hadisi: «Rasûlullah (sallallâhu aleyhi ve sellem) ile bir yolculuğa çıktık; Rasûlullah ihtiyacını gidermeye, gözden kaybolup görünmeyecek bir yere gitmeden gitmezdi.» (3) Ali’nin (radıyallâhu anh) hadisi: Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Âdemoğlu tuvalete girdiğinde cinlerle onun avret yerleri arasındaki perde, “Bismillah” demesidir.» (4) Enes’in (radıyallâhu anh) hadisi: Nebî (sallallâhu aleyhi ve sellem) tuvalete girince «Allah’ım! Erkek ve dişi şeytanlardan sana sığınırım» derdi. (5)',
     '١/ ١٠',
     'في حديث علي أن **البسملة ستر** يحجب عورات بني آدم عن أعين الجن؛ وفي حديث أنس أن الخلاء موضع الشياطين، فيستعيذ المسلم بالله منهم. وفي حديث جابر **الحياء والستر**: كان ﷺ يبتعد حتى لا يُرى.\n\n'
     '**شرح الحواشي:** (٣) حديث جابر رواه أبو داود وابن ماجه بإسناد صحيح. (٤) حديث علي رواه الترمذي وابن ماجه، وصحّحه الألباني. (٥) حديث أنس متفق عليه.',
     'Ali hadisinde **besmelenin bir perde olduğu** bildirilir: Âdemoğlunun avret yerlerini cinlerin gözlerinden örter. Enes hadisinde tuvaletin şeytanların bulunduğu yer olduğu, Müslümanın onlardan Allah’a sığındığı anlaşılır. Câbir hadisinde **hayâ ve örtünme** vardır: Nebî (sallallâhu aleyhi ve sellem) görünmemek için uzaklaşırdı.\n\n'
     '**Dipnotların şerhi:** (3) Câbir hadisini Ebû Dâvûd ve İbn Mâce sahih isnadla rivayet etmiştir. (4) Ali hadisini Tirmizî ve İbn Mâce rivayet etmiş, Elbânî sahih saymıştır. (5) Enes hadisi Buhârî ve Müslim’dedir.',
     fn=['(٣) رواه أبو داود برقم (٢)، وابن ماجه برقم (٣٣٥)، واللفظ له، وإسناده صحيح. انظر صحيح ابن ماجه (١/ ٦٠).', '(٤) رواه ابن ماجه برقم (٢٩٧)، والترمذي برقم (٦٠٦) وحسنه أحمد شاكر في حاشية الترمذي، وصححه الألباني. صحيح الجامع الصغير برقم (٣٦١١).', '(٥) رواه البخاري برقم (١٤٢)، ومسلم برقم (٣٧٥).']),
  PS('وحديث عائشة ﵂: (كان ﷺ إذا خرج من الخلاء قال: غفرانك) (١). وحديث ابن عمر ﵄: (أن النبي ﷺ كان إذا أراد الحاجة لا يرفع ثوبه حتى يدنو من الأرض) (٢).',
     'Âişe’nin (radıyallâhu anhâ) hadisi: «Nebî (sallallâhu aleyhi ve sellem) tuvaletten çıkınca “Bağışlamanı dilerim” derdi.» (1) İbn Ömer’in (radıyallâhu anhümâ) hadisi: «Nebî (sallallâhu aleyhi ve sellem) ihtiyacını gidermek istediğinde yere yaklaşmadan elbisesini kaldırmazdı.» (2)',
     '١/ ١١',
     '**«غفرانك»** أي: أسألك غفرانك. وفيه أن المسلم يذكر ربه ويستغفره عند خروجه. وفي إخراج الأذى من البدن **نعمة عظيمة**، من حُرمها عرف قدرها.\n\n'
     'وفي حديث ابن عمر **أدب الستر**: لا يرفع ثوبه إلا عند الحاجة، حين يقرب من الأرض.\n\n'
     '**شرح الحواشي:** (١) حديث عائشة رواه أبو داود والترمذي، وحسّنه الألباني. (٢) حديث ابن عمر رواه أبو داود والترمذي، وصحّحه الألباني.',
     '**«Gufrâneke»**, «bağışlamanı dilerim» demektir. Müslüman tuvaletten çıkarken Rabbini anar ve O’ndan bağışlanma diler. Eziyet veren şeyin bedenden çıkması **büyük bir nimettir**; ondan mahrum kalan onun değerini bilir.\n\n'
     'İbn Ömer hadisinde **örtünme edebi** vardır: Elbisesini ancak ihtiyaç anında, yere yaklaşınca kaldırır.\n\n'
     '**Dipnotların şerhi:** (1) Âişe hadisini Ebû Dâvûd ve Tirmizî rivayet etmiş, Elbânî hasen saymıştır. (2) İbn Ömer hadisini Ebû Dâvûd ve Tirmizî rivayet etmiş, Elbânî sahih saymıştır.',
     fn=['(١) رواه أبو داود برقم (١٧)، والترمذي برقم (٧)، وقال: حسن غريب. وحسنه الألباني (صحيح الجامع الصغير ٤٧٠٧).', '(٢) رواه أبو داود برقم (١٤)، والترمذي برقم (١٤) وصححه الألباني، انظر صحيح الجامع الصغير برقم (٤٦٥٢).'],
     note=dict(ar='تنبيه على الحاشية (١): حديث «غفرانك» في «سنن أبي داود» برقم (٣٠)؛ أما (١٧) فرقم الباب في بعض الطبعات.', tr='(1) numaralı dipnot hakkında: «Gufrâneke» hadisi Ebû Dâvûd’un Sünen’inde 30 numaradadır; 17, bazı baskılarda babın numarasıdır.')),
 ]),
 dict(ar='المسألة الرابعة: ما يحرم فعله على من أراد قضاء الحاجة', tr='Dördüncü mesele: İhtiyacını gidermek isteyene haram olanlar', paras=[
  PS('يحرم البول في الماء [[الراكد|rakid]]؛ لحديث جابر عن النبي ﷺ: (أنه نهى عن البول في الماء الراكد) (٣). ولا يمسك ذكره بيمينه وهو يبول، ولا يستنجي بها. لقوله ﷺ: (إذا بال أحدكم فلا يأخذن ذكره بيمينه، ولا يستنجي بيمينه) (٤).',
     'Durgun suya küçük abdest yapmak haramdır. Câbir’in Nebî’den (sallallâhu aleyhi ve sellem) rivayeti buna delildir: «Durgun suya küçük abdest yapmayı nehyetti.» (3) Küçük abdest yaparken tenasül organını sağ eliyle tutmaz ve sağ eliyle istincâ yapmaz. Çünkü Nebî (sallallâhu aleyhi ve sellem) şöyle buyurmuştur: «Biriniz küçük abdest yaptığında tenasül organını sağ eliyle tutmasın, sağ eliyle istincâ da yapmasın.» (4)',
     '١/ ١١',
     '**الماء الراكد** هو الذي لا يجري، كالبركة؛ والبول فيه يُفسده على من يحتاج إليه. وفي هذا حفظ لموارد الناس، وهو ما يسمّيه الناس اليوم «حماية البيئة»، وقد سبقت إليه الشريعة.\n\n'
     '**واليمين** في الإسلام مكرَّمة، تُستعمل فيما يشرف: الأكل، والمصافحة، والأخذ والعطاء؛ فلا تُستعمل في إزالة الأذى.\n\n'
     '**شرح الحواشي:** (٣) حديث جابر في صحيح مسلم، وعند البخاري نحوه من حديث أبي هريرة. (٤) الحديث متفق عليه.',
     '**Durgun su**, havuz gibi akmayan sudur; ona küçük abdest yapmak, ona ihtiyacı olanlar için onu bozar. Bunda insanların su kaynaklarını korumak vardır; bugün insanların «çevreyi korumak» dediği şey budur ve şeriat buna önceden dikkat çekmiştir.\n\n'
     '**Sağ el** İslam’da saygındır; yemek, tokalaşmak, alıp vermek gibi şerefli işlerde kullanılır; pislik gidermede kullanılmaz.\n\n'
     '**Dipnotların şerhi:** (3) Câbir hadisi Müslim’in Sahîh’indedir; Buhârî’de de Ebû Hureyre’den benzeri vardır. (4) Hadis Buhârî ve Müslim’dedir.',
     fn=['(٣) رواه مسلم برقم (٢٨١)، ونحوه عند البخاري برقم (٢٣٩). والراكد: هو الساكن الذي لا يجري.', '(٤) رواه البخاري برقم (١٥٤) واللفظ له، ومسلم برقم (٢٦٧).']),
  PS('ويحرم عليه البول أو الغائط في الطريق أو في الظل أو في الحدائق العامة أو تحت شجرة مثمرة أو موارد المياه؛ لما روى معاذ قال: قال رسول الله ﷺ: (اتقوا [[الملاعن|malaain]] الثلاث: البراز في الموارد، وقارعة الطريق، والظل) (٥)، ولحديث أبي هريرة ﵁ أن النبي ﷺ قال: (اتقوا اللاعنين)، قالوا: وما اللاعنان يا رسول الله؟ قال: (الذي يَتَخَلى في طريق الناس أو في ظلهم) (٦).',
     'Yolda, gölgede, umumi parklarda, meyve veren ağacın altında veya su kaynaklarında küçük ya da büyük abdest yapmak ona haramdır. Muâz’ın rivayeti buna delildir: Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Lanete sebep olan üç şeyden sakının: su kaynaklarına, yolun ortasına ve gölgeye ihtiyaç gidermek.» (5) Ebû Hureyre’nin (radıyallâhu anh) hadisi de öyledir: Nebî (sallallâhu aleyhi ve sellem) «Lanete sebep olan iki şeyden sakının» buyurdu. «Ey Allah’ın Rasûlü, onlar nedir?» dediler. «İnsanların yoluna veya gölgesine ihtiyacını gideren kimse» buyurdu. (6)',
     '١/ ١١',
     '**لماذا سُمّيت «ملاعن»؟** لأن من وجد الأذى في طريقه، أو في الظل الذي يستريح فيه، أو عند الماء الذي يشرب منه، لعن فاعله غالبًا؛ فهي أسباب لِلَّعن. فالنبي ﷺ يحمي أمته من أن تُلعن، ويحذّرها من إيذاء الناس.\n\n'
     'وكل مكان يرتفق به الناس داخل في هذا: **الطريق** لأنه ممرّهم، و**الظل** لأنهم يستريحون فيه، و**الحدائق العامة**، و**الشجرة المثمرة** لأن ثمرها قد يسقط فيتنجس، و**موارد المياه**.\n\n'
     'وفي هذا أدب عام: أن يتّقي المسلم كل ما قد يجلب عليه دعاء الناس عليه.\n\n'
     '**شرح الحواشي:** (٥) حديث معاذ رواه أبو داود وابن ماجه، وإسناده حسن. (٦) حديث أبي هريرة في صحيح مسلم.',
     '**Bunlara neden «lanete sebep olanlar» denildi?** Çünkü yolunda, dinlendiği gölgede veya içtiği suyun başında pislik bulan kimse çoğu zaman bunu yapana lanet eder; bunlar lanetin sebepleridir. Nebî (sallallâhu aleyhi ve sellem) ümmetini lanetlenmekten korur ve insanlara eziyet etmekten sakındırır.\n\n'
     'İnsanların yararlandığı her yer buna girer: **yol** (geçtikleri yer), **gölge** (dinlendikleri yer), **umumi parklar**, **meyve veren ağaç** (meyvesi düşüp necis olabilir) ve **su kaynakları**.\n\n'
     'Burada genel bir edep vardır: Müslüman, insanların aleyhine dua etmesine yol açabilecek her şeyden sakınır.\n\n'
     '**Dipnotların şerhi:** (5) Muâz hadisini Ebû Dâvûd ve İbn Mâce rivayet etmiştir; isnadı hasendir. (6) Ebû Hureyre hadisi Müslim’in Sahîh’indedir.',
     fn=['(٥) رواه أبو داود برقم (٢٦)، وابن ماجه برقم (٣٢٨). وإسناده حسن انظر إرواء الغليل (١/ ١٠٠).', '(٦) رواه مسلم برقم (٢٦٩).']),
  PS('كما يحرم عليه قراءة القرآن، ويحرم عليه الاستجمار بالروث أو العظم أو بالطعام المحترم؛ لحديث جابر ﵁: (نهى النبي ﷺ أن يتمسح بعظم أو ببعر) (٧). ويحرم قضاء الحاجة بين قبور المسلمين، قال النبي ﷺ: (لا أبالي أوسط القبور قضيت حاجتي، أو وسط السوق؟) (٨).',
     'Ayrıca ona Kur’ân okumak haramdır; tezek, kemik veya saygın bir yiyecekle isticmâr yapmak da haramdır. Câbir’in (radıyallâhu anh) hadisi buna delildir: «Nebî (sallallâhu aleyhi ve sellem) kemikle veya tezekle silinmeyi nehyetti.» (7) Müslümanların kabirleri arasında ihtiyaç gidermek de haramdır. Nebî (sallallâhu aleyhi ve sellem) şöyle buyurmuştur: «Kabirlerin ortasında mı ihtiyacımı gidermişim, çarşının ortasında mı, umursamam.» (8)',
     '١/ ١١',
     '**قراءة القرآن** حال قضاء الحاجة تحرم، تعظيمًا لكلام الله.\n\n'
     '**والعظم والروث** لا يُستجمر بهما؛ فالروث نجس لا يُطهِّر، والعظم لا يُنقي، وقد جاء في الحديث أنهما طعام الجن ودوابّهم. **والطعام المحترم** أولى بالمنع.\n\n'
     'وفي حديث القبور تقبيح شديد: قضاء الحاجة بين القبور مثل قضائها وسط السوق أمام الناس، فكلاهما قبيح. **وللموتى حرمة** كحرمة الأحياء.\n\n'
     '**شرح الحواشي:** (٧) حديث جابر في صحيح مسلم. (٨) حديث القبور رواه ابن ماجه، وصحّحه الألباني.',
     '**Kur’ân okumak** ihtiyaç giderirken haramdır; Allah’ın kelâmına saygı içindir.\n\n'
     '**Kemik ve tezekle** isticmâr yapılmaz: Tezek necistir, temizlemez; kemik temizlemez; hadiste bunların cinlerin ve hayvanlarının yiyeceği olduğu gelmiştir. **Saygın yiyecek** ise yasağa öncelikle girer.\n\n'
     'Kabir hadisinde ağır bir kınama vardır: Kabirlerin arasında ihtiyaç gidermek, çarşının ortasında insanların önünde gidermek gibidir; ikisi de çirkindir. **Ölülerin de dirilerin saygınlığı gibi bir saygınlığı vardır.**\n\n'
     '**Dipnotların şerhi:** (7) Câbir hadisi Müslim’in Sahîh’indedir. (8) Kabir hadisini İbn Mâce rivayet etmiş, Elbânî sahih saymıştır.',
     fn=['(٧) رواه مسلم برقم (٢٦٣).', '(٨) رواه ابن ماجه برقم (١٥٦٧) وصححه الألباني في إرواء الغليل (١/ ١٠٢).']),
 ]),
 dict(ar='المسألة الخامسة: ما يكره فعله للمُتَخَلِّي', tr='Beşinci mesele: Tuvaletteki kimse için mekruh olanlar', paras=[
  PS('يكره حال قضاء الحاجة استقبال مهب الريح بلا حائل؛ لئلا يرتد البول إليه، ويكره الكلام؛ فقد مرّ رجل والنبي ﷺ يبول، فسلَّم عليه، فلم يردّ عليه (١).',
     'İhtiyaç giderirken engel olmadan rüzgârın estiği yöne dönmek mekruhtur; idrar üzerine geri sıçramasın diye. Konuşmak da mekruhtur. Nebî (sallallâhu aleyhi ve sellem) küçük abdestini yaparken bir adam geçip selam verdi; selamını almadı. (1)',
     '١/ ١٢',
     'انتقل الكتاب من المحرّم إلى **المكروه**: وهو ما يُثاب تاركه ولا يأثم فاعله.\n\n'
     '**استقبال الريح:** علّته ظاهرة في الكتاب: لئلا يرتدّ رشاش البول إليه فيتنجّس.\n\n'
     '**الكلام:** النبي ﷺ لم يردّ السلام وهو على حاجته، مع أن ردّ السلام واجب؛ فدلّ على أن الكلام في هذه الحال لا ينبغي.\n\n'
     '**شرح الحواشي:** (١) الحديث في صحيح مسلم من حديث ابن عمر رضي الله عنهما.',
     'Kitap haramdan **mekruha** geçmiştir: Mekruh, terk edene sevap verilen, yapan günaha girmeyen şeydir.\n\n'
     '**Rüzgâra dönmek:** Gerekçesi kitapta açıktır: İdrar sıçrayıp üzerine gelmesin ve onu necis kılmasın.\n\n'
     '**Konuşmak:** Selama karşılık vermek vacip olduğu hâlde Nebî (sallallâhu aleyhi ve sellem) ihtiyacını giderirken selamı almamıştır; bu, o hâlde konuşmanın uygun olmadığını gösterir.\n\n'
     '**Dipnotların şerhi:** (1) Hadis, İbn Ömer’in (radıyallâhu anhümâ) rivayetiyle Müslim’in Sahîh’indedir.',
     fn=['(١) رواه مسلم برقم (٣٧٠).']),
  PS('ويكره أن يبول في شَق ونحوه؛ لحديث قتادة عن عبد الله بن سرجس: (أن النبي ﷺ نهى أن يبال في الجُحْر، قيل لقتادة: فما بال الجحر؟ قال: يقال: إنها مساكن الجن) (٢). ولأنه لا يأمن أن يكون فيه حيوان فيؤذيه، أو يكون مسكناً للجن فيؤذيهم.',
     'Yarık ve benzeri bir yere küçük abdest yapmak mekruhtur. Katâde’nin Abdullah b. Sercis’ten rivayet ettiği hadis buna delildir: «Nebî (sallallâhu aleyhi ve sellem) deliğe küçük abdest yapılmasını nehyetti.» Katâde’ye: «Deliğin nesi var?» denildi. «Onların cinlerin barınakları olduğu söylenir» dedi. (2) Ayrıca içinde kendisine eziyet verecek bir hayvan bulunmasından ya da cinlerin barınağı olup onlara eziyet vermekten emin olamaz.',
     '١/ ١٢',
     'علّتان في النهي: **أن يؤذيه** ما في الجحر من حيّة أو عقرب أو غيرهما، **أو يؤذي** من يسكنه من الجن. فالشريعة تمنع الأذى من الجهتين.\n\n'
     '**شرح الحواشي:** (٢) الحديث رواه أبو داود والنسائي، ونقل ابن حجر تصحيحه عن ابن خزيمة وابن السكن.',
     'Yasakta iki gerekçe vardır: Delikteki yılan, akrep veya başka bir hayvanın **ona eziyet vermesi** ya da orada yaşayan cinlere **eziyet vermesi**. Şeriat eziyeti iki taraftan da önler.\n\n'
     '**Dipnotların şerhi:** (2) Hadisi Ebû Dâvûd ve Nesâî rivayet etmiş; İbn Hacer, İbn Huzeyme ve İbnü’s-Seken’in sahih saydığını nakletmiştir.',
     fn=['(٢) رواه أبو داود برقم (٢٩)، والنسائي برقم (٣٤). ونقل الحافظ ابن حجر في التلخيص (١/ ١٠٦) تصحيحه عن ابن خزيمة وابن السكن. وقال الشيخ ابن عثيمين: أقل أحواله أن يكون حسناً (الشرح الممتع ١/ ٩٥ - ٩٦).']),
  PS('ويكره أن يدخل الخلاء بشيء فيه ذكْرُ الله إلا لحاجة؛ لأن النبي ﷺ (كان إذا دخل الخلاء وضع خاتمه) (٣). أما عند الحاجة والضرورة فلا بأس، كالحاجة إلى الدخول بالأوراق النقدية التي فيها اسم الله؛ فإنه إن تركها خارجاً كانت عرضة للسرقة أو النسيان.',
     'İçinde Allah’ın zikri bulunan bir şeyle tuvalete girmek, ihtiyaç olmadıkça mekruhtur. Çünkü Nebî (sallallâhu aleyhi ve sellem) «tuvalete girince yüzüğünü çıkarırdı.» (3) İhtiyaç ve zaruret hâlinde ise sakıncası yoktur; üzerinde Allah’ın adı bulunan kâğıt paralarla girme ihtiyacı gibi; çünkü onları dışarıda bıraksa çalınabilir veya unutulabilir.',
     '١/ ١٢',
     'كان خاتم النبي ﷺ منقوشًا عليه «محمد رسول الله»، فكان يضعه عند دخول الخلاء. ومثله اليوم: **قلادة أو حُليّ فيه لفظ الجلالة**، يُنزع قبل الدخول إن أمكن.\n\n'
     '**والحاجة تُبيح ذلك:** كالنقود التي فيها اسم الله، يخاف عليها السرقة أو النسيان.\n\n'
     '**شرح الحواشي:** (٣) الحديث رواه أصحاب السنن، وضعّفه أبو داود والألباني. ومع ضعفه فالأولى ألا يدخل الخلاء بما فيه اسم الله بلا حاجة، **إكرامًا لاسمه تعالى**، كما قالت الحاشية.',
     'Nebî’nin (sallallâhu aleyhi ve sellem) yüzüğünde «Muhammed Rasûlullah» yazılıydı; tuvalete girerken onu çıkarırdı. Bugün bunun benzeri, **üzerinde Allah lafzı bulunan bir kolye veya takıdır**; mümkünse girmeden önce çıkarılır.\n\n'
     '**İhtiyaç bunu mubah kılar:** Çalınmasından veya unutulmasından korkulan, üzerinde Allah’ın adı bulunan paralar gibi.\n\n'
     '**Dipnotların şerhi:** (3) Hadisi Sünen sahipleri rivayet etmiş; Ebû Dâvûd ve Elbânî zayıf saymıştır. Zayıf olsa da, dipnotta denildiği gibi, **Allah’ın adına saygı için** ihtiyaç olmadan içinde Allah’ın adı bulunan bir şeyle tuvalete girmemek daha uygundur.',
     fn=['(٣) رواه أبو داود برقم (١٩)، والترمذي برقم (١٧٤٦)، والنسائي برقم (٥٢٢٨)، وابن ماجه برقم (٣٠٣)، وقال أبو داود بعد إخراجه: هذا حديث منكر. وقال الترمذي: هذا حديث حسن غريب. وضعفه الألباني؛ وعلى القول بضعف هذا الحديث وعدم صلاحيته للاحتجاج في هذه المسألة، فإن الأولى والأفضل ألا يدخل الخلاء بشيء فيه اسم الله بلا ضرورة؛ إكراماً لاسمه تعالى وإجلالاً.']),
  PS('أما المصحف فإنه يحرم الدخول به سواء كان ظاهراً أو خفياً؛ لأنه كلام الله وهو أشرف الكلام، ودخول الخلاء به فيه نوع من الإهانة.',
     'Mushafla girmek ise, açıkta olsun gizli olsun, haramdır; çünkü o, sözlerin en şereflisi olan Allah’ın kelâmıdır ve onunla tuvalete girmekte bir tür saygısızlık vardır.',
     '١/ ١٢',
     'فرّق الكتاب بين أمرين: **ما فيه ذكر الله** يُكره الدخول به إلا لحاجة، و**المصحف** يحرم الدخول به مطلقًا، ولو كان في جيبه أو حقيبته. والفرق أن المصحف كلام الله، أشرف الكلام، فحرمته أعظم.\n\n'
     '**القاعدة في الباب كله:** الشريعة حفظت الطهارة، والستر، وتعظيم شعائر الله، ودفع الأذى عن الناس.',
     'Kitap iki şeyi ayırmıştır: **İçinde Allah’ın zikri bulunan şeyle** ihtiyaç olmadıkça girmek mekruhtur; **Mushafla** girmek ise cebinde veya çantasında olsa bile mutlak olarak haramdır. Fark şudur: Mushaf, sözlerin en şereflisi olan Allah’ın kelâmıdır; saygınlığı daha büyüktür.\n\n'
     '**Bölümün tamamındaki kaide:** Şeriat temizliği, örtünmeyi, Allah’ın şiarlarına saygıyı ve insanlardan eziyeti uzaklaştırmayı korumuştur.'),
 ]),
]

# ------------------------------------------------------------------ الدرس الرابع: السواك وسنن الفطرة (الباب الرابع، ١/ ١٣–١٦)
GLOSS.update({
 'shaws': dict(w='يَشُوص', ar='الشوص: الدلك.', tr='Şavs: ovmak.', src='حاشية الكتاب (١/ ١٣)'),
 'arak': dict(w='أراك', ar='الأرَاك: شجر من الحمض يستاك بقضبانه، واسمه الكَبَاث.', tr='Erâk: dallarıyla misvak yapılan, hamd türünden bir ağaç.', src='حاشية الكتاب (١/ ١٤)'),
 'istihdad': dict(w='الاستحداد', ar='حلق العانة، وهي الشعر النابت حول الفرج؛ سمّي بذلك لاستعمال الحديدة فيه وهي الموسى.', tr='Kasık kıllarını tıraş etmek; ustura (demir) kullanıldığı için bu adı almıştır.', src='الكتاب نفسه (١/ ١٤–١٥)'),
 'hashafa': dict(w='الحَشَفَة', ar='الحشفة: هي رأس الذكر.', tr='Erkek tenasül organının baş kısmı.', src='حاشية الكتاب (١/ ١٥)'),
 'qulfa': dict(w='القُلْفَة', ar='الجلدة التي تغطي الحشفة، والتي تقطع في الختان.', tr='Sünnette kesilen, organın başını örten deri.', src='حاشية الكتاب (١/ ١٥)'),
 'jazz': dict(w='جزّوا', ar='الجز: القص. وإرخاء اللحية: تركها وعدم التعرض لها.', tr='Cezz: kısaltmak. Sakalı salıvermek: onu bırakıp dokunmamak.', src='حاشية الكتاب (١/ ١٥)'),
 'barajim': dict(w='البراجم', ar='العقد التي في ظهور الأصابع، يجتمع فيها الوسخ.', tr='Parmakların üst yüzündeki, kirin biriktiği eklem yerleri.', src='الكتاب نفسه (١/ ١٦)'),
})
GLOSS_TR_SRC.update({
 'حاشية الكتاب (١/ ١٣)': 'Kitabın dipnotu (1/ 13)',
 'حاشية الكتاب (١/ ١٤)': 'Kitabın dipnotu (1/ 14)',
 'حاشية الكتاب (١/ ١٥)': 'Kitabın dipnotu (1/ 15)',
 'الكتاب نفسه (١/ ١٤–١٥)': 'Kitabın kendisi (1/ 14–15)',
 'الكتاب نفسه (١/ ١٦)': 'Kitabın kendisi (1/ 16)',
})

SHARH[104] = [
 dict(ar='الباب الرابع: في السواك وسنن الفطرة', tr='Dördüncü bölüm: Misvak ve fıtrat sünnetleri', paras=[
  PS('السواك: هو استعمال عود أو نحوه في الأسنان أو اللثة؛ لإزالة ما يعلق بهما من الأطعمة والروائح.',
     'Misvak: Yemek artıklarını ve kokuları gidermek için dişlerde veya diş etlerinde bir çubuk ya da benzerini kullanmaktır.',
     '١/ ١٣',
     'بدأ الكتاب بتعريف السواك، وفيه ثلاثة أشياء: **الآلة** (عود أو نحوه)، و**المحلّ** (الأسنان واللثة)، و**المقصود** (إزالة ما يعلق بهما من الطعام والرائحة).\n\n'
     'فالسواك يُطلق على الفعل، ويُطلق على العود الذي يُستاك به.',
     'Kitap misvakın tanımıyla başlar; tanımda üç şey vardır: **araç** (çubuk vb.), **yer** (dişler ve diş etleri) ve **amaç** (yemek artığını ve kokuyu gidermek).\n\n'
     'Misvak kelimesi hem fiil için hem de onunla yapılan çubuk için kullanılır.'),
 ]),
 dict(ar='المسألة الأولى: حكمه', tr='Birinci mesele: Hükmü', paras=[
  PS('السواك مسنون في جميع الأوقات، حتى الصائم لو تَسَوَّك في حال صيامه فلا بأس بذلك سواء كان أول النهار أو آخره؛ لأن النبي ﷺ رغَّب فيه ترغيباً مطلقاً، ولم يقيده بوقت دون آخر، حيث قال ﷺ: (السواك مطهرة للفم مرضاة للرب) (١). وقال ﷺ: (لولا أن أشق على أمتي لأمرتهم بالسواك عند كل صلاة) (٢).',
     'Misvak her vakitte sünnettir. Oruçlu kimse orucu sırasında misvak kullansa, günün başında olsun sonunda olsun, sakıncası yoktur. Çünkü Nebî (sallallâhu aleyhi ve sellem) onu bir vakitle sınırlamadan genel olarak teşvik etmiş ve şöyle buyurmuştur: «Misvak ağzı temizler, Rabbi razı eder.» (1) Yine buyurmuştur: «Ümmetime zorluk vermeyecek olsaydım, onlara her namazda misvak kullanmalarını emrederdim.» (2)',
     '١/ ١٣',
     '**الحكم:** سنة في كل وقت. **والدليل على العموم:** أن النبي ﷺ رغّب فيه ترغيبًا مطلقًا، ولم يخصّه بوقت؛ فيدخل فيه الصائم في أول النهار وآخره.\n\n'
     '**وفي الحديث الثاني قاعدة أصولية:** أن **الأمر يقتضي الوجوب**. فالنبي ﷺ ترك أن يأمر بالسواك عند كل صلاة **خوف المشقة**؛ لأنه لو أمر به لصار واجبًا. فدلّ على أنه سنة مؤكدة لا واجب، وعلى رحمته ﷺ بأمته.\n\n'
     '**شرح الحواشي:** (١) حديث «السواك مطهرة» ذكره البخاري بلا إسناد بصيغة الجزم، ووصله أحمد والنسائي، وصحّحه الألباني. (٢) حديث «لولا أن أشق» متفق عليه من حديث أبي هريرة رضي الله عنه.',
     '**Hüküm:** Her vakitte sünnettir. **Genellik delili:** Nebî (sallallâhu aleyhi ve sellem) onu bir vakte tahsis etmeden genel olarak teşvik etmiştir; günün başında ve sonunda oruçlu da buna girer.\n\n'
     '**İkinci hadiste usûle dair bir kaide vardır:** **Emir vacipliği gerektirir.** Nebî (sallallâhu aleyhi ve sellem) her namazda misvakı emretmeyi **zorluk korkusuyla** terk etmiştir; çünkü emretseydi vacip olurdu. Bu, misvakın vacip değil, müekked bir sünnet olduğunu ve onun ümmetine olan rahmetini gösterir.\n\n'
     '**Dipnotların şerhi:** (1) «Misvak ağzı temizler» hadisini Buhârî kesinlik bildiren bir ifadeyle senetsiz zikretmiş; Ahmed ve Nesâî senedli rivayet etmiş, Elbânî sahih saymıştır. (2) «Zorluk vermeyecek olsaydım» hadisi Ebû Hureyre’den (radıyallâhu anh) Buhârî ve Müslim’dedir.',
     fn=['(١) أخرجه البخاري في كتاب الصوم ٢/ ٤٠ معلقاً بصيغة الجزم، ورواه أحمد (٦/ ٤٧)، والنسائي (١/ ١٠). وصححه الألباني في الإرواء (١/ ١٠٥).', '(٢) متفق عليه: البخاري برقم (٨٨٧)، ومسلم في كتاب الطهارة برقم (٢٥٢).']),
 ]),
 dict(ar='المسألة الثانية: متى يتأكد؟', tr='İkinci mesele: Ne zaman daha da önem kazanır?', paras=[
  PS('ويتأكد عند الوضوء، وعند الانتباه من النوم، وعند تغير رائحة الفم، وعند قراءة القرآن، وعند الصلاة. وكذا عند دخول المسجد والمنزل؛ لحديث القدام بن شريح، عن أبيه قال: سألت عائشة، قلت: بأيِّ شيء كان يبدأ النبي ﷺ إذا دخل بيته؟ قالت: بالسواك (٣). ويتأكد كذلك عند طول السكوت، وصفرة الأسنان، للأحاديث السابقة.',
     'Misvak abdestte, uykudan uyanınca, ağız kokusu değişince, Kur’ân okurken ve namazda daha da önem kazanır. Mescide ve eve girerken de öyledir. Mikdâm b. Şureyh’in babasından rivayeti buna delildir: «Âişe’ye sordum: Nebî (sallallâhu aleyhi ve sellem) evine girince ilk ne ile başlardı? “Misvakla” dedi.» (3) Uzun süre susunca ve dişler sararınca da önceki hadisler gereği önem kazanır.',
     '١/ ١٣',
     'السواك سنة في كل وقت، لكن **يتأكد** في مواضع، أي يكون أشدّ استحبابًا. ويجمعها أمران: **العبادة** (الوضوء، والصلاة، والقراءة، ودخول المسجد)، و**تغيّر الفم** (القيام من النوم، وطول السكوت، وتغيّر الرائحة، وصفرة الأسنان).\n\n'
     'وفي حديث عائشة أدب جميل: أول ما يبدأ به النبي ﷺ إذا دخل بيته **السواك**؛ فيلقى أهله بفم طيب.\n\n'
     '**شرح الحواشي:** (٣) الحديث في صحيح مسلم.',
     'Misvak her vakitte sünnettir; ama bazı yerlerde **daha da önem kazanır**, yani daha kuvvetli müstehap olur. Bunları iki şey toplar: **ibadet** (abdest, namaz, Kur’ân okumak, mescide girmek) ve **ağzın değişmesi** (uykudan kalkmak, uzun susmak, kokunun değişmesi, dişlerin sararması).\n\n'
     'Âişe hadisinde güzel bir edep vardır: Nebî (sallallâhu aleyhi ve sellem) evine girince ilk olarak **misvakla** başlardı; ailesini güzel kokulu bir ağızla karşılardı.\n\n'
     '**Dipnotların şerhi:** (3) Hadis Müslim’in Sahîh’indedir.',
     fn=['(٣) أخرجه مسلم برقم (٢٥٣).'],
     note=dict(ar='تنبيه: اسم الراوي «المقدام بن شريح»، بالميم.', tr='Not: Râvinin adı «el-Mikdâm b. Şureyh»tir.')),
  PS('وكان رسول الله ﷺ إذا قام من الليل [[يَشُوصُ|shaws]] (٤) فاه بالسواك (٥)، والمسلم مأمور عند العبادة والتقرب إلى الله، أن يكون على أحسن حال من النظافة والطهارة.',
     'Rasûlullah (sallallâhu aleyhi ve sellem) geceleyin kalkınca ağzını misvakla ovardı (4) (5). Müslümana ibadet ederken ve Allah’a yaklaşırken temizlik ve taharetin en güzel hâlinde olması emredilmiştir.',
     '١/ ١٣',
     'هذه **قاعدة الباب كله**: المسلم إذا وقف بين يدي ربه، أو تقرّب إليه بعبادة، فهو على أحسن حال من النظافة. ومن هنا تأكّد السواك عند الصلاة والقراءة ودخول المسجد.\n\n'
     '**شرح الحواشي:** (٤) **الشوص** الدلك؛ أي يدلك أسنانه بالسواك. (٥) الحديث متفق عليه من حديث حذيفة رضي الله عنه.',
     'Bu, **bölümün tamamının kaidesidir**: Müslüman Rabbinin huzurunda durduğunda veya bir ibadetle O’na yaklaştığında temizliğin en güzel hâlindedir. Bu yüzden misvak namazda, Kur’ân okurken ve mescide girerken daha da önem kazanır.\n\n'
     '**Dipnotların şerhi:** (4) **Şavs** ovmaktır; yani dişlerini misvakla ovardı. (5) Hadis Huzeyfe’den (radıyallâhu anh) Buhârî ve Müslim’dedir.',
     fn=['(٤) الشوص: الدلك.', '(٥) رواه البخاري في كتاب الوضوء باب السواك برقم (٢٤٥)، ومسلم في كتاب الطهارة باب السواك برقم (٢٥٥).']),
 ]),
 dict(ar='المسألة الثالثة: بم يكون؟', tr='Üçüncü mesele: Neyle yapılır?', paras=[
  PS('يسن أن يكون التسوك بعود رطب لا يتفتت، ولا يجرح الفم؛ فإن النبي ﷺ كان يستاك بعود [[أراك|arak]] (١). وله أن يتسوك بيده اليمنى أو اليسرى، فالأمر في هذا واسع.',
     'Misvakın, dağılmayan ve ağzı yaralamayan taze bir çubukla yapılması sünnettir; çünkü Nebî (sallallâhu aleyhi ve sellem) erâk çubuğuyla misvak kullanırdı. (1) Sağ veya sol eliyle misvak kullanabilir; bu konuda genişlik vardır.',
     '١/ ١٤',
     'صفات العود المسنون ثلاث: **رطب** حتى يلين، و**لا يتفتت** فيبقى في الفم، و**لا يجرح** اللثة. وأفضله عود الأراك، وهو المعروف عند الناس بـ«السواك».\n\n'
     '**وباليمين أو اليسار:** الأمر واسع، فلا يتحرّج المسلم من أيّهما.\n\n'
     '**شرح الحواشي:** (١) **الأراك** شجر يُستاك بقضبانه، أي بأغصانه الرقيقة.',
     'Sünnet olan çubuğun üç vasfı vardır: yumuşasın diye **taze**, ağızda parçalar kalmasın diye **dağılmayan** ve diş etlerini **yaralamayan**. En faziletlisi, insanlar arasında «misvak» diye bilinen erâk çubuğudur.\n\n'
     '**Sağ veya sol elle:** Bu konuda genişlik vardır; Müslüman ikisinden birini kullanmakta sıkıntıya düşmez.\n\n'
     '**Dipnotların şerhi:** (1) **Erâk**, ince dallarıyla misvak yapılan bir ağaçtır.',
     fn=['(١) الأرَاك: شجر من الحمض يستاك بقضبانه، واسمه الكَبَاث.']),
  PS('فإن لم يكن عنده عود يستاك به حال الوضوء، أجزأه التسوك بأصبعه، كما روى ذلك عليُّ بن أبي طالب ﵁ في صفة وضوء النبي ﷺ. (٢)',
     'Abdest alırken misvak kullanacağı bir çubuk yoksa, parmağıyla misvak kullanması yeterlidir; Ali b. Ebî Tâlib (radıyallâhu anh) Nebî’nin (sallallâhu aleyhi ve sellem) abdestini anlatırken bunu rivayet etmiştir. (2)',
     '١/ ١٤',
     'هذا **البديل** عند فقد العود: الإصبع، ويدلك بها أسنانه. والمقصود من السواك تنظيف الأسنان والفم؛ فإذا أجزأت الإصبع، **فالفرشاة المعروفة يحصل بها المقصود أيضًا**، فلا يتحرّج من استعمالها. ويبقى عود الأراك أوفق للسنة.\n\n'
     '**شرح الحواشي:** (٢) الحديث أخرجه أحمد، وصحّحه ابن حجر.',
     'Çubuk bulunmadığında **yerine geçen** budur: parmak; onunla dişlerini ovar. Misvaktan maksat dişleri ve ağzı temizlemektir; parmak yettiğine göre **bilinen diş fırçasıyla da bu maksat hâsıl olur**, onu kullanmakta sıkıntı yoktur. Erâk çubuğu ise sünnete daha uygundur.\n\n'
     '**Dipnotların şerhi:** (2) Hadisi Ahmed rivayet etmiş, İbn Hacer sahih saymıştır.',
     fn=['(٢) أخرجه أحمد في المسند (١/ ١٥٨)، وصححه ابن حجر في التلخيص الحبير (١/ ٧٠).']),
 ]),
 dict(ar='المسألة الرابعة: فوائد السواك', tr='Dördüncü mesele: Misvakın faydaları', paras=[
  PS('ومن أهمها ما ورد في الحديث السابق: أنه مطهرة للفم في الدنيا مرضاة للرب في الآخرة. فينبغي للمسلم أن يتعاهد هذه السنة، ولا يتركها؛ لما فيها من فوائد عظيمة. وقد يمر على بعض المسلمين مدة من الوقت كالشهر والشهرين وهم لم يتسوكوا إما تكاسلاً وإما جهلاً، وهؤلاء قد فاتهم الأجر العظيم والفوائد الكثيرة؛ بسبب تركهم هذه السُّنةَ التي كان يحافظ عليها النبي ﷺ، وكاد يأمر بها أمته أَمْرَ إيجاب، لولا خوف المشقة.',
     'Faydalarının en önemlisi önceki hadiste geçendir: Dünyada ağzı temizler, ahirette Rabbi razı eder. Müslümanın bu sünnete devam etmesi ve onu terk etmemesi gerekir; çünkü onda büyük faydalar vardır. Bazı Müslümanlar tembellik veya bilgisizlik yüzünden bir iki ay misvak kullanmadan geçirir. Bunlar, Nebî’nin (sallallâhu aleyhi ve sellem) devam ettiği ve zorluk korkusu olmasa ümmetine vacip olarak emredeceği bu sünneti terk ettikleri için büyük sevabı ve pek çok faydayı kaçırmışlardır.',
     '١/ ١٤',
     'فائدتان في حديث واحد: **دنيوية** (طهارة الفم)، و**أخروية** (رضا الرب). وكفى بالثانية سببًا للمحافظة عليه.\n\n'
     'ثم نبّه الكتاب على حال من يترك السواك الشهر والشهرين: فهذا قد فاته أجر سنة كاد النبي ﷺ أن يوجبها.\n\n'
     'وفي هذا **حفظ لنعمة الأسنان**: نعمة لا يُعرف قدرها إلا عند فقدها؛ فالعلاج لا يعيد السنّ كما خلقها الله، وإنما يرمّمها.',
     'Tek hadiste iki fayda vardır: **dünyevî** (ağzın temizliği) ve **uhrevî** (Rabbin rızası). İkincisi bile ona devam etmek için yeterli bir sebeptir.\n\n'
     'Sonra kitap, bir iki ay misvakı terk edenin durumuna dikkat çekmiştir: Bu kimse, Nebî’nin (sallallâhu aleyhi ve sellem) neredeyse vacip kılacağı bir sünnetin sevabını kaçırmıştır.\n\n'
     'Bunda **diş nimetini korumak** vardır: Değeri ancak kaybedilince anlaşılan bir nimettir; tedavi dişi Allah’ın yarattığı gibi geri getiremez, ancak onarır.'),
  PS('وقد ذكروا فوائد أخرى للسواك، منها: أنه يقوي الأسنان، ويشد اللثة، وينقي الصوت، وينشط العبد.',
     'Misvakın başka faydaları da zikredilmiştir: Dişleri güçlendirir, diş etlerini sıkılaştırır, sesi berraklaştırır ve kulu dinçleştirir.',
     '١/ ١٤',
     'هذه فوائد ذكرها أهل العلم من التجربة، تضاف إلى الفائدتين المنصوص عليهما في الحديث.',
     'Bunlar âlimlerin tecrübeyle zikrettiği faydalardır; hadiste açıkça bildirilen iki faydaya eklenir.'),
 ]),
 dict(ar='المسألة الخامسة: سنن الفطرة', tr='Beşinci mesele: Fıtrat sünnetleri', paras=[
  PS('وتسمى أيضاً: خصال الفطرة؛ وذلك لأن فاعلها يتصف بالفطرة التي فطر الله الناس عليها واستحبها لهم؛ ليكونوا على أحسن هيئة وأكمل صورة. عن أبي هريرة ﵁ قال: قال رسول الله ﷺ: (خمس من الفطرة: الاستحداد والختان وقص الشارب ونتف الإبط وتقليم الأظافر) (٣).',
     'Bunlara fıtrat hasletleri de denir; çünkü bunları yapan kimse, Allah’ın insanları üzerine yarattığı ve onlar için sevdiği fıtratla vasıflanır; böylece en güzel görünüşte ve en mükemmel surette olurlar. Ebû Hureyre’den (radıyallâhu anh), Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurmuştur: «Beş şey fıtrattandır: kasık kıllarını tıraş etmek, sünnet olmak, bıyığı kısaltmak, koltuk altı kıllarını yolmak ve tırnakları kesmek.» (3)',
     '١/ ١٤',
     '**لماذا ذُكرت سنن الفطرة مع السواك؟** لأنها كلها من باب النظافة والتجمّل. وهذه فائدة من دراسة الفقه كاملًا: أن تعرف أين تجد المسألة في كتب الفقه، فقد تُذكر تحت باب لا يدلّ عليها اسمه مباشرة.\n\n'
     '**والفطرة:** الخِلقة التي خلق الله الناس عليها؛ فهذه الخصال يستحسنها كل صاحب طبع سليم.\n\n'
     '**شرح الحواشي:** (٣) الحديث متفق عليه.',
     '**Fıtrat sünnetleri neden misvakla birlikte anılmıştır?** Çünkü hepsi temizlik ve güzellik konusundandır. Bu, fıkhı bütün olarak okumanın bir faydasıdır: Bir meseleyi fıkıh kitaplarında nerede bulacağınızı bilirsiniz; bazen adı ona doğrudan delâlet etmeyen bir babda anılır.\n\n'
     '**Fıtrat:** Allah’ın insanları üzerine yarattığı yaratılış; selim tabiatlı herkes bu hasletleri güzel bulur.\n\n'
     '**Dipnotların şerhi:** (3) Hadis Buhârî ve Müslim’dedir.',
     fn=['(٣) متفق عليه: رواه البخاري برقم (٥٨٨٩)، ومسلم برقم (٢٥٧).']),
  PS('١ - [[الاستحداد|istihdad]]: وهو حَلْقُ العانة، وهي الشعر النابت حول الفرج، سمي بذلك لاستعمال الحديدة فيه وهي المُوسَى. وفي إزالته جمال ونظافة، ويمكن إزالته بغير الحلق كالمزيلات المصنعة.',
     '1. İstihdâd: Kasık kıllarını, yani tenasül organının çevresinde biten kılları tıraş etmektir. Bunda demir, yani ustura kullanıldığı için bu adı almıştır. Onu gidermekte güzellik ve temizlik vardır; tıraş dışında, hazır temizleyici ürünlerle de giderilebilir.',
     '١/ ١٥',
     'الاسم مأخوذ من **الحديدة**، لكن المقصود **الإزالة**؛ فتحصل السنة بالحلق، وبالمزيلات المصنّعة، وبغيرهما.',
     'İsim **demirden** alınmıştır; ama amaç **gidermektir**. Sünnet tıraşla, hazır temizleyicilerle veya başka bir yolla yerine gelir.'),
  PS('٢ - الختان: وهو إزالة الجلدة التي تغطي [[الحَشَفَة|hashafa]] (١) حتى تبرز الحشفة، وهذا في حق الذكر. أما الأنثى: فقطع لحمة زائدة فوق محل الإيلاج. قيل: إنها تشبه عُرف الديك. والصحيح: أنه واجب في حق الرجال، سنة في حق النساء. والحكمة في ختان الرجل: تطهير الذكر من النجاسة المحتقنة في [[القُلْفَة|qulfa]] (٢). وفوائده كثيرة. أما المرأة: فإنه يُقَلِّل من غُلْمَتِها أي: شدة شهوتها. ويستحب أن يكون في اليوم السابع للمولود؛ لأنه أسرع للبرء، ولينشأ الصغير على أكمل حال.',
     '2. Sünnet (hitan): Erkekte organın başını örten deriyi, baş ortaya çıkacak şekilde kesmektir. (1) Kadında ise birleşme yerinin üstündeki fazla bir et parçasını kesmektir. Doğru olan görüşe göre erkeklere vacip, kadınlara sünnettir. Erkeğin sünnetindeki hikmet, organı sünnet derisinde (2) biriken necasetten temizlemektir; faydaları çoktur. Kadındaki hikmeti ise şehvetin şiddetini azaltmaktır. Doğumun yedinci gününde yapılması müstehaptır; çünkü daha çabuk iyileşir ve çocuk en mükemmel hâl üzere yetişir.',
     '١/ ١٥',
     'فرّق الكتاب في الحكم بين الرجل والمرأة: **واجب في حق الرجال، سنة في حق النساء**.\n\n'
     'و**علّة الوجوب** في الرجل **الطهارة**: فالقلفة تحبس النجاسة، فإزالتها تُعين على الطهارة التي هي شرط الصلاة. **ووقته المستحب** اليوم السابع، لأن الصغير أسرع برءًا.\n\n'
     '**شرح الحواشي:** (١) **الحشفة** رأس الذكر. (٢) **القلفة** الجلدة التي تغطيها، وهي التي تُقطع في الختان.',
     'Kitap hükümde erkek ile kadını ayırmıştır: **Erkeklere vacip, kadınlara sünnettir.**\n\n'
     'Erkekteki **vacip olmasının gerekçesi taharettir**: Sünnet derisi necaseti tutar; onu gidermek, namazın şartı olan taharete yardım eder. **Müstehap vakti** yedinci gündür; çünkü küçük çocuk daha çabuk iyileşir.\n\n'
     '**Dipnotların şerhi:** (1) **Haşefe**, organın baş kısmıdır. (2) **Kulfe**, onu örten ve sünnette kesilen deridir.',
     fn=['(١) الحشفة: هي رأس الذكر.', '(٢) وهي الجلدة التي تغطي الحشفة، والتي تقطع في الختان.']),
  PS('٣ - قص الشارب وإحفاؤه: وهو المبالغة في قَصِّه؛ لما في ذلك من التجمل، والنظافة، ومخالفة الكفار. وقد وردت الأحاديث الصحيحة في الحث على قَصِّه، وإعفاء اللحية، وإرسالها وإكرامها؛ لما في بقاء اللحية من الجمال ومظهر الرجولة، وقد عَكَسَ كثير من الناس الأمر، فصاروا يوفرون شواربهم، ويحلقون لحاهم، أو يقصرونها.',
     '3. Bıyığı kısaltmak ve iyice kesmek: Kesmede ileri gitmektir; bunda güzellik, temizlik ve kâfirlere muhalefet vardır. Sahih hadisler bıyığı kısaltmayı, sakalı salıvermeyi, uzatmayı ve ona özen göstermeyi teşvik etmiştir; çünkü sakalın kalmasında güzellik ve erkeklik görünümü vardır. Pek çok insan işi tersine çevirmiş; bıyıklarını uzatıp sakallarını tıraş etmiş veya kısaltmıştır.',
     '١/ ١٥',
     '**الإحفاء:** المبالغة في قصّ الشارب، ولا سيما ما طال على الشفة حتى لا يصيب الطعام والشراب. وفيه ثلاث حِكَم ذكرها الكتاب: **التجمّل، والنظافة، ومخالفة الكفار**.\n\n'
     'ثم ذكر الكتاب ما وقع فيه كثير من الناس من **عكس السنة**: توفير الشارب، وحلق اللحية أو تقصيرها.',
     '**İhfâ:** Bıyığı kesmede ileri gitmek; özellikle yemeğe ve içeceğe değmesin diye dudağın üzerine uzayanı. Kitap bunda üç hikmet zikretmiştir: **güzellik, temizlik ve kâfirlere muhalefet.**\n\n'
     'Sonra kitap, pek çok insanın düştüğü **sünnete ters** durumu anmıştır: bıyığı uzatmak, sakalı tıraş etmek veya kısaltmak.'),
  PS('وفي كل هذا مخالفة للسنة والأوامر الواردة في وجوب إعفائها؛ منها: حديث أبي هريرة ﵁ قال: قال رسول الله ﷺ: ([[جزُّوا|jazz]] الشوارب، وأرخوا اللحى، وخالفوا المجوس) (٣). وحديث ابن عمر ﵄ عن النبي ﷺ قال: (خالفوا المشركين، وفِّروا اللحى، وأحفوا الشوارب) (٤). فعلى المسلم أن يلتزم بهذا الهدي النبوي، ويخالف الأعداء، ويتميز عن التشبه بالنساء.',
     'Bütün bunlarda sünnete ve sakalı salıvermenin vacip olduğunu bildiren emirlere aykırılık vardır. Bunlardan biri Ebû Hureyre’nin (radıyallâhu anh) hadisidir: Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Bıyıkları kısaltın, sakalları salıverin, Mecûsîlere muhalefet edin.» (3) İbn Ömer’in (radıyallâhu anhümâ) Nebî’den (sallallâhu aleyhi ve sellem) hadisi: «Müşriklere muhalefet edin: Sakalları bol bırakın, bıyıkları iyice kısaltın.» (4) Müslümanın bu nebevî yola bağlı kalması, düşmanlara muhalefet etmesi ve kadınlara benzemekten ayrılması gerekir.',
     '١/ ١٥',
     '**الحكم:** إعفاء اللحية **واجب**؛ لأن الأحاديث جاءت بصيغة الأمر: «أَرْخُوا»، «وَفِّرُوا»، والأمر يقتضي الوجوب، كما تقدّم في حديث السواك.\n\n'
     '**والعلّة:** مخالفة المجوس والمشركين، والتميّز عن التشبه بالنساء.\n\n'
     '**شرح الحواشي:** (٣) حديث أبي هريرة في صحيح مسلم. و**الجزّ** القصّ، و**إرخاء اللحية** تركها وعدم التعرض لها. (٤) حديث ابن عمر في الصحيحين، واللفظ للبخاري.',
     '**Hüküm:** Sakalı salıvermek **vaciptir**; çünkü hadisler emir kipiyle gelmiştir: «salıverin», «bol bırakın». Misvak hadisinde geçtiği gibi emir vacipliği gerektirir.\n\n'
     '**Gerekçe:** Mecûsîlere ve müşriklere muhalefet etmek ve kadınlara benzemekten ayrılmak.\n\n'
     '**Dipnotların şerhi:** (3) Ebû Hureyre hadisi Müslim’in Sahîh’indedir. **Cezz** kısaltmak, **sakalı salıvermek** ona dokunmadan bırakmaktır. (4) İbn Ömer hadisi Buhârî ve Müslim’dedir; lafız Buhârî’nindir.',
     fn=['(٣) أخرجه مسلم برقم (٢٦٠)، والجز: القص. وإرخاء اللحية: تركها وعدم التعرض لها.', '(٤) رواه البخاري برقم (٥٨٩٢)، ومسلم برقم (٢٥٨). واللفظ للبخاري.'],
     note=dict(ar='تنبيه على الحاشية (٤): حديث ابن عمر في «صحيح مسلم» برقم (٢٥٩).', tr='(4) numaralı dipnot hakkında: İbn Ömer hadisi Müslim’in Sahîh’inde 259 numaradadır.')),
  PS('٤ - تقليم الأظافر: وهو قَصُّها بحيث لا تترك حتى تطول. والتقليم يجملها، ويزيل الأوساخ المتراكمة تحتها، وقد خالف هذه الفطرة النبوية بعض المسلمين فصاروا يطيلون أظافرهم، أو أظافر إصبع معين من أيديهم. كل ذلك من تزيين الشيطان والتقليد لأعداء الله.',
     '4. Tırnakları kesmek: Uzamaya bırakılmayacak şekilde kesmektir. Kesmek onları güzelleştirir ve altlarında biriken kirleri giderir. Bazı Müslümanlar bu nebevî fıtrata aykırı davranarak tırnaklarını ya da elindeki belli bir parmağın tırnağını uzatmışlardır. Bunların hepsi şeytanın süslemesi ve Allah düşmanlarını taklittir.',
     '١/ ١٦',
     'حكمتان للتقليم: **الجمال**، و**النظافة**، فالوسخ يتجمّع تحت الأظفار الطويلة. وإطالة الأظفار عادة تخالف الفطرة، وإن زيّنها الشيطان للناس.',
     'Tırnak kesmenin iki hikmeti vardır: **güzellik** ve **temizlik**; çünkü uzun tırnakların altında kir birikir. Tırnak uzatmak, şeytan insanlara süslü gösterse de fıtrata aykırı bir âdettir.'),
  PS('٥ - نتف الإبط: أي إزالة الشعر النابت فيه، فيسن إزالة هذا الشعر بالنتف أو الحلق أو غيرهما؛ لما في إزالته من النظافة وقطع الروائح الكريهة التي تتجمع مع وجود هذا الشعر، فهذا هو ديننا الحنيف، أمرنا بهذه الخصال؛ لما فيها من التجمل والتطهر والنظافة، وليكون المسلم على أحسن حال، مبتعداً عن تقليد الكفار والجهال، مفتخراً بدينه، مطيعاً لربه، متبعاً لسنة نبيه ﷺ.',
     '5. Koltuk altı kıllarını yolmak: Orada biten kılları gidermektir. Bu kılları yolarak, tıraş ederek veya başka bir yolla gidermek sünnettir; çünkü bunda temizlik ve bu kıllarla birlikte biriken kötü kokuların önlenmesi vardır. İşte hanîf dinimiz bize bu hasletleri emretmiştir; çünkü bunlarda güzellik, taharet ve temizlik vardır. Böylece Müslüman en güzel hâlde olur; kâfirleri ve cahilleri taklitten uzak durur, diniyle iftihar eder, Rabbine itaat eder ve Nebî’sinin (sallallâhu aleyhi ve sellem) sünnetine uyar.',
     '١/ ١٦',
     'النتف هو الأفضل لأنه لفظ الحديث، لكن **المقصود الإزالة**؛ فتحصل السنة بالحلق وغيره.\n\n'
     'ثم ختم الكتاب الخصال الخمس بالمقصد الجامع: **التجمّل والتطهّر والنظافة**، وأن يكون المسلم على أحسن حال، **مفتخرًا بدينه** لا مقلّدًا لغيره.',
     'Yolmak, hadisin lafzı olduğu için daha faziletlidir; ama **amaç gidermektir**; sünnet tıraşla ve başka yollarla da yerine gelir.\n\n'
     'Sonra kitap beş hasleti toplayıcı amaçla bitirmiştir: **güzellik, taharet ve temizlik**; Müslümanın en güzel hâlde olması ve başkasını taklit etmeden **diniyle iftihar etmesi**.'),
  PS('ويضاف إلى هذه الخصال الخمس: السواك، واستنشاق الماء، والمضمضة، وغسل [[البراجم|barajim]] -وهي العقد التي في ظهور الأصابع، يجتمع فيها الوسخ-، والاستنجاء، وذلك لحديث عائشة ﵂ قالت: قال رسول الله ﷺ: (عشر من الفطرة: قص الشارب، وإعفاء اللحية، والسواك، واستنشاق الماء، وقص الأظفار، وغسل البراجم، ونتف الإبط، وحلق العانة، وانتقاص الماء) يعني الاستنجاء. قال مصعب بن شيبة -أحد رواة الحديث-: "ونسيت العاشرة، إلا أن تكون المضمضة". (١)',
     'Bu beş haslete misvak, suyu buruna çekmek, ağzı çalkalamak, berâcimi —parmakların üst yüzündeki, kirin biriktiği eklem yerlerini— yıkamak ve istincâ eklenir. Âişe’nin (radıyallâhu anhâ) hadisi buna delildir: Rasûlullah (sallallâhu aleyhi ve sellem) şöyle buyurdu: «On şey fıtrattandır: bıyığı kısaltmak, sakalı salıvermek, misvak, suyu buruna çekmek, tırnakları kesmek, parmak eklemlerini yıkamak, koltuk altı kıllarını yolmak, kasık kıllarını tıraş etmek ve suyu azaltmak», yani istincâ. Hadisin râvilerinden Mus’ab b. Şeybe: «Onuncusunu unuttum; mazmaza olmalı» demiştir. (1)',
     '١/ ١٦',
     'حديث عائشة يزيد على الخمس: **إعفاء اللحية، والسواك، والاستنشاق، والمضمضة، وغسل البراجم، والاستنجاء**. فخصال الفطرة كلها **نظافة**: للفم، والأنف، والأصابع، والبدن.\n\n'
     '**وانتقاص الماء:** الاستنجاء، كما فسّره الكتاب. وفي قول الراوي «نسيت العاشرة» أمانة الرواة: لم يجزم بما لم يحفظ.\n\n'
     '**شرح الحواشي:** (١) الحديث في صحيح مسلم.',
     'Âişe hadisi beşe şunları ekler: **sakalı salıvermek, misvak, suyu buruna çekmek, ağzı çalkalamak, parmak eklemlerini yıkamak ve istincâ.** Fıtrat hasletlerinin hepsi **temizliktir**: ağzın, burnun, parmakların ve bedenin.\n\n'
     '**İntikâsu’l-mâ:** Kitabın açıkladığı gibi istincâdır. Râvinin «onuncusunu unuttum» demesinde râvilerin emaneti vardır: Ezberlemediği şeyi kesin olarak söylememiştir.\n\n'
     '**Dipnotların şerhi:** (1) Hadis Müslim’in Sahîh’indedir.',
     fn=['(١) رواه مسلم برقم (٢٦١).']),
 ]),
]

# ------------------------------------------------------------------ الدرس الخامس: الوضوء (الباب الخامس، ١/ ١٧–٢٣)
GLOSS.update({
 'wadaa': dict(w='الوضاءة', ar='الحسن والنظافة.', tr='Güzellik ve temizlik.', src='الكتاب نفسه (١/ ١٧)'),
 'ghulul': dict(w='غُلُول', ar='الغلول: السرقة من أموال الغنيمة وغيرها.', tr='Gulûl: ganimet ve benzeri ortak mallardan çalmak.', src='حاشية الكتاب (١/ ١٧)'),
 'lumaa': dict(w='لُمعَةٌ', ar='اللمعة: الموضع الذي لم يصبه الماء في الوضوء أو الغسل.', tr='Lum’a: abdestte veya gusülde su değmeyen yer.', src='الكتاب نفسه (١/ ١٩)'),
 'wika': dict(w='وِكَاءُ', ar='الخيط الذي يربط به الخريطة والقربة.', tr='Kırbanın veya kesenin ağzını bağlayan ip.', src='حاشية الكتاب (١/ ٢١)'),
 'sah': dict(w='السَّه', ar='الدبر. والمعنى: أن العينين في يقظتهما بمنزلة الحبل الذي يربط به، فزوال اليقظة كزوال هذا الرباط.', tr='Makat. Anlamı: Gözler uyanıkken bağlayan ip gibidir; uyanıklığın gitmesi bu bağın çözülmesi gibidir.', src='حاشية الكتاب (١/ ٢١)'),
})
GLOSS_TR_SRC.update({
 'الكتاب نفسه (١/ ١٧)': 'Kitabın kendisi (1/ 17)',
 'حاشية الكتاب (١/ ١٧)': 'Kitabın dipnotu (1/ 17)',
 'الكتاب نفسه (١/ ١٩)': 'Kitabın kendisi (1/ 19)',
 'حاشية الكتاب (١/ ٢١)': 'Kitabın dipnotu (1/ 21)',
})

SHARH[105] = [
 dict(ar='المسألة الأولى: تعريفه، وحكمه', tr='Birinci mesele: Tanımı ve hükmü', paras=[
  PS('الوُضوء لغة: مشتق من [[الوضاءة|wadaa]]، وهي الحسن والنظافة. وشرعاً: استعمال الماء في الأعضاء الأربعة -وهي الوجه واليدان والرأس والرجلان- على صفة مخصوصة في الشرع، على وجه التعبد لله تعالى.',
     'Abdest (vudû) sözlükte: «vedâe» kelimesinden türemiştir; güzellik ve temizlik demektir. Şer’an: Suyu dört organda —yüz, eller, baş ve ayaklarda— şeriatta belirlenmiş bir şekilde, Allah Teâlâ’ya ibadet maksadıyla kullanmaktır.',
     '١/ ١٧',
     'تعلّمنا في الأبواب السابقة الماء والإناء والاستنجاء والسواك، وكلها مقدّمات لهذا الباب.\n\n'
     'وفي التعريف الشرعي ثلاثة قيود: **الأعضاء الأربعة**، و**الصفة المخصوصة** (فلا يكفي أي غسل)، و**التعبّد لله**؛ ومنه نفهم أن **النية** لا بد منها، فمن غسل هذه الأعضاء للتبرّد وحده لم يتوضأ.\n\n'
     'والوضوء بضمّ الواو: الفعل، وبفتحها: الماء الذي يُتوضأ به.',
     'Önceki bölümlerde suyu, kabı, istincâyı ve misvakı öğrendik; hepsi bu bölüme hazırlıktır.\n\n'
     'Şer’î tanımda üç kayıt vardır: **dört organ**, **belirlenmiş şekil** (her yıkama yetmez) ve **Allah’a ibadet**. Buradan **niyetin** şart olduğunu anlarız: Bu organları yalnızca serinlemek için yıkayan abdest almış olmaz.\n\n'
     'Arapçada «vudû» fiilin, «vadû» abdest alınan suyun adıdır.'),
  PS('وحكمه: أنه واجب على المُحْدِث إذا أراد الصلاة وما في حكمها، كالطواف ومسِّ المصحف.',
     'Hükmü: Abdestsiz kimse namaz ve onun hükmündeki şeyleri, tavaf ve Mushafa dokunmak gibi, istediğinde farzdır.',
     '١/ ١٧',
     '**المُحدِث:** من عليه حدث أصغر، كمن بال أو نام. فالوضوء لا يجب لذاته في كل وقت، بل **يجب لغيره**: للصلاة وما في حكمها. فمن كان على وضوء لم يجب عليه أن يتوضأ مرة أخرى.',
     '**Muhdis:** küçük hadesi olan kimse; küçük abdest yapan veya uyuyan gibi. Abdest her vakitte kendisi için farz değildir; **başka bir şey için farzdır**: namaz ve onun hükmündekiler için. Abdestli olanın tekrar abdest alması gerekmez.'),
 ]),
 dict(ar='المسألة الثانية: الدليل على وجوبه، وعلى من يجب، ومتى يجب؟', tr='İkinci mesele: Farz olduğunun delili, kime ve ne zaman farz olduğu', paras=[
  PS('أما الدليل على وجوبه: فقوله تعالى ﴿يَا أَيُّهَا الَّذِينَ آمَنُوا إِذَا قُمْتُمْ إِلَى الصَّلَاةِ فَاغْسِلُوا وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى الْمَرَافِقِ وَامْسَحُوا بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى الْكَعْبَيْنِ﴾ [المائدة: ٦]. وقوله ﷺ: (لا يقبل الله صلاةً بغير طُهُور، ولا صدقة من [[غُلُول|ghulul]]) (١). وقوله ﷺ: (لا يقبل الله صلاة من أحدث حتى يتوضأ) (٢). ولم ينقل عن أحد من المسلمين في ذلك خلاف، فثبتت بذلك مشروعية الوضوء: بالكتاب، والسنة، والإجماع.',
     'Farz olduğunun delili Allah Teâlâ’nın şu sözüdür: «Ey iman edenler! Namaza kalktığınızda yüzlerinizi ve dirseklere kadar ellerinizi yıkayın, başlarınızı meshedin ve topuklara kadar ayaklarınızı (yıkayın).» [Mâide, 6] Nebî’nin (sallallâhu aleyhi ve sellem) şu sözü: «Allah temizlik olmadan namazı, haksız alınan maldan da sadakayı kabul etmez.» (1) Ve şu sözü: «Allah, abdesti bozulan kimsenin namazını abdest alıncaya kadar kabul etmez.» (2) Müslümanlardan hiç kimseden bu konuda ihtilaf nakledilmemiştir; böylece abdestin meşruiyeti Kitap, Sünnet ve icmâ ile sabit olmuştur.',
     '١/ ١٧',
     'ثلاثة أدلة يحفظها الطالب: **الكتاب** (آية المائدة)، و**السنة** (لا يقبل الله صلاة بغير طهور)، و**الإجماع**.\n\n'
     'و**الآية** نفسها هي أصل فروض الوضوء الأربعة الأولى: الوجه، واليدان، والرأس، والرجلان، كما سيأتي.\n\n'
     '**شرح الحواشي:** (١) الحديث في صحيح مسلم من حديث ابن عمر رضي الله عنهما. و**الغلول** السرقة من الغنيمة قبل قسمتها. (٢) الحديث في الصحيحين من حديث أبي هريرة رضي الله عنه.',
     'Öğrencinin ezberleyeceği üç delil: **Kitap** (Mâide âyeti), **Sünnet** (Allah temizlik olmadan namazı kabul etmez) ve **icmâ**.\n\n'
     '**Âyet** de abdestin ilk dört farzının aslıdır: yüz, eller, baş ve ayaklar; ileride gelecek.\n\n'
     '**Dipnotların şerhi:** (1) Hadis İbn Ömer’den (radıyallâhu anhümâ) Müslim’in Sahîh’indedir. **Gulûl**, ganimetten paylaştırılmadan önce çalmaktır. (2) Hadis Ebû Hureyre’den (radıyallâhu anh) Buhârî ve Müslim’dedir.',
     fn=['(١) رواه مسلم برقم (٢٢٤). والغلول: السرقة من أموال الغنيمة وغيرها.', '(٢) رواه مسلم برقم (٢٢٣).'],
     note=dict(ar='تنبيه على الحاشية (٢): الحديث في «صحيح مسلم» برقم (٢٢٥)، وفي «صحيح البخاري» برقم (١٣٥).', tr='(2) numaralı dipnot hakkında: Hadis Müslim’in Sahîh’inde 225, Buhârî’nin Sahîh’inde 135 numaradadır.')),
  PS('وأما على مَنْ يجب: فيجب على المسلم البالغ العاقل إذا أراد الصلاة وما في حكمها. وأما متى يجب؟ فإذا دخل وقت الصلاة أو أراد الإنسان الفعل الذي يشترط له الوضوء، وإن لم يكن ذلك متعلقاً بوقت، كالطواف ومس المصحف.',
     'Kime farzdır: Namaz ve onun hükmündekileri isteyen, ergenlik çağına girmiş akıllı Müslümana. Ne zaman farzdır: Namaz vakti girince veya kişi, vakte bağlı olmasa da tavaf ve Mushafa dokunmak gibi abdestin şart olduğu bir fiili yapmak isteyince.',
     '١/ ١٧',
     '**على من:** ثلاثة أوصاف: مسلم، بالغ، عاقل؛ وهذه شروط التكليف.\n\n'
     '**متى:** للصلاة إذا دخل وقتها، وللطواف ومسّ المصحف عند إرادتهما، لأنهما لا يتعلّقان بوقت. ولا حرج أن يتوضأ قبل دخول الوقت.',
     '**Kime:** üç vasıf: Müslüman, ergen ve akıllı; bunlar dinen sorumluluğun şartlarıdır.\n\n'
     '**Ne zaman:** Namaz için vakti girince; tavaf ve Mushafa dokunmak için bunları isteyince, çünkü bunlar bir vakte bağlı değildir. Vakit girmeden abdest almakta sakınca yoktur.'),
 ]),
 dict(ar='المسألة الثالثة: في شروطه', tr='Üçüncü mesele: Şartları', paras=[
  PS('ويشترط لصحة الوضوء ما يأتي: أ) الإسلام، والعقل، والتمييز، فلا يصح من الكافر، ولا المجنون، ولا يكون معتبراً من الصغير الذي دون سن التمييز. ب) النية: لحديث: (إنما الأعمال بالنيات) (١). ولا يشرع التلفظ بها؛ لعدم ثبوته عن النبي ﷺ.',
     'Abdestin sahih olması için şunlar şarttır: a) İslam, akıl ve temyiz: Kâfirden ve deliden sahih olmaz; temyiz yaşına girmemiş küçüğün abdesti muteber değildir. b) Niyet: «Ameller ancak niyetlere göredir» hadisi gereği. (1) Niyeti dille söylemek meşru değildir; çünkü Nebî’den (sallallâhu aleyhi ve sellem) sabit olmamıştır.',
     '١/ ١٨',
     '**التمييز:** أن يفرّق الصغير بين العبادة واللعب، فيستطيع أن ينوي.\n\n'
     '**النية محلّها القلب:** فمن قام إلى الماء يريد الوضوء فقد نوى. **والتلفظ بها** كقول «نويت أن أتوضأ» لم يفعله النبي ﷺ ولا أصحابه، فلا يُشرع.\n\n'
     '**شرح الحواشي:** (١) حديث «إنما الأعمال بالنيات» متفق عليه، وهو أول حديث في صحيح البخاري.',
     '**Temyiz:** Küçüğün ibadet ile oyunu ayırabilmesi ve böylece niyet edebilmesi.\n\n'
     '**Niyetin yeri kalptir:** Abdest almak isteyerek suya kalkan niyet etmiştir. **Dille söylemek**, «Abdest almaya niyet ettim» demek gibi, Nebî’nin (sallallâhu aleyhi ve sellem) ve ashabının yaptığı bir şey değildir; meşru değildir.\n\n'
     '**Dipnotların şerhi:** (1) «Ameller ancak niyetlere göredir» hadisi Buhârî ve Müslim’dedir; Buhârî’nin Sahîh’indeki ilk hadistir.',
     fn=['(١) رواه البخاري برقم (١)، ومسلم برقم (١٩٠٧).']),
  PS('ج) الماء الطهور: لما تقدم في المياه، أما الماء النجس فلا يصح الوضوء به. د) إزالة ما يمنع وصول الماء إلى البشرة، من شمع أو عجين ونحوهما: كطلاء الأظافر الذي يعرف بين النساء اليوم. هـ) الاستجمار أو الاستنجاء عند وجود سببهما لما تقدم. و) الموالاة. ز) الترتيب. وسيأتي الكلام عليهما بعد قليل. ح) غسل جميع الأعضاء الواجب غسلها.',
     'c) Tahûr su: Sular bölümünde geçtiği gibi; necis su ile abdest sahih olmaz. d) Mum, hamur ve benzeri, suyun cilde ulaşmasına engel olan şeyleri gidermek; bugün kadınlar arasında bilinen oje gibi. e) Sebebi bulunduğunda isticmâr veya istincâ; geçtiği gibi. f) Muvâlât. g) Tertip; ikisi biraz sonra gelecek. h) Yıkanması farz olan bütün organları yıkamak.',
     '١/ ١٨',
     '**إزالة الحائل:** كل ما يكوّن طبقة على الجلد فيمنع وصول الماء، كالطلاء والشمع والعجين والدهان العازل، يجب إزالته قبل الوضوء. فالمرأة التي على أظفارها طلاء لا يصح وضوؤها حتى تزيله. أما اللون الذي لا طبقة له، كالحِنّاء، فلا يمنع.\n\n'
     '**الاستنجاء قبل الوضوء:** هذا ترتيب الكتاب؛ فالمسلم يستنجي أولًا ثم يتوضأ.\n\n'
     'ودرس المياه والاستنجاء صار هنا **شرطين** من شروط الوضوء؛ فالأبواب يبني بعضها على بعض.',
     '**Engeli gidermek:** Ciltte tabaka oluşturup suyun ulaşmasını engelleyen her şey, oje, mum, hamur ve su geçirmeyen boya gibi, abdestten önce giderilmelidir. Tırnaklarında oje bulunan kadının abdesti, onu gidermedikçe sahih olmaz. Kına gibi tabakası olmayan renk ise engel değildir.\n\n'
     '**Abdestten önce istincâ:** Kitabın sıralaması budur; Müslüman önce istincâ yapar, sonra abdest alır.\n\n'
     'Sular ve istincâ dersleri burada abdestin iki **şartı** olmuştur; bölümler birbirinin üzerine kurulur.'),
 ]),
 dict(ar='المسألة الرابعة: فروضه -أي أعضاؤه-', tr='Dördüncü mesele: Farzları, yani organları', paras=[
  PS('وهي ستة: ١ - غسل الوجه بكامله؛ لقوله تعالى: ﴿إِذَا قُمْتُمْ إِلَى الصَّلَاةِ فَاغْسِلُوا وُجُوهَكُمْ﴾ [المائدة: ٦]، ومنه المضمضة والاستنشاق؛ لأن الفم والأنف من الوجه. ٢ - غسل اليدين إلى المرفقين؛ لقوله تعالى: ﴿وَأَيْدِيَكُمْ إِلَى الْمَرَافِقِ﴾ [المائدة: ٦].',
     'Bunlar altıdır: 1. Yüzün tamamını yıkamak; Allah Teâlâ’nın «Namaza kalktığınızda yüzlerinizi yıkayın» [Mâide, 6] sözü gereği. Mazmaza ve istinşak da buna dahildir; çünkü ağız ve burun yüzdendir. 2. Elleri dirseklerle birlikte yıkamak; «dirseklere kadar ellerinizi» [Mâide, 6] sözü gereği.',
     '١/ ١٨',
     '**الوجه:** ما تحصل به المواجهة؛ فيدخل فيه الفم والأنف، فلهذا كانت **المضمضة والاستنشاق من فرض غسل الوجه**.\n\n'
     '**اليدان إلى المرفقين:** من أطراف الأصابع إلى المرفق، والمرفق داخل في الغسل. **وانتبه:** بعض الناس يغسل كفّيه أول الوضوء، ثم يغسل وجهه، ثم يغسل من الرسغ إلى المرفق فقط؛ وهذا لا يصح، لأن غسل الكفين أول الوضوء سنة، والفرض بعد الوجه أن تُغسل اليد كلها من أطراف الأصابع.',
     '**Yüz:** Karşılaşmanın onunla olduğu kısım; ağız ve burun buna girer. Bu yüzden **mazmaza ve istinşak, yüzü yıkama farzına dahildir.**\n\n'
     '**Dirseklere kadar eller:** Parmak uçlarından dirseğe kadar; dirsek de yıkamaya dahildir. **Dikkat:** Bazı insanlar abdestin başında ellerini yıkar, sonra yüzünü, sonra yalnızca bilekten dirseğe kadar yıkar; bu sahih değildir. Çünkü başta elleri yıkamak sünnettir; yüzden sonraki farz, eli parmak uçlarından itibaren tamamen yıkamaktır.'),
  PS('٣ - مسح الرأس كله مع الأذنين؛ لقوله تعالى: ﴿وَامْسَحُوا بِرُءُوسِكُمْ﴾ [المائدة: ٦]. وقوله ﷺ: (الأذنان من الرأس) (٢). فلا يُجزئ مسح بعض الرأس دون بعضه.',
     '3. Kulaklarla birlikte başın tamamını meshetmek; «Başlarınızı meshedin» [Mâide, 6] âyeti ve Nebî’nin (sallallâhu aleyhi ve sellem) «Kulaklar baştandır» sözü gereği. (2) Başın bir kısmını meshedip diğerini bırakmak yetmez.',
     '١/ ١٨',
     'هذا اختيار الكتاب: **يجب مسح الرأس كله**. ووجهه أن الباء في ﴿بِرُءُوسِكُمْ﴾ للإلصاق، أي ألصقوا المسح برؤوسكم، وقد بيّن النبي ﷺ ذلك بفعله: بدأ بمقدّم رأسه حتى ذهب بيديه إلى قفاه، ثم ردّهما إلى المكان الذي بدأ منه.\n\n'
     'و**الأذنان من الرأس**، فتُمسحان معه، ولا تحتاجان ماءً جديدًا.\n\n'
     '**شرح الحواشي:** (٢) الحديث رواه الترمذي وابن ماجه، وصحّحه الألباني وجمع طرقه.',
     'Kitabın tercihi budur: **Başın tamamını meshetmek farzdır.** Gerekçesi şudur: «Başlarınızı» kelimesindeki «bi» harfi yapıştırma içindir, yani meshi başlarınıza ulaştırın. Nebî (sallallâhu aleyhi ve sellem) bunu fiiliyle açıklamıştır: Başının önünden başlayıp ellerini ensesine kadar götürmüş, sonra başladığı yere geri getirmiştir.\n\n'
     '**Kulaklar baştandır**; onunla birlikte meshedilir, yeni su gerekmez.\n\n'
     '**Dipnotların şerhi:** (2) Hadisi Tirmizî ve İbn Mâce rivayet etmiş; Elbânî sahih saymış ve yollarını toplamıştır.',
     fn=['(٢) رواه الترمذي برقم (٣٧) وابن ماجه برقم (٤٤٣) وصححه الألباني (صحيح سنن ابن ماجه برقم ٣٥٧، والسلسلة الصحيحة برقم ٣٦) وأفاض الشيخ ﵀ في جمع طرقه والكلام عليه.']),
  PS('٤ - غسل الرجلين إلى الكعبين؛ لقوله تعالى: ﴿وَأَرْجُلَكُمْ إِلَى الْكَعْبَيْنِ﴾ [المائدة: ٦]. ٥ - الترتيب: لأن الله تعالى ذكره مرتباً؛ وتوضأ رسول الله ﷺ مرتباً على حسب ما ذكر الله سبحانه: الوجه، فاليدين، فالرأس، فالرجلين، كما ورد ذلك في صفة وضوئه ﷺ في حديث عبد الله بن زيد (١) وغيره.',
     '4. Ayakları topuklarla birlikte yıkamak; «topuklara kadar ayaklarınızı» [Mâide, 6] âyeti gereği. 5. Tertip: Çünkü Allah Teâlâ onları sıralı zikretmiş; Rasûlullah (sallallâhu aleyhi ve sellem) de Allah’ın zikrettiği sıraya göre abdest almıştır: yüz, eller, baş, ayaklar. Abdullah b. Zeyd’in (1) ve başkalarının Nebî’nin (sallallâhu aleyhi ve sellem) abdestini anlattığı hadislerde böyle gelmiştir.',
     '١/ ١٩',
     '**الكعبان:** العظمان الناتئان في جانبي القدم، وهما داخلان في الغسل.\n\n'
     '**الترتيب:** دليله أمران: أن الله ذكر الأعضاء مرتّبة، **وأدخل الممسوح (الرأس) بين المغسولات** (اليدين والرجلين)، ولا يُفعل هذا في الكلام إلا لفائدة، وهي الترتيب؛ وأن النبي ﷺ توضأ مرتّبًا دائمًا.\n\n'
     '**شرح الحواشي:** (١) حديث عبد الله بن زيد في صفة الوضوء أخرجه مسلم.',
     '**Topuklar:** Ayağın iki yanındaki çıkıntılı kemikler; yıkamaya dahildir.\n\n'
     '**Tertip:** İki delili vardır: Allah organları sıralı zikretmiş ve **meshedileni (başı) yıkananların (eller ve ayaklar) arasına koymuştur**; söz ancak bir fayda için böyle kurulur; bu fayda tertiptir. Ayrıca Nebî (sallallâhu aleyhi ve sellem) her zaman sıralı abdest almıştır.\n\n'
     '**Dipnotların şerhi:** (1) Abdullah b. Zeyd’in abdesti anlattığı hadisi Müslim rivayet etmiştir.',
     fn=['(١) أخرجه مسلم برقم (٢٣٥).']),
  PS('٦ - الموالاة: بأن يكون غسل العضو عقب الذي قبله مباشرة بدون تأخير، فقد كان النبي ﷺ يتوضأ متوالياً، ولحديث خالد بن معدان: (أن النبي ﷺ رأى رجلاً يصلي وفي ظهر قدمه [[لُمعَةٌ|lumaa]] قدر الدرهم لم يصبها الماء، فأمره أن يعيد الوضوء) (٢)، فلو لم تكن الموالاة شرطاً لأمره بغسل ما فاته، ولم يأمره بإعادة الوضوء كله. واللُّمْعَة: الموضع الذي لم يصبه الماء في الوضوء أو الغسل.',
     '6. Muvâlât: Her organı, öncekinin hemen ardından gecikmeden yıkamaktır. Nebî (sallallâhu aleyhi ve sellem) peş peşe abdest alırdı. Hâlid b. Ma’dân’ın hadisi de buna delildir: «Nebî (sallallâhu aleyhi ve sellem) namaz kılan bir adam gördü; ayağının üstünde su değmemiş dirhem büyüklüğünde bir kuru yer vardı; ona abdesti yeniden almasını emretti.» (2) Muvâlât şart olmasaydı, yalnızca yıkanmayan yeri yıkamasını emreder, bütün abdesti yeniden almasını emretmezdi. Lum’a: abdestte veya gusülde su değmeyen yerdir.',
     '١/ ١٩',
     '**الموالاة:** ألا يؤخّر غسل عضو حتى ينشف الذي قبله في الزمن المعتدل.\n\n'
     '**ووجه الدلالة من الحديث دقيق:** الرجل كان قد صلّى، أي طال الفصل بين وضوئه وتدارك اللمعة، ففاتت الموالاة؛ فأمره بإعادة الوضوء كله. ولو كانت الموالاة غير واجبة لكفاه أن يغسل اللمعة وحدها.\n\n'
     'وفي الحديث درس عملي: **تفقّد ظهور القدمين والعقبين** عند الوضوء، فهي مواضع يقصّر فيها الناس.\n\n'
     '**شرح الحواشي:** (٢) الحديث رواه أحمد وأبو داود، وصحّحه الألباني.',
     '**Muvâlât:** Normal havada önceki organ kurumadan sonrakini yıkamayı geciktirmemek.\n\n'
     '**Hadisteki delil yönü incedir:** Adam namazını kılmıştı; yani abdesti ile kuru yeri telafi etmesi arasında uzun bir ara geçmiş, muvâlât kaçmıştı. Bu yüzden bütün abdesti yeniden almasını emretti. Muvâlât vacip olmasaydı, yalnızca kuru yeri yıkaması yeterdi.\n\n'
     'Hadiste pratik bir ders vardır: Abdest alırken **ayakların üstünü ve topukları kontrol etmek**; insanlar buralarda kusur eder.\n\n'
     '**Dipnotların şerhi:** (2) Hadisi Ahmed ve Ebû Dâvûd rivayet etmiş, Elbânî sahih saymıştır.',
     fn=['(٢) رواه أحمد (٣/ ٤٢٤)، وأبو داود برقم (١٧٥)، وصححه الألباني. انظر إرواء الغليل (١/ ١٢٧).']),
 ]),
 dict(ar='المسألة الخامسة: سننه', tr='Beşinci mesele: Sünnetleri', paras=[
  PS('هناك أفعال يستحب فعلها عند الوضوء ويؤجر عليها من فعلها، ومن تركها فلا حرج عليه، وتسمى هذه الأفعال بسنن الوضوء، وهي: ١ - التسمية في أوله: لقوله ﷺ: (لا وضوء لمن لم يذكر اسم الله عليه) (٣). ٢ - السواك: لقوله ﷺ: (لولا أن أشق على أمتي لأمرتهم بالسواك مع كل وضوء) (٤). ٣ - غسل الكفين ثلاثاً في أول الوضوء: لفعله ﷺ ذلك، إذ كان يغسل كفيه ثلاثاً كما ورد في صفة وضوئه.',
     'Abdestte yapılması müstehap olan fiiller vardır; yapan sevap kazanır, terk edene günah yoktur. Bunlara abdestin sünnetleri denir: 1. Başta besmele; Nebî’nin (sallallâhu aleyhi ve sellem) «Allah’ın adını anmayanın abdesti yoktur» sözü gereği. (3) 2. Misvak; «Ümmetime zorluk vermeyecek olsaydım, onlara her abdestte misvak kullanmalarını emrederdim» sözü gereği. (4) 3. Abdestin başında elleri üç kez yıkamak; Nebî’nin (sallallâhu aleyhi ve sellem) fiili gereği; abdestinin tarifinde geldiği gibi ellerini üç kez yıkardı.',
     '١/ ١٩',
     '**الفرق بين الفرض والسنة:** الفرض لا يصح الوضوء بدونه، والسنة كمال يُؤجر عليه ولا يبطل الوضوء بتركه.\n\n'
     '**التسمية:** قول «بسم الله» عند البدء. **والسواك:** تقدّم أنه يتأكد عند الوضوء. **وغسل الكفين ثلاثًا** أول الوضوء سنة، وليس هو غسل اليدين المفروض.\n\n'
     '**شرح الحواشي:** (٣) حديث التسمية أخرجه أحمد وأبو داود وغيرهما، وحسّنه جماعة من الأئمة والألباني. (٤) حديث السواك ذكره البخاري معلّقًا بصيغة الجزم، ووصله النسائي.',
     '**Farz ile sünnet arasındaki fark:** Farz olmadan abdest sahih olmaz; sünnet ise sevap kazandıran bir kemaldir, terk edilmesi abdesti bozmaz.\n\n'
     '**Besmele:** Başlarken «Bismillah» demek. **Misvak:** Abdestte daha da önem kazandığı geçmişti. **Elleri üç kez yıkamak** abdestin başında sünnettir; farz olan elleri yıkamak bu değildir.\n\n'
     '**Dipnotların şerhi:** (3) Besmele hadisini Ahmed, Ebû Dâvûd ve başkaları rivayet etmiş; bir grup imam ve Elbânî hasen saymıştır. (4) Misvak hadisini Buhârî kesinlik bildiren ifadeyle muallak zikretmiş, Nesâî senedli rivayet etmiştir.',
     fn=['(٣) أخرجه أحمد (٢/ ٤١٨)، وأبو داود برقم (١٠١)، والحاكم (١/ ١٤٧) وغيرهم من حديث أبي هريرة ﵁، وحسنه: ابن الصلاح، وابن كثير، والعراقي، وقواه المنذري وابن حجر، وقال الألباني: حسن. (إرواء الغليل ١/ ١٢٢).', '(٤) أخرجه البخاري معلقاً بصيغة جزم: ك الصيام، ب سواك الرطب واليابس للصائم. ووصله النسائي (انظر: فتح الباري ٤/ ١٥٩).']),
  PS('٤ - المبالغة في المضمضة والاستنشاق لغير الصائم: فقد ورد في صفة وضوئه ﷺ: (فمضمضَ واستنثَر)، ولقوله ﷺ: (وبالغ في الاستنشاق إلا أن تكون صائماً) (١). ٥ - الدلك، وتخليل اللحية الكثيفة بالماء حتى يدخل الماء في داخلها: لفعله ﷺ، فإنه (كان إذا توضأ يدلك ذراعيه) (٢)، وكذلك (كان يدخل الماء تحت حنكه ويخلل به لحيته) (٣).',
     '4. Oruçlu olmayan için mazmaza ve istinşakta mübalağa: Nebî’nin (sallallâhu aleyhi ve sellem) abdestinin tarifinde «Ağzını çalkaladı ve burnuna su çekip sümkürdü» geçmiştir; ayrıca «Oruçlu olman hariç, suyu buruna çekmede mübalağa et» buyurmuştur. (1) 5. Ovmak ve sık sakalı, su içine girecek şekilde hilâllemek: Nebî’nin (sallallâhu aleyhi ve sellem) fiili gereği; o, abdest alınca kollarını ovardı (2) ve suyu çenesinin altına sokup sakalını hilâllerdi. (3)',
     '١/ ٢٠',
     '**المبالغة:** المضمضة إدخال الماء في الفم وإدارته، والمبالغة تحريكه بقوة في جميع الفم؛ والاستنشاق جذب الماء بالنفَس إلى الأنف، والمبالغة جذبه إلى أقصاه. **واستثنى الصائم** لئلا يصل الماء إلى جوفه فيفسد صومه.\n\n'
     '**التخليل** للحية **الكثيفة** التي لا تُرى البشرة من تحتها؛ أما الخفيفة فيجب غسل ما تحتها.\n\n'
     '**شرح الحواشي:** (١) حديث المبالغة رواه أبو داود والنسائي، وصحّحه الألباني. (٢) حديث الدلك رواه ابن حبان وابن خزيمة والحاكم وأحمد. (٣) حديث التخليل رواه أبو داود، وصحّحه الألباني.',
     '**Mübalağa:** Mazmaza suyu ağza alıp çalkalamak, mübalağa onu bütün ağızda kuvvetlice hareket ettirmektir. İstinşak suyu nefesle buruna çekmek, mübalağa en uca kadar çekmektir. **Oruçlu hariç tutulmuştur**; su midesine ulaşıp orucu bozulmasın diye.\n\n'
     '**Hilâllemek**, altındaki cilt görünmeyen **sık sakal** içindir; seyrek sakalın altını yıkamak ise farzdır.\n\n'
     '**Dipnotların şerhi:** (1) Mübalağa hadisini Ebû Dâvûd ve Nesâî rivayet etmiş, Elbânî sahih saymıştır. (2) Ovma hadisini İbn Hibbân, İbn Huzeyme, Hâkim ve Ahmed rivayet etmiştir. (3) Hilâlleme hadisini Ebû Dâvûd rivayet etmiş, Elbânî sahih saymıştır.',
     fn=['(١) أخرجه أبو داود برقم (١٤٢)، والنسائي (١/ ٦٦ رقم ٨٧)، وصححه الألباني (صحيح النسائي رقم ٨٥).', '(٢) رواه ابن حبان في صحيحه (٣/ ٣٦٣) برقم (١٠٨٢)، والبيهقي في السنن الكبرى (١/ ١٩٦)، والحاكم في المستدرك (١/ ٢٤٣) وصححه، وابن خزيمة في صحيحه (١/ ٦٢)، والإمام أحمد في مسنده (٤/ ٣٩).', '(٣) رواه أبو داود برقم (١٤٥)، وصححه الألباني (الإرواء برقم ٩٢).']),
  PS('٦ - تقديم اليمنى على اليسرى في اليدين والرجلين: لفعله ﷺ، فإنه (كان يحب التيامن في تنعله وترجله وطهوره وفي شأنه كله) (٤). ٧ - تثليث الغسل في الوجه واليدين والرجلين: فالواجب مرة واحدة، ويستحب ثلاثاً، لفعله ﷺ فقد ثبت عنه: (أنه توضأ مرة مرة ومرتين مرتين وثلاثاً ثلاثاً) (٥).',
     '6. Ellerde ve ayaklarda sağı soldan önce yıkamak: Nebî’nin (sallallâhu aleyhi ve sellem) fiili gereği; o, «ayakkabı giymesinde, taranmasında, temizlenmesinde ve bütün işlerinde sağdan başlamayı severdi.» (4) 7. Yüzü, elleri ve ayakları üçer kez yıkamak: Farz bir kezdir, üç kez müstehaptır; Nebî’nin (sallallâhu aleyhi ve sellem) fiili gereği; ondan «birer kez, ikişer kez ve üçer kez abdest aldığı» sabittir. (5)',
     '١/ ٢٠',
     '**التيامن:** البدء باليمين في اليدين والرجلين. أما الوجه والرأس والأذنان فتُغسل أو تُمسح معًا.\n\n'
     '**التثليث:** الفرض مرة تعمّ العضو، والثلاث أكمل، ولا يُزاد عليها. وفعل النبي ﷺ للمرة والمرتين بيان للجواز.\n\n'
     '**شرح الحواشي:** (٤) حديث التيامن متفق عليه من حديث عائشة رضي الله عنها. (٥) الوضوء مرة مرة ومرتين مرتين وثلاثًا ثلاثًا في صحيح البخاري، وعند مسلم الثلاث.',
     '**Teyâmün:** Ellerde ve ayaklarda sağdan başlamak. Yüz, baş ve kulaklar ise birlikte yıkanır veya meshedilir.\n\n'
     '**Üçlemek:** Farz, organı kaplayan bir yıkamadır; üç kez daha kâmildir, üçten fazlası yapılmaz. Nebî’nin (sallallâhu aleyhi ve sellem) bir ve iki kez yıkaması caiz olduğunu göstermek içindir.\n\n'
     '**Dipnotların şerhi:** (4) Sağdan başlama hadisi Âişe’den (radıyallâhu anhâ) Buhârî ve Müslim’dedir. (5) Birer, ikişer ve üçer kez abdest Buhârî’nin Sahîh’inde, üçer kez olanı Müslim’dedir.',
     fn=['(٤) متفق عليه: رواه البخاري برقم (١٦٨)، ومسلم برقم (٢٢٦).', '(٥) متفق عليه: رواه البخاري برقم (١٥٧، ١٥٨، ١٥٩) ومسلم برقم (٢٢٦) وعنده ذكر الثلاث فقط.'],
     note=dict(ar='تنبيه على الحاشية (٤): حديث التيامن في «صحيح مسلم» برقم (٢٦٨)؛ أما (٢٢٦) فحديث عثمان في صفة الوضوء.', tr='(4) numaralı dipnot hakkında: Sağdan başlama hadisi Müslim’in Sahîh’inde 268 numaradadır; 226 ise Osman’ın abdesti anlattığı hadistir.')),
  PS('٨ - الذكر الوارد بعد الوضوء: لقوله ﷺ: (ما منكم أحد يتوضأ فيسبغ الوضوء ثم يقول: أشهد أن لا إله إلا الله وحده لا شريك له، وأشهد أن محمداً عبده ورسوله، إلا فتحت له أبواب الجنة الثمانية، يدخل من أيها شاء) (٦).',
     '8. Abdestten sonra gelen zikir: Nebî’nin (sallallâhu aleyhi ve sellem) şu sözü gereği: «Sizden kim abdest alır, abdestini güzelce tamamlar, sonra “Allah’tan başka ilah olmadığına, O’nun tek olduğuna, ortağı bulunmadığına şahitlik ederim; Muhammed’in O’nun kulu ve rasûlü olduğuna şahitlik ederim” derse, cennetin sekiz kapısı ona açılır; dilediğinden girer.» (6)',
     '١/ ٢٠',
     'تأمّل الجمع بين **الطهارتين**: طهارة البدن بالماء، وطهارة القلب بالتوحيد؛ فيختم المسلم وضوءه بكلمة التوحيد، ويسأل الله أن يجعله من التوابين والمتطهرين.\n\n'
     '**ويُسبغ الوضوء:** يتمّه ويعمّ به الأعضاء.\n\n'
     '**شرح الحواشي:** (٦) الحديث في صحيح مسلم، وزاد الترمذي: «اللَّهُمَّ اجْعَلْنِي مِنَ التَّوَّابِينَ، وَاجْعَلْنِي مِنَ الْمُتَطَهِّرِينَ»، وصحّحها الألباني.',
     'İki temizliğin birleşmesine dikkat edin: bedenin su ile, kalbin tevhid ile temizliği. Müslüman abdestini tevhid kelimesiyle bitirir ve Allah’tan kendisini tövbe edenlerden ve temizlenenlerden kılmasını ister.\n\n'
     '**Abdesti güzelce tamamlamak:** organları kaplayarak eksiksiz yapmak.\n\n'
     '**Dipnotların şerhi:** (6) Hadis Müslim’in Sahîh’indedir; Tirmizî şunu ekler: «Allah’ım, beni tövbe edenlerden kıl, temizlenenlerden kıl.» Elbânî bu ilaveyi sahih saymıştır.',
     fn=['(٦) أخرجه مسلم برقم (٢٣٤) وزاد الترمذي: (اللهم اجعلني من التوابين واجعلني من المتطهرين) برقم (٥٥)، وصححه بهذه الزيادة الألباني (الإرواء برقم ٩٦).']),
 ]),
 dict(ar='المسألة السادسة: في نواقضه', tr='Altıncı mesele: Abdesti bozanlar', paras=[
  PS('والنواقض: هي الأشياء التي تبطل الوضوء وتفسده. وهي ستة: ١ - الخارج من السبيلين: أي من مخرج البول والغائط، والخارج: إما أن يكون بولاً أو غائطاً أو منيّاً أو مذيّاً أو دم استحاضة أو ريحاً قليلاً كان أو كثيراً؛ لقوله تعالى: ﴿أَوْ جَاءَ أَحَدٌ مِنْكُمْ مِنَ الْغَائِطِ﴾ [النساء: ٤٣]. وقوله ﷺ: (لا يقبل الله صلاة أحدكم إذا أحدث حتى يتوضأ) وقد تقدَّم. وقوله ﷺ: (ولكن من غائط أو بول ونوم) (١). وقوله ﷺ فيمن شك هل خرج منه ريح أو لا: (فلا ينصرف حتى يسمع صوتاً أو يجد ريحاً) (٢).',
     'Abdesti bozanlar, onu geçersiz kılan ve ifsat eden şeylerdir; altı tanedir: 1. İki yoldan, yani idrar ve dışkı çıkış yerlerinden çıkan: İdrar, dışkı, meni, mezi, istihâza kanı veya yel; az olsun çok olsun. Allah Teâlâ’nın «Ya da biriniz ayak yolundan gelirse» [Nisâ, 43] sözü; Nebî’nin (sallallâhu aleyhi ve sellem) daha önce geçen «Allah, abdesti bozulan birinizin namazını abdest alıncaya kadar kabul etmez» sözü; «Fakat dışkıdan, idrardan ve uykudan (dolayı abdest alınır)» sözü (1) ve yel çıkıp çıkmadığından şüphe eden hakkında «Bir ses işitmedikçe veya bir koku almadıkça (namazdan) ayrılmasın» sözü (2) gereği.',
     '١/ ٢١',
     '**الناقض الأول** يجمع كل ما خرج من المخرجين: المعتاد (البول والغائط والريح)، وغير المعتاد (كدم الاستحاضة)، **قليلًا كان أو كثيرًا**.\n\n'
     '**وحديث الشكّ قاعدة عظيمة:** اليقين لا يزول بالشك. فمن تيقّن الطهارة وشكّ في الحدث، فهو على طهارته حتى يتيقّن، بسماع صوت أو وجود رائحة. وفي هذا علاج للوسوسة.\n\n'
     '**شرح الحواشي:** (١) حديث صفوان بن عسّال رواه أحمد والنسائي والترمذي وصحّحه، وحسّنه الألباني. (٢) حديث الشك متفق عليه.',
     '**Birinci bozan**, iki çıkış yerinden çıkan her şeyi kapsar: alışılmış olanı (idrar, dışkı ve yel) ve alışılmamış olanı (istihâza kanı gibi), **az olsun çok olsun**.\n\n'
     '**Şüphe hadisi büyük bir kaidedir:** Kesinlik şüpheyle kalkmaz. Temizliğinden emin olup hadesten şüphe eden, ses işitmek veya koku almakla kesin bilinceye kadar temizliği üzeredir. Bunda vesveseye bir tedavi vardır.\n\n'
     '**Dipnotların şerhi:** (1) Safvân b. Assâl hadisini Ahmed, Nesâî ve Tirmizî rivayet etmiş; Tirmizî sahih, Elbânî hasen saymıştır. (2) Şüphe hadisi Buhârî ve Müslim’dedir.',
     fn=['(١) رواه أحمد (٤/ ٢٣٩)، والنسائي برقم (١/ ٨٣)، والترمذي برقم (٩٦) وصححه، وحسنه الألباني في الإرواء (١/ ١٤١).', '(٢) متفق عليه: البخاري برقم (١٣٧)، ومسلم برقم (٣٦١).']),
  PS('٢ - خروج النجاسة من بقية البدن: فإن كان بولاً أو غائطاً نقض مطلقاً لدخوله في النصوص السابقة، وإن كان غيرهما كالدم والقيء: فإن فحش وكَثُرَ فالأَولى أن يتوضأ منه؛ عملاً بالأحوط، وإن كان يسيراً فلا يتوضأ منه بالاتفاق.',
     '2. Bedenin diğer yerlerinden necaset çıkması: İdrar veya dışkı ise önceki nasların kapsamına girdiği için her durumda bozar. Kan ve kusmuk gibi başka bir şey ise: Çok ve fahiş olursa ihtiyata uyarak ondan dolayı abdest almak daha iyidir; az olursa ittifakla ondan dolayı abdest alınmaz.',
     '١/ ٢١',
     'فرّق الكتاب بين نوعين: **البول والغائط** إذا خرجا من غير المخرج المعتاد، كمن له فتحة في بطنه، ينقضان مطلقًا. **والدم والقيء:** الكثير الفاحش **الأولى** أن يتوضأ منه احتياطًا، واليسير **لا ينقض بالاتفاق**. فمن جرح إصبعه فخرجت قطرات دم، فوضوؤه باقٍ.',
     'Kitap iki türü ayırmıştır: **İdrar ve dışkı**, karındaki bir açıklıktan çıkması gibi alışılmış yerden başka bir yerden çıksa da her durumda bozar. **Kan ve kusmuk:** Fahiş çokluğundan dolayı ihtiyaten abdest almak **daha iyidir**; azı **ittifakla bozmaz**. Parmağı kesilip birkaç damla kan çıkan kimsenin abdesti bozulmaz.'),
  PS('٣ - زوال العقل أو تغطيته بإغماء أو نوم: لقوله ﷺ: (ولكن من غائط وبول ونوم). وقوله: (العين [[وِكَاءُ|wika]] (٣) [[السَّه|sah]] (٤)، فمن نام فليتوضأ) (٥). وأما الجنون والإغماء والسكر ونحوه فينقض إجماعاً، والنوم الناقض هو المستغرق الذي لا يبقى معه إدراك على أي هيئة كان النوم، أما النوم اليسير فإنه لا ينقض الوضوء، لأن الصحابة ﵃ كان يصيبهم النعاس وهم في انتظار الصلاة، ويقومون، يُصَلُّون، ولا يتوضؤون (٦).',
     '3. Aklın gitmesi veya bayılma ya da uykuyla örtülmesi: Nebî’nin (sallallâhu aleyhi ve sellem) «Fakat dışkıdan, idrardan ve uykudan» sözü ve «Göz, makadın bağıdır (3) (4); kim uyursa abdest alsın» sözü (5) gereği. Delilik, bayılma, sarhoşluk ve benzerleri icmâ ile abdesti bozar. Bozan uyku, hangi şekilde olursa olsun, farkındalığın kalmadığı derin uykudur. Hafif uyku ise abdesti bozmaz; çünkü sahâbe (radıyallâhu anhüm) namazı beklerken uyuklar, kalkıp namaz kılar ve abdest almazlardı. (6)',
     '١/ ٢١',
     '**العلّة:** النوم مظنّة الحدث، لأن النائم لا يشعر بما يخرج منه. ولهذا شبّه الحديث العينين **بالوِكاء**، أي الرباط: ما دام مستيقظًا فهو يحسّ بنفسه، فإذا نام انحلّ الرباط.\n\n'
     '**والضابط** في النوم الناقض: **ذهاب الإدراك**، لا هيئة النائم. فالنعاس اليسير الذي يسمع معه من حوله لا ينقض، كما في فعل الصحابة.\n\n'
     '**شرح الحواشي:** (٣) **الوكاء** الخيط الذي تُربط به القربة. (٤) **السَّه** الدبر. (٥) الحديث رواه أبو داود وابن ماجه، وحسّنه الألباني. (٦) نعاس الصحابة في صحيح مسلم.',
     '**Gerekçe:** Uyku, hadesin muhtemel olduğu bir hâldir; çünkü uyuyan kendisinden çıkanı hissetmez. Bu yüzden hadis gözleri **vikâya**, yani bağa benzetmiştir: Uyanık olduğu sürece kendini hisseder; uyuyunca bağ çözülür.\n\n'
     '**Ölçü:** Bozan uykuda ölçü, uyuyanın şekli değil, **farkındalığın gitmesidir**. Etrafındakileri işittiği hafif uyuklama, sahâbenin fiilinde olduğu gibi bozmaz.\n\n'
     '**Dipnotların şerhi:** (3) **Vikâ**, kırbanın bağlandığı iptir. (4) **Seh**, makattır. (5) Hadisi Ebû Dâvûd ve İbn Mâce rivayet etmiş, Elbânî hasen saymıştır. (6) Sahâbenin uyuklaması Müslim’in Sahîh’indedir.',
     fn=['(٣) الخيط الذي يربط به الخريطة والقربة.', '(٤) الدبر. والمعنى: أن العينين في يقظتهما بمنزلة الحبل الذي يربط به، فزوال اليقظة كزوال هذا الرباط.', '(٥) رواه أبو داود برقم (٢٠٣)، وابن ماجه برقم (٤٧٧)، وحسنه الألباني في الإرواء (١/ ١٤٨).', '(٦) صحيح مسلم برقم (٣٧٦).']),
  PS('٤ - مس فرج الآدمي بلا حائل: لحديث بسرة بنت صفوان ﵂ أن النبي ﷺ قال: (من مسّ ذكره فليتوضأ) (١). وفي حديث أبي أيوب وأم حبيبة: (من مسّ فرجه فليتوضأ) (٢).',
     '4. İnsanın avret yerine engelsiz dokunmak: Büsre bint Safvân’ın (radıyallâhu anhâ) hadisi gereği; Nebî (sallallâhu aleyhi ve sellem) «Kim tenasül organına dokunursa abdest alsın» buyurmuştur. (1) Ebû Eyyûb ve Ümmü Habîbe’nin hadisinde: «Kim avret yerine dokunursa abdest alsın.» (2)',
     '١/ ٢٢',
     'قيدان في هذا الناقض: **بلا حائل**، فمن مسّ من وراء الثوب لم ينتقض وضوؤه؛ و**الفرج**، أي القُبُل أو الدُّبُر. وقوله «فرج الآدمي» يشمل فرجه وفرج غيره، كالأم تغسّل طفلها.\n\n'
     '**شرح الحواشي:** (١) حديث بسرة رواه أبو داود والنسائي والترمذي وقال: حسن صحيح، وصحّحه الألباني. (٢) رواية أم حبيبة عند ابن ماجه وصحّحها الألباني، وحديث أبي أيوب لم يقف الألباني على إسناده.',
     'Bu bozanda iki kayıt vardır: **engelsiz**; elbisenin üstünden dokunanın abdesti bozulmaz; ve **avret yeri**, yani ön veya arka. «İnsanın avret yeri» ifadesi, çocuğunu yıkayan anne gibi kendisinin ve başkasının avret yerini kapsar.\n\n'
     '**Dipnotların şerhi:** (1) Büsre hadisini Ebû Dâvûd, Nesâî ve Tirmizî rivayet etmiş; Tirmizî «hasen sahih» demiş, Elbânî sahih saymıştır. (2) Ümmü Habîbe rivayeti İbn Mâce’dedir, Elbânî sahih saymıştır; Ebû Eyyûb hadisinin isnadını Elbânî bulamamıştır.',
     fn=['(١) أخرجه أبو داود برقم (١٨١) واللفظ له، والنسائي برقم (١٦٣)، والترمذي برقم (٨٢) وقال: حديث حسن صحيح، وابن ماجه برقم (٤٤٧٩)، وصححه الألباني في الإرواء (١/ ١٥٠).', '(٢) رواية أم حبيبة أخرجها: ابن ماجه برقم (٤٨١)، وصححها الألباني في الإرواء (١/ ١٥١)، أما حديث أبي أيوب فقال الألباني: "لم أقف على إسناده" الإرواء (١/ ١٥١).'],
     note=dict(ar='تنبيه على الحاشية (١): حديث بسرة في «سنن ابن ماجه» برقم (٤٧٩).', tr='(1) numaralı dipnot hakkında: Büsre hadisi İbn Mâce’nin Sünen’inde 479 numaradadır.')),
  PS('٥ - أكل لحم الإبل: لحديث جابر بن سمرة أن رجلاً سأل النبي ﷺ: أنتوضأ من لحوم الغنم؟ قال: (إن شئت توضأ وإن شئت لا تتوضأ)، قال: أنتوضأ من لحوم الإبل؟ قال: (نعم توضأ من لحوم الإبل). (٣) ٦ - الردة عن الإسلام: لقوله تعالى: ﴿وَمَنْ يَكْفُرْ بِالْإِيمَانِ فَقَدْ حَبِطَ عَمَلُهُ﴾ [المائدة: ٥]. وكل ما أوجب الغسل أوجب الوضوء غير الموت.',
     '5. Deve eti yemek: Câbir b. Semüre’nin hadisi gereği; bir adam Nebî’ye (sallallâhu aleyhi ve sellem) sordu: «Koyun etinden dolayı abdest alalım mı?» «İstersen al, istersen alma» buyurdu. «Deve etinden dolayı abdest alalım mı?» dedi. «Evet, deve etinden dolayı abdest al» buyurdu. (3) 6. İslam’dan dönmek: Allah Teâlâ’nın «Kim imanı inkâr ederse ameli boşa gitmiştir» [Mâide, 5] sözü gereği. Guslü gerektiren her şey, ölüm hariç, abdesti de gerektirir.',
     '١/ ٢٢',
     '**لحم الإبل:** الحديث فرّق بين الغنم والإبل؛ فخيّر في الغنم، وأمر في الإبل، فدلّ على أن لحم الإبل ناقض. ونحن نتّبع النص، علمنا الحكمة أو لم نعلمها.\n\n'
     '**الردة** تحبط العمل، ومنه الطهارة؛ فمن ارتدّ ثم رجع إلى الإسلام توضأ.\n\n'
     '**«وكل ما أوجب الغسل أوجب الوضوء»:** أي ما أوجب الغسل كالجنابة فهو ناقض للوضوء أيضًا، فلا يصلي حتى يتطهّر. واستُثني الموت.\n\n'
     '**شرح الحواشي:** (٣) الحديث في صحيح مسلم.',
     '**Deve eti:** Hadis koyun ile deveyi ayırmıştır: Koyunda serbest bırakmış, devede emretmiştir; bu, deve etinin abdesti bozduğunu gösterir. Hikmetini bilelim veya bilmeyelim, nassa uyarız.\n\n'
     '**İslam’dan dönmek** ameli boşa çıkarır; taharet de buna dahildir. Dönüp sonra İslam’a giren abdest alır.\n\n'
     '**«Guslü gerektiren her şey abdesti de gerektirir»:** Cünüplük gibi guslü gerektiren şey abdesti de bozar; temizlenmeden namaz kılınmaz. Ölüm bundan hariç tutulmuştur.\n\n'
     '**Dipnotların şerhi:** (3) Hadis Müslim’in Sahîh’indedir.',
     fn=['(٣) رواه مسلم برقم (٣٦٠).']),
 ]),
 dict(ar='المسألة السابعة: ما يجب له الوضوء', tr='Yedinci mesele: Abdestin farz olduğu durumlar', paras=[
  PS('ويجب على المكلف فعل الوضوء للأمور الآتية: ١ - الصلاة: لحديث ابن عمر مرفوعاً: (لا يقبل الله صلاة بغير طُهُور، ولا صدقة من غلول) (٤). ٢ - الطواف بالبيت الحرام فرضاً كان أو نفلاً: لفعله ﷺ (فإنه توضأ ثم طاف بالبيت) (٥)، ولقوله ﷺ: (الطواف بالبيت صلاة إلا أن الله أباح فيه الكلام) (٦)، ولمنعه الحائض من الطواف حتى تطهر (٧).',
     'Mükellefin şunlar için abdest alması farzdır: 1. Namaz: İbn Ömer’in merfû hadisi gereği: «Allah temizlik olmadan namazı, haksız alınan maldan da sadakayı kabul etmez.» (4) 2. Kâbe’yi tavaf, farz olsun nafile olsun: Nebî’nin (sallallâhu aleyhi ve sellem) fiili gereği, «abdest alıp Kâbe’yi tavaf etmiştir» (5); «Kâbe’yi tavaf namazdır; ancak Allah onda konuşmayı mubah kılmıştır» sözü (6) ve hayızlı kadını temizlenene kadar tavaftan alıkoyması (7) gereği.',
     '١/ ٢٢',
     '**الطواف صلاة** في الحكم، إلا أن الكلام فيه مباح؛ فيُشترط له ما يُشترط للصلاة من الطهارة. وفي منع الحائض من الطواف دليل على أن الطهارة شرط له.\n\n'
     '**شرح الحواشي:** (٤) حديث ابن عمر في صحيح مسلم. (٥) وضوؤه ثم طوافه في الصحيحين. (٦) حديث «الطواف بالبيت صلاة» رواه ابن حبان والحاكم والبيهقي، وصحّحه الألباني. (٧) منع الحائض من الطواف في الصحيحين من حديث عائشة رضي الله عنها.',
     '**Tavaf** hüküm bakımından **namazdır**; ancak onda konuşmak mubahtır. Bu yüzden namaz için şart olan taharet onun için de şarttır. Hayızlı kadının tavaftan alıkonulması, taharetin tavafın şartı olduğuna delildir.\n\n'
     '**Dipnotların şerhi:** (4) İbn Ömer hadisi Müslim’in Sahîh’indedir. (5) Abdest alıp tavaf etmesi Buhârî ve Müslim’dedir. (6) «Kâbe’yi tavaf namazdır» hadisini İbn Hibbân, Hâkim ve Beyhakî rivayet etmiş, Elbânî sahih saymıştır. (7) Hayızlının tavaftan alıkonulması Âişe’den (radıyallâhu anhâ) Buhârî ve Müslim’dedir.',
     fn=['(٤) رواه مسلم برقم (٢٢٤)، والترمذي برقم (١).', '(٥) رواه البخاري برقم (١٦١٤)، ومسلم برقم (١٢٣٥).', '(٦) رواه ابن حبان برقم (٣٨٣٦)، والحاكم (١/ ٤٥٩) وصحح إسناده، ووافقه الذهبي، والبيهقي (٥/ ٨٧) وغيرهم، وصححه الألباني (الإرواء برقم ١٢١).', '(٧) رواه البخاري برقم (٣٠٥)، ومسلم برقم (١٢١١).']),
  PS('٣ - مس المصحف ببشرته بلا حائل: لقوله تعالى: ﴿لَا يَمَسُّهُ إِلَّا الْمُطَهَّرُونَ﴾ [الواقعة: ٧٩]. ولقوله ﷺ: (لا يمس القرآن إلا طاهر) (١).',
     '3. Mushafa cildiyle engelsiz dokunmak: Allah Teâlâ’nın «Ona tertemiz olanlardan başkası dokunamaz» [Vâkıa, 79] sözü ve Nebî’nin (sallallâhu aleyhi ve sellem) «Kur’ân’a ancak temiz olan dokunur» sözü (1) gereği.',
     '١/ ٢٣',
     'فرّق بين أمرين: **قراءة القرآن من الحفظ**، فلا يجب لها الوضوء بل يُستحب؛ و**مسّ المصحف** بالبشرة بلا حائل، فيجب له الوضوء. فمن أراد أن يقرأ من المصحف وهو محدث، أمسكه بحائل.\n\n'
     '**شرح الحواشي:** (١) الحديث أخرجه مالك والدارقطني والبيهقي والحاكم، وصحّحه الألباني.',
     'İki şeyi ayırın: **Ezberden Kur’ân okumak** için abdest farz değil, müstehaptır; **Mushafa** cildiyle engelsiz **dokunmak** için ise abdest farzdır. Abdestsiz olarak Mushaftan okumak isteyen, onu bir engelle tutar.\n\n'
     '**Dipnotların şerhi:** (1) Hadisi Mâlik, Dârekutnî, Beyhakî ve Hâkim rivayet etmiş; Elbânî sahih saymıştır.',
     fn=['(١) أخرجه مالك (١/ ١٩٩)، والدارقطني (١/ ١٢١)، والبيهقي (١/ ٨٧)، والحاكم (١/ ٣٩٥) وصححه، وصححه الألباني (الإرواء برقم ١٢٢).']),
 ]),
 dict(ar='المسألة الثامنة: ما يستحب له الوضوء', tr='Sekizinci mesele: Abdestin müstehap olduğu durumlar', paras=[
  PS('يستحب الوضوء ويندب في الأحوال التالية: ١ - عند ذكر الله تعالى وقراءة القرآن. ٢ - عند كل صلاة: لمواظبته ﷺ على ذلك، كما في حديث أنس ﵁ قال: (كان النبي ﷺ يتوضأ عند كل صلاة) (٢).',
     'Abdest şu durumlarda müstehap ve mendubtur: 1. Allah Teâlâ’yı zikrederken ve Kur’ân okurken. 2. Her namaz için: Nebî’nin (sallallâhu aleyhi ve sellem) buna devam etmesi gereği; Enes’in (radıyallâhu anh) hadisinde: «Nebî (sallallâhu aleyhi ve sellem) her namazda abdest alırdı.» (2)',
     '١/ ٢٣',
     '**الوضوء على الوضوء:** من كان على طهارة يُستحب له أن يجدّد الوضوء لكل صلاة، اقتداءً بالنبي ﷺ؛ ولا يجب.\n\n'
     '**شرح الحواشي:** (٢) حديث أنس في صحيح البخاري.',
     '**Abdest üstüne abdest:** Abdestli olanın her namaz için abdestini yenilemesi, Nebî’ye (sallallâhu aleyhi ve sellem) uyarak müstehaptır; farz değildir.\n\n'
     '**Dipnotların şerhi:** (2) Enes hadisi Buhârî’nin Sahîh’indedir.',
     fn=['(٢) أخرجه البخاري برقم (٢١٤).']),
  PS('٣ - يستحب الوضوء للجنب إذا أراد أن يعود للجماع، أو أراد النوم أو الأكل أو الشرب: لحديث أبي سعيد الخدري ﵁ أن رسول الله ﷺ قال: (إذا أتى أحدكم أهله، ثم أراد أن يعود، فليتوضأ) (٣). ولحديث عائشة ﵂: (أن رسول الله ﷺ كان إذا أراد أن ينام وهو جنب، توضأ وضوءه للصلاة، قبل أن ينام) (٤). وفي رواية لها: (فأراد أن يأكل أو ينام) (٥).',
     '3. Cünüp kimsenin tekrar birleşmek, uyumak, yemek veya içmek istediğinde abdest alması müstehaptır: Ebû Saîd el-Hudrî’nin (radıyallâhu anh) hadisi gereği; Rasûlullah (sallallâhu aleyhi ve sellem) «Biriniz hanımına yaklaşır, sonra tekrar etmek isterse abdest alsın» buyurmuştur. (3) Âişe’nin (radıyallâhu anhâ) hadisi gereği: «Rasûlullah (sallallâhu aleyhi ve sellem) cünüp iken uyumak istediğinde, uyumadan önce namaz abdesti gibi abdest alırdı.» (4) Onun başka bir rivayetinde: «…yemek veya uyumak istediğinde.» (5)',
     '١/ ٢٣',
     'الجنب إذا أخّر الغسل، فالوضوء **يخفّف الجنابة**، وقد يُنشّطه على الغسل فلا يؤخّره. والغسل أفضل.\n\n'
     '**شرح الحواشي:** (٣) حديث أبي سعيد في صحيح مسلم. (٤) حديث عائشة في صحيح مسلم. (٥) والرواية الأخرى بعده في صحيح مسلم.',
     'Cünüp kimse guslü geciktirirse, abdest **cünüplüğü hafifletir** ve onu gusle teşvik edebilir; böylece geciktirmez. Gusül ise daha faziletlidir.\n\n'
     '**Dipnotların şerhi:** (3) Ebû Saîd hadisi Müslim’in Sahîh’indedir. (4) Âişe hadisi Müslim’in Sahîh’indedir. (5) Diğer rivayet de ondan sonra Müslim’dedir.',
     fn=['(٣) أخرجه مسلم برقم (٣٠٨).', '(٤) أخرجه مسلم برقم (٣٠٥).', '(٥) انظر المصدر السابق، الحديث الذي يليه.']),
  PS('٤ - الوضوء قبل الغسل: لحديث عائشة ﵂ قالت: (كان رسول الله ﷺ إذا اغتسل من الجنابة يبدأ، فيغسل يديه، ثم يفرغ بيمينه على شماله، فيغسل فرجه، ثم يتوضأ وضوءه للصلاة ... ) الحديث (٦). ٥ - عند النوم: لحديث البراء بن عازب ﵁ قال: قال النبي ﷺ: (إذا أتيت مضجعك فتوضَّأ وضوءك للصلاة، ثم اضطجع على شقك الأيمن ... ) الحديث (٧).',
     '4. Gusülden önce abdest: Âişe’nin (radıyallâhu anhâ) hadisi gereği: «Rasûlullah (sallallâhu aleyhi ve sellem) cünüplükten yıkanacağı zaman önce ellerini yıkar, sonra sağ eliyle sol eline su döküp avret yerini yıkar, sonra namaz abdesti gibi abdest alırdı…» (6) 5. Uyurken: Berâ b. Âzib’in (radıyallâhu anh) hadisi gereği; Nebî (sallallâhu aleyhi ve sellem) şöyle buyurdu: «Yatağına gideceğin zaman namaz abdesti gibi abdest al, sonra sağ yanına uzan…» (7)',
     '١/ ٢٣',
     '**الوضوء قبل الغسل** من سنن الغسل، وسيأتي في باب الغسل.\n\n'
     '**والوضوء عند النوم:** أن ينام المسلم على طهارة وذكر، على شقّه الأيمن.\n\n'
     '**خلاصة الباب:** الوضوء واجب لثلاثة: الصلاة، والطواف، ومسّ المصحف؛ ومستحب لغيرها.\n\n'
     '**شرح الحواشي:** (٦) حديث صفة الغسل في صحيح مسلم. (٧) حديث البراء في صحيح البخاري.',
     '**Gusülden önce abdest** guslün sünnetlerindendir; gusül bölümünde gelecek.\n\n'
     '**Uyurken abdest:** Müslümanın sağ yanı üzere, temiz ve zikir hâlinde uyuması.\n\n'
     '**Bölümün özeti:** Abdest üç şey için farzdır: namaz, tavaf ve Mushafa dokunmak; diğerleri için müstehaptır.\n\n'
     '**Dipnotların şerhi:** (6) Gusül tarifi hadisi Müslim’in Sahîh’indedir. (7) Berâ hadisi Buhârî’nin Sahîh’indedir.',
     fn=['(٦) أخرجه مسلم برقم (٣١٦).', '(٧) أخرجه البخاري برقم (٢٤٧).']),
 ]),
]

# ------------------------------------------------------------------ 106: المسح على الخفين والعمامة والجبيرة
GLOSS.update({
 'khuff': dict(w='الخُفّ', ar='ما يُلبس على الرِّجل من جلد ونحوه، وجمعه: خِفاف. ويلحق به كل ما يُلبس على الرجلين من صوف ونحوه.', tr='Ayağa giyilen deri ve benzeri şey; çoğulu «hıfâf». Yünden ve benzerinden ayağa giyilen her şey de onun hükmündedir.', src='الكتاب نفسه (١/ ٢٤)'),
 'jawrab': dict(w='الجوارب', ar='ما يُلبس على الرِّجل من غير الجلد، كالخِرَق ونحوها، وهو ما يُسمّى الآن بالشُّرّاب.', tr='Ayağa giyilen, deriden olmayan bez ve benzeri şeyler; bugün çorap dediğimiz şey.', src='الكتاب نفسه (١/ ٢٤)'),
 'jabira': dict(w='الجبيرة', ar='أعواد ونحوها كالجبس، مما يُربط على الكسر ليُجبر ويلتئم.', tr='Kırık kaynayıp iyileşsin diye üzerine bağlanan tahta parçaları ve alçı gibi şeyler.', src='الكتاب نفسه (١/ ٢٧)'),
 'imama': dict(w='العمامة', ar='ما يُعمَّم به الرأس، ويُكوَّر عليه.', tr='Başa sarılan ve üzerine dolanan şey (sarık).', src='الكتاب نفسه (١/ ٢٧)'),
 'khimar': dict(w='الخمار', ar='خمار المرأة: ما تغطي به رأسها.', tr='Kadının başını örttüğü şey (başörtüsü).', src='الكتاب نفسه (١/ ٢٧)'),
})
GLOSS_TR_SRC.update({
 'الكتاب نفسه (١/ ٢٤)': 'Kitabın kendisi (1/ 24)',
 'الكتاب نفسه (١/ ٢٧)': 'Kitabın kendisi (1/ 27)',
})

SHARH[106] = [
 dict(ar='الباب السادس: في المسح على الخفين والعمامة والجبيرة', tr='Altıncı bölüm: Mestler, sarık ve sargı üzerine mesh', paras=[
  PS('[[الخُفُّ|khuff]]: هو ما يلبس على الرِّجْلِ من جلد ونحوه، وجمعه: خِفاف. ويلحق بالخفين كل ما يلبس على الرجلين من صوف ونحوه.',
     'Mest (huff): Ayağa giyilen deri ve benzeri şeydir; çoğulu «hıfâf»tır. Yünden ve benzerinden ayağa giyilen her şey de mestlere katılır.',
     '١/ ٢٤',
     'تعلّمنا في الباب السابق أن غسل الرجلين إلى الكعبين من فروض الوضوء. وهذا الباب **رخصة** في هذا الفرض: من لبس خفّين بشروطه مسح عليهما بدل الغسل.\n\n'
     'والتعريف يبيّن أن العبرة **بما يُلبس على الرجل** ويسترها، لا بنوع المادة؛ فالجلد أصل الخف، ويلحق به الصوف ونحوه.',
     'Önceki bölümde ayakları topuklara kadar yıkamanın abdestin farzlarından olduğunu öğrendik. Bu bölüm o farzda bir **ruhsattır**: Şartlarına uygun mest giyen, yıkamak yerine onların üzerine mesheder.\n\n'
     'Tanım gösteriyor ki önemli olan malzemenin türü değil, **ayağa giyilip onu örtmesidir**; mestin aslı deridir, yün ve benzeri de ona katılır.'),
 ]),
 dict(ar='المسألة الأولى: حكم المسح على الخفين ودليله', tr='Birinci mesele: Mestler üzerine meshin hükmü ve delili', paras=[
  PS('المسح على الخفين جائز باتفاق أهل السنة والجماعة. وهو رخصة من الله ﷿ تخفيفاً منه على عباده ودفعاً للحرج والمشقة عنهم. وقد دل على جوازه السنة والإجماع.',
     'Mestler üzerine mesh Ehl-i Sünnet vel-Cemâat’in ittifakıyla caizdir. Allah Azze ve Celle’den kullarına bir kolaylık ve onlardan sıkıntı ile meşakkati kaldırmak için bir ruhsattır. Caiz olduğuna Sünnet ve icmâ delildir.',
     '١/ ٢٤',
     '**الرخصة:** ما شرعه الله تخفيفًا على عباده عند وجود سببها. وفي ذكر «أهل السنة والجماعة» إشارة إلى أن إنكار المسح صار من علامات أهل البدع، فذكره العلماء في كتب العقيدة.',
     '**Ruhsat:** Allah’ın, sebebi bulunduğunda kullarına kolaylık olarak meşru kıldığı şeydir. «Ehl-i Sünnet vel-Cemâat» denmesi, meshi inkâr etmenin bidat ehlinin alametlerinden olduğuna işarettir; bu yüzden âlimler onu akide kitaplarında da zikretmiştir.'),
  PS('أما السنة: فقد تواترت الأحاديث الصحيحة على ثبوته عن النبي ﷺ من فعله وأمره بذلك وترخيصه فيه. قال الإمام أحمد ﵀: ليس في قلبي من المسح شيء، فيه أربعون حديثاً عن النبي ﷺ. والمراد بقوله: ليس في قلبي أدنى شك في جوازه. وقال الحسن البصري: حدثني سبعون من أصحاب رسول الله ﷺ أنه مسح على الخفين.',
     'Sünnete gelince: Nebî’den (sallallâhu aleyhi ve sellem) meshin sabit olduğuna dair sahih hadisler tevâtür derecesindedir: kendisinin yapması, bunu emretmesi ve buna izin vermesiyle. İmam Ahmed (rahimehullah) şöyle der: «Mesh konusunda kalbimde hiçbir şey yok; bu konuda Nebî’den kırk hadis vardır.» Yani: Caiz olduğunda kalbimde en küçük bir şüphe yok. Hasan el-Basrî de: «Rasûlullah’ın ashabından yetmiş kişi bana onun mestler üzerine meshettiğini anlattı» demiştir.',
     '١/ ٢٤',
     '**المتواتر:** ما رواه جمع كثير يستحيل في العادة اتفاقهم على الكذب. وفي النص ثلاثة طرق للسنة: **فعله** ﷺ، و**أمره**، و**ترخيصه**.\n\n'
     'وقول الإمام أحمد وقول الحسن البصري يبيّنان كثرة الأحاديث والرواة، فلا مجال للشك في هذه الرخصة.',
     '**Mütevâtir:** Yalan üzerinde birleşmeleri âdeten imkânsız olan büyük bir topluluğun rivayet ettiği haberdir. Metinde sünnetin üç yolu vardır: Nebî’nin (s.a.v.) **fiili**, **emri** ve **izni**.\n\n'
     'İmam Ahmed’in ve Hasan el-Basrî’nin sözleri hadislerin ve râvilerin çokluğunu gösterir; bu ruhsatta şüpheye yer yoktur.'),
  PS('ومن هذه الأحاديث: حديث جرير بن عبد الله قال: (رأيت رسول الله ﷺ بال ثم توضأ ومسح على خفيه) (١). قال الأعمش عن إبراهيم: كان يعجبهم هذا الحديث؛ لأن إسلام جرير كان بعد نزول المائدة -يعني آية الوضوء-.',
     'Bu hadislerden biri Cerîr b. Abdullah’ın hadisidir: «Rasûlullah’ı (sallallâhu aleyhi ve sellem) küçük abdestini yapıp sonra abdest alırken ve mestleri üzerine meshederken gördüm.» (1) A’meş, İbrâhîm’den şöyle nakleder: Bu hadis onların hoşuna giderdi; çünkü Cerîr, Mâide sûresi, yani abdest âyeti indikten sonra Müslüman olmuştu.',
     '١/ ٢٤',
     'قد يقول قائل: آية الوضوء أمرت بغسل الرجلين، فلعل المسح كان قبلها ثم نُسخ. فجاء حديث جرير جوابًا: جرير **أسلم بعد نزول الآية**، ورأى النبي ﷺ يمسح؛ فالمسح **باقٍ غير منسوخ**، والآية في من لم يلبس الخفين.\n\n'
     '**شرح الحواشي:** (١) حديث جرير في صحيح مسلم، وفي البخاري نحوه من حديث المغيرة رضي الله عنه.',
     'Biri şöyle diyebilir: Abdest âyeti ayakları yıkamayı emretti; belki mesh ondan önceydi ve neshedildi. Cerîr’in hadisi buna cevaptır: Cerîr **âyet indikten sonra Müslüman olmuş** ve Nebî’yi (s.a.v.) meshederken görmüştür. Demek ki mesh **neshedilmemiştir**; âyet mest giymeyen içindir.\n\n'
     '**Dipnotların şerhi:** (1) Cerîr hadisi Müslim’in Sahîh’indedir; Buhârî’de de Muğîre’den (radıyallâhu anh) benzeri vardır.',
     fn=['(١) رواه مسلم برقم (٢٧٢)، وروى نحوه البخاري عن المغيرة في باب المسح على الخفين برقم (٢٠٣).']),
  PS('وقد أجمع العلماء من أهل السنة والجماعة على مشروعيته في السفر والحضر لحاجة أو غيرها.',
     'Ehl-i Sünnet vel-Cemâat âlimleri, meshin yolculukta da yolculuk dışında da, ihtiyaç olsun olmasın meşru olduğunda icmâ etmişlerdir.',
     '١/ ٢٤',
     'فلا يُشترط للمسح أن يكون الإنسان مسافرًا، ولا أن يكون في برد أو مشقة؛ بل يجوز للمقيم في بيته إذا لبس الخفين بشروطه.',
     'Dolayısıyla mesh için kişinin yolcu olması, soğukta veya zorlukta bulunması şart değildir; şartlarına uygun mest giyen, evinde mukim olan kimse de meshedebilir.'),
  PS('وكذلك يجوز المسح على [[الجوارب|jawrab]]، وهي ما يلبس على الرجْل من غير الجلد كالخِرَق ونحوها، وهو ما يسمى الآن بالشُّرَّاب؛ لأنهما كالخف في حاجة الرجل إليهما، والعلة فيهما واحدة، وقد انتشر لبسها أكثر من الخف، فيجوز المسح عليها إذا كانت ساترة.',
     'Aynı şekilde çoraplar üzerine mesh de caizdir. Çorap, ayağa giyilen ve deriden olmayan, bez ve benzerinden yapılan şeydir; bugün «çorap» denilen şeydir. Çünkü ayağın onlara ihtiyacı mest gibidir, sebep ikisinde de aynıdır ve çorap giymek mestten daha yaygın olmuştur. Bu yüzden ayağı örtüyorsa üzerine meshetmek caizdir.',
     '١/ ٢٤',
     'هذا من **القياس**: الجورب يأخذ حكم الخف، لأن **العلة واحدة**، وهي حاجة الرجل إلى ما يُلبس عليها ويشقّ نزعه عند كل وضوء.\n\n'
     'وقيّد الكتاب الجواز بقوله: **«إذا كانت ساترة»**؛ وهو الشرط الثاني الآتي: ستر محل الفرض.',
     'Bu bir **kıyastır**: Çorap mestin hükmünü alır; çünkü **sebep aynıdır**: Ayağın, üzerine giyilen ve her abdestte çıkarılması zor olan şeye ihtiyacı.\n\n'
     'Kitap caizliği **«ayağı örtüyorsa»** kaydıyla sınırlamıştır; bu, birazdan gelecek ikinci şarttır: farz yerini örtmek.'),
 ]),
 dict(ar='المسألة الثانية: شروط المسح على الخفين، وما يقوم مقامهما', tr='İkinci mesele: Mestler ve onların yerini tutanlar üzerine meshin şartları', paras=[
  PS('وهذه الشروط هي: ١ - لبسهما على طهارة: لما روى المغيرة قال: كنت مع النبي ﷺ في سفر فأهويت لأنزع خفيه فقال: (دعهما فإني أدخلتهما طاهرتين، فمسح عليهما) (١).',
     'Bu şartlar şunlardır: 1. Onları abdestli olarak giymek: Muğîre’nin rivayeti gereği: Bir yolculukta Nebî (sallallâhu aleyhi ve sellem) ile birlikteydim; mestlerini çıkarmak için elimi uzattım. «Bırak onları; çünkü ben onları temizken giydim» buyurdu ve üzerlerine meshetti. (1)',
     '١/ ٢٥',
     '**«أهويت»:** مددت يدي. **«أدخلتهما طاهرتين»:** أي أدخلت رجليّ فيهما وهما طاهرتان، بعد وضوء كامل.\n\n'
     'وجه الدلالة: أن النبي ﷺ علّل جواز المسح بأنه لبسهما على طهارة؛ فمن لبسهما محدثًا لم يمسح.\n\n'
     '**شرح الحواشي:** (١) الحديث متفق عليه.',
     '**«Elimi uzattım»:** Arapçası «ehveytü». **«Onları temizken giydim»:** yani ayaklarım temizken, tam bir abdestten sonra onlara soktum.\n\n'
     'Delil yönü: Nebî (s.a.v.) meshin caizliğini mestleri abdestli giymesine bağlamıştır; abdestsizken giyen meshedemez.\n\n'
     '**Dipnotların şerhi:** (1) Hadis Buhârî ve Müslim’dedir.',
     fn=['(١) متفق عليه: أخرجه البخاري برقم (٢٠٦)، ومسلم برقم (٢٧٤).']),
  PS('٢ - سترهما لمحل الفرض: أي: المفروض غسله من الرجل، فلو ظهر من محل الفرض شيء، لم يصح المسح. ٣ - إباحتهما: فلا يجوز المسح على المغصوب، والمسروق، ولا الحرير لرجل؛ لأن لبسه معصية، فلا تستباح به الرخصة. ٤ - طهارة عينهما: فلا يصح المسح على النجس، كالمتخذ من جلد حمار.',
     '2. Farz yerini örtmeleri: Yani ayağın yıkanması farz olan kısmını; farz yerinden bir şey açıkta kalırsa mesh sahih olmaz. 3. Mubah olmaları: Gasp edilmiş ve çalınmış mest üzerine, erkek için ipek üzerine mesh caiz değildir; çünkü onu giymek günahtır, günahla ruhsattan faydalanılmaz. 4. Kendilerinin temiz olması: Necis olan, eşek derisinden yapılmış mest gibi, üzerine mesh sahih olmaz.',
     '١/ ٢٥',
     '**محل الفرض:** القدم إلى الكعبين، كما في آية الوضوء. فالخف القصير الذي لا يغطي الكعبين لا يُمسح عليه.\n\n'
     '**«لا تُستباح الرخصة بالمعصية»:** الرخصة نعمة وتخفيف، فلا تُنال بشيء حرّمه الله.\n\n'
     '**طهارة العين:** جلد الحمار نجس لأنه لا تحلّه الذكاة، كما تقدّم في باب الآنية.',
     '**Farz yeri:** Abdest âyetinde olduğu gibi topuklara kadar ayak. Topukları örtmeyen kısa mest üzerine meshedilmez.\n\n'
     '**«Günahla ruhsattan faydalanılmaz»:** Ruhsat bir nimet ve kolaylıktır; Allah’ın haram kıldığı bir şeyle elde edilmez.\n\n'
     '**Kendisinin temiz olması:** Eşek derisi necistir, çünkü kesmek onu helâl kılmaz; Kaplar bölümünde geçtiği gibi.'),
  PS('٥ - أن يكون المسح في المدة المحددة شرعاً: وهي للمقيم يوم وليلة، وللمسافر ثلاثة أيام بلياليهن. هذه شروط خمسة استنبطها أهل العلم لصحة المسح على الخفين من النصوص النبوية والقواعد العامة، لابد من مراعاتها عند إرادة المسح.',
     '5. Meshin şer’an belirlenen süre içinde olması: Bu süre mukim için bir gün bir gece, yolcu için üç gün üç gecedir. Bunlar, âlimlerin mestler üzerine meshin sahih olması için Nebî’nin sözlerinden ve genel kaidelerden çıkardıkları beş şarttır; meshetmek isteyen bunlara mutlaka dikkat etmelidir.',
     '١/ ٢٥',
     'الشروط الخمسة يحفظها الطالب: **طهارة اللبس، والستر، والإباحة، وطهارة العين، والمدة**. وسيأتي تفصيل المدة في المسألة الرابعة.',
     'Öğrencinin ezberleyeceği beş şart: **abdestli giymek, örtmek, mubah olmak, kendisinin temiz olması ve süre**. Sürenin ayrıntısı dördüncü meselede gelecek.'),
 ]),
 dict(ar='المسألة الثالثة: كيفية المسح وصفته', tr='Üçüncü mesele: Meshin keyfiyeti ve şekli', paras=[
  PS('المحل المشروع مسحه ظاهر الخف، والواجب في ذلك ما يطلق عليه اسم المسح. وكيفية المسح: أن يمسح أكثر أعلى الخف؛ لحديث المغيرة بن شعبة الذي بيَّن فيه وصف مسح رسول الله ﷺ على خفه في الوضوء، فقال: (رأيت النبي ﷺ يمسح على الخفين: على ظاهرهما) (٢).',
     'Meshedilmesi meşru olan yer mestin üstüdür; farz olan, «mesh» adının verilebileceği kadarıdır. Meshin şekli: Mestin üstünün çoğunu meshetmektir. Muğîre b. Şu’be’nin, Rasûlullah’ın (sallallâhu aleyhi ve sellem) abdestte mesti üzerine meshini anlattığı hadisi gereği: «Nebî’yi (sallallâhu aleyhi ve sellem) mestlerin üzerine, üst taraflarına meshederken gördüm.» (2)',
     '١/ ٢٥',
     '**المسح** غير الغسل: هو إمرار اليد المبلولة بالماء على ظاهر الخف. فلا يُغسل الخف، ولا يُتتبّع بالماء.\n\n'
     '**شرح الحواشي:** (٢) الحديث رواه الترمذي، وحسّنه، وقال الألباني: حسن صحيح.',
     '**Mesh** yıkamak değildir: Suyla ıslatılmış eli mestin üstünden geçirmektir. Mest yıkanmaz, her yerine su ulaştırılmaya çalışılmaz.\n\n'
     '**Dipnotların şerhi:** (2) Hadisi Tirmizî rivayet etmiş ve hasen demiştir; Elbânî «hasen sahih» demiştir.',
     fn=['(٢) أخرجه الترمذي برقم (٩٨)، وقال: حسن. وقال الألباني: حسن صحيح (صحيح الترمذي برقم ٨٥).']),
  PS('ولا يجزئ مسح أسفله وعقبه ولا يسن. لقول عليٍّ ﵁: (لو كان الدين بالرأي لكان أسفل الخف أولى بالمسح من أعلاه، وقد رأيت النبي ﷺ يمسح على ظاهر خفه) (٣). ولو جمع بين الأعلى والأسفل صَحَّ مع الكراهة.',
     'Altını ve topuğunu meshetmek yeterli değildir, sünnet de değildir. Ali’nin (radıyallâhu anh) şu sözü gereği: «Din akılla olsaydı mestin altı meshedilmeye üstünden daha lâyık olurdu. Ben Nebî’yi (sallallâhu aleyhi ve sellem) mestinin üstüne meshederken gördüm.» (3) Üstüyle altını birlikte meshederse sahih olur, fakat mekruhtur.',
     '١/ ٢٥',
     'في قول علي رضي الله عنه **قاعدة عظيمة**: العبادات تُتلقّى من النص، لا من الرأي. فالعقل قد يرى أن أسفل الخف أولى بالمسح لأنه يلاقي الأرض والأذى، لكن السنة جاءت بمسح أعلاه، فنتّبعها.\n\n'
     '**شرح الحواشي:** (٣) الأثر رواه أبو داود والبيهقي، وصحّح الحافظ ابن حجر إسناده.',
     'Ali’nin (radıyallâhu anh) sözünde **büyük bir kaide** vardır: İbadetler akıl yürütmeden değil, nastan alınır. Akıl, yere ve pisliğe değdiği için mestin altını meshe daha lâyık görebilir; ama Sünnet üstünün meshedilmesiyle gelmiştir, biz de ona uyarız.\n\n'
     '**Dipnotların şerhi:** (3) Bu sözü Ebû Dâvûd ve Beyhakî rivayet etmiş, Hâfız İbn Hacer sahih saymıştır.',
     fn=['(٣) رواه أبو داود برقم (١٦٢)، والبيهقي (١/ ٢٩٢)، وصححه الحافظ ابن حجر (التلخيص الحبير ١/ ١٦٠).']),
 ]),
 dict(ar='المسألة الرابعة: مدته', tr='Dördüncü mesele: Süresi', paras=[
  PS('ومدة المسح على الخفين بالنسبة للمقيم ومن سفره لا يبيح له القصر: يوم وليلة، وبالنسبة للمسافر سفراً يبيح له القصر: ثلاثة أيام بلياليها، لحديث علي ﵁ قال: (جعل رسول الله ﷺ ثلاثة أيام ولياليهن للمسافر، ويوماً وليلة للمقيم) (١).',
     'Mestler üzerine mesh süresi, mukim ve yolculuğu namazı kısaltmayı mubah kılmayan kimse için bir gün bir gece; namazı kısaltmayı mubah kılan yolculuktaki yolcu için üç gün üç gecedir. Ali’nin (radıyallâhu anh) hadisi gereği: «Rasûlullah (sallallâhu aleyhi ve sellem) yolcu için üç gün üç gece, mukim için bir gün bir gece belirledi.» (1)',
     '١/ ٢٦',
     '**يوم وليلة** = أربع وعشرون ساعة، و**ثلاثة أيام بلياليها** = اثنتان وسبعون ساعة، تُحسب من ابتداء المدة الآتي في المسألة السادسة.\n\n'
     'و**السفر الذي يبيح القصر** يأتي تفصيله في كتاب الصلاة إن شاء الله؛ ومن سافر سفرًا لا يبيح القصر فحكمه حكم المقيم.\n\n'
     '**شرح الحواشي:** (١) الحديث في صحيح مسلم.',
     '**Bir gün bir gece** = yirmi dört saat; **üç gün üç gece** = yetmiş iki saat. Altıncı meselede gelecek başlangıç anından itibaren sayılır.\n\n'
     '**Namazı kısaltmayı mubah kılan yolculuk** inşallah Namaz Kitabı’nda ayrıntılı olarak gelecek; bu nitelikte olmayan bir yolculuğa çıkan, mukim hükmündedir.\n\n'
     '**Dipnotların şerhi:** (1) Hadis Müslim’in Sahîh’indedir.',
     fn=['(١) رواه مسلم برقم (٨٥).'],
     note=dict(ar='تنبيه على الحاشية (١): الرقم (٨٥) هو رقمه في كتاب الطهارة من «صحيح مسلم»؛ ورقمه في الترقيم المشهور (٢٧٦).', tr='(1) numaralı dipnot hakkında: 85, hadisin Müslim’in Sahîh’indeki Taharet Kitabı içindeki numarasıdır; meşhur numaralandırmada 276’dır.')),
 ]),
 dict(ar='المسألة الخامسة: مبطلاته', tr='Beşinci mesele: Meshi bozanlar', paras=[
  PS('ويبطل المسح بما يأتي: ١ - إذا حصل ما يوجب الغسل بطل المسح، لحديث صفوان بن عسال قال: (كان النبي ﷺ يأمرنا إذا كنا سفراً ألا ننزع خفافنا ثلاثة أيام ولياليهن إلا من جنابة) (٢).',
     'Mesh şunlarla bozulur: 1. Guslü gerektiren bir şey olursa mesh bozulur. Safvân b. Assâl’ın hadisi gereği: «Nebî (sallallâhu aleyhi ve sellem), yolcu olduğumuzda cünüplük dışında mestlerimizi üç gün üç gece çıkarmamamızı bize emrederdi.» (2)',
     '١/ ٢٦',
     '**«سَفْرًا»:** مسافرين. ووجه الدلالة في قوله **«إلا من جنابة»**: أن الجنابة استُثنيت، فمن أجنب وجب عليه أن ينزع الخفين ويغسل جميع بدنه. فالمسح على الخفين للحدث الأصغر فقط.\n\n'
     '**شرح الحواشي:** (٢) الحديث رواه أحمد والنسائي والترمذي وصحّحه، وحسّنه الألباني.',
     '**«Sefran»:** yolcular. Delil yönü **«cünüplük dışında»** sözündedir: Cünüplük istisna edilmiştir; cünüp olan mestleri çıkarıp bütün bedenini yıkamalıdır. Yani mest üzerine mesh yalnızca küçük hades içindir.\n\n'
     '**Dipnotların şerhi:** (2) Hadisi Ahmed, Nesâî ve Tirmizî rivayet etmiş, Tirmizî sahih saymış; Elbânî hasen demiştir.',
     fn=['(٢) رواه أحمد (٤/ ٢٣٩)، والنسائي (١/ ٨٤)، والترمذي برقم (٩٦) وصححه، وحسنه الألباني في (الإرواء برقم ١٠٤).']),
  PS('٢ - إذا ظهر بعض محل الفرض، أي: ظهور بعض القدم، بطل المسح. ٣ - نرع الخفين يبطل المسح، ونزع أحد الخفين كنزعهما في قول أكثر أهل العلم. ٤ - انقضاء مدة المسح مبطل له؛ لأن المسح مؤقت بزمن معين من قبل الشارع، فلا تجوز الزيادة على المدة المقررة لمفهوم أحاديث التوقيت.',
     '2. Farz yerinin bir kısmı, yani ayağın bir kısmı görünürse mesh bozulur. 3. Mestleri çıkarmak meshi bozar; âlimlerin çoğuna göre birini çıkarmak ikisini çıkarmak gibidir. 4. Mesh süresinin bitmesi onu bozar; çünkü mesh Şâri’ tarafından belirli bir zamanla sınırlanmıştır; süreyi belirleyen hadislerin mefhumu gereği belirlenen sürenin aşılması caiz değildir.',
     '١/ ٢٦',
     '**ظهور القدم ونزع الخف** يرجعان إلى الشرط الثاني: الستر؛ فإذا زال الستر زال المسح.\n\n'
     '**انقضاء المدة:** يرجع إلى الشرط الخامس. و«مفهوم أحاديث التوقيت»: أن تحديد المدة يدل على أن ما بعدها ممنوع.\n\n'
     '**ملاحظة لغوية:** «نرع» في المتن خطأ طباعي صوابه «نزع».',
     '**Ayağın görünmesi ve mesti çıkarmak** ikinci şarta, örtmeye döner: Örtü kalkınca mesh de kalkar.\n\n'
     '**Sürenin bitmesi** beşinci şarta döner. «Süre hadislerinin mefhumu»: Sürenin belirlenmesi, sonrasının yasak olduğunu gösterir.'),
 ]),
 dict(ar='المسألة السادسة: ابتداء مدة المسح', tr='Altıncı mesele: Mesh süresinin başlangıcı', paras=[
  PS('وتبتدئ مدة المسح من الحدث بعد اللبس، كمن توضأ لصلاة الفجر، ولبس الخفين، وبعد طلوع الشمس أحدث، ولم يتوضأ، ثم توضأ قبل صلاة الظهر، فابتداء المدة من طلوع الشمس وقت الحدث. وقال بعض العلماء: ابتداؤها من حيث توضأ قبل صلاة الظهر، أي: من المسح بعد الحدث.',
     'Mesh süresi, giydikten sonraki hadesten başlar. Mesela sabah namazı için abdest alıp mestleri giyen, güneş doğduktan sonra abdesti bozulan ve abdest almayan, sonra öğle namazından önce abdest alan kimse için sürenin başlangıcı, abdestin bozulduğu vakit olan güneşin doğuşudur. Bazı âlimler ise başlangıcın, öğleden önce abdest aldığı andan, yani hadesten sonraki ilk meshten olduğunu söylemiştir.',
     '١/ ٢٦',
     'قدّم الكتاب القول الأول: **المدة من الحدث بعد اللبس**، ومثّل له. ثم ذكر قولًا ثانيًا لبعض العلماء: أنها من **أول مسح بعد الحدث**.\n\n'
     'والفرق بين القولين في المثال: على الأول تُحسب المدة من طلوع الشمس، وعلى الثاني من وقت الوضوء قبل الظهر. وهذا الدرس يعتمد ما قدّمه الكتاب.',
     'Kitap birinci görüşü öne almış ve örnek vermiştir: **Süre, giydikten sonraki hadesten** başlar. Sonra bazı âlimlerin ikinci görüşünü zikretmiştir: **hadesten sonraki ilk meshten** başlar.\n\n'
     'Örnekte iki görüş arasındaki fark: Birinciye göre süre güneşin doğuşundan, ikinciye göre öğleden önceki abdest vaktinden sayılır. Bu ders, kitabın öne aldığı görüşü esas alır.'),
 ]),
 dict(ar='المسألة السابعة: المسح على الجبيرة والعمامة وخمر النساء', tr='Yedinci mesele: Sargı, sarık ve kadınların başörtüsü üzerine mesh', paras=[
  PS('[[الجبيرة|jabira]]: هي أعواد ونحوها كالجبس مما يربط على الكسر ليجبر ويلتئم، ويمسح عليها. وكذلك يمسح على اللصوق واللفائف التي توضع على الجروح، فكل هذه الأشياء يمسح عليها بشرط أن تكون على قدر الحاجة، فإن تجاوزت قدر الحاجة لزمه نَزْعُ ما زاد على الحاجة.',
     'Cebîre (sargı): Kırığın üzerine, kaynayıp iyileşsin diye bağlanan tahta parçaları ve alçı gibi şeylerdir; üzerine meshedilir. Aynı şekilde yaraların üzerine konan yara bantları ve sargılar üzerine de meshedilir. Bütün bunlar üzerine, ihtiyaç kadar olmaları şartıyla meshedilir; ihtiyacı aşarsa, ihtiyaçtan fazlasını çıkarması gerekir.',
     '١/ ٢٧',
     '**قدر الحاجة:** موضع الكسر أو الجرح، وما لا بد منه حوله لتثبيت الجبيرة. فإن وضع لفافة كبيرة على جرح صغير، وأمكنه نزع الزائد، لزمه نزعه.',
     '**İhtiyaç kadar:** Kırığın veya yaranın yeri ile sargıyı sabitlemek için etrafında mutlaka gereken kısım. Küçük bir yaraya büyük bir sargı koyan, fazlasını çıkarabiliyorsa çıkarması gerekir.'),
  PS('ويجوز المسح عليها في الحدث الأكبر والأصغر، وليس للمسح عليها وقت محدد بل يمسح عليها إلى نزعها أو شفاء ما تحتها. والدليل على ذلك: أن المسح على الجبيرة ضرورة والضرورة تقدر بقدرها ولا فرق فيها بين الحدثين.',
     'Büyük ve küçük hadeste üzerine meshetmek caizdir. Üzerine meshin belirli bir süresi yoktur; çıkarılıncaya veya altındaki yer iyileşinceye kadar meshedilir. Delili: Sargı üzerine mesh bir zarurettir; zaruret kendi ölçüsünce takdir edilir ve zarurette iki hades arasında fark yoktur.',
     '١/ ٢٧',
     'هنا يظهر الفرق بين **الخف** و**الجبيرة**: الخف رخصة للحدث الأصغر بمدة محددة، والجبيرة **ضرورة** تُمسح في الحدثين بلا مدة؛ لأن صاحبها لا يستطيع نزعها متى شاء.\n\n'
     '**«الضرورة تُقدّر بقدرها»:** يُباح منها ما تندفع به الحاجة فقط، لا أكثر.',
     'Burada **mest** ile **sargı** arasındaki fark ortaya çıkar: Mest, küçük hades için belirli süreli bir ruhsattır; sargı ise iki hadeste de süresiz meshedilen bir **zarurettir**; çünkü sahibi onu istediği zaman çıkaramaz.\n\n'
     '**«Zaruret kendi ölçüsünce takdir edilir»:** Ondan yalnızca ihtiyacı giderecek kadarı mubah olur, fazlası değil.'),
  PS('وكذلك يجوز المسح على [[العمامة|imama]]، وهي ما يعمم به الرأس، ويكور عليه، والدليل على ذلك: حديث المغيرة بن شعبة ﵁ (أن النبي ﷺ مسح على عمامته وعلى الناصية والخفين) (١). وحديث: (أنه ﷺ مسح على الخفين والخمار) (٢). يعني العمامة.',
     'Aynı şekilde sarık üzerine meshetmek de caizdir. Sarık, başa sarılan ve üzerine dolanan şeydir. Delili Muğîre b. Şu’be’nin (radıyallâhu anh) hadisidir: «Nebî (sallallâhu aleyhi ve sellem) sarığının, alnının üstündeki saçlarının (nâsiye) ve mestlerinin üzerine meshetti.» (1) Bir de şu hadis: «O (sallallâhu aleyhi ve sellem) mestlerin ve hımârın üzerine meshetti.» (2) Yani sarığın.',
     '١/ ٢٧',
     '**الناصية:** مقدّم شعر الرأس. وفي الحديث أنه ﷺ مسح على الناصية ثم أتمّ على العمامة.\n\n'
     '**«الخمار» في الحديث الثاني:** المراد به العمامة، لأنها تُخمّر الرأس أي تغطيه.\n\n'
     '**شرح الحواشي:** (١) حديث المغيرة في صحيح مسلم. (٢) والثاني في صحيح مسلم أيضًا، من حديث بلال رضي الله عنه.',
     '**Nâsiye:** Başın ön kısmındaki saçlar. Hadiste Nebî’nin (s.a.v.) nâsiyeye meshedip sarığın üzerinde tamamladığı vardır.\n\n'
     '**İkinci hadisteki «hımâr»:** Sarık kastedilmiştir; çünkü başı örter.\n\n'
     '**Dipnotların şerhi:** (1) Muğîre hadisi Müslim’in Sahîh’indedir. (2) İkincisi de Bilâl’den (radıyallâhu anh) Müslim’in Sahîh’indedir.',
     fn=['(١) رواه مسلم برقم (٢٧٤).', '(٢) رواه مسلم برقم (٢٧٥).']),
  PS('والمسح عليها ليس له وقت محدد، ولكن لو سلك سبيل الاحتياط فلم يمسحها إلا إذا لبسها على طهارة وفي المدة المحددة للمسح على الخفين، لكان حسناً.',
     'Sarık üzerine meshin belirli bir süresi yoktur. Ama ihtiyat yolunu tutup onu ancak abdestli giydiğinde ve mestler üzerine mesh için belirlenen süre içinde meshederse güzel olur.',
     '١/ ٢٧',
     'الأصل في العمامة أنه لا وقت لها؛ والاحتياط **مستحسن لا واجب**: أن يعاملها معاملة الخف في الطهارة والمدة.',
     'Sarıkta asıl olan süresinin olmamasıdır; ihtiyat ise **farz değil, güzel olandır**: Taharet ve süre bakımından ona mest gibi davranmak.'),
  PS('أما [[خمار|khimar]] المرأة وهو ما تغطي به رأسها، فالأولى ألا تمسح عليه، إلا إذا كان هناك مشقة في نزعه، أو لمرض في الرأس أو نحو ذلك. ولو كان الرأس ملبداً بحناء أو غيره فيجوز المسح عليه؛ لفعل النبي ﷺ. وعموماً طهارة الرأس فيها شيء من التسهيل والتيسير على هذه الأمة.',
     'Kadının başörtüsüne gelince, o kadının başını örttüğü şeydir. Daha uygun olanı onun üzerine meshetmemesidir; ancak çıkarmakta zorluk olursa veya başta hastalık ya da benzeri bir durum varsa meshedebilir. Baş kına veya başka bir şeyle sıvanmış (yapıştırılmış) ise üzerine meshetmek caizdir; Nebî (sallallâhu aleyhi ve sellem) böyle yapmıştır. Genel olarak başın temizliğinde bu ümmete bir kolaylık ve genişlik vardır.',
     '١/ ٢٧',
     '**«ملبّدًا»:** أي جُعل على الشعر شيء يلصقه ويجمعه، كالحناء؛ وقد لبّد النبي ﷺ رأسه في الإحرام.\n\n'
     '**«الأولى»:** أي الأفضل؛ فالمرأة تنزع خمارها وتمسح رأسها، إلا عند المشقة أو المرض فتمسح عليه.\n\n'
     '**والقاعدة في آخر الباب:** طهارة الرأس مبنية على **المسح** لا الغسل، وفيها تيسير؛ ولذلك جاز المسح على العمامة والرأس الملبّد.',
     '**«Sıvanmış»:** Saçın üzerine, kına gibi onu yapıştırıp toplayan bir şey konmuş olması; Nebî (s.a.v.) ihramda başını böyle yapmıştır.\n\n'
     '**«Daha uygun olan»:** yani daha faziletlisi; kadın başörtüsünü çıkarıp başını mesheder; zorluk veya hastalık hâlinde ise üzerine mesheder.\n\n'
     '**Bölümün sonundaki kaide:** Başın temizliği yıkamaya değil **meshe** dayanır ve onda kolaylık vardır; bu yüzden sarık ve sıvanmış baş üzerine mesh caiz olmuştur.'),
 ]),
]

# ------------------------------------------------------------------ 107: الغسل
GLOSS.update({
 'fadakh': dict(w='فَضَخْتَ', ar='فَضْخُ الماء: دَفْقُه، والمراد المنيّ.', tr='Suyu atarak çıkarmak; kastedilen menidir.', src='حاشية الكتاب (١/ ٢٨)'),
 'ijza': dict(w='كيفية إجزاء', ar='كيفية الإجزاء: هي التي تشتمل على ما يجب فقط، وكيفية الاستحباب والكمال: هي التي تشتمل على الواجب والمسنون.', tr='Yeterli şekil: yalnızca farz olanı içerir; müstehap ve kâmil şekil: farzı ve sünneti içerir.', src='حاشية الكتاب (١/ ٢٩)'),
})
GLOSS_TR_SRC.update({
 'حاشية الكتاب (١/ ٢٨)': 'Kitabın dipnotu (1/ 28)',
 'حاشية الكتاب (١/ ٢٩)': 'Kitabın dipnotu (1/ 29)',
})

SHARH[107] = [
 dict(ar='المسألة الأولى: معنى الغسل، وحكمه، ودليله', tr='Birinci mesele: Guslün anlamı, hükmü ve delili', paras=[
  PS('١ - معناه: الغُسل لغة: مصدر من غسل الشيء يَغسله غَسْلاً وغُسْلاً، وهو تمام غسل الجسد كله. ومعناه شرعاً: تعميم البدن بالماء. أو: استعمال ماء طهور في جميع البدن، على صفة مخصوصة، على وجه التعبد لله سبحانه.',
     '1. Anlamı: Gusül sözlükte «gasele» fiilinin mastarıdır; bütün bedeni tamamen yıkamaktır. Şer’î anlamı: Bütün bedene su ulaştırmak; ya da tahûr suyu bütün bedende, belirli bir şekilde, Allah Sübhânehû’ya ibadet maksadıyla kullanmaktır.',
     '١/ ٢٨',
     'تعلّمنا الوضوء للحدث الأصغر، وهذا الباب **للحدث الأكبر**.\n\n'
     'وفي التعريف الثاني قيود كالوضوء: **ماء طهور**، و**جميع البدن**، و**صفة مخصوصة**، و**التعبّد**؛ فمن اغتسل للتبرّد وحده دون نية رفع الحدث لم يرتفع حدثه.',
     'Abdesti küçük hades için öğrendik; bu bölüm **büyük hades** içindir.\n\n'
     'İkinci tanımda abdestteki gibi kayıtlar vardır: **tahûr su**, **bütün beden**, **belirli şekil** ve **ibadet**. Hadesi kaldırma niyeti olmadan yalnızca serinlemek için yıkanan kimsenin hadesi kalkmaz.'),
  PS('٢ - حكمه: والغسل واجب إذا وجد سبب لوجوبه. لقوله تعالى: (وَإِنْ كُنْتُمْ جُنُبًا فَاطَّهَّرُوا) [المائدة: ٦]، والأحاديث التي ورد فيها كيفية الغسل عن عدد من الصحابة نقلاً عن رسول الله ﷺ دالة على وجوبه. وسيأتي طرف منها قريباً إن شاء الله.',
     '2. Hükmü: Gusül, farz olmasının bir sebebi bulunduğunda farzdır. Allah Teâlâ’nın «Eğer cünüp iseniz temizlenin» [Mâide, 6] sözü gereği. Birçok sahâbînin Rasûlullah’tan (sallallâhu aleyhi ve sellem) naklettiği, guslün şeklini anlatan hadisler de farz olduğunu gösterir; bunlardan bir kısmı inşallah birazdan gelecek.',
     '١/ ٢٨',
     'الغسل **يجب لغيره**، كالوضوء: إذا وُجد سببه، وأراد ما لا يصح إلا بالطهارة. و**«فاطّهّروا»** في الآية بعد ذكر الوضوء معناها: عمّموا أبدانكم بالماء.',
     'Gusül, abdest gibi **başka bir şey için farzdır**: Sebebi bulunduğunda ve ancak temizlikle sahih olan bir şeyi istediğinde. Âyette abdestten sonra gelen **«temizlenin»** sözü, bedenlerinize su ulaştırın demektir.'),
 ]),
 dict(ar='موجبات الغسل', tr='Guslü gerektirenler', paras=[
  PS('٣ - موجباته: ويجب الغسل للأسباب الآتية: ١ - خروج المنيّ من مخرجه: ويشترط أن يكون دفقاً بلذة من ذكر أو أنثى، لقوله تعالى: (وَإِنْ كُنْتُمْ جُنُبًا فَاطَّهَّرُوا) [المائدة: ٦]، ولقوله ﷺ لعلي: (إذا [[فَضَخْتَ|fadakh]] (١) الماء فاغتسل) (٢). ما لم يكن نائماً ونحوه فلا تشترط اللذة؛ لأن النائم قد لا يحس به، ولقوله ﷺ لما سئل: هل على المرأة غسل إذا احتلمت؟ قال: (نعم إذا رأت الماء) (٣). وهذا كله مجمع عليه.',
     '3. Gerektirenler: Gusül şu sebeplerle farz olur: 1. Meninin çıkış yerinden çıkması: Erkekten veya kadından, atılarak ve lezzetle çıkması şarttır. Allah Teâlâ’nın «Eğer cünüp iseniz temizlenin» [Mâide, 6] sözü ve Nebî’nin (sallallâhu aleyhi ve sellem) Ali’ye: «Suyu atarak çıkardığında gusül abdesti al» (1)(2) sözü gereği. Uyuyan ve benzeri ise bundan hariçtir; onda lezzet şart değildir, çünkü uyuyan bunu hissetmeyebilir. Ayrıca Nebî’ye (s.a.v.) «Kadın ihtilam olursa ona gusül gerekir mi?» diye sorulunca «Evet, suyu (meniyi) görürse» (3) buyurmuştur. Bunların hepsinde icmâ vardır.',
     '١/ ٢٨',
     'في المستيقظ **شرطان**: الدفق واللذة. فإن خرج منه شيء بلا لذة، لمرض أو برد، لم يجب الغسل. أما **النائم** فالعبرة عنده بوجود الماء بعد الاستيقاظ، شعر بلذة أو لم يشعر.\n\n'
     '**شرح الحواشي:** (١) الفضخ: الدفق. (٢) حديث علي رواه أبو داود، وصحّحه الألباني. (٣) حديث أم سليم في صحيح مسلم.',
     'Uyanık olanda **iki şart** vardır: atılarak çıkması ve lezzet. Hastalık veya soğuk sebebiyle lezzetsiz bir şey çıkarsa gusül farz olmaz. **Uyuyanda** ise ölçü, uyandıktan sonra meniyi görmesidir; lezzet hissetsin veya hissetmesin.\n\n'
     '**Dipnotların şerhi:** (1) Fadh: atarak çıkarmak. (2) Ali hadisini Ebû Dâvûd rivayet etmiş, Elbânî sahih saymıştır. (3) Ümmü Süleym hadisi Müslim’in Sahîh’indedir.',
     fn=['(١) فَضْخُ الماء: أي دَفْقُهُ، والمراد المَنِيّ.', '(٢) رواه أبو داود برقم (٢٠٦)، وصححه الألباني (الإرواء برقم ١٢٥).', '(٣) رواه مسلم برقم (٣١٣).']),
  PS('٢ - تغييب حشفة الذكر كلها أو قدرها في الفرج، وإن لم يحصل إنزال بلا حائل: لقوله ﷺ: (إذا جلس بين شعبها الأربع، ومس الختانُ الختانَ، وجب الغسل) (٤). لكن لا يجب الغسل في هذه الحالة إلا على ابن عشر أو بنت تسع فما فوق.',
     '2. Birleşme, meni gelmese bile, engel olmaksızın: Nebî’nin (sallallâhu aleyhi ve sellem) şu sözü gereği: «Erkek, kadının dört uzvu arasına oturur ve sünnet yerleri birbirine değerse gusül farz olur.» (4) Ancak bu durumda gusül, on yaşındaki erkek çocuk ve dokuz yaşındaki kız çocuğu ile daha büyükleri için farzdır.',
     '١/ ٢٨',
     '**«مسّ الختانُ الختانَ»:** كناية عن الجماع، أي تحاذي موضعَي الختان؛ وهو أدب نبوي في التعبير عمّا يُستحيا منه. والحكم: **الجماع وحده يوجب الغسل، ولو لم يُنزل**.\n\n'
     '**شرح الحواشي:** (٤) الحديث في صحيح مسلم.',
     '**«Sünnet yerleri birbirine değerse»:** Birleşmeden kinayedir; utanılan şeyi ifade etmede nebevî bir edeptir. Hüküm: **Birleşme tek başına guslü gerektirir, meni gelmese de**.\n\n'
     '**Dipnotların şerhi:** (4) Hadis Müslim’in Sahîh’indedir.',
     fn=['(٤) رواه مسلم برقم (٣٤٩).']),
  PS('٣ - إسلام الكافر ولو مرتداً: (لأن النبي ﷺ أمر قيس بن عاصم حين أسلم أن يغتسل) (١). ٤ - انقطاع دم الحيض والنفاس: لحديث عائشة أن النبي ﷺ قال لفاطمة بنت أبي حبيش: (إذا أقبلت الحيضة فدعي الصلاة، وإذا أدبرت فاغتسلي وصَلِّي) (٢). والنفاس كالحيض بالإجماع.',
     '3. Kâfirin Müslüman olması, dinden dönmüş olsa bile: «Çünkü Nebî (sallallâhu aleyhi ve sellem), Kays b. Âsım Müslüman olduğunda ona gusletmesini emretmiştir.» (1) 4. Hayız ve lohusalık kanının kesilmesi: Âişe’nin hadisi gereği; Nebî (s.a.v.) Fâtıma bint Ebî Hubeyş’e şöyle buyurdu: «Hayız geldiğinde namazı bırak; gittiğinde gusledip namaz kıl.» (2) Lohusalık icmâ ile hayız gibidir.',
     '١/ ٢٩',
     '**إسلام الكافر:** يغتسل عند دخوله في الإسلام، ولو كان مرتدًّا ثم رجع.\n\n'
     '**«إذا أدبرت»:** أي انقطع الدم وانتهت أيام الحيض؛ فالغسل يجب **بانقطاع** الدم، لا بخروجه.\n\n'
     '**شرح الحواشي:** (١) حديث قيس بن عاصم رواه أبو داود والنسائي والترمذي وحسّنه، وصحّحه الألباني. (٢) حديث عائشة متفق عليه.',
     '**Kâfirin Müslüman olması:** İslam’a girerken gusleder; dinden dönüp sonra geri gelmiş olsa bile.\n\n'
     '**«Gittiğinde»:** yani kan kesilip hayız günleri bitince; gusül kanın çıkmasıyla değil, **kesilmesiyle** farz olur.\n\n'
     '**Dipnotların şerhi:** (1) Kays b. Âsım hadisini Ebû Dâvûd, Nesâî ve Tirmizî rivayet etmiş, Tirmizî hasen demiş, Elbânî sahih saymıştır. (2) Âişe hadisi Buhârî ve Müslim’dedir.',
     fn=['(١) رواه أبو داود برقم (٣٥٥)، والنسائي (١/ ١٠٩)، والترمذي برقم (٦٠٥) وحسنه، وصححه الألباني في الإرواء (١/ ١٦٣ - ١٦٤).', '(٢) رواه البخاري برقم (٣٢٠)، ومسلم برقم (٣٣٣).']),
  PS('٥ - الموت: لقوله ﷺ في حديث غسل ابنته زينب حين توفيت: (اغسلنها) (٣). وقال في المحرم: (اغسلوه بماء وسدر) (٤). وذلك تعبداً؛ لأنه لو كان عن حدث لم يرتفع مع بقاء سببه.',
     '5. Ölüm: Nebî’nin (sallallâhu aleyhi ve sellem) kızı Zeyneb vefat ettiğinde onun yıkanmasıyla ilgili hadiste «Onu yıkayın» (3) sözü ve ihramlı ölen hakkında «Onu su ve sidirle yıkayın» (4) sözü gereği. Bu, ibadet (taabbüd) olarak yapılır; çünkü hadesten dolayı olsaydı, sebebi devam ettiği sürece kalkmazdı.',
     '١/ ٢٩',
     '**«تعبّدًا»:** أي نفعله امتثالًا لأمر الله، وإن لم نعلم علّته. ووجه ذلك: أن **الموت** سبب باقٍ لا يزول، فلو كان الغسل لرفع حدث الموت لم يرتفع ما دام سببه قائمًا. و**السِّدْر:** ورق شجر النبق، يُدقّ ويُجعل في الماء للتنظيف، كما تقدّم في باب المياه.\n\n'
     '**شرح الحواشي:** (٣) و(٤) الحديثان متفق عليهما.',
     '**«Taabbüd»:** Gerekçesini bilmesek de Allah’ın emrine uyarak yaparız. Delil yönü: **Ölüm** sürüp giden bir sebeptir; gusül ölüm hadesini kaldırmak için olsaydı, sebebi devam ettikçe kalkmazdı. **Sidir:** Arabistan kirazı ağacının yaprağıdır; ezilip temizlik için suya konur; Sular bölümünde geçtiği gibi.\n\n'
     '**Dipnotların şerhi:** (3) ve (4) İki hadis de Buhârî ve Müslim’dedir.',
     fn=['(٣) متفق عليه، رواه البخاري برقم (١٢٥٣)، ومسلم برقم (٩٣٩).', '(٤) متفق عليه: رواه البخاري برقم (١٢٦٦) كتاب الجنائز، ومسلم برقم (١٢٠٦).']),
 ]),
 dict(ar='المسألة الثانية: في صفة الغسل وكيفيته', tr='İkinci mesele: Guslün şekli ve keyfiyeti', paras=[
  PS('للغسل من الجنابة كيفيتان، كيفية استحباب، و[[كيفية إجزاء|ijza]] (٥). أما كيفية الاستحباب: فهي أن يغسل يديه، ثم يغسل فرجه، وما أصابه من الأذى، ثم يتوضأ وضوءه للصلاة، ثم يأخذ بيده ماءً فيخلل به شعر رأسه، مدخلاً أصابعه في أصول الشعر حتى يروي بشرته، ثم يحثو على رأسه ثلاث حثيات، ثم يفيض الماء على سائر بدنه؛ لحديث عائشة المتفق عليه.',
     'Cünüplük guslünün iki şekli vardır: müstehap şekil ve yeterli şekil. (5) Müstehap şekil şudur: Ellerini yıkar, sonra avret yerini ve ona bulaşan pisliği yıkar, sonra namaz abdesti gibi abdest alır, sonra eliyle su alıp parmaklarını saç diplerine sokarak derisini ıslatıncaya kadar saçını hilâller, sonra başına üç avuç su döker, sonra bedeninin geri kalanına su akıtır. Âişe’nin Buhârî ve Müslim’deki hadisi gereği.',
     '١/ ٢٩',
     'رتّب الكتاب الصفة الكاملة **ست خطوات**: اليدان، ثم الفرج، ثم الوضوء، ثم تخليل الشعر، ثم ثلاث حثيات، ثم سائر البدن.\n\n'
     '**الحثية:** ملء الكفين من الماء. و**«يروي بشرته»:** يُوصل الماء إلى جلد الرأس حتى يبتلّ.\n\n'
     '**شرح الحواشي:** (٥) الحاشية تفسّر المصطلحين: الإجزاء ما اشتمل على الواجب فقط، والكمال ما اشتمل على الواجب والمسنون.',
     'Kitap kâmil şekli **altı adımda** sıralamıştır: eller, avret yeri, abdest, saçı hilâllemek, üç avuç ve bedenin geri kalanı.\n\n'
     '**Hasye:** iki avuç dolusu su. **«Derisini ıslatmak»:** suyu baş derisine ulaştırıp ıslatmak.\n\n'
     '**Dipnotların şerhi:** (5) Dipnot iki terimi açıklar: Yeterli olan yalnızca farzı içerir; kâmil olan farzı ve sünneti içerir.',
     fn=['(٥) وكيفية الإجزاء: هي التي تشتمل على ما يجب فقط، وكيفية الاستحباب والكمال: هي التي تشتمل على الواجب والمسنون.']),
  PS('وأما كيفية الإجزاء: أن يعم بدنه بالماء ابتداءً مع النية لحديث ميمونة: (وضع رسول الله ﷺ وَضُوءَ الجنابة، فأفرغ على يديه فغسلهما مرتين أو ثلاثاً، ثم تمضمض، واستنشق، وغسل وجهه وذراعيه، ثم أفاض الماء على رأسه، ثم غسل جسده، فأتيته بالمنديل فلم يُرِدْها، وجعل ينفض الماء بيديه) (٦). ومثله حديث عائشة وفيه: (ثم يخلل شعره بيده. حتى إذا ظن أنه قد روى بشرته، أفاض عليه الماء ثلاث مرات، ثم غسل سائر جسده) (١).',
     'Yeterli şekil ise: Niyetle birlikte doğrudan bütün bedene su ulaştırmaktır. Meymûne’nin hadisi gereği: «Rasûlullah’a (sallallâhu aleyhi ve sellem) cünüplük guslü için su koydum. Ellerine döküp onları iki veya üç kez yıkadı; sonra ağzına ve burnuna su verdi, yüzünü ve kollarını yıkadı; sonra başına su döktü, sonra bedenini yıkadı. Ona bir havlu getirdim, almak istemedi; suyu elleriyle silkelemeye başladı.» (6) Âişe’nin hadisi de böyledir; orada: «Sonra eliyle saçını hilâllerdi; derisini ıslattığını düşündüğünde üzerine üç kez su döker, sonra bedeninin geri kalanını yıkardı.» (1)',
     '١/ ٢٩–٣٠',
     '**«ابتداءً»:** أي ولو لم يتوضأ قبله، ولم يرتّب؛ فالواجب **التعميم مع النية**. وحديث ميمونة فيه صفة كاملة أيضًا؛ وفيه أنه ﷺ لم يأخذ المنديل، فدلّ على أن تنشيف الأعضاء ليس من السنة اللازمة.\n\n'
     '**شرح الحواشي:** (٦) حديث ميمونة متفق عليه. (١) وحديث عائشة متفق عليه.',
     '**«Doğrudan»:** yani önce abdest almasa ve sıraya uymasa da; farz olan **niyetle bütün bedene su ulaştırmaktır**. Meymûne hadisinde de kâmil şekil vardır; ayrıca Nebî’nin (s.a.v.) havluyu almadığı geçer; bu, kurulanmanın lâzım bir sünnet olmadığını gösterir.\n\n'
     '**Dipnotların şerhi:** (6) Meymûne hadisi Buhârî ve Müslim’dedir. (1) Âişe hadisi de Buhârî ve Müslim’dedir.',
     fn=['(٦) متفق عليه: رواه البخاري برقم (٢٤٩)، ومسلم برقم (٣١٧).', '(١) متفق عليه: رواه البخاري برقم (٢٤٨)، ومسلم برقم (٣١٦).']),
  PS('ولا يجب على المرأة نقض شعرها في الغسل من الجنابة، ويلزمها ذلك في الغسل من الحيض؛ لحديث أم سلمة قالت: قلت: يا رسول الله إني امرأة أشدُّ ضفر رأسي، أفأنقضه لغسل الجنابة؟ قال: (لا. إنما يكفيك أن تحثي على رأسك ثلاث حثيات، ثم تفيضين عليك الماء، فتطهرين) (٢).',
     'Kadının cünüplük guslünde saçını çözmesi farz değildir; hayız guslünde ise gerekir. Ümmü Seleme’nin hadisi gereği: «Ey Allah’ın Rasûlü! Ben saçımı sıkıca ören bir kadınım; cünüplük guslü için onu çözeyim mi?» dedim. Buyurdu ki: «Hayır; başına üç avuç su dökmen, sonra üzerine su akıtman sana yeter; böylece temizlenirsin.» (2)',
     '١/ ٣٠',
     '**الضَّفْر:** فتل الشعر وجدله. ففي غسل الجنابة يكفيها أن تصبّ الماء على رأسها ثلاث حثيات حتى يصل إلى أصول الشعر، دون نقض الضفائر؛ وفي غسل الحيض تنقضه، كما قرّره الكتاب.\n\n'
     '**شرح الحواشي:** (٢) حديث أم سلمة في صحيح مسلم.',
     '**Dafr:** saçı örmek. Cünüplük guslünde örgüleri çözmeden başına üç avuç su dökmesi ve suyun saç diplerine ulaşması yeterlidir; hayız guslünde ise kitabın belirttiği gibi saçını çözer.\n\n'
     '**Dipnotların şerhi:** (2) Ümmü Seleme hadisi Müslim’in Sahîh’indedir.',
     fn=['(٢) رواه مسلم برقم (٣٣٠).']),
 ]),
 dict(ar='المسألة الثالثة: الأغسال المستحبة', tr='Üçüncü mesele: Müstehap gusüller', paras=[
  PS('تقدم بيان الأغسال الواجبة، وأما الأغسال المسنونة والمستحبة، فهي: ١ - الاغتسال عند كل جماع: لحديث أبي رافع أن النبي ﷺ كان ذات ليلة يغتسل عند هذه وعند هذه قال: فقلت يا رسول الله ألا تجعله واحداً؟ قال: (هذا أزكى وأطيب وأطهر) (٣). ٢ - الغسل للجمعة: لقوله ﷺ: (إذا جاء أحدكم الجمعة فليغتسل) (٤). وهو آكد الأغسال المستحبة.',
     'Farz gusüller açıklandı. Sünnet ve müstehap gusüller ise şunlardır: 1. Her birleşmede gusletmek: Ebû Râfi’nin hadisi gereği; Nebî (sallallâhu aleyhi ve sellem) bir gece hanımlarının her birinin yanında gusletti. «Ey Allah’ın Rasûlü! Bunu tek bir gusül yapsan olmaz mı?» dedim. Buyurdu ki: «Bu daha temiz, daha güzel ve daha arıdır.» (3) 2. Cuma için gusül: «Biriniz cumaya geldiğinde gusletsin» (4) sözü gereği. Bu, müstehap gusüllerin en kuvvetlisidir.',
     '١/ ٣٠',
     '**«آكد الأغسال المستحبة»:** أي أشدّها تأكيدًا، فلا ينبغي للمسلم أن يتركه.\n\n'
     '**شرح الحواشي:** (٣) حديث أبي رافع رواه أبو داود وابن ماجه، وحسّنه الألباني. (٤) حديث الجمعة في صحيح البخاري.',
     '**«En kuvvetlisi»:** yani en çok vurgulananı; Müslüman onu terk etmemelidir.\n\n'
     '**Dipnotların şerhi:** (3) Ebû Râfi’ hadisini Ebû Dâvûd ve İbn Mâce rivayet etmiş, Elbânî hasen saymıştır. (4) Cuma hadisi Buhârî’nin Sahîh’indedir.',
     fn=['(٣) رواه أبو داود برقم (٢١٦)، وابن ماجه برقم (٥٩٠)، وحسَّنه الألباني (صحيح ابن ماجه برقم ٤٨٦).', '(٤) أخرجه البخاري برقم (٨٧٧).'],
     note=dict(ar='تنبيه على الحاشية (٣): الحديث في «سنن أبي داود» برقم (٢١٩) في الترقيم المشهور، لا (٢١٦).', tr='(3) numaralı dipnot hakkında: Hadis, meşhur numaralandırmada Ebû Dâvûd’da 216 değil 219 numaradadır.')),
  PS('٣ - الاغتسال للعيدين. ٤ - الاغتسال عند الإحرام بالعمرة والحج: فإنه ﷺ اغتسل لإحرامه. ٥ - الغسل من غسل الميت: لقوله ﷺ: (من غَسَّلَ ميتاً فليغتسل) (٥).',
     '3. İki bayram için gusül. 4. Umre ve hac için ihrama girerken gusül: Çünkü Nebî (sallallâhu aleyhi ve sellem) ihramı için gusletmiştir. 5. Ölü yıkayanın gusletmesi: «Ölü yıkayan gusletsin» (5) sözü gereği.',
     '١/ ٣٠',
     'هذه الأغسال **مستحبة لا واجبة**؛ فمن تركها لم يأثم، ومن فعلها أُجر.\n\n'
     '**شرح الحواشي:** (٥) الحديث رواه ابن ماجه، وصحّحه الألباني.',
     'Bu gusüller **farz değil, müstehaptır**: Terk eden günaha girmez, yapan sevap kazanır.\n\n'
     '**Dipnotların şerhi:** (5) Hadisi İbn Mâce rivayet etmiş, Elbânî sahih saymıştır.',
     fn=['(٥) رواه ابن ماجه برقم (١٤٦٣)، وصححه الألباني (الإرواء برقم ١٤٤).']),
 ]),
 dict(ar='المسألة الرابعة: الأحكام المترتبة على من وجب عليه الغسل', tr='Dördüncü mesele: Gusül gereken kimseyle ilgili hükümler', paras=[
  PS('١ - لا يجوز له المكث في المسجد إلا عابر سبيل لقوله تعالى: (وَلَا جُنُبًا إِلَّا عَابِرِي سَبِيلٍ حَتَّى تَغْتَسِلُوا) [النساء: ٤٣]، فإذا توضأ جاز له المكث في المسجد، لثبوت ذلك عن جماعة من الصحابة على عهد النبي ﷺ، ولأن الوضوء يخفف الحدث، والوضوء أحد الطهورين.',
     '1. Yoldan geçen hariç mescitte kalması caiz değildir. Allah Teâlâ’nın «Cünüpken de —yoldan geçenler hariç— gusledinceye kadar (namaza yaklaşmayın)» [Nisâ, 43] sözü gereği. Abdest alırsa mescitte kalması caizdir; çünkü bu, Nebî (s.a.v.) zamanında ashaptan bir topluluktan sabittir; abdest hadesi hafifletir ve abdest iki temizlikten biridir.',
     '١/ ٣٠–٣١',
     '**«عابر سبيل»:** المارّ في المسجد دون جلوس. **و«الوضوء يخفّف الحدث»:** أي يرفع الحدث الأصغر، فيبقى الأكبر مخفّفًا.',
     '**«Yoldan geçen»:** mescitte oturmadan geçen. **«Abdest hadesi hafifletir»:** küçük hadesi kaldırır; büyük hades hafiflemiş olarak kalır.'),
  PS('٢ - لا يجوز له مس المصحف. لقوله تعالى: (لَا يَمَسُّهُ إِلَّا الْمُطَهَّرُونَ) [الواقعة: ٧٩]. وقوله ﷺ: (لا يمس المصحف إلا طاهر) (١). ٣ - لا يجوز له قراءة القرآن. فلا يقرأ الجنب شيئاً من القرآن حتى يغتسل. لحديث علي قال: (كان ﵊ لا يمنعه من قراءة القرآن شيء إلا الجنابة) (٢)، ولأن في منعه من القراءة حثَّاً له على المبادرة إلى الاغتسال، وإزالة المانع له من القراءة. ويحرم عليه أيضاً: ٤ - الصلاة. ٥ - والطواف بالبيت. كما سبق بيان ذلك عند الكلام على مسألة: (ما يجب له الوضوء). من الباب الخامس.',
     '2. Mushafa dokunması caiz değildir: Allah Teâlâ’nın «Ona tertemiz olanlardan başkası dokunamaz» [Vâkıa, 79] sözü ve Nebî’nin (s.a.v.) «Mushafa ancak temiz olan dokunur» (1) sözü gereği. 3. Kur’ân okuması caiz değildir: Cünüp, gusledinceye kadar Kur’ân’dan hiçbir şey okumaz. Ali’nin hadisi gereği: «Onu (aleyhissalâtü vesselâm) Kur’ân okumaktan cünüplükten başka hiçbir şey alıkoymazdı.» (2) Ayrıca okumaktan alıkonulması, onu gusletmeye ve okumasına engel olan şeyi gidermeye acele etmeye teşvik eder. Ona şunlar da haramdır: 4. Namaz. 5. Kâbe’yi tavaf; beşinci bölümde «Abdestin farz olduğu durumlar» meselesinde açıklandığı gibi.',
     '١/ ٣١',
     'فرّق بين **المحدث حدثًا أصغر**، فيجوز له أن يقرأ من حفظه ولا يمسّ المصحف، وبين **الجنب**، فلا يقرأ ولا يمسّ حتى يغتسل.\n\n'
     '**شرح الحواشي:** (١) الحديث أخرجه مالك والحاكم، وصحّحه الألباني. (٢) حديث علي رواه أحمد وابن ماجه والترمذي وقال: حسن صحيح.',
     '**Küçük hadesli** ile **cünübü** ayırın: Küçük hadesli ezberden okuyabilir ama Mushafa dokunamaz; cünüp ise gusledinceye kadar ne okur ne dokunur.\n\n'
     '**Dipnotların şerhi:** (1) Hadisi Mâlik ve Hâkim rivayet etmiş, Elbânî sahih saymıştır. (2) Ali hadisini Ahmed, İbn Mâce ve Tirmizî rivayet etmiş; Tirmizî «hasen sahih» demiştir.',
     fn=['(١) أخرجه مالك في الموطأ (٤٦٨)، والحاكم في المستدرك (٣/ ٤٨٥)، وصححه الألباني (الإرواء برقم ١٢٢).', '(٢) رواه الإمام أحمد برقم (١٠١٤)، وابن ماجه برقم (٥٩٤)، والترمذي برقم (١٤٦)، قال الترمذي: حسن صحيح. وصححه الحاكم (المستدرك ٤/ ١٠٧). ونقل الحافظ ابن حجر تصحيحه عن: ابن السكن، وعبد الحق، والبغوي، وأن شعبة حسَّنه. (التلخيص الحبير ١/ ١٣٩).']),
 ]),
]
