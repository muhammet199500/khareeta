# -*- coding: utf-8 -*-
"""Tap-a-word meanings on the written lesson pages (text.html).

TR: Turkish lesson words a general reader may not know. Each entry:
    k   key
    re  regex for the word and its suffixed forms (Turkish case on the first letter written out)
    w   headword shown in the popup
    m   plain-Turkish meaning
    src optional: where the meaning comes from. Leave it out for an everyday-word explanation;
        never invent one. «Bu dersteki tanım» = the lesson defines it itself.
AR: Arabic lesson words → a key of sharh.GLOSS (meanings there are sourced).
    The word is matched with or without tashkeel, after an optional و/ف/ب/ل/ك.

Only the first occurrence in each main section (h2) is marked, so a reader who jumps to a
section still finds it, and the page does not fill with underlines. Headings, links and
Qur'an text ﴿…﴾ are never marked.
"""

DERS = 'Bu dersteki tanım'

TR = [
    # ── fıkıh ──
    dict(k='fikih', re=r'(?<!el-)[Ff]ıkh?\w*', w='Fıkıh', m='Sözlükte «anlamak». Dinde: amelle ilgili şer’î hükümleri ayrıntılı delilleriyle bilmek.', src=DERS),
    dict(k='istilah', re=r'[Iı]stılah\w*', w='Istılah', m='Bir ilmin kendi içinde kullandığı özel anlam (terim anlamı). «Istılahta» = dinî terim olarak.'),
    dict(k='icma', re=r'[İi]cmâ\w*', w='İcmâ', m='Müslüman âlimlerin dinî bir hükümde görüş birliği etmesi.'),
    dict(k='kiyas', re=r'[Kk]ıyas\w*', w='Kıyas', m='Hükmü âyet veya hadiste açıkça geçmeyen bir meseleye, aynı sebebi taşıyan ve hükmü bilinen bir meselenin hükmünü vermek.'),
    dict(k='mukellef', re=r'[Mm]ükellef\w*', w='Mükellef', m='Dinin emir ve yasaklarından sorumlu olan kimse: akıllı ve ergenlik çağına girmiş kişi.'),
    dict(k='muamelat', re=r'[Mm]uamelât\w*', w='Muamelât', m='İnsanlar arasındaki alışveriş, kira gibi işlerle ilgili hükümler.'),
    dict(k='taharet', re=r'[Tt]aharet\w*', w='Taharet', m='Temizlik. Fıkıhta: hadesi kaldırmak ve necaseti gidermek.', src=DERS),
    dict(k='hades', re=r'[Hh]ades\w*', w='Hades', m='Abdestsizlik veya cünüplük hâli: bedende bulunan ve namaz gibi ibadetlere engel olan durum. Küçük hades abdestle, büyük hades gusülle kalkar.', src='Kitabın dipnotu (1/ 1)'),
    dict(k='necaset', re=r'[Nn]ecaset\w*', w='Necaset', m='Pislik; idrar ve dışkı gibi. Beden, elbise veya mekânda bulunur ve giderilmesiyle temizlenir. Arapçada «habes» de denir.', src='Kitabın dipnotu (1/ 1)'),
    dict(k='necis', re=r'[Nn]ecis\w*', w='Necis', m='Pis; temiz olmayan.'),
    dict(k='tahur', re=r'[Tt]ahûr\w*', w='Tahûr', m='Hem kendisi temiz hem de başkasını temizleyen su; yağmur, kuyu ve deniz suyu gibi.', src=DERS),
    dict(k='gusul', re=r'[Gg]us(?:ül|l)\w*', w='Gusül', m='Boy abdesti: niyet ederek bütün bedeni yıkamak.'),
    dict(k='teyemmum', re=r'[Tt]eyemmüm\w*', w='Teyemmüm', m='Su bulunmadığında veya kullanılamadığında, abdest ya da gusül yerine temiz toprakla yapılan temizlik.'),
    dict(k='cunup', re=r'[Cc]ünüp\w*', w='Cünüp', m='Gusül (boy abdesti) alması gereken hâldeki kimse.'),
    dict(k='hayiz', re=r'[Hh]ayız\w*', w='Hayız', m='Kadının aylık âdet hâli.'),
    dict(k='kulle', re=r'[Kk]ulle\w*', w='Kulle', m='Büyük testi. İki kulle yaklaşık beş kırba, yani yaklaşık 160,5 litre su eder.', src='Kitabın dipnotu (1/ 3)'),
    dict(k='kirba', re=r'[Kk]ırba\w*', w='Kırba', m='Deriden yapılmış su tulumu.'),
    dict(k='sidr', re=r'[Ss]idr\w*', w='Sidr', m='Nebk ağacı (bir tür hünnap ağacı). Hadiste geçtiği gibi yaprağı suya katılarak yıkanmada kullanılırdı.', src='İbn Sîde, el-Muhkem (8/ 445)'),
    dict(k='usnan', re=r'[Üü]şnan\w*', w='Üşnan', m='Çorak ve tuzlu yerlerde yetişen otlardan bir bitki; elleri yıkamada kullanılır.', src='Kitabın dipnotu (1/ 3)'),
    dict(k='sur', re=r'[Ss]ür’\w*', w='Sür’', m='Artık su: bir insan veya hayvan içtikten sonra kapta kalan su.', src=DERS),
    dict(k='vasif', re=r'[Vv]as(?:ıf|f)\w*', w='Vasıf', m='Özellik. Suyun üç vasfı: kokusu, tadı ve rengi.'),
    dict(k='nekre', re=r'[Nn]ekre\w*', w='Nekre', m='Arapça dil bilgisinde belirsiz isim. Olumsuz bir cümlede geçerse, o türün hepsini kapsar.'),
    dict(k='hasen', re=r'(?<=«)hasen\b', w='Hasen', m='Hadis ilminde: delil olarak kabul edilen, derecesi sahihe yakın hadis.'),
    # ── tevhid ──
    dict(k='tagut', re=r'[Tt]âğut\w*', w='Tâğut', m='Kulun Allah’a karşı haddini aştığı her şey: Allah’ı bırakıp kendisine ibadet edilen (ve buna razı olan), uyulan veya itaat edilen.', src='Bu dersteki tanım (İbnü’l-Kayyim)'),
    dict(k='itikad', re=r'[İi]tikad\w*', w='İtikad', m='Kalbin bir şeye kesin olarak inanması; kalbe yerleşen ve sarsılmayan inanç.', src=DERS),
    dict(k='keyfiyet', re=r'[Kk]eyfiyet\w*', w='Keyfiyet', m='Bir şeyin nasıl olduğu, nasıl yapıldığı.'),
    dict(k='batil', re=r'[Bb]âtıl\w*', w='Bâtıl', m='Geçersiz, boş; haktan uzak olan.'),
    dict(k='bugz', re=r'[Bb]uğz\w*', w='Buğz', m='Sevmemek, hoşlanmamak; sevginin zıddı.', src=DERS),
    dict(k='tekfir', re=r'[Tt]ekfir\w*', w='Tekfir', m='Bir kimsenin kâfir olduğuna hükmetmek.'),
    dict(k='ictinab', re=r'[İi]ctinab\w*', w='İctinab', m='Bir şeyden uzak durmak: onu yapmamak ve ona götüren yollardan da sakınmak.', src=DERS),
    dict(k='nefy', re=r'[Nn]efy\w*', w='Nefy', m='Reddetmek, olumsuzlamak. «Lâ ilâhe» (hiçbir ilah yoktur) kısmı nefydir.', src=DERS),
    dict(k='isbat', re=r'[İi]sbat\w*', w='İsbat', m='Kabul edip ortaya koymak. «illallah» (ancak Allah) kısmı isbattır.', src=DERS),
    dict(k='rukun', re=r'[Rr]ük(?:ün|n)\w*', w='Rükün', m='Bir şeyin temel parçası; o olmadan şeyin kendisi olmaz.'),
    dict(k='muvahhid', re=r'[Mm]uvahhid\w*', w='Muvahhid', m='Allah’ı birleyen, ibadeti yalnız O’na yapan kimse.'),
    dict(k='mabud', re=r'[Mm]abud\w*', w='Mabud', m='İbadet edilen.'),
    dict(k='beri', re=r'\bberi(?:dir|\b(?= ol))', w='Beri olmak', m='Uzak olmak, ilgisini kesmek.'),
    dict(k='beraat', re=r'[Bb]eraat\w*', w='Beraat', m='Uzak olmak, ilgiyi kesmek.'),
    dict(k='inabe', re=r'[İi]nâbe\w*', w='İnâbe', m='Allah’a yönelmek, O’na dönmek.'),
    dict(k='mutmain', re=r'[Mm]utmain\w*', w='Mutmain', m='Kalbi yatışmış, emin ve huzurlu.'),
    dict(k='reyb', re=r'\b[Rr]eyb\w*', w='Reyb', m='Şüphe.'),
    dict(k='tugyan', re=r'[Tt]uğyan\w*', w='Tuğyan', m='Haddi aşmak, taşkınlık.'),
    dict(k='selef', re=r'\bSelef\w*', w='Selef', m='Sahabe ve onlardan sonra gelen ilk nesillerin âlimleri.'),
    dict(k='munker', re=r'[Mm]ünker\w*', w='Münker', m='Dinin kötü saydığı ve yasakladığı iş.'),
    dict(k='meveddet', re=r'[Mm]eveddet\w*', w='Meveddet', m='Kalpten sevgi ve dostluk bağı.'),
    dict(k='kerahiyet', re=r'[Kk]erâhiyet\w*', w='Kerâhiyet', m='Hoşlanmamak.'),
    dict(k='gayb', re=r'\b[Gg]ayb\w*', w='Gayb', m='İnsanların göremediği ve bilemediği şeyler; onları ancak Allah bilir.'),
    dict(k='gaip', re=r'\b[Gg]aip\w*', w='Gaip', m='Orada bulunmayan, uzakta olan.'),
    dict(k='cahiliye', re=r'[Cc]ahiliye\w*', w='Cahiliye', m='İslam’dan önceki dönem ve o dönemin bâtıl âdetleri.'),
    dict(k='aza', re=r'\b[Aa]zalar\w*', w='Azalar', m='Beden organları: el, dil, ayak gibi.'),
    dict(k='medet', re=r'\b[Mm]edet\b', w='Medet istemek', m='Sıkıntı anında yardım istemek.'),
    dict(k='munafik', re=r'[Mm]ünafık\w*', w='Münafık', m='İçinden inanmadığı hâlde dışından Müslüman görünen kimse.'),
    dict(k='ehlikitap', re=r'Ehl-i Kitap\w*', w='Ehl-i Kitap', m='Yahudiler ve Hristiyanlar.'),
    dict(k='zahir', re=r'[Zz]ahir(?:î|en)\w*', w='Zahirî', m='Dış görünüşe ait; dıştan görünen.'),
    dict(k='vacip', re=r'\b[Vv]acip\w*', w='Vacip', m='Yapılması zorunlu olan.'),
    dict(k='haslet', re=r'[Hh]aslet\w*', w='Haslet', m='Güzel huy, özellik.'),
    dict(k='fisk', re=r'\b[Ff]ısk\w*', w='Fısk', m='Allah’ın emrinin dışına çıkmak; büyük günah işlemek.'),
    dict(k='munezzeh', re=r'[Mm]ünezzeh\w*', w='Münezzeh', m='Her türlü eksiklikten uzak.'),
]

