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
