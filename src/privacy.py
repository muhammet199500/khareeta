"""Privacy policy text (Arabic and Turkish). Kept in its own file so the teacher can review it.
CONTACT is the public contact address shown in the policy and in the store listing."""
CONTACT = 'iletisim@tevhidim.com'
UPDATED = {'ar': '٢٥ نوفمبر ٢٠٢٦', 'tr': '25 Kasım 2026'}

PRIVACY = {
'ar': dict(title='سياسة الخصوصية', sub='ما الذي يحفظه موقع «وتواصوا بالحق» وتطبيقه، وما الذي لا يحفظه.', updated='آخر تحديث', body=[
 ('باختصار', [
  'لا يحتاج الموقع إلى حساب ولا تسجيل، ولا نطلب اسمك ولا بريدك ولا رقم هاتفك.',
  'تقدّمك في الدروس، وإجاباتك في الواجبات، واسمك الذي تكتبه عند إرسال الواجب، كل ذلك يُحفظ على جهازك أنت فقط، ولا يصل إلينا.',
  'لا نبيع أي بيانات، ولا نعرض إعلانات، ولا نستعمل ملفات تعريف الارتباط (cookies) للتتبّع.',
 ]),
 ('ما يُحفظ على جهازك فقط', [
  'علامات «أنهيتُ» في الدروس والواجبات، وأفضل نتيجة في الاختبار، وحجم الخط، وآخر درس فتحته.',
  'إجاباتك في متابعة الواجب اليومي والمحاسبة الختامية، واسمك إن كتبته في خانة إرسال الواجب.',
  'نسخة من صفحات الموقع ليعمل دون إنترنت.',
  'تستطيع حذف ذلك كله في أي وقت بمسح بيانات الموقع من إعدادات المتصفح، أو بزر «مسح تقدّمي المحفوظ على هذا الجهاز».',
 ]),
 ('إرسال الواجب', [
  'عند ضغط «أرسِل واجبي» يُصنع ملف PDF على جهازك، وأنت تختار التطبيق الذي ترسله به (مثل واتساب أو تيليجرام) والشخص الذي يصله. لا يمرّ الملف بخوادمنا.',
 ]),
 ('التذكير بالواجب (اختياري)', [
  'إن ضغطت «فعّل التذكير» وسمحت بالإشعارات، نحفظ لدى خدمتنا على Cloudflare: عنوان الإشعارات الذي يعطيه متصفحك لهذا الغرض، ومنطقتك الزمنية، ولغة الموقع، وتاريخ آخر يوم ضغطت فيه «أنهيتُ»، ورقمًا عشوائيًا يميّز جهازك.',
  'لا نعرف من هذه البيانات اسمك ولا هويتك، ونستعملها لإرسال التذكير في وقته وإيقافه حين تنهي واجبك فقط.',
  'تُحذف حين تضغط «أوقِف التذكير»، أو حين تمنع الإشعارات من إعدادات جهازك.',
 ]),
 ('إحصاءات الزيارات', [
  'نستعمل Cloudflare Web Analytics لمعرفة أعداد الزيارات العامة والصفحات الأكثر قراءة. لا يستعمل ملفات تعريف الارتباط، ولا يتتبّع الزائر من موقع إلى آخر، ولا يعرّفنا بأي زائر بعينه.',
 ]),
 ('الاستضافة', [
  'يُستضاف الموقع على GitHub Pages، ويمرّ نطاقه عبر Cloudflare. هذه الخدمات تعالج بيانات تقنية لازمة لإيصال الصفحات إليك، مثل عنوان IP، بحسب سياسات الخصوصية الخاصة بها.',
 ]),
 ('الأطفال', [
  'الدروس موجّهة للعامة، ولا نجمع عمدًا بيانات شخصية من أحد، صغيرًا كان أو كبيرًا.',
 ]),
 ('التواصل والتعديلات', [
  f'لأي سؤال عن الخصوصية راسلنا على: {CONTACT}',
  'إن عدّلنا هذه السياسة نضع تاريخ التعديل في أعلاها.',
 ]),
]),
'tr': dict(title='Gizlilik Politikası', sub='«Ve Tevâsav bi’l-Hak» sitesi ve uygulamasının neyi sakladığı, neyi saklamadığı.', updated='Son güncelleme', body=[
 ('Kısaca', [
  'Site hesap ya da kayıt gerektirmez; adınızı, e-postanızı veya telefon numaranızı istemeyiz.',
  'Derslerdeki ilerlemeniz, ödev cevaplarınız ve ödevi gönderirken yazdığınız adınız yalnızca kendi cihazınızda saklanır; bize ulaşmaz.',
  'Hiçbir veriyi satmayız, reklam göstermeyiz ve takip amaçlı çerez (cookie) kullanmayız.',
 ]),
 ('Yalnızca cihazınızda saklananlar', [
  'Derslerdeki ve ödevlerdeki «Bitirdim» işaretleri, testteki en iyi sonucunuz, yazı boyutu ve en son açtığınız ders.',
  'Günlük ödev takibindeki ve son muhasebedeki cevaplarınız; ödev gönderme alanına yazdıysanız adınız.',
  'Sitenin internetsiz çalışması için sayfaların bir kopyası.',
  'Bunların hepsini istediğiniz zaman tarayıcı ayarlarından site verilerini silerek ya da «Bu cihazda kayıtlı ilerlememi sil» düğmesiyle silebilirsiniz.',
 ]),
 ('Ödevin gönderilmesi', [
  '«Ödevimi gönder»e dokunduğunuzda cihazınızda bir PDF dosyası oluşturulur; onu hangi uygulamayla (WhatsApp, Telegram gibi) ve kime göndereceğinizi siz seçersiniz. Dosya sunucularımızdan geçmez.',
 ]),
 ('Ödev hatırlatması (isteğe bağlı)', [
  '«Hatırlatmayı aç»a dokunup bildirimlere izin verirseniz, Cloudflare üzerindeki hizmetimizde şunlar saklanır: tarayıcınızın bu amaçla verdiği bildirim adresi, saat diliminiz, site dili, en son «Bitirdim» dediğiniz günün tarihi ve cihazınızı ayırt eden rastgele bir numara.',
  'Bu bilgilerden adınızı ya da kimliğinizi öğrenemeyiz; yalnızca hatırlatmayı zamanında göndermek ve ödevinizi bitirdiğinizde durdurmak için kullanırız.',
  '«Hatırlatmayı kapat»a dokunduğunuzda ya da cihaz ayarlarından bildirimleri engellediğinizde silinir.',
 ]),
 ('Ziyaret istatistikleri', [
  'Genel ziyaret sayılarını ve en çok okunan sayfaları görmek için Cloudflare Web Analytics kullanırız. Çerez kullanmaz, ziyaretçiyi siteden siteye takip etmez ve bize hiçbir ziyaretçiyi tek tek tanıtmaz.',
 ]),
 ('Barındırma', [
  'Site GitHub Pages üzerinde barındırılır ve alan adı Cloudflare üzerinden geçer. Bu hizmetler, sayfaları size ulaştırmak için gerekli teknik verileri (IP adresi gibi) kendi gizlilik politikalarına göre işler.',
 ]),
 ('Çocuklar', [
  'Dersler herkese yöneliktir; küçük ya da büyük, kimseden bilerek kişisel veri toplamayız.',
 ]),
 ('İletişim ve değişiklikler', [
  f'Gizlilikle ilgili her türlü sorunuz için: {CONTACT}',
  'Bu politikayı değiştirirsek, değişiklik tarihini en üste yazarız.',
 ]),
]),
}