# Arabic lesson pages: word forms (bare letters) → sharh.GLOSS key
AR = [
    ('الحدث', 'hadath'),
    ('الخبث', 'khabath'),
    ('قلتين', 'qulla'), ('القلتين', 'qulla'), ('القلتان', 'qulla'), ('قلتان', 'qulla'), ('القلة', 'qulla'),
    ('الأشنان', 'ushnan'), ('أشنان', 'ushnan'),
    ('السدر', 'sidr'), ('سدر', 'sidr'),
    ('ولغ', 'walagh'),
    ('رجس', 'rijs'),
]

# Arabic lesson pages: terms with a plain meaning written here (no source line unless one is real).
# docs: optional, only in these lessons (a word whose meaning depends on the lesson).
# forms: the word as it is written in the lessons, bare letters (tashkeel and alif/hamza forms are ignored when matching).
AR_TERMS = [
    dict(k='a_ijma', forms=['الإجماع', 'إجماع'], w='الإجماع', m='اتفاق علماء المسلمين المجتهدين في عصرٍ من العصور على حكم شرعي.'),
    dict(k='a_qiyas', forms=['القياس', 'قياس'], w='القياس', m='إعطاء مسألةٍ لم يأتِ فيها نص حكمَ مسألةٍ جاء فيها نص؛ لاشتراكهما في سبب الحكم (العلّة).'),
    dict(k='a_sunna', forms=['السنة'], w='السنة', m='ما ثبت عن النبي ﷺ من قول أو فعل أو تقرير.'),
    dict(k='a_istilah', forms=['اصطلاحا', 'الاصطلاح'], w='اصطلاحًا', m='أي: في المعنى الخاص الذي يستعمله أهل العلم لهذه الكلمة، لا في معناها اللغوي العام.'),
    dict(k='a_mukallaf', forms=['المكلفين', 'المكلف', 'مكلف'], w='المكلَّف', m='البالغ العاقل الذي تلزمه أوامر الشرع ونواهيه.'),
    dict(k='a_muamalat', forms=['المعاملات'], w='المعاملات', m='أحكام ما يجري بين الناس من بيعٍ وإجارةٍ ونحوهما.'),
    dict(k='a_tahur', forms=['الطهور'], w='الطَّهور', m='الماء الطاهر في نفسه، المطهِّر لغيره؛ كماء المطر والبئر والبحر.'),
    dict(k='a_sur', forms=['السؤر', 'الأسآر', 'سؤر'], w='السُّؤر', m='ما يبقى في الإناء بعد أن يشرب منه الشارب، إنسانًا كان أو حيوانًا.'),
    dict(k='a_nakira', forms=['نكرة'], w='نكرة', m='اسمٌ غير معيَّن، مثل «ماء» لا «الماء». وإذا جاءت النكرة بعد نفيٍ شملت كل أفرادها.'),
    dict(k='a_junub', forms=['الجنب', 'جنبا'], w='الجُنُب', m='من وجب عليه الغُسل.'),
    dict(k='a_haid', forms=['الحائض'], w='الحائض', m='المرأة في أيام حيضها (عادتها الشهرية).'),
    dict(k='a_taghut', forms=['الطاغوت'], w='الطاغوت', m='قال ابن القيم: «الطاغوت ما تجاوز به العبد حدّه من معبود أو متبوع أو مطاع».'),
    dict(k='a_itiqad', forms=['الاعتقاد', 'اعتقاد'], w='الاعتقاد', m='تصديق القلب الجازم بالشيء، حتى يستقر فيه فلا يتزلزل.'),
    dict(k='a_nafy', docs=('lesson1', 'lesson2', 'lesson3'), forms=['النفي'], w='النفي', m='في كلمة التوحيد: «لا إله»، أي نفي استحقاق العبادة عن كل ما سوى الله.'),
    dict(k='a_ithbat', docs=('lesson1', 'lesson2', 'lesson3'), forms=['الإثبات'], w='الإثبات', m='في كلمة التوحيد: «إلا الله»، أي إثبات استحقاق العبادة لله وحده.'),
    dict(k='a_takfir', forms=['التكفير'], w='التكفير', m='الحكم على الشخص بأنه كافر.'),
    dict(k='a_inaba', forms=['الإنابة'], w='الإنابة', m='الرجوع إلى الله والإقبال عليه.'),
    dict(k='a_munkar', forms=['منكرا', 'المنكر'], w='المنكر', m='كل ما نهى عنه الشرع وقبّحه.'),
    dict(k='a_ghayb', forms=['الغيب'], w='الغيب', m='ما غاب عن الناس فلا يعلمونه، ولا يعلمه إلا الله.'),
]
