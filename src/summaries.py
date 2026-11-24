# Content of the one-page printable lesson summaries.
# Block kinds: p (paragraphs), chips, bullets, table (rows of [term, desc]), note (small text)
# Quran text is written inside ﴿ ﴾ and is styled automatically.

SUM = {
 (1, 'ar'): dict(
  eb='صفة الكفر بالطاغوت · النقطة الأولى · ملخص الدرس',
  sub='الخريطة الكاملة للدرس في صفحة واحدة',
  blocks=[
   dict(t='أصل الدرس', p=['قال الشيخ محمد بن عبد الوهاب: صفة الكفر بالطاغوت <b>«أن تعتقد بطلان عبادة غير الله، وتتركها، وتبغضها، وتكفّر أهلها، وتعاديهم»</b>.'],
        chips=['الاعتقاد ← درسنا', 'الترك', 'البغض', 'التكفير', 'المعاداة'], on=0),
   dict(t='معنى الاعتقاد', p=['<b>لغةً:</b> من «عَقَدَ»: الشدّ والربط والإحكام.', '<b>اصطلاحًا:</b> الجزم والتصديق القلبي بأمر، بحيث يستقر في القلب ويطمئن إليه.'],
        chips=['الجزم', 'التصديق القلبي', 'الاستقرار', 'الاطمئنان']),
   dict(t='المعرفة والقول والاعتقاد', bullets=[
        '<b>المعرفة وحدها لا تكفي:</b> ﴿وَجَحَدُوا بِهَا وَاسْتَيْقَنَتْهَا أَنْفُسُهُمْ﴾ <i>[النمل: ١٤]</i>',
        '<b>القول وحده لا يكفي:</b> ﴿يَقُولُونَ بِأَلْسِنَتِهِمْ مَا لَيْسَ فِي قُلُوبِهِمْ﴾ <i>[الفتح: ١١]</i>',
        '<b>المطلوب الجزم:</b> ﴿ثُمَّ لَمْ يَرْتَابُوا﴾ <i>[الحجرات: ١٥]</i>']),
   dict(t='مراتب الإدراك', table=[['الاعتقاد الجازم', 'تصديق لا تردد فيه'], ['الظن', 'احتمال راجح مع بقاء احتمال النقيض'], ['الشك', 'احتمالان متساويان'], ['الوهم', 'احتمال مرجوح']],
        note='وليس كل جازم صحيحًا: المطلوب جزمٌ في القلب ومضمونٌ موافق للشرع.'),
   dict(t='حقيقة الاعتقاد: ثلاثة معانٍ', bullets=[
        'الله وحده هو المستحق للعبادة <i>[الأنعام: ١٠٢]</i>',
        'كل عبادة صُرفت لغيره باطلة <i>[الحج: ٦٢]</i>',
        'كل ما سواه لا يستحق شيئًا منها <i>[النساء: ١٧٢]</i>'],
        note='بدأت العبارة بـ«أن تعتقد» قبل «أن تترك»: المقصود أولًا ما يعتقده القلب.'),
   dict(t='الأدلة الشرعية', bullets=[
        '﴿وَأَنَّ مَا يَدْعُونَ مِنْ دُونِهِ هُوَ الْبَاطِلُ﴾ <i>[الحج: ٦٢]</i>',
        '﴿أَنِ اعْبُدُوا اللَّهَ وَاجْتَنِبُوا الطَّاغُوتَ﴾ <i>[النحل: ٣٦]</i>',
        '﴿فَمَنْ يَكْفُرْ بِالطَّاغُوتِ وَيُؤْمِنْ بِاللَّهِ﴾ <i>[البقرة: ٢٥٦]</i>',
        '﴿إِنَّنِي بَرَاءٌ مِمَّا تَعْبُدُونَ ۝ إِلَّا الَّذِي فَطَرَنِي﴾ <i>[الزخرف: ٢٦–٢٧]</i>',
        '«مَنْ قَالَ: لَا إِلَهَ إِلَّا اللَّهُ، وَكَفَرَ بِمَا يُعْبَدُ مِنْ دُونِ اللَّهِ…» <i>[مسلم: ٢٣]</i>']),
   dict(t='مسائل تطبيقية', wide=True, bullets=[
        '<b>الترك وحده لا يكفي:</b> قد يكون للبيئة والعادة، أما الاعتقاد فحكم شرعي ثابت.',
        '<b>أنواع العبادة:</b> الدعاء، والذبح، والنذر، والسجود، والتوكل والخوف والرجاء التعبدي؛ وليس كل فعل عبادة.',
        '<b>كلمة التوحيد:</b> «لا إله» نفي يقابل الكفر بالطاغوت، و«إلا الله» إثبات يقابل الإيمان بالله.',
        '<b>لا خلط:</b> بطلان العبادة غير الحكم على المعبود، وغير الحكم على فاعلها المعيّن.']),
  ],
  jamiaT='العبارة الجامعة',
  jamia='اعتقاد بطلان عبادة الطاغوت هو أن يجزم المسلم بقلبه، بعد فهم حقيقة المسألة، بأن الله وحده هو المستحق للعبادة، وأن كل عبادة صُرفت لغيره باطلة لا تصح شرعًا، وأن كل مخلوق سواه لا يستحق شيئًا من العبادة، مهما بلغت منزلته أو صلاحه؛ وهذا الاعتقاد تصديق قلبي جازم بالحق الذي جاء به الوحي.',
  src='المصادر: الآيات من المصحف الشريف (رواية حفص)؛ عبارة الشيخ من رسالته «معنى الطاغوت ورؤوس أنواعه»؛ الحديث في صحيح مسلم، كتاب الإيمان (٢٣).',
 ),
 (1, 'tr'): dict(
  eb='Tâğutu inkârın keyfiyeti · Birinci husus · Ders özeti',
  sub='Dersin tam haritası tek sayfada',
  blocks=[
   dict(t='Dersin Esası', p=['Şeyh Muhammed b. Abdülvehhab’a göre tâğutu inkârın keyfiyeti beş husustur:'],
        chips=['İtikad ← dersimiz', 'Terk', 'Buğz', 'Tekfir', 'Düşmanlık'], on=0),
   dict(t='İtikadın Anlamı', p=['<b>Sözlükte:</b> «akd» kökünden: bağlamak, düğümlemek, sağlamlaştırmak.', '<b>Terim olarak:</b> Bir şeye kesin olarak ve kalben tasdik ederek inanmak; öyle ki kalpte yerleşsin ve kalp ona mutmain olsun.'],
        chips=['Kesinlik', 'Kalbî tasdik', 'Yerleşiklik', 'İtminan']),
   dict(t='Bilgi, Söz ve İtikad', bullets=[
        '<b>Bilgi tek başına yetmez:</b> «Kalpleri kesin olarak inandığı hâlde… inkâr ettiler.» <i>(Neml, 14)</i>',
        '<b>Söz tek başına yetmez:</b> «Kalplerinde olmayanı dilleriyle söylerler.» <i>(Fetih, 11)</i>',
        '<b>İstenen kesinliktir:</b> «…sonra hiç şüpheye düşmeyenler.» <i>(Hucurât, 15)</i>']),
   dict(t='İdrak Mertebeleri', table=[['Kesin itikad', 'Tereddüt içermeyen tasdik'], ['Zan', 'Karşıt ihtimal devam ederken ağır basan ihtimal'], ['Şek', 'Eşit iki ihtimal'], ['Vehim', 'Zayıf ihtimal']],
        note='Her kesin inanç doğru değildir: istenen, kalpte kesinlik ve şeriata uygun içeriktir.'),
   dict(t='İtikadın Hakikati: Üç Anlam', bullets=[
        'İbadete yalnızca Allah layıktır <i>(En’âm, 102)</i>',
        'O’ndan başkasına yapılan her ibadet bâtıldır <i>(Hac, 62)</i>',
        'O’ndan başka hiçbir şey ibadetten bir şeye layık değildir <i>(Nisâ, 172)</i>'],
        note='İfade «terk etmen»den önce «inanman» ile başlar: önce kalbin neye inandığı kastedilir.'),
   dict(t='Şer’î Deliller', bullets=[
        'Hac, 62 · Nahl, 36 · Bakara, 256 · Zuhruf, 26–27',
        'Târık b. Eşyem hadisi: «Kim Lâ ilâhe illallah der ve Allah’tan başka ibadet edilenleri inkâr ederse, malı ve kanı haram olur…» <i>(Müslim, 23)</i>']),
   dict(t='Uygulamalı Meseleler', wide=True, bullets=[
        '<b>Sadece terk yetmez:</b> çevre ve alışkanlıktan olabilir; itikad ise sabit bir şer’î hükümdür.',
        '<b>İbadet çeşitleri:</b> dua, kurban, adak, secde, tevekkül, korku ve ümit; her fiil ibadet değildir.',
        '<b>Tevhid kelimesi:</b> «Lâ ilâhe» nefy = tâğutu inkâr; «illallah» isbat = Allah’a iman.',
        '<b>Karıştırılmamalı:</b> ibadetin bâtıllığı, mabud ve belirli âbid hakkındaki hükümden farklıdır.']),
  ],
  jamiaT='Özet ifade',
  jamia='Müslümanın; ibadete yalnızca Allah’ın layık olduğuna, O’ndan başkasına yöneltilen her ibadetin bâtıl olduğuna ve makamı ne olursa olsun hiçbir mahlûkun ibadetten bir şeye layık olmadığına kalben kesin olarak inanmasıdır.',
  src='Kaynaklar: Ayetler Mushaf’tan (Hafs rivayeti); Şeyhin sözü «Ma‘ne’t-Tâğût ve Ruûsu Envâih» risalesinden; hadis Müslim, Îmân 23. Meal ifadeleri hazırlayana aittir.',
 ),
 (2, 'ar'): dict(
  eb='صفة الكفر بالطاغوت · النقطة الثانية · ملخص الدرس',
  sub='الخريطة الكاملة للدرس في صفحة واحدة',
  blocks=[
   dict(t='أصل الدرس', p=['قال الشيخ محمد بن عبد الوهاب: صفة الكفر بالطاغوت <b>«أن تعتقد بطلان عبادة غير الله، وتتركها، وتبغضها، وتكفّر أهلها، وتعاديهم»</b>.'],
        chips=['الاعتقاد', 'الترك ← درسنا', 'البغض', 'التكفير', 'المعاداة'], on=1),
   dict(t='معنى الترك', p=['<b>لغةً:</b> مفارقة الشيء والتخلّي عنه: ﴿إِنِّي تَرَكْتُ مِلَّةَ قَوْمٍ﴾ <i>[يوسف: ٣٧]</i>.', '<b>الاجتناب:</b> أن تكون في جانب والشيء في جانب؛ وهو أبلغ من الترك.', '<b>اصطلاحًا:</b> أن يمتنع المسلم عن صرف أي عبادة لغير الله، ويبتعد عن وسائلها ومواضعها، امتثالًا لأمر الله.']),
   dict(t='صور الترك الأربع', bullets=[
        '<b>ترك صرف العبادة لغير الله:</b> دعاءً وذبحًا ونذرًا وسجودًا.',
        '<b>ترك المشاركة فيها مع أهلها</b> ولو لم يباشر الفعل.',
        '<b>اجتناب الوسائل والذرائع:</b> كالغلو في الصالحين.',
        '<b>الثبات على الترك</b> ولو خالفه الناس.'],
        chips=['القلب', 'اللسان', 'الجوارح'], chipsLabel='ميادين الترك:'),
   dict(t='الاعتقاد والترك', table=[['ترك بلا اعتقاد', 'عادة أو بيئة؛ لا يكفي'], ['اعتقاد بلا ترك', 'يزعم بطلانها ثم يفعلها؛ تناقض'], ['اعتقاد وترك', 'يعتقد بطلانها ويتركها لله؛ هو المطلوب']],
        note='الاعتقاد أصل، والترك ثمرته وبرهانه.'),
   dict(t='الترك وكلمة التوحيد', bullets=[
        '<b>النفي «لا إله»:</b> في القلب اعتقاد البطلان، وفي العمل ترك عبادة غير الله.',
        '<b>الإثبات «إلا الله»:</b> إفراد الله وحده بالعبادة.',
        '«مَنْ قَالَ: لَا إِلَهَ إِلَّا اللَّهُ، وَكَفَرَ بِمَا يُعْبَدُ مِنْ دُونِ اللَّهِ…» <i>[مسلم: ٢٣]</i>'],
        note='من قالها ثم صرف العبادة لغير الله نقض بعمله ما أثبته بلسانه.'),
   dict(t='الأدلة الشرعية', bullets=[
        '﴿أَنِ اعْبُدُوا اللَّهَ وَاجْتَنِبُوا الطَّاغُوتَ﴾ <i>[النحل: ٣٦]</i>',
        '﴿وَالَّذِينَ اجْتَنَبُوا الطَّاغُوتَ أَنْ يَعْبُدُوهَا﴾ <i>[الزمر: ١٧]</i>',
        '﴿وَأَعْتَزِلُكُمْ وَمَا تَدْعُونَ مِنْ دُونِ اللَّهِ﴾ <i>[مريم: ٤٨]</i>',
        '﴿وَإِذِ اعْتَزَلْتُمُوهُمْ وَمَا يَعْبُدُونَ إِلَّا اللَّهَ﴾ <i>[الكهف: ١٦]</i>',
        '﴿لَا أَعْبُدُ مَا تَعْبُدُونَ﴾ <i>[الكافرون: ٢]</i>',
        'حديث بُوانة: «هَلْ كَانَ فِيهَا وَثَنٌ مِنْ أَوْثَانِ الْجَاهِلِيَّةِ يُعْبَدُ؟» <i>[أبو داود]</i>']),
   dict(t='مسائل تطبيقية وثمرات', wide=True, bullets=[
        '<b>في الشدة:</b> يفزع إلى الله وحده، ويترك الاستغاثة بالأموات.',
        '<b>الذبح والنذر والمراسم:</b> لا يشارك في ذبيحة لصاحب قبر، ولا يحضر احتفالًا تُصرف فيه عبادة لغير الله.',
        '<b>العادات الموروثة:</b> يتركها إن كانت عبادة لغير الله ولو انتشرت، كما ترك إبراهيم ما عليه قومه.',
        '<b>لا خلط:</b> ترك العبادة لا يعني ترك البرّ والتعامل المباح <i>[الممتحنة: ٨]</i>.',
        '<b>الثمرات:</b> البشرى، والعوض الخير، والهداية والرحمة، وصدق التوحيد، وحرية القلب.']),
  ],
  jamiaT='العبارة الجامعة',
  jamia='ترك عبادة الطاغوت هو أن يمتنع المسلم عن صرف أي عبادة لغير الله بقلبه ولسانه وجوارحه، ويجتنب ما يفضي إليها، امتثالًا لأمر الله، ويثبت على ذلك ولو خالفه الناس؛ وهو الثمرة العملية لاعتقاد بطلانها، والبرهان على صدقه.',
  src='المصادر: الآيات من المصحف الشريف (رواية حفص)؛ عبارة الشيخ من رسالته «معنى الطاغوت ورؤوس أنواعه»؛ حديث «من قال لا إله إلا الله» في صحيح مسلم، كتاب الإيمان (٢٣)؛ حديث بُوانة رواه أبو داود والبيهقي.',
 ),
 (2, 'tr'): dict(
  eb='Tâğutu inkârın keyfiyeti · İkinci husus · Ders özeti',
  sub='Dersin tam haritası tek sayfada',
  blocks=[
   dict(t='Dersin Esası', p=['Şeyh Muhammed b. Abdülvehhab’a göre tâğutu inkârın keyfiyeti beş husustur:'],
        chips=['İtikad', 'Terk ← dersimiz', 'Buğz', 'Tekfir', 'Düşmanlık'], on=1),
   dict(t='Terkin Anlamı', p=['<b>Sözlükte:</b> bir şeyden ayrılıp onu bırakmak <i>(Yûsuf, 37)</i>.', '<b>İctinab:</b> sen bir yanda, o şey başka bir yanda; terkten daha kapsamlıdır.', '<b>Terim olarak:</b> Allah’ın emrine uyarak O’ndan başkasına hiçbir ibadet yöneltmemek, vasıtalarından ve mekânlarından uzak durmak.']),
   dict(t='Terkin Dört Şekli', bullets=[
        '<b>İbadeti başkasına yöneltmemek:</b> dua, kurban, adak, secde.',
        '<b>Ehliyle birlikte katılmamak,</b> bizzat yapmasa bile.',
        '<b>Vasıtalardan kaçınmak:</b> salihler hakkında aşırılık gibi.',
        '<b>Terkte sebat etmek,</b> insanlar muhalefet etse de.'],
        chips=['Kalp', 'Dil', 'Azalar'], chipsLabel='Terkin alanları:'),
   dict(t='İtikad ve Terk', table=[['İtikadsız terk', 'Âdet ya da çevre; yeterli değildir'], ['Terksiz itikad', 'Bâtıl der, sonra yapar; çelişkidir'], ['İtikad ve terk', 'Bâtıl olduğuna inanır, Allah için terk eder; istenen budur']],
        note='İtikad asıldır; terk onun meyvesi ve delilidir.'),
   dict(t='Terk ve Tevhid Kelimesi', bullets=[
        '<b>Nefy «Lâ ilâhe»:</b> kalpte bâtıllığa itikad, amelde terk.',
        '<b>İsbat «illallah»:</b> ibadette yalnız Allah’ı birlemek.',
        '«Kim Lâ ilâhe illallah der ve Allah’tan başka ibadet edilenleri inkâr ederse…» <i>(Müslim, 23)</i>'],
        note='Söyleyip ibadeti başkasına yönelten, sözünü ameliyle bozar.'),
   dict(t='Şer’î Deliller', bullets=[
        '«Allah’a ibadet edin ve tâğuttan kaçının.» <i>(Nahl, 36)</i>',
        '«Tâğuta ibadet etmekten kaçınanlar…» <i>(Zümer, 17)</i>',
        'İbrahim’in uzaklaşması <i>(Meryem, 48)</i> · Ashâb-ı Kehf <i>(Kehf, 16)</i>',
        '«Sizin ibadet ettiklerinize ibadet etmem.» <i>(Kâfirûn, 2)</i>',
        'Buvâne hadisi: «Orada ibadet edilen bir put var mıydı?» <i>(Ebû Dâvûd)</i>']),
   dict(t='Uygulamalı Meseleler ve Meyveler', wide=True, bullets=[
        '<b>Sıkıntıda:</b> yalnız Allah’a sığınır, ölülerden medet istemeyi terk eder.',
        '<b>Kurban, adak ve törenler:</b> kabir sahibi için kesilen kurbana ve Allah’tan başkasına ibadet edilen törene katılmaz.',
        '<b>Miras kalan âdetler:</b> yaygın olsa da Allah’tan başkasına ibadet olanı terk eder, İbrahim gibi.',
        '<b>Karıştırılmamalı:</b> ibadeti terk, iyiliği ve mübah ilişkiyi terk etmek değildir <i>(Mümtehine, 8)</i>.',
        '<b>Meyveleri:</b> müjde, hayırlı karşılık, hidayet ve rahmet, tevhidin sadakati, kalbin özgürlüğü.']),
  ],
  jamiaT='Özet ifade',
  jamia='Tâğuta ibadeti terk etmek; Müslümanın Allah’tan başkasına hiçbir ibadeti kalbiyle, diliyle ve azalarıyla yöneltmemesi, buna götüren şeylerden kaçınması, bunu Allah’ın emrine uymak için yapması ve insanlar muhalefet etse de bunda sebat etmesidir.',
  src='Kaynaklar: Ayetler Mushaf’tan (Hafs rivayeti); Şeyhin sözü «Ma‘ne’t-Tâğût ve Ruûsu Envâih» risalesinden; «Lâ ilâhe illallah» hadisi Müslim, Îmân 23; Buvâne hadisi Ebû Dâvûd ve Beyhakî. Meal ifadeleri hazırlayana aittir.',
 ),
}
