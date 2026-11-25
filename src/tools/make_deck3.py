"""Writes the lesson-3 slide decks (src/decks/ar3, tr3) from the lesson-2 slide patterns (same classes, no new design).
Content follows src/content/lesson3-ar.md / lesson3-tr.md («بغض الطاغوت وعبادته وأهله»)."""
import json, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
DECKS = os.path.join(HERE, '..', 'decks')

ORDER = ['cover', 'intro', 'plan', 'lugha', 'istilah', 'mutaallaq', 'tawaghit', 'ahl', 'suwar', 'alaqa', 'three', 'sharh',
         'adilla1', 'adilla2', 'adilla3', 'hadith1', 'hadith2', 'hadith3', 'tawhid', 'aks', 'amthila', 'tanbihat', 'thamarat',
         'review1', 'review2', 'review3', 'jamia', 'khatima']

def foot(t): return f'<div class="foot"><p class="ft">{t}</p><div class="pn"></div></div>'

# ------------------------------------------------------------------ Arabic
FA = foot('بغض الطاغوت وعبادته وأهله')
LOGO_AR = '<img class="logo" src="/_blob/616b521e594b4b694e97dac38da64dd6" alt="شعار وتواصوا بالحق">'
AR = {
'cover': f'''<section id="cover" class="dark mid glow" data-transition="fade">
<div class="cover-body">
{LOGO_AR}
<p class="eb">صفة الكفر بالطاغوت · النقطة الثالثة</p>
<h1>بغضُ الطاغوتِ<br>وعبادتِه وأهلِه</h1>
<hr class="gl">
<p class="lead">معنى البغض، وما يتعلق به: عبادة غير الله والطاغوت وأهلها، وصوره، وعلاقته بالاعتقاد والترك، ثم الأدلة الشرعية، وارتباطه بكلمة التوحيد.</p>
</div>
<aside>الحمد لله رب العالمين، والصلاة والسلام على نبينا محمد. تناولنا في الدرسين السابقين النقطة الأولى: اعتقاد بطلان عبادة الطاغوت، والنقطة الثانية: تركها. ونتناول اليوم النقطة الثالثة: البغض، وهو عمل من أعمال القلب.</aside>
</section>''',
'intro': f'''<section id="intro" class="c">
<div class="head">
<p class="eb">أصل الدرس</p>
<h2>صفة الكفر بالطاغوت</h2>
</div>
<div class="vbox">
<p class="quote">«أن تعتقد بطلان عبادة غير الله، وتتركها، وتبغضها، وتكفّر أهلها، وتعاديهم»</p>
<p class="ref">الشيخ محمد بن عبد الوهاب رحمه الله، رسالة «معنى الطاغوت ورؤوس أنواعه»</p>
</div>
<div class="steps">
<div class="step"><p class="k">١ · الدرس الأول</p><p class="t">الاعتقاد</p></div>
<div class="step"><p class="k">٢ · الدرس الثاني</p><p class="t">الترك</p></div>
<div class="step on"><p class="k">٣ · موضوع درسنا</p><p class="t">البغض</p></div>
<div class="step"><p class="k">٤</p><p class="t">التكفير</p></div>
<div class="step"><p class="k">٥</p><p class="t">المعاداة</p></div>
</div>
<p class="note">لا يكفي أن يعلم القلب ويصدّق، بل لا بد أن يحب ما يحبه الله ويبغض ما يبغضه الله.</p>
{FA}
<aside>الاعتقاد تصديق القلب وجزمه، والترك عمل الجوارح، والبغض عمل من أعمال القلب. والمؤمن يبغض عبادة غير الله، ويبغض الطاغوت الذي يُعبد من دون الله، ويبغض أهل عبادته، كما فعل إبراهيم عليه السلام والذين معه.</aside>
</section>''',
'plan': f'''<section id="plan" class="c alt">
<div class="head">
<p class="eb">خطة الدرس</p>
<h2>محاور الدرس</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="num">١</p><h3>معنى البغض</h3><p class="txt">في اللغة والاصطلاح</p></div>
<div class="card" style="--i:1"><p class="num">٢</p><h3>ما يتعلق به</h3><p class="txt">عبادة غير الله، والطاغوت، وأهلها، وصور البغض</p></div>
<div class="card" style="--i:2"><p class="num">٣</p><h3>أدلته</h3><p class="txt">من الكتاب والسنة، مع وجه الدلالة</p></div>
<div class="card" style="--i:3"><p class="num">٤</p><h3>ارتباطه بالتوحيد</h3><p class="txt">وأمثلة، وتنبيهات من النصوص، وثمرات</p></div>
</div>
<div class="vbox">
<p class="tag">الغاية من الدرس</p>
<p class="lead">أن يبغض الطالب بقلبه عبادة غير الله، والطاغوت، وأهل عبادته، بغضًا في الله، كما فعل إبراهيم عليه السلام والذين معه.</p>
</div>
{FA}
<aside>نبدأ بمعنى البغض، ثم ما يتعلق به، ثم صوره، ثم علاقته بالنقطتين السابقتين، ثم الأدلة، وارتباطه بكلمة التوحيد، ونختم بأمثلة وتنبيهات وأسئلة.</aside>
</section>''',
'lugha': f'''<section id="lugha" class="c">
<div class="head">
<p class="eb">أولًا · معنى البغض</p>
<h2>البغض والكراهية في اللغة</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">البغض</p>
<h3>ضد الحب، والبغضاء شدة البغض</h3>
<p class="txt">قال الجوهري: «البُغْضُ: ضدُّ الحبِّ... والبَغْضاءُ: شدّة البُغْضِ» [الصحاح].</p>
<hr class="rule">
<p class="ayah sm">﴿وَبَدَا بَيْنَنَا وَبَيْنَكُمُ الْعَدَاوَةُ وَالْبَغْضَاءُ أَبَدًا﴾</p>
<p class="ref">الممتحنة: 4</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">الكراهية · لفظ قريب</p>
<h3>وبه جاء القرآن والسنة في هذا الباب</h3>
<p class="txt">وفي الحديث: «وَأَنْ يَكْرَهَ أَنْ يَعُودَ فِي الْكُفْرِ».</p>
<hr class="rule">
<p class="ayah sm">﴿وَكَرَّهَ إِلَيْكُمُ الْكُفْرَ﴾</p>
<p class="ref">الحجرات: 7</p>
</div>
</div>
{FA}
<aside>البغض ضد الحب، والبغضاء أشده. والكراهية لفظ قريب منه، وقد جاء بهما القرآن والسنة في وصف موقف المؤمن من الكفر وأهله.</aside>
</section>''',
'istilah': f'''<section id="istilah" class="c">
<div class="head">
<p class="eb">أولًا · معنى البغض</p>
<h2>البغض في هذا الباب</h2>
</div>
<p class="defn">أن يبغض المسلم بقلبه عبادة غير الله، والطاغوت الذي يُعبد من دون الله، وأهل عبادته، بغضًا لله وفي الله، فلا يرضى بها ولا يحبها ولا يوادّهم عليها.</p>
<div class="row">
<div class="card" style="--i:0">
<h3>عمل من أعمال القلب</h3>
<p class="txt">الاعتقاد تصديق القلب، والبغض عمل القلب: أن يبغض ما يبغضه الله ومن يبغضه الله.</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">تنبيه</p>
<h3>البغض هنا عبادة قلبية</h3>
<p class="txt">يتقرب بها المسلم إلى الله، لأنه بغضٌ لما يبغضه الله ولمن يبغضه الله، وهو من أوثق عرى الإيمان.</p>
</div>
</div>
{FA}
<aside>فالمسلم لا يكون محايدًا بين التوحيد والشرك، ولا بين أهل التوحيد وأهل الشرك.</aside>
</section>''',
'mutaallaq': f'''<section id="mutaallaq" class="c alt">
<div class="head">
<p class="eb">ثانيًا · ما يتعلق به البغض</p>
<h2>البغض يتعلق بثلاثة أمور</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="num">١</p><h3>عبادة غير الله</h3><p class="txt">الشرك وكل عبادة تُصرف لغير الله: الدعاء، والذبح، والنذر، والسجود، والاستغاثة بالأموات.</p></div>
<div class="card" style="--i:1"><p class="num">٢</p><h3>الطاغوت</h3><p class="txt">كل ما عُبد من دون الله وهو راضٍ، وكل من دعا إلى عبادة نفسه أو جاوز حدّه بما هو من حق الله.</p></div>
<div class="card ink" style="--i:2"><p class="num">٣</p><h3>أهلها</h3><p class="txt">أهل عبادة غير الله، من أجل شركهم وكفرهم، ولو كانوا أقرب قريب.</p></div>
</div>
<div class="vbox">
<p class="tag">قدوتنا</p>
<p class="lead">﴿إِنَّا بُرَآءُ مِنْكُمْ وَمِمَّا تَعْبُدُونَ مِنْ دُونِ اللَّهِ كَفَرْنَا بِكُمْ وَبَدَا بَيْنَنَا وَبَيْنَكُمُ الْعَدَاوَةُ وَالْبَغْضَاءُ أَبَدًا﴾ [الممتحنة: 4]</p>
</div>
{FA}
<aside>عبادة غير الله يكرهها المسلم كما يكره أن يُلقى في النار، ولا يرضاها ولا يستحسنها، ولو زُيّنت بالأسماء والمواسم والاحتفالات. وفي آية الممتحنة اجتمعت الثلاثة: البراءة من القوم، ومما يعبدون، وإعلان البغضاء.</aside>
</section>''',
'tawaghit': f'''<section id="tawaghit" class="c">
<div class="head">
<p class="eb">ثانيًا · ٢. بغض الطاغوت</p>
<h2>رؤوس الطواغيت خمسة</h2>
</div>
<div class="tiles">
<div class="row">
<div class="tile"><p class="tag">١</p><p class="txt">إبليس لعنه الله</p></div>
<div class="tile"><p class="tag">٢</p><p class="txt">من عُبد وهو راضٍ</p></div>
<div class="tile"><p class="tag">٣</p><p class="txt">من دعا الناس إلى عبادة نفسه</p></div>
</div>
<div class="row">
<div class="tile"><p class="tag">٤</p><p class="txt">من ادعى شيئًا من علم الغيب</p></div>
<div class="tile"><p class="tag">٥</p><p class="txt">من حكم بغير ما أنزل الله</p></div>
</div>
</div>
<p class="ref">الشيخ محمد بن عبد الوهاب رحمه الله، «ثلاثة الأصول»</p>
<p class="note"><b>تنبيه:</b> من عُبد وهو غير راضٍ، كعيسى عليه السلام والملائكة والصالحين، فليس طاغوتًا ولا يُبغض، بل يُحب ويُتولّى؛ والمبغوض عبادتهم من دون الله [المائدة: 117].</p>
{FA}
<aside>«والطواغيت كثيرون، ورؤوسهم خمسة». يبغضهم المؤمن لأنهم نازعوا الله في حقه، ودعوا الناس إلى عبادة غيره. قال إبراهيم عليه السلام: ﴿فَإِنَّهُمْ عَدُوٌّ لِي إِلَّا رَبَّ الْعَالَمِينَ﴾ [الشعراء: 77].</aside>
</section>''',
'ahl': f'''<section id="ahl" class="c alt">
<div class="head">
<p class="eb">ثانيًا · ٣. بغض أهلها</p>
<h2>لا يوادّهم ولو كانوا أقرب قريب</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">من القرآن</p>
<p class="ayah sm">﴿لَا تَجِدُ قَوْمًا يُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ يُوَادُّونَ مَنْ حَادَّ اللَّهَ وَرَسُولَهُ وَلَوْ كَانُوا آبَاءَهُمْ أَوْ أَبْنَاءَهُمْ أَوْ إِخْوَانَهُمْ أَوْ عَشِيرَتَهُمْ﴾</p>
<p class="ref">المجادلة: 22</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">من كلام الشيخ</p>
<p class="txt">«أن من أطاع الرسول، ووحّد الله، لا يجوز له موالاة من حادّ الله ورسوله، ولو كان أقرب قريب».</p>
<p class="ref">«ثلاثة الأصول»</p>
</div>
</div>
<div class="vbox">
<p class="tag">بغضٌ في الله</p>
<p class="lead">يبغضهم لما هم عليه من الشرك، فإذا تركوه ووحّدوا الله زال البغض: ﴿حَتَّى تُؤْمِنُوا بِاللَّهِ وَحْدَهُ﴾ [الممتحنة: 4].</p>
</div>
{FA}
<aside>بغض أهلها هو أن يبغض المسلم أهل عبادة غير الله من أجل شركهم وكفرهم؛ فلا يحبهم ولا يوادّهم ولو كانوا أقرب قريب.</aside>
</section>''',
'suwar': f'''<section id="suwar" class="c">
<div class="head">
<p class="eb">ثالثًا · صور البغض</p>
<h2>في القلب واللسان والجوارح</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="tag">١ · القلب · أصل البغض</p><h3>يكرهها ولا يرضاها</h3><p class="txt">ينفر منها، ويحزن ويغار لله إذا رآها ويحب زوالها، ولا يحب الطاغوت ولا أهل عبادته ولا يوادّهم.</p></div>
<div class="card" style="--i:1"><p class="tag">٢ · اللسان</p><h3>لا يمدح الشرك ولا أهله</h3><p class="txt">يبيّن بطلانه، ويتبرأ منه ومن أهله: ﴿إِنَّا بُرَآءُ مِنْكُمْ وَمِمَّا تَعْبُدُونَ مِنْ دُونِ اللَّهِ﴾.</p></div>
<div class="card ink" style="--i:2"><p class="tag">٣ · الجوارح</p><h3>لا يحضر مواضع الشرك</h3><p class="txt">ولا مواسمه مستمتعًا أو متفرجًا، ويُنكر الشرك بحسب استطاعته: بيده أو بلسانه أو بقلبه.</p></div>
</div>
{FA}
<aside>القلب أصل البغض ومحلّه، ويظهر أثره في اللسان والجوارح.</aside>
</section>''',
'alaqa': f'''<section id="alaqa" class="c alt">
<div class="head">
<p class="eb">رابعًا · العلاقة بالنقطتين السابقتين</p>
<h2>الاعتقاد أصل، والترك والبغض ثمرتاه</h2>
</div>
<div class="eq">
<div class="eqbox"><p class="tag">الاعتقاد · الدرس الأول</p><p class="t">يجزم القلب ببطلان عبادة غير الله</p></div>
<p class="op">+</p>
<div class="eqbox"><p class="tag">الترك · الدرس الثاني</p><p class="t">تتركها الجوارح</p></div>
<p class="op">+</p>
<div class="eqbox res"><p class="tag">البغض · هذا الدرس</p><p class="t">يبغضها القلب ويبغض الطاغوت وأهله</p></div>
</div>
<p class="lead">فالنقاط الثلاث متلازمة: الاعتقاد أصل في القلب، والترك ثمرته في الجوارح، والبغض ثمرته في عاطفة القلب.</p>
{FA}
<aside>القلب له تصديق، وله عاطفة. فالاعتقاد يتعلق بتصديقه، والبغض يتعلق بعاطفته، والترك يتعلق بالجوارح.</aside>
</section>''',
'three': f'''<section id="three" class="c">
<div class="head">
<p class="eb">رابعًا · العلاقة بالنقطتين السابقتين</p>
<h2>ثلاث حالات</h2>
</div>
<table class="tbl">
<tr class="h"><th style="width:24%">الحكم</th><th style="width:52%">حقيقتها</th><th style="width:24%">الحالة</th></tr>
<tr><td>خلل في الكفر بالطاغوت</td><td>يترك عبادة غير الله، لكن قلبه يميل إليها أو يحب أهلها ويستحسن ما هم عليه</td><td>ترك بلا بغض</td></tr>
<tr><td>لم يحقق هذه النقطة</td><td>يعلم بطلانها، لكنه لا يبغضها ولا يبغض أهلها، ويقول: «كلٌّ حرّ في عبادته»</td><td>اعتقاد بلا بغض</td></tr>
<tr class="hl"><td>هو المطلوب</td><td>يعتقد بطلانها، ويتركها، ويبغضها ويبغض الطاغوت وأهله</td><td>اعتقاد وترك وبغض</td></tr>
</table>
<p class="note">المسلم لا يكون محايدًا بين التوحيد والشرك، ولا بين أهل التوحيد وأهل الشرك.</p>
{FA}
<aside>اسأل الطلاب أولًا: أي الحالات الثلاث هي حال الموحّد؟ ثم انتقل إلى الشريحة التالية لشرح كل حالة بمثال.</aside>
</section>''',
'sharh': f'''<section id="sharh" class="c alt">
<div class="head">
<p class="eb">رابعًا · شرح الحالات</p>
<h2>كل حالة بمثال</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="tag">ترك بلا بغض</p><h3>يفرح بمواسم الشرك</h3><p class="txt">لا يذبح لغير الله ولا يطوف بالقبور، لكنه يحب أجواء مواسم الشرك ويمدح أهلها. والقلب الذي يستحسن الشيء قريب من فعله.</p></div>
<div class="card" style="--i:1"><p class="tag">اعتقاد بلا بغض</p><h3>«كلٌّ حرّ في عبادته»</h3><p class="txt">يقول: أعلم أن دعاء الأموات شرك، لكنه إذا رأى من يفعله لم يتحرك في قلبه شيء، ويوادّ أهله.</p></div>
<div class="card ink" style="--i:2"><p class="tag">اعتقاد وترك وبغض</p><h3>حال الموحّد</h3><p class="txt">يجزم ببطلانها، ويتركها، ويبغضها ويبغض الطاغوت وأهله في الله، كإبراهيم عليه السلام والذين معه.</p></div>
</div>
{FA}
<aside>الحالة الأولى ترك بجوارحه لكن قلبه لم يبغض ما يبغضه الله. والثانية يعلم الحكم لكن قلبه لم يغَر على حق الله.</aside>
</section>''',
'adilla1': f'''<section id="adilla1" class="c">
<div class="head">
<p class="eb">خامسًا · الأدلة الشرعية</p>
<h2>من القرآن الكريم (١)</h2>
</div>
<div class="row">
<div class="card ink" style="--i:0">
<p class="tag">الدليل الأول · أسوة إبراهيم والذين معه</p>
<p class="ayah">﴿قَدْ كَانَتْ لَكُمْ أُسْوَةٌ حَسَنَةٌ فِي إِبْرَاهِيمَ وَالَّذِينَ مَعَهُ إِذْ قَالُوا لِقَوْمِهِمْ إِنَّا بُرَآءُ مِنْكُمْ وَمِمَّا تَعْبُدُونَ مِنْ دُونِ اللَّهِ كَفَرْنَا بِكُمْ وَبَدَا بَيْنَنَا وَبَيْنَكُمُ الْعَدَاوَةُ وَالْبَغْضَاءُ أَبَدًا حَتَّى تُؤْمِنُوا بِاللَّهِ وَحْدَهُ﴾</p>
<p class="ref">الممتحنة: 4</p>
<hr class="rule">
<h3>وجه الدلالة</h3>
<p class="txt">تبرّؤوا من قومهم ومما يعبدون، وأعلنوا البغضاء، وجعل الله ذلك أسوة حسنة. ففيها بغض المعبودات الباطلة وبغض أهلها، وغايته ﴿حَتَّى تُؤْمِنُوا بِاللَّهِ وَحْدَهُ﴾.</p>
</div>
</div>
{FA}
<aside>البغضاء أشد البغض، وقد جعلها الله من الأسوة الحسنة للمؤمنين.</aside>
</section>''',
'adilla2': f'''<section id="adilla2" class="c alt">
<div class="head">
<p class="eb">خامسًا · الأدلة الشرعية</p>
<h2>من القرآن الكريم (٢)</h2>
</div>
<div class="row">
<div class="card ink" style="--i:0">
<p class="tag">الدليل الثاني · نفي مودة من حادّ الله ورسوله</p>
<p class="ayah">﴿لَا تَجِدُ قَوْمًا يُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ يُوَادُّونَ مَنْ حَادَّ اللَّهَ وَرَسُولَهُ وَلَوْ كَانُوا آبَاءَهُمْ أَوْ أَبْنَاءَهُمْ أَوْ إِخْوَانَهُمْ أَوْ عَشِيرَتَهُمْ﴾</p>
<p class="ref">المجادلة: 22</p>
<hr class="rule">
<h3>وجه الدلالة</h3>
<p class="txt">نفى الله الإيمان عمّن يوادّ من حادّ الله ورسوله ولو كان أقرب الناس إليه. والمودة محبة القلب، فدلّ على أن المؤمن لا يحب أهل الشرك، بل يبغضهم في الله.</p>
</div>
</div>
{FA}
<aside>وتمام الآية: ﴿أُولَئِكَ كَتَبَ فِي قُلُوبِهِمُ الْإِيمَانَ وَأَيَّدَهُمْ بِرُوحٍ مِنْهُ﴾، وهي من ثمرات البغض في الله.</aside>
</section>''',
'adilla3': f'''<section id="adilla3" class="c">
<div class="head">
<p class="eb">خامسًا · الأدلة الشرعية</p>
<h2>من القرآن الكريم (٣)</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">الدليل الثالث · عداوة إبراهيم لما يُعبد من دون الله</p>
<p class="ayah sm">﴿قَالَ أَفَرَأَيْتُمْ مَا كُنْتُمْ تَعْبُدُونَ ۝ أَنْتُمْ وَآبَاؤُكُمُ الْأَقْدَمُونَ ۝ فَإِنَّهُمْ عَدُوٌّ لِي إِلَّا رَبَّ الْعَالَمِينَ﴾</p>
<p class="ref">الشعراء: 75-77</p>
<hr class="rule">
<h3>وجه الدلالة</h3>
<p class="txt">أعلن عداوته لكل ما يُعبد من دون الله ولو كان معبود الآباء، واستثنى رب العالمين؛ فاجتمع النفي والإثبات.</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">الدليل الرابع · الكفر مكروه إلى المؤمنين</p>
<p class="ayah sm">﴿وَلَكِنَّ اللَّهَ حَبَّبَ إِلَيْكُمُ الْإِيمَانَ وَزَيَّنَهُ فِي قُلُوبِكُمْ وَكَرَّهَ إِلَيْكُمُ الْكُفْرَ وَالْفُسُوقَ وَالْعِصْيَانَ أُولَئِكَ هُمُ الرَّاشِدُونَ﴾</p>
<p class="ref">الحجرات: 7</p>
<hr class="rule">
<h3>وجه الدلالة</h3>
<p class="txt">جعل الله كراهية الكفر من نعمته على المؤمنين، ووصفهم بها بأنهم ﴿الرَّاشِدُونَ﴾. وعبادة غير الله أعظم الكفر.</p>
</div>
</div>
{FA}
<aside>إبراهيم عليه السلام أعلن عداوته لمعبودات قومه، وهي من الطاغوت الذي يُبغض.</aside>
</section>''',
'hadith1': f'''<section id="hadith1" class="c dark">
<div class="head">
<p class="eb">الدليل الخامس · من السنة النبوية</p>
<h2>حديث أنس بن مالك رضي الله عنه</h2>
</div>
<div class="head">
<p class="ayah big">«ثَلَاثٌ مَنْ كُنَّ فِيهِ وَجَدَ حَلَاوَةَ الْإِيمَانِ: أَنْ يَكُونَ اللَّهُ وَرَسُولُهُ أَحَبَّ إِلَيْهِ مِمَّا سِوَاهُمَا، وَأَنْ يُحِبَّ الْمَرْءَ لَا يُحِبُّهُ إِلَّا لِلَّهِ، وَأَنْ يَكْرَهَ أَنْ يَعُودَ فِي الْكُفْرِ كَمَا يَكْرَهُ أَنْ يُقْذَفَ فِي النَّارِ»</p>
<p class="ref">متفق عليه، واللفظ للبخاري</p>
</div>
<div class="card" style="--i:0; flex:none">
<h3>وجه الدلالة</h3>
<p class="txt">جعل النبي ﷺ كراهية الكفر من خصال الإيمان التي يجد بها العبد حلاوته، وشبّهها بكراهية الإلقاء في النار.</p>
</div>
{FA}
<aside>حلاوة الإيمان من ثمرات البغض في الله.</aside>
</section>''',
'hadith2': f'''<section id="hadith2" class="c dark">
<div class="head">
<p class="eb">الدليل السادس · من السنة النبوية</p>
<h2>حديث أبي أمامة رضي الله عنه</h2>
</div>
<div class="head">
<p class="ayah big">«مَنْ أَحَبَّ لِلَّهِ، وَأَبْغَضَ لِلَّهِ، وَأَعْطَى لِلَّهِ، وَمَنَعَ لِلَّهِ، فَقَدِ اسْتَكْمَلَ الْإِيمَانَ»</p>
<p class="ref">رواه أبو داود</p>
</div>
<div class="card" style="--i:0; flex:none">
<h3>وجه الدلالة</h3>
<p class="txt">جعل النبي ﷺ البغض لله من استكمال الإيمان. ومن أعظم ما يُبغض لله الشرك وأهله.</p>
</div>
{FA}
<aside>الحب في الله والبغض في الله متلازمان، وهما من استكمال الإيمان.</aside>
</section>''',
'hadith3': f'''<section id="hadith3" class="c dark">
<div class="head">
<p class="eb">الدليل السابع · من السنة النبوية</p>
<h2>حديث أبي سعيد الخدري رضي الله عنه</h2>
</div>
<div class="head">
<p class="ayah big">«مَنْ رَأَى مِنْكُمْ مُنْكَرًا فَلْيُغَيِّرْهُ بِيَدِهِ، فَإِنْ لَمْ يَسْتَطِعْ فَبِلِسَانِهِ، فَإِنْ لَمْ يَسْتَطِعْ فَبِقَلْبِهِ، وَذَلِكَ أَضْعَفُ الْإِيمَانِ»</p>
<p class="ref">رواه مسلم</p>
</div>
<div class="card" style="--i:0; flex:none">
<h3>وجه الدلالة</h3>
<p class="txt">إنكار القلب، وهو بغضه للمنكر، لا يسقط عن أحد. وعبادة غير الله أعظم المنكرات، فبغضها بالقلب واجب على كل مسلم في كل حال.</p>
</div>
{FA}
<aside>فبغض عبادة غير الله بالقلب واجب على كل مسلم في كل حال.</aside>
</section>''',
'tawhid': f'''<section id="tawhid" class="c dark">
<div class="head">
<p class="eb">سادسًا · البغض وكلمة التوحيد</p>
<h2>لا معبود بحق إلا الله</h2>
</div>
<div class="row">
<div class="panel" style="--i:0">
<p class="pill">النفي</p>
<p class="kalima">لا إله</p>
<p class="txt">في تصديق القلب: اعتقاد البطلان، وفي العمل: الترك، وفي عاطفة القلب: <b>بغض عبادة غير الله والطاغوت وأهله</b>.</p>
</div>
<div class="panel" style="--i:1">
<p class="pill">الإثبات</p>
<p class="kalima">إلا الله</p>
<p class="txt">اعتقاد استحقاق الله وحده للعبادة، ومحبة الله ومحبة أهل توحيده، وإفراد الله بالعبادة.</p>
</div>
</div>
<p class="lead">المحبة والبغض متلازمان: فمن أحب الله حقًّا أبغض ما يبغضه الله ومن يبغضه الله.</p>
{FA}
<aside>الدرس الأول تناول مقتضى النفي في تصديق القلب، والدرس الثاني مقتضاه في العمل، وهذا الدرس مقتضاه في عاطفة القلب.</aside>
</section>''',
'aks': f'''<section id="aks" class="c alt">
<div class="head">
<p class="eb">سادسًا · البغض وكلمة التوحيد</p>
<h2>قلب الموحّد وقلب المشرك</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">المؤمنون أشد حبًّا لله</p>
<p class="ayah sm">﴿وَمِنَ النَّاسِ مَنْ يَتَّخِذُ مِنْ دُونِ اللَّهِ أَنْدَادًا يُحِبُّونَهُمْ كَحُبِّ اللَّهِ وَالَّذِينَ آمَنُوا أَشَدُّ حُبًّا لِلَّهِ﴾</p>
<p class="ref">البقرة: 165</p>
<hr class="rule">
<p class="txt">فمن أحب الله حقًّا أبغض ما يبغضه الله ومن يبغضه الله.</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">والعكس حال المشركين</p>
<p class="ayah sm">﴿وَإِذَا ذُكِرَ اللَّهُ وَحْدَهُ اشْمَأَزَّتْ قُلُوبُ الَّذِينَ لَا يُؤْمِنُونَ بِالْآخِرَةِ وَإِذَا ذُكِرَ الَّذِينَ مِنْ دُونِهِ إِذَا هُمْ يَسْتَبْشِرُونَ﴾</p>
<p class="ref">الزمر: 45</p>
<hr class="rule">
<p class="txt">قلوبهم تنفر من التوحيد وتفرح بالشرك، وقلب الموحّد بالعكس: يفرح بالتوحيد وينفر من الشرك.</p>
</div>
</div>
{FA}
<aside>اسأل الطلاب: ما علامة قلب الموحّد بحسب آية الزمر؟ والجواب: يفرح بالتوحيد، وينفر من الشرك.</aside>
</section>''',
'amthila': f'''<section id="amthila" class="c">
<div class="head">
<p class="eb">سابعًا · أمثلة تطبيقية</p>
<h2>من الواقع</h2>
</div>
<div class="tiles">
<div class="row">
<div class="tile"><p class="tag">المواسم والاحتفالات</p><p class="txt">لا يفرح بها، ولا يذهب إليها متفرجًا مستمتعًا، ولا يهنّئ أهلها بها.</p></div>
<div class="tile"><p class="tag">المدح والاستحسان</p><p class="txt">لا يمدح الشرك ولا أهله، ولا يقول عن مظاهره: «ما أجملها!».</p></div>
<div class="tile"><p class="tag">القرابة</p><p class="txt">يبغض ما عليه قريبه من الشرك، ولا يوادّه عليه، ولا تحمله القرابة على الرضا به.</p></div>
</div>
<div class="row">
<div class="tile"><p class="tag">العادات الموروثة</p><p class="txt">يبغض ما فيها من عبادة لغير الله ولو كانت عادة الآباء، كما قال إبراهيم.</p></div>
<div class="tile"><p class="tag">محاسبة القلب</p><p class="txt">إذا وجد ميلًا أو مودة عالجه بالعلم بالتوحيد، وبدعاء الله أن يكرّه إليه الكفر.</p></div>
</div>
</div>
{FA}
<aside>ناقش الأمثلة مع الطلاب، واطلب منهم أمثلة من بيئتهم.</aside>
</section>''',
'tanbihat': f'''<section id="tanbihat" class="c alt">
<div class="head">
<p class="eb">تنبيهات من النصوص</p>
<h2>أربعة تنبيهات</h2>
</div>
<div class="row">
<div class="col">
<div class="notlist">
<p class="nl"><b>١. من عُبد وهو غير راضٍ لا يُبغض</b>: كعيسى عليه السلام والملائكة والصالحين؛ فالمبغوض عبادتهم من دون الله، لا هم [المائدة: 117].</p>
<p class="nl"><b>٢. البغض في الله لا يُسقط البرّ بالوالدين</b>: ﴿فَلَا تُطِعْهُمَا وَصَاحِبْهُمَا فِي الدُّنْيَا مَعْرُوفًا﴾ [لقمان: 15].</p>
</div>
</div>
<div class="col">
<div class="notlist">
<p class="nl"><b>٣. البغض لا يُسقط العدل</b>: ﴿وَلَا يَجْرِمَنَّكُمْ شَنَآنُ قَوْمٍ عَلَى أَلَّا تَعْدِلُوا اعْدِلُوا هُوَ أَقْرَبُ لِلتَّقْوَى﴾ [المائدة: 8].</p>
<p class="nl"><b>٤. التكفير والمعاداة نقطتان مستقلتان</b>: يأتي بيانهما في الدرسين القادمين.</p>
</div>
</div>
</div>
{FA}
<aside>الشنآن هو البغض؛ فلا يحمل المسلمَ بغضُه على ترك العدل.</aside>
</section>''',
'thamarat': f'''<section id="thamarat" class="c">
<div class="head">
<p class="eb">ثامنًا</p>
<h2>ثمرات البغض في الله</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="tag">١</p><h3>حلاوة الإيمان</h3><p class="txt">كما في حديث أنس رضي الله عنه.</p></div>
<div class="card" style="--i:1"><p class="tag">٢</p><h3>استكمال الإيمان</h3><p class="txt">«مَنْ أَحَبَّ لِلَّهِ، وَأَبْغَضَ لِلَّهِ... فَقَدِ اسْتَكْمَلَ الْإِيمَانَ».</p></div>
<div class="card" style="--i:2"><p class="tag">٣</p><h3>الرشد</h3><p class="txt">﴿أُولَئِكَ هُمُ الرَّاشِدُونَ﴾ كما في آية الحجرات.</p></div>
</div>
<div class="row">
<div class="card" style="--i:3"><p class="tag">٤</p><h3>الاقتداء بإبراهيم</h3><p class="txt">والذين معه، الأسوة الحسنة التي أمر الله بالتأسي بها.</p></div>
<div class="card ink" style="--i:4"><p class="tag">٥</p><h3>كتابة الإيمان والتأييد</h3><p class="txt">﴿أُولَئِكَ كَتَبَ فِي قُلُوبِهِمُ الْإِيمَانَ وَأَيَّدَهُمْ بِرُوحٍ مِنْهُ﴾.</p></div>
</div>
{FA}
<aside>اختم هذا المبحث بتذكير الطلاب بالدعاء: اللهم حبّب إلينا الإيمان وزيّنه في قلوبنا، وكرّه إلينا الكفر والفسوق والعصيان، واجعلنا من الراشدين.</aside>
</section>''',
'review1': f'''<section id="review1" class="c alt">
<div class="head">
<p class="eb">ترسيخ المعنى</p>
<h2>أسئلة المراجعة (١)</h2>
</div>
<div class="qa"><p class="qn">١</p><div class="qbody"><p class="q">ما معنى البغض لغة؟ وما معنى البغضاء؟</p><p class="a fragment">البغض ضد الحب، والبغضاء شدة البغض.</p></div></div>
<div class="qa"><p class="qn">٢</p><div class="qbody"><p class="q">ما الأمور الثلاثة التي يتعلق بها البغض في هذه النقطة؟</p><p class="a fragment">عبادة غير الله، والطاغوت الذي يُعبد من دون الله وهو راضٍ، وأهل عبادته.</p></div></div>
<div class="qa"><p class="qn">٣</p><div class="qbody"><p class="q">اذكر رؤوس الطواغيت الخمسة.</p><p class="a fragment">إبليس، ومن عُبد وهو راضٍ، ومن دعا الناس إلى عبادة نفسه، ومن ادعى شيئًا من علم الغيب، ومن حكم بغير ما أنزل الله.</p></div></div>
{FA}
<aside>اطرح السؤال أولًا واترك الطلاب يجيبون، ثم اضغط لإظهار الجواب.</aside>
</section>''',
'review2': f'''<section id="review2" class="c">
<div class="head">
<p class="eb">ترسيخ المعنى</p>
<h2>أسئلة المراجعة (٢)</h2>
</div>
<div class="qa"><p class="qn">٤</p><div class="qbody"><p class="q">ما وجه الدلالة من آية المجادلة على هذه النقطة؟</p><p class="a fragment">نفى الله الإيمان عمّن يوادّ من حادّ الله ورسوله ولو كان أقرب الناس إليه؛ فالمؤمن لا يحب أهل الشرك، بل يبغضهم في الله.</p></div></div>
<div class="qa"><p class="qn">٥</p><div class="qbody"><p class="q">هل يُبغض عيسى عليه السلام لأن النصارى عبدوه؟ ولماذا؟</p><p class="a fragment">لا؛ لأنه عُبد وهو غير راضٍ، فليس طاغوتًا، بل يُحب ويُتولّى، والمبغوض عبادته من دون الله [المائدة: 117].</p></div></div>
<div class="qa"><p class="qn">٦</p><div class="qbody"><p class="q">رجل يحب قريبه المشرك ويوادّه على ما هو عليه. ما الخلل في حاله؟</p><p class="a fragment">لم يبغض أهل الشرك في الله، والله نفى الإيمان عمّن يوادّ من حادّ الله ورسوله ولو كانوا آباءهم أو أبناءهم أو إخوانهم أو عشيرتهم.</p></div></div>
{FA}
<aside>اسأل أيضًا: لماذا لا يكفي الاعتقاد والترك دون البغض؟ والجواب: لأن القلب لا بد أن يحب ما يحبه الله ويبغض ما يبغضه الله ومن يبغضه الله.</aside>
</section>''',
'review3': f'''<section id="review3" class="c alt">
<div class="head">
<p class="eb">ترسيخ المعنى · صح أو خطأ</p>
<h2>أسئلة المراجعة (٣)</h2>
</div>
<div class="qa"><p class="qn">٧</p><div class="qbody"><p class="q">يكفي المسلمَ أن يعلم بطلان عبادة غير الله، ولو لم يبغضها ولم يبغض أهلها.</p><p class="a fragment">خطأ؛ فلا بد أن يبغضها ويبغض أهلها في الله، والمسلم لا يكون محايدًا بين التوحيد والشرك.</p></div></div>
<div class="qa"><p class="qn">٨</p><div class="qbody"><p class="q">كل من عُبد من دون الله يُبغض، ولو كان غير راضٍ بعبادته.</p><p class="a fragment">خطأ؛ من عُبد وهو غير راضٍ كعيسى عليه السلام والملائكة والصالحين لا يُبغض، والمبغوض عبادتهم من دون الله.</p></div></div>
<div class="qa"><p class="qn">٩</p><div class="qbody"><p class="q">البغض في الله من استكمال الإيمان.</p><p class="a fragment">صح؛ «مَنْ أَحَبَّ لِلَّهِ، وَأَبْغَضَ لِلَّهِ... فَقَدِ اسْتَكْمَلَ الْإِيمَانَ».</p></div></div>
{FA}
<aside>اطلب من الطالب أن يعلّل جوابه في كل عبارة، لا أن يكتفي بقول: صح أو خطأ.</aside>
</section>''',
'jamia': '''<section id="jamia" class="gold mid">
<p class="eb">الخلاصة التي يحفظها الطالب</p>
<p class="jamia">البغض في هذه النقطة هو أن يبغض المسلم بقلبه عبادة غير الله، والطاغوت الذي يُعبد من دون الله وهو راضٍ، وأهل عبادته، بغضًا في الله، فلا يرضى بالشرك ولا يحبه، ولا يوادّ أهله ولو كانوا أقرب قريب، ويظهر أثر ذلك في لسانه وجوارحه.</p>
<aside>يُطلب من الطلاب حفظ هذه العبارة. وتذكيرهم بأن الدرس القادم في النقطة الرابعة: تكفير أهلها.</aside>
</section>''',
'khatima': f'''<section id="khatima" class="dark mid glow">
<div class="cover-body">
{LOGO_AR}
<p class="eb">خاتمة الدرس</p>
<p class="closing">نسأل الله تعالى أن يحبّب إلينا الإيمان ويزيّنه في قلوبنا، وأن يكرّه إلينا الكفر والفسوق والعصيان، وأن يجعلنا من الراشدين، وأن يثبتنا على التوحيد حتى نلقاه.</p>
<hr class="gl">
<p class="lead">والحمد لله رب العالمين</p>
</div>
<aside>خلاصة: البغض ثمرة اعتقاد بطلان عبادة غير الله في عاطفة القلب، كما أن الترك ثمرته في الجوارح. وهو من مقتضيات «لا إله» في كلمة التوحيد، ومن أصل الكفر بالطاغوت.</aside>
</section>''',
}

# ------------------------------------------------------------------ Turkish
FT = foot('Tâğuta, İbadetine ve Ehline Buğz')
LOGO_TR = '<img class="logo" src="/_blob/2f989340cf22fbab08c67ed80788ff94" alt="Ve Tevâsav bi\'l-Hak logosu">'
def meal(s, sm=True): return f'<p class="meal{" sm" if sm else ""}">{s}</p>'
TR = {
'cover': f'''<section id="cover" class="dark mid glow" data-transition="fade">
<div class="cover-body">
{LOGO_TR}
<p class="eb">Tâğutu inkârın keyfiyeti · Üçüncü husus</p>
<h1>Tâğuta, İbadetine<br>ve Ehline Buğz</h1>
<hr class="gl">
<p class="lead">Buğzun anlamı; ilgili olduğu şeyler: Allah’tan başkasına ibadet, tâğut ve ehli; şekilleri; itikad ve terk ile ilişkisi; şer’î deliller ve tevhid kelimesiyle bağı.</p>
</div>
<aside>Hamd âlemlerin Rabbi Allah’a, salât ve selam Peygamberimiz Muhammed’e olsun. Önceki iki derste birinci hususu, yani tâğuta ibadetin bâtıl olduğuna itikadı ve ikinci hususu, yani onu terk etmeyi işledik. Bugün üçüncü hususu ele alıyoruz: buğz; bu, kalbin amellerindendir.</aside>
</section>''',
'intro': f'''<section id="intro" class="c">
<div class="head">
<p class="eb">Dersin esası</p>
<h2>Tâğutu inkârın keyfiyeti</h2>
</div>
<div class="vbox">
<p class="arq">«أن تعتقد بطلان عبادة غير الله، وتتركها، وتبغضها، وتكفّر أهلها، وتعاديهم»</p>
<p class="meal">«Allah’tan başkasına yapılan ibadetin bâtıl olduğuna inanman, onu terk etmen, ona buğz etmen, ehlini tekfir etmen ve onlara düşmanlık etmendir.»</p>
<p class="ref">Şeyh Muhammed b. Abdülvehhab (rahimehullah), «Ma‘ne’t-Tâğût ve Ruûsu Envâih» risalesi</p>
</div>
<div class="steps">
<div class="step"><p class="k">1 · Birinci ders</p><p class="t">İtikad</p></div>
<div class="step"><p class="k">2 · İkinci ders</p><p class="t">Terk</p></div>
<div class="step on"><p class="k">3 · Dersimiz</p><p class="t">Buğz</p></div>
<div class="step"><p class="k">4</p><p class="t">Tekfir</p></div>
<div class="step"><p class="k">5</p><p class="t">Düşmanlık</p></div>
</div>
{FT}
<aside>Kalbin bilmesi ve tasdik etmesi yetmez; Allah’ın sevdiğini sevmesi, Allah’ın buğz ettiğine de buğz etmesi gerekir. Mümin, Allah’tan başkasına ibadete, tâğuta ve ona ibadet edenlere buğz eder; tıpkı İbrahim (aleyhisselâm) ve onunla birlikte olanlar gibi.</aside>
</section>''',
'plan': f'''<section id="plan" class="c alt">
<div class="head">
<p class="eb">Dersin planı</p>
<h2>Dersin başlıkları</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="num">1</p><h3>Buğzun anlamı</h3><p class="txt">Sözlük ve ıstılah anlamı</p></div>
<div class="card" style="--i:1"><p class="num">2</p><h3>İlgili olduğu şeyler</h3><p class="txt">Allah’tan başkasına ibadet, tâğut, ehli ve buğzun şekilleri</p></div>
<div class="card" style="--i:2"><p class="num">3</p><h3>Delilleri</h3><p class="txt">Kitap ve Sünnet’ten, delil yönüyle</p></div>
<div class="card" style="--i:3"><p class="num">4</p><h3>Tevhidle bağı</h3><p class="txt">Örnekler, nasslardan uyarılar ve meyveler</p></div>
</div>
<div class="vbox">
<p class="tag">Dersin amacı</p>
<p class="lead">Öğrencinin, kalbiyle Allah’tan başkasına ibadete, tâğuta ve ona ibadet edenlere Allah yolunda buğz etmesidir; tıpkı İbrahim (aleyhisselâm) ve onunla birlikte olanlar gibi.</p>
</div>
{FT}
<aside>Buğzun anlamıyla başlıyoruz; sonra ilgili olduğu şeyler, şekilleri, önceki iki husus ile ilişkisi, deliller ve tevhid kelimesiyle bağı; örnekler, uyarılar ve sorularla bitiriyoruz.</aside>
</section>''',
'lugha': f'''<section id="lugha" class="c">
<div class="head">
<p class="eb">Birinci bölüm · Buğzun anlamı</p>
<h2>Sözlükte buğz ve kerâhiyet</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">Buğz</p>
<h3>Sevginin zıddı; bağzâ ise şiddetli buğzdur</h3>
<p class="txt">Cevherî: «Buğz, sevginin zıddıdır… Bağzâ ise şiddetli buğzdur.» (es-Sıhâh)</p>
<hr class="rule">
<p class="ayah sm">﴿وَبَدَا بَيْنَنَا وَبَيْنَكُمُ الْعَدَاوَةُ وَالْبَغْضَاءُ أَبَدًا﴾</p>
{meal('«Bizimle sizin aranızda ebedî bir düşmanlık ve buğz başlamıştır.»')}
<p class="ref">Mümtehine, 4</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">Kerâhiyet · Yakın bir lafız</p>
<h3>Kur’an ve Sünnet bu bapta onu da kullanır</h3>
<p class="txt">Hadiste: «Küfre dönmekten hoşlanmaması.»</p>
<hr class="rule">
<p class="ayah sm">﴿وَكَرَّهَ إِلَيْكُمُ الْكُفْرَ﴾</p>
{meal('«Küfrü size çirkin gösterdi.»')}
<p class="ref">Hucurât, 7</p>
</div>
</div>
{FT}
<aside>Buğz sevginin zıddıdır, bağzâ onun en şiddetlisidir. Kerâhiyet ona yakın bir lafızdır; Kur’an ve Sünnet müminin küfre ve ehline karşı tutumunu her ikisiyle de anlatmıştır.</aside>
</section>''',
'istilah': f'''<section id="istilah" class="c">
<div class="head">
<p class="eb">Birinci bölüm · Buğzun anlamı</p>
<h2>Bu baptaki buğz</h2>
</div>
<p class="defn">Müslümanın kalbiyle Allah’tan başkasına ibadete, tâğuta ve ona ibadet edenlere Allah için buğz etmesidir; o ibadete razı olmaz, onu sevmez ve ehliyle sevgi bağı kurmaz.</p>
<div class="row">
<div class="card" style="--i:0">
<h3>Kalbin amellerinden biri</h3>
<p class="txt">İtikad kalbin tasdikidir; buğz ise kalbin amelidir: Allah’ın buğz ettiğine ve Allah’ın buğz ettiği kimseye buğz etmek.</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">Uyarı</p>
<h3>Buradaki buğz kalbî bir ibadettir</h3>
<p class="txt">Müslüman onunla Allah’a yaklaşır; imanın en sağlam kulplarındandır.</p>
</div>
</div>
{FT}
<aside>Müslüman tevhid ile şirk arasında da, tevhid ehli ile şirk ehli arasında da tarafsız olmaz.</aside>
</section>''',
'mutaallaq': f'''<section id="mutaallaq" class="c alt">
<div class="head">
<p class="eb">İkinci bölüm · Buğzun ilgili olduğu şeyler</p>
<h2>Buğz üç şeyle ilgilidir</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="num">1</p><h3>Allah’tan başkasına ibadet</h3><p class="txt">Şirk ve Allah’tan başkasına yöneltilen her ibadet: dua, kurban, adak, secde, ölülerden medet istemek.</p></div>
<div class="card" style="--i:1"><p class="num">2</p><h3>Tâğut</h3><p class="txt">Allah’ı bırakıp kendisine ibadet edilen ve buna razı olan; kendisine ibadete çağıran ya da Allah’ın hakkında haddini aşan.</p></div>
<div class="card ink" style="--i:2"><p class="num">3</p><h3>Ehli</h3><p class="txt">Allah’tan başkasına ibadet edenler; şirkleri ve küfürleri sebebiyle, en yakın akraba olsalar bile.</p></div>
</div>
<div class="vbox">
<p class="tag">Örneğimiz</p>
<p class="lead">«Biz sizden ve Allah’ı bırakıp ibadet ettiklerinizden uzağız. Sizi inkâr ettik. Bizimle sizin aranızda ebedî bir düşmanlık ve buğz başlamıştır.» (Mümtehine, 4)</p>
</div>
{FT}
<aside>Müslüman, Allah’tan başkasına ibadetten ateşe atılmaktan hoşlanmadığı gibi hoşlanmaz; isimlerle, mevsimlerle ve kutlamalarla süslense bile ona razı olmaz. Mümtehine ayetinde üçü bir araya gelmiştir: kavimden ve ibadet ettiklerinden beri olmak ve buğzu ilan etmek.</aside>
</section>''',
'tawaghit': f'''<section id="tawaghit" class="c">
<div class="head">
<p class="eb">İkinci bölüm · 2. Tâğuta buğz</p>
<h2>Tâğutların başları beştir</h2>
</div>
<div class="tiles">
<div class="row">
<div class="tile"><p class="tag">1</p><p class="txt">Allah’ın lânet ettiği İblis</p></div>
<div class="tile"><p class="tag">2</p><p class="txt">Kendisine ibadet edilen ve buna razı olan</p></div>
<div class="tile"><p class="tag">3</p><p class="txt">İnsanları kendisine ibadete çağıran</p></div>
</div>
<div class="row">
<div class="tile"><p class="tag">4</p><p class="txt">Gaybı bildiğini iddia eden</p></div>
<div class="tile"><p class="tag">5</p><p class="txt">Allah’ın indirdiğinden başkasıyla hükmeden</p></div>
</div>
</div>
<p class="ref">Şeyh Muhammed b. Abdülvehhab (rahimehullah), «Üç Esas» (Selâsetü’l-Usûl)</p>
<p class="note"><b>Uyarı:</b> Kendisine ibadet edilen ve buna razı olmayan, İsa (aleyhisselâm), melekler ve salihler gibi, tâğut değildir ve ona buğz edilmez; aksine sevilir ve dost edinilir. Buğz edilen, onlara Allah’tan başka ibadet edilmesidir (Mâide, 117).</p>
{FT}
<aside>«Tâğutlar çoktur; başları beştir.» Mümin onlara buğz eder; çünkü onlar Allah’ın hakkında O’na ortaklık iddia etmiş ve insanları O’ndan başkasına ibadete çağırmışlardır. İbrahim (aleyhisselâm): «İşte onlar benim düşmanımdır; ancak âlemlerin Rabbi müstesna.» (Şuarâ, 77)</aside>
</section>''',
'ahl': f'''<section id="ahl" class="c alt">
<div class="head">
<p class="eb">İkinci bölüm · 3. Ehline buğz</p>
<h2>En yakın akraba olsalar bile sevgi bağı kurmaz</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">Kur’an’dan</p>
<p class="ayah sm">﴿لَا تَجِدُ قَوْمًا يُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ يُوَادُّونَ مَنْ حَادَّ اللَّهَ وَرَسُولَهُ وَلَوْ كَانُوا آبَاءَهُمْ أَوْ أَبْنَاءَهُمْ أَوْ إِخْوَانَهُمْ أَوْ عَشِيرَتَهُمْ﴾</p>
{meal('«Allah’a ve ahiret gününe iman eden bir topluluğun, babaları, oğulları, kardeşleri ya da akrabaları olsalar bile, Allah’a ve Rasûlü’ne karşı gelenlerle sevgi bağı kurduğunu göremezsin.»')}
<p class="ref">Mücâdele, 22</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">Şeyh’in sözünden</p>
<p class="txt">«Rasûle itaat eden ve Allah’ı birleyen kimsenin, en yakın akrabası olsa bile, Allah’a ve Rasûlü’ne karşı gelen kimseyi dost edinmesi caiz değildir.»</p>
<p class="ref">«Üç Esas»</p>
</div>
</div>
<div class="vbox">
<p class="tag">Allah yolunda bir buğz</p>
<p class="lead">Onlara şirkleri sebebiyle buğz eder; şirki bırakıp Allah’ı birlediklerinde buğz da kalkar: «Siz bir olan Allah’a iman edinceye kadar.» (Mümtehine, 4)</p>
</div>
{FT}
<aside>Ehline buğz; Müslümanın Allah’tan başkasına ibadet edenlere, şirkleri ve küfürleri sebebiyle buğz etmesidir; en yakın akrabası olsalar bile onları sevmez ve onlarla sevgi bağı kurmaz.</aside>
</section>''',
'suwar': f'''<section id="suwar" class="c">
<div class="head">
<p class="eb">Üçüncü bölüm · Buğzun şekilleri</p>
<h2>Kalpte, dilde ve azalarda</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="tag">1 · Kalp · Buğzun aslı</p><h3>Ondan hoşlanmaz, razı olmaz</h3><p class="txt">Ondan nefret eder; onu görünce Allah için üzülür ve kıskanır, ortadan kalkmasını ister; tâğutu ve ehlini sevmez, onlarla sevgi bağı kurmaz.</p></div>
<div class="card" style="--i:1"><p class="tag">2 · Dil</p><h3>Şirki ve ehlini övmez</h3><p class="txt">Bâtıllığını açıklar; ondan ve ehlinden beri olduğunu söyler: «Biz sizden ve Allah’ı bırakıp ibadet ettiklerinizden uzağız.»</p></div>
<div class="card ink" style="--i:2"><p class="tag">3 · Azalar</p><h3>Şirk mekânlarında bulunmaz</h3><p class="txt">Mevsimlerinde hoşlanarak ya da seyirci olarak bulunmaz; gücü yettiğince şirki eliyle, diliyle ya da kalbiyle reddeder.</p></div>
</div>
{FT}
<aside>Buğzun aslı ve yeri kalptir; etkisi dilde ve azalarda görünür.</aside>
</section>''',
'alaqa': f'''<section id="alaqa" class="c alt">
<div class="head">
<p class="eb">Dördüncü bölüm · Önceki iki husus ile ilişkisi</p>
<h2>İtikad asıldır; terk ve buğz onun meyveleridir</h2>
</div>
<div class="eq">
<div class="eqbox"><p class="tag">İtikad · Birinci ders</p><p class="t">Kalp, Allah’tan başkasına ibadetin bâtıllığına kesin inanır</p></div>
<p class="op">+</p>
<div class="eqbox"><p class="tag">Terk · İkinci ders</p><p class="t">Azalar onu terk eder</p></div>
<p class="op">+</p>
<div class="eqbox res"><p class="tag">Buğz · Bu ders</p><p class="t">Kalp ona, tâğuta ve ehline buğz eder</p></div>
</div>
<p class="lead">Üç husus birbirinden ayrılmaz: itikad kalpteki asıldır, terk onun azalardaki meyvesidir, buğz ise kalbin duygusundaki meyvesidir.</p>
{FT}
<aside>Kalbin bir tasdiki, bir de duygusu vardır. İtikad tasdikiyle, buğz duygusuyla, terk ise azalarla ilgilidir.</aside>
</section>''',
'three': f'''<section id="three" class="c">
<div class="head">
<p class="eb">Dördüncü bölüm · Önceki iki husus ile ilişkisi</p>
<h2>Üç durum</h2>
</div>
<table class="tbl">
<tr class="h"><th style="width:24%">Durum</th><th style="width:52%">Hakikati</th><th style="width:24%">Hüküm</th></tr>
<tr><td>Buğzsuz terk</td><td>Terk eder, fakat kalbi ona meyleder ya da ehlini sever ve onların hâlini güzel bulur</td><td>Tâğutu inkârda kusur</td></tr>
<tr><td>Buğzsuz itikad</td><td>Bâtıl olduğunu bilir, fakat ona da ehline de buğz etmez; «Herkes ibadetinde özgürdür» der</td><td>Bu hususu gerçekleştirmemiştir</td></tr>
<tr class="hl"><td>İtikad, terk ve buğz</td><td>Bâtıllığına inanır, terk eder, ona buğz eder; tâğuta ve ehline de buğz eder</td><td>İstenen budur</td></tr>
</table>
<p class="note">Müslüman tevhid ile şirk arasında da, tevhid ehli ile şirk ehli arasında da tarafsız olmaz.</p>
{FT}
<aside>Önce öğrencilere sorun: Bu üç durumdan hangisi muvahhidin hâlidir? Sonra her durumu bir örnekle açıklamak için sonraki slayta geçin.</aside>
</section>''',
'sharh': f'''<section id="sharh" class="c alt">
<div class="head">
<p class="eb">Dördüncü bölüm · Durumların açıklaması</p>
<h2>Her durum bir örnekle</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="tag">Buğzsuz terk</p><h3>Şirk mevsimlerine sevinir</h3><p class="txt">Kurban kesmez, kabir tavaf etmez; fakat şirk mevsimlerinin havasını sever ve ehlini över. Bir şeyi güzel bulan kalp onu yapmaya yakındır.</p></div>
<div class="card" style="--i:1"><p class="tag">Buğzsuz itikad</p><h3>«Herkes ibadetinde özgürdür»</h3><p class="txt">Ölülere duanın şirk olduğunu bilir; fakat yapanı görünce kalbinde hiçbir şey kıpırdamaz ve onunla sevgi bağı kurar.</p></div>
<div class="card ink" style="--i:2"><p class="tag">İtikad, terk ve buğz</p><h3>Muvahhidin hâli</h3><p class="txt">Bâtıllığına inanır, terk eder, ona buğz eder; tâğuta ve ehline de Allah yolunda buğz eder; İbrahim ve beraberindekiler gibi.</p></div>
</div>
{FT}
<aside>Birinci durumda azalarıyla terk etmiş, fakat kalbi Allah’ın buğz ettiğine buğz etmemiştir. İkinci durumda hükmü bilir, fakat kalbi Allah’ın hakkını kıskanmamıştır.</aside>
</section>''',
'adilla1': f'''<section id="adilla1" class="c">
<div class="head">
<p class="eb">Beşinci bölüm · Şer’î deliller</p>
<h2>Kur’an-ı Kerim’den (1)</h2>
</div>
<div class="row">
<div class="card ink" style="--i:0">
<p class="tag">Birinci delil · İbrahim ve beraberindekilerin örnekliği</p>
<p class="ayah sm">﴿قَدْ كَانَتْ لَكُمْ أُسْوَةٌ حَسَنَةٌ فِي إِبْرَاهِيمَ وَالَّذِينَ مَعَهُ إِذْ قَالُوا لِقَوْمِهِمْ إِنَّا بُرَآءُ مِنْكُمْ وَمِمَّا تَعْبُدُونَ مِنْ دُونِ اللَّهِ كَفَرْنَا بِكُمْ وَبَدَا بَيْنَنَا وَبَيْنَكُمُ الْعَدَاوَةُ وَالْبَغْضَاءُ أَبَدًا حَتَّى تُؤْمِنُوا بِاللَّهِ وَحْدَهُ﴾</p>
{meal('«İbrahim’de ve onunla birlikte olanlarda sizin için güzel bir örnek vardır. Hani kavimlerine şöyle demişlerdi: Biz sizden ve Allah’ı bırakıp ibadet ettiklerinizden uzağız. Sizi inkâr ettik. Bir olan Allah’a iman edinceye kadar bizimle sizin aranızda ebedî bir düşmanlık ve buğz başlamıştır.»')}
<p class="ref">Mümtehine, 4</p>
<hr class="rule">
<h3>Delil yönü</h3>
<p class="txt">Kavimlerinden ve ibadet ettiklerinden beri olduklarını söyleyip buğzu ilan ettiler; Allah bunu güzel örnek kıldı. Ayet bâtıl mabudlara ve ehline buğza delildir; sınırı «Allah’a iman edinceye kadar»dır.</p>
</div>
</div>
{FT}
<aside>Bağzâ buğzun en şiddetlisidir; Allah onu müminler için güzel örnekten kılmıştır.</aside>
</section>''',
'adilla2': f'''<section id="adilla2" class="c alt">
<div class="head">
<p class="eb">Beşinci bölüm · Şer’î deliller</p>
<h2>Kur’an-ı Kerim’den (2)</h2>
</div>
<div class="row">
<div class="card ink" style="--i:0">
<p class="tag">İkinci delil · Allah’a ve Rasûlü’ne karşı gelenlerle sevgi bağının nefyi</p>
<p class="ayah">﴿لَا تَجِدُ قَوْمًا يُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ يُوَادُّونَ مَنْ حَادَّ اللَّهَ وَرَسُولَهُ وَلَوْ كَانُوا آبَاءَهُمْ أَوْ أَبْنَاءَهُمْ أَوْ إِخْوَانَهُمْ أَوْ عَشِيرَتَهُمْ﴾</p>
{meal('«Allah’a ve ahiret gününe iman eden bir topluluğun, babaları, oğulları, kardeşleri ya da akrabaları olsalar bile, Allah’a ve Rasûlü’ne karşı gelenlerle sevgi bağı kurduğunu göremezsin.»')}
<p class="ref">Mücâdele, 22</p>
<hr class="rule">
<h3>Delil yönü</h3>
<p class="txt">Allah, en yakını olsa bile Allah’a ve Rasûlü’ne karşı gelenle sevgi bağı kurandan imanı nefyetti. Meveddet kalbin sevgisidir; mümin şirk ehlini sevmez, onlara Allah yolunda buğz eder.</p>
</div>
</div>
{FT}
<aside>Ayetin devamı: «İşte Allah onların kalplerine imanı yazmış ve onları kendi katından bir ruhla desteklemiştir.» Bu, Allah için buğzun meyvelerindendir.</aside>
</section>''',
'adilla3': f'''<section id="adilla3" class="c">
<div class="head">
<p class="eb">Beşinci bölüm · Şer’î deliller</p>
<h2>Kur’an-ı Kerim’den (3)</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">Üçüncü delil · İbrahim’in düşmanlığı</p>
<p class="ayah sm">﴿قَالَ أَفَرَأَيْتُمْ مَا كُنْتُمْ تَعْبُدُونَ ۝ أَنْتُمْ وَآبَاؤُكُمُ الْأَقْدَمُونَ ۝ فَإِنَّهُمْ عَدُوٌّ لِي إِلَّا رَبَّ الْعَالَمِينَ﴾</p>
{meal('«Gördünüz mü neye ibadet ediyormuşsunuz; siz ve eski atalarınız? İşte onlar benim düşmanımdır; ancak âlemlerin Rabbi müstesna.»')}
<p class="ref">Şuarâ, 75-77</p>
<hr class="rule">
<h3>Delil yönü</h3>
<p class="txt">Ataların mabudu olsa bile Allah’ı bırakıp ibadet edilen her şeye düşmanlığını ilan etti, yalnız âlemlerin Rabbini istisna etti.</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">Dördüncü delil · Küfür müminlere çirkin gösterilmiştir</p>
<p class="ayah sm">﴿وَلَكِنَّ اللَّهَ حَبَّبَ إِلَيْكُمُ الْإِيمَانَ وَزَيَّنَهُ فِي قُلُوبِكُمْ وَكَرَّهَ إِلَيْكُمُ الْكُفْرَ وَالْفُسُوقَ وَالْعِصْيَانَ أُولَئِكَ هُمُ الرَّاشِدُونَ﴾</p>
{meal('«Fakat Allah size imanı sevdirdi, onu kalplerinizde süsledi; küfrü, fıskı ve isyanı size çirkin gösterdi. İşte doğru yolda olanlar onlardır.»')}
<p class="ref">Hucurât, 7</p>
<hr class="rule">
<h3>Delil yönü</h3>
<p class="txt">Allah, küfre karşı hoşnutsuzluğu müminlere nimeti saydı ve onları bununla «doğru yolda olanlar» diye niteledi.</p>
</div>
</div>
{FT}
<aside>Allah’tan başkasına ibadet küfrün en büyüğüdür.</aside>
</section>''',
'hadith1': f'''<section id="hadith1" class="c dark">
<div class="head">
<p class="eb">Beşinci delil · Sünnet’ten</p>
<h2>Enes b. Mâlik (r.a.) hadisi</h2>
</div>
<div class="head">
<p class="ayah big">«ثَلَاثٌ مَنْ كُنَّ فِيهِ وَجَدَ حَلَاوَةَ الْإِيمَانِ: أَنْ يَكُونَ اللَّهُ وَرَسُولُهُ أَحَبَّ إِلَيْهِ مِمَّا سِوَاهُمَا، وَأَنْ يُحِبَّ الْمَرْءَ لَا يُحِبُّهُ إِلَّا لِلَّهِ، وَأَنْ يَكْرَهَ أَنْ يَعُودَ فِي الْكُفْرِ كَمَا يَكْرَهُ أَنْ يُقْذَفَ فِي النَّارِ»</p>
{meal('«Üç şey kimde bulunursa imanın tadını bulur: Allah ve Rasûlü’nün ona her şeyden sevgili olması, bir kimseyi yalnız Allah için sevmesi ve ateşe atılmaktan hoşlanmadığı gibi küfre dönmekten hoşlanmaması.»', False)}
<p class="ref">Buhârî ve Müslim; lafız Buhârî’nin</p>
</div>
<div class="card" style="--i:0; flex:none">
<h3>Delil yönü</h3>
<p class="txt">Peygamber (s.a.v.) küfürden hoşlanmamayı imanın tadını veren hasletlerden saydı ve onu ateşe atılmaktan hoşlanmamaya benzetti.</p>
</div>
{FT}
<aside>İmanın tadı, Allah için buğzun meyvelerindendir.</aside>
</section>''',
'hadith2': f'''<section id="hadith2" class="c dark">
<div class="head">
<p class="eb">Altıncı delil · Sünnet’ten</p>
<h2>Ebû Ümâme (r.a.) hadisi</h2>
</div>
<div class="head">
<p class="ayah big">«مَنْ أَحَبَّ لِلَّهِ، وَأَبْغَضَ لِلَّهِ، وَأَعْطَى لِلَّهِ، وَمَنَعَ لِلَّهِ، فَقَدِ اسْتَكْمَلَ الْإِيمَانَ»</p>
{meal('«Kim Allah için sever, Allah için buğz eder, Allah için verir ve Allah için vermezse imanını kemale erdirmiş olur.»', False)}
<p class="ref">Ebû Dâvûd</p>
</div>
<div class="card" style="--i:0; flex:none">
<h3>Delil yönü</h3>
<p class="txt">Peygamber (s.a.v.) Allah için buğz etmeyi imanı kemale erdirmekten saydı. Allah için buğz edilen şeylerin en büyüğü şirk ve ehlidir.</p>
</div>
{FT}
<aside>Allah için sevmek ve Allah için buğz etmek birbirinden ayrılmaz; ikisi de imanı kemale erdirmektendir.</aside>
</section>''',
'hadith3': f'''<section id="hadith3" class="c dark">
<div class="head">
<p class="eb">Yedinci delil · Sünnet’ten</p>
<h2>Ebû Saîd el-Hudrî (r.a.) hadisi</h2>
</div>
<div class="head">
<p class="ayah big">«مَنْ رَأَى مِنْكُمْ مُنْكَرًا فَلْيُغَيِّرْهُ بِيَدِهِ، فَإِنْ لَمْ يَسْتَطِعْ فَبِلِسَانِهِ، فَإِنْ لَمْ يَسْتَطِعْ فَبِقَلْبِهِ، وَذَلِكَ أَضْعَفُ الْإِيمَانِ»</p>
{meal('«Sizden kim bir münker görürse onu eliyle değiştirsin; gücü yetmezse diliyle; buna da gücü yetmezse kalbiyle. Bu da imanın en zayıfıdır.»', False)}
<p class="ref">Müslim</p>
</div>
<div class="card" style="--i:0; flex:none">
<h3>Delil yönü</h3>
<p class="txt">Kalple reddetmek, yani kalbin münkere buğz etmesi, kimseden düşmez. Allah’tan başkasına ibadet münkerlerin en büyüğüdür; ona kalben buğz her Müslümana her hâlde vaciptir.</p>
</div>
{FT}
<aside>Allah’tan başkasına ibadete kalben buğz etmek, her Müslümana her hâlde vaciptir.</aside>
</section>''',
'tawhid': f'''<section id="tawhid" class="c dark">
<div class="head">
<p class="eb">Altıncı bölüm · Buğz ve tevhid kelimesi</p>
<h2>Hak olarak ibadet edilen yalnız Allah’tır</h2>
</div>
<div class="row">
<div class="panel" style="--i:0">
<p class="kalima">لا إله</p>
<p class="tag" style="color:#D9B26A">Nefy · Lâ ilâhe</p>
<p class="txt">Kalbin tasdikinde: bâtıllığına itikad; amelde: terk; kalbin duygusunda: <b>Allah’tan başkasına ibadete, tâğuta ve ehline buğz</b>.</p>
<p class="pill">= Tâğutu inkâr</p>
</div>
<div class="panel" style="--i:1">
<p class="kalima">إلا الله</p>
<p class="tag" style="color:#D9B26A">İsbat · illallah</p>
<p class="txt">İbadete yalnız Allah’ın layık olduğuna itikad, Allah’ı ve tevhid ehlini sevmek, ibadette Allah’ı birlemek.</p>
<p class="pill">= Allah’a iman</p>
</div>
</div>
<p class="lead">Sevgi ve buğz birbirinden ayrılmaz: Allah’ı gerçekten seven, Allah’ın buğz ettiğine ve buğz ettiği kimseye buğz eder.</p>
{FT}
<aside>Birinci ders nefyin kalbin tasdikindeki, ikinci ders amelindeki gereğini; bu ders ise kalbin duygusundaki gereğini ele alıyor.</aside>
</section>''',
'aks': f'''<section id="aks" class="c alt">
<div class="head">
<p class="eb">Altıncı bölüm · Buğz ve tevhid kelimesi</p>
<h2>Muvahhidin kalbi ve müşrikin kalbi</h2>
</div>
<div class="row">
<div class="card" style="--i:0">
<p class="tag">Müminlerin Allah sevgisi daha güçlüdür</p>
<p class="ayah sm">﴿وَمِنَ النَّاسِ مَنْ يَتَّخِذُ مِنْ دُونِ اللَّهِ أَنْدَادًا يُحِبُّونَهُمْ كَحُبِّ اللَّهِ وَالَّذِينَ آمَنُوا أَشَدُّ حُبًّا لِلَّهِ﴾</p>
{meal('«İnsanlardan bazıları Allah’tan başkasını O’na denk tutar, onları Allah’ı sever gibi severler. İman edenlerin Allah’a sevgisi ise daha güçlüdür.»')}
<p class="ref">Bakara, 165</p>
<hr class="rule">
<p class="txt">Allah’ı gerçekten seven, Allah’ın buğz ettiğine ve buğz ettiği kimseye buğz eder.</p>
</div>
<div class="card ink" style="--i:1">
<p class="tag">Müşriklerin hâli bunun tersidir</p>
<p class="ayah sm">﴿وَإِذَا ذُكِرَ اللَّهُ وَحْدَهُ اشْمَأَزَّتْ قُلُوبُ الَّذِينَ لَا يُؤْمِنُونَ بِالْآخِرَةِ وَإِذَا ذُكِرَ الَّذِينَ مِنْ دُونِهِ إِذَا هُمْ يَسْتَبْشِرُونَ﴾</p>
{meal('«Allah tek olarak anıldığında ahirete inanmayanların kalpleri daralır; O’ndan başkaları anıldığında ise hemen sevinirler.»')}
<p class="ref">Zümer, 45</p>
<hr class="rule">
<p class="txt">Onların kalpleri tevhidden nefret edip şirke sevinir; muvahhidin kalbi tevhide sevinir, şirkten nefret eder.</p>
</div>
</div>
{FT}
<aside>Öğrencilere sorun: Zümer ayetine göre muvahhidin kalbinin alameti nedir? Cevap: Tevhide sevinir, şirkten nefret eder.</aside>
</section>''',
'amthila': f'''<section id="amthila" class="c">
<div class="head">
<p class="eb">Yedinci bölüm · Uygulamalı örnekler</p>
<h2>Hayattan</h2>
</div>
<div class="tiles">
<div class="row">
<div class="tile"><p class="tag">Mevsimler ve kutlamalar</p><p class="txt">Onlara sevinmez, hoşlanarak seyretmeye gitmez, ehlini onlarla tebrik etmez.</p></div>
<div class="tile"><p class="tag">Övmek ve güzel bulmak</p><p class="txt">Şirki ve ehlini övmez; şirk görüntüleri için «Ne güzel!» demez.</p></div>
<div class="tile"><p class="tag">Akrabalık</p><p class="txt">Akrabasının şirkine buğz eder, bu hâli üzerine onunla sevgi bağı kurmaz, ona razı olmaz.</p></div>
</div>
<div class="row">
<div class="tile"><p class="tag">Miras kalan âdetler</p><p class="txt">Ataların âdeti olsa da içindeki ibadete buğz eder; İbrahim’in dediği gibi.</p></div>
<div class="tile"><p class="tag">Kalbi muhasebe</p><p class="txt">Bir meyil ya da sevgi bulursa tevhid ilmiyle ve Allah’a, küfrü çirkin göstermesi için duayla tedavi eder.</p></div>
</div>
</div>
{FT}
<aside>Örnekleri öğrencilerle tartışın ve kendi çevrelerinden örnekler isteyin.</aside>
</section>''',
'tanbihat': f'''<section id="tanbihat" class="c alt">
<div class="head">
<p class="eb">Nasslardan uyarılar</p>
<h2>Dört uyarı</h2>
</div>
<div class="row">
<div class="col">
<div class="notlist">
<p class="nl"><b>1. Kendisine ibadet edilen ve buna razı olmayana buğz edilmez</b>: İsa (aleyhisselâm), melekler ve salihler gibi; buğz edilen onlara ibadet edilmesidir, kendileri değil (Mâide, 117).</p>
<p class="nl"><b>2. Allah için buğz, anne babaya iyiliği düşürmez</b>: «Onlara itaat etme; dünyada onlarla iyi geçin.» (Lokmân, 15)</p>
</div>
</div>
<div class="col">
<div class="notlist">
<p class="nl"><b>3. Buğz adaleti düşürmez</b>: «Bir topluluğa olan buğzunuz sizi adaletsizliğe sürüklemesin. Adaletli olun; bu, takvaya daha yakındır.» (Mâide, 8)</p>
<p class="nl"><b>4. Tekfir ve düşmanlık ayrı iki husustur</b>: Gelecek iki derste açıklanacaktır.</p>
</div>
</div>
</div>
{FT}
<aside>Şenaân buğz demektir; Müslümanın buğzu onu adaleti terk etmeye sevk etmez.</aside>
</section>''',
'thamarat': f'''<section id="thamarat" class="c">
<div class="head">
<p class="eb">Sekizinci bölüm</p>
<h2>Allah için buğzun meyveleri</h2>
</div>
<div class="row">
<div class="card" style="--i:0"><p class="tag">1</p><h3>İmanın tadı</h3><p class="txt">Enes (r.a.) hadisinde geçtiği gibi.</p></div>
<div class="card" style="--i:1"><p class="tag">2</p><h3>İmanı kemale erdirmek</h3><p class="txt">«Kim Allah için sever, Allah için buğz eder… imanını kemale erdirmiş olur.»</p></div>
<div class="card" style="--i:2"><p class="tag">3</p><h3>Doğru yolda olmak</h3><p class="txt">«İşte doğru yolda olanlar onlardır.» (Hucurât, 7)</p></div>
</div>
<div class="row">
<div class="card" style="--i:3"><p class="tag">4</p><h3>İbrahim’e uymak</h3><p class="txt">Ve beraberindekilere; Allah’ın örnek alınmasını emrettiği güzel örnek onlardır.</p></div>
<div class="card ink" style="--i:4"><p class="tag">5</p><h3>İmanın yazılması ve destek</h3><p class="txt">«Allah onların kalplerine imanı yazmış ve onları kendi katından bir ruhla desteklemiştir.»</p></div>
</div>
{FT}
<aside>Bu bölümü öğrencilere şu duayı hatırlatarak bitirin: Allah’ım, imanı bize sevdir ve kalplerimizde süsle; küfrü, fıskı ve isyanı bize çirkin göster ve bizi doğru yolda olanlardan eyle.</aside>
</section>''',
'review1': f'''<section id="review1" class="c alt">
<div class="head">
<p class="eb">Anlamı pekiştirmek</p>
<h2>Tekrar soruları (1)</h2>
</div>
<div class="qa"><p class="qn">1</p><div class="qbody"><p class="q">Buğzun sözlük anlamı nedir? Bağzâ ne demektir?</p><p class="a fragment">Buğz sevginin zıddıdır; bağzâ ise şiddetli buğzdur.</p></div></div>
<div class="qa"><p class="qn">2</p><div class="qbody"><p class="q">Bu husustaki buğzun ilgili olduğu üç şey nedir?</p><p class="a fragment">Allah’tan başkasına ibadet, kendisine ibadet edilen ve buna razı olan tâğut ve ona ibadet edenler.</p></div></div>
<div class="qa"><p class="qn">3</p><div class="qbody"><p class="q">Tâğutların beş başını sayın.</p><p class="a fragment">İblis, kendisine ibadet edilen ve buna razı olan, insanları kendisine ibadete çağıran, gaybı bildiğini iddia eden ve Allah’ın indirdiğinden başkasıyla hükmeden.</p></div></div>
{FT}
<aside>Önce soruyu sorun, öğrencilerin cevaplamasını bekleyin, sonra tıklayarak cevabı gösterin.</aside>
</section>''',
'review2': f'''<section id="review2" class="c">
<div class="head">
<p class="eb">Anlamı pekiştirmek</p>
<h2>Tekrar soruları (2)</h2>
</div>
<div class="qa"><p class="qn">4</p><div class="qbody"><p class="q">Mücâdele ayetinin bu husustaki delil yönü nedir?</p><p class="a fragment">Allah, en yakını olsa bile Allah’a ve Rasûlü’ne karşı gelenle sevgi bağı kurandan imanı nefyetti; mümin şirk ehlini sevmez, onlara Allah yolunda buğz eder.</p></div></div>
<div class="qa"><p class="qn">5</p><div class="qbody"><p class="q">Hristiyanlar ona ibadet ettiği için İsa (aleyhisselâm)’a buğz edilir mi? Neden?</p><p class="a fragment">Hayır; çünkü kendisine ibadet edilmesine razı değildir, tâğut değildir; aksine sevilir ve dost edinilir. Buğz edilen, ona Allah’tan başka ibadet edilmesidir (Mâide, 117).</p></div></div>
<div class="qa"><p class="qn">6</p><div class="qbody"><p class="q">Bir adam müşrik akrabasını seviyor ve onun bu hâli üzerine onunla sevgi bağı kuruyor. Kusuru nedir?</p><p class="a fragment">Şirk ehline Allah yolunda buğz etmemiştir; Allah, babaları, oğulları, kardeşleri ya da akrabaları olsalar bile, karşı gelenlerle sevgi bağı kurandan imanı nefyetmiştir.</p></div></div>
{FT}
<aside>Şunu da sorun: Buğz olmadan itikad ve terk neden yetmez? Cevap: Kalbin, Allah’ın sevdiğini sevmesi; Allah’ın buğz ettiğine ve buğz ettiği kimseye buğz etmesi gerekir.</aside>
</section>''',
'review3': f'''<section id="review3" class="c alt">
<div class="head">
<p class="eb">Anlamı pekiştirmek · Doğru mu, yanlış mı?</p>
<h2>Tekrar soruları (3)</h2>
</div>
<div class="qa"><p class="qn">7</p><div class="qbody"><p class="q">Ona da ehline de buğz etmese bile, Müslümanın Allah’tan başkasına ibadetin bâtıl olduğunu bilmesi yeterlidir.</p><p class="a fragment">Yanlış; ona ve ehline Allah yolunda buğz etmesi gerekir. Müslüman tevhid ile şirk arasında tarafsız olmaz.</p></div></div>
<div class="qa"><p class="qn">8</p><div class="qbody"><p class="q">Kendisine ibadet edilmesine razı olmasa bile, Allah’tan başka ibadet edilen herkese buğz edilir.</p><p class="a fragment">Yanlış; İsa (aleyhisselâm), melekler ve salihler gibi razı olmayana buğz edilmez; buğz edilen onlara ibadet edilmesidir.</p></div></div>
<div class="qa"><p class="qn">9</p><div class="qbody"><p class="q">Allah için buğz, imanı kemale erdirmektendir.</p><p class="a fragment">Doğru; «Kim Allah için sever, Allah için buğz eder… imanını kemale erdirmiş olur.»</p></div></div>
{FT}
<aside>Öğrenciden her ifadede cevabını gerekçelendirmesini isteyin; sadece «doğru» ya da «yanlış» demekle yetinmesin.</aside>
</section>''',
'jamia': '''<section id="jamia" class="gold mid">
<p class="eb">Öğrencinin ezberleyeceği özet</p>
<p class="jamia">Bu husustaki buğz; Müslümanın kalbiyle Allah’tan başkasına ibadete, Allah’ı bırakıp kendisine ibadet edilen ve buna razı olan tâğuta ve ona ibadet edenlere Allah yolunda buğz etmesidir. Şirke razı olmaz ve onu sevmez; en yakın akrabası olsalar bile ehliyle sevgi bağı kurmaz. Bunun etkisi dilinde ve azalarında görünür.</p>
<aside>Öğrencilerden bu ifadeyi ezberlemeleri istenir. Sonraki ders dördüncü husus hakkındadır: ehlini tekfir etmek.</aside>
</section>''',
'khatima': f'''<section id="khatima" class="dark mid glow">
<div class="cover-body">
{LOGO_TR}
<p class="eb">Dersin sonu</p>
<p class="closing">Allah Teâlâ’dan imanı bize sevdirmesini ve kalplerimizde süslemesini, küfrü, fıskı ve isyanı bize çirkin göstermesini, bizi doğru yolda olanlardan kılmasını ve O’na kavuşuncaya kadar bizi tevhid üzere sabit kılmasını dileriz.</p>
<hr class="gl">
<p class="lead">Hamd âlemlerin Rabbi Allah’a mahsustur.</p>
</div>
<aside>Özet: Bu buğz, Allah’tan başkasına ibadetin bâtıl olduğuna itikadın kalbin duygusundaki meyvesidir; terk de onun azalardaki meyvesidir. Tevhid kelimesindeki «Lâ ilâhe»nin gereklerinden ve tâğutu inkârın aslındandır.</aside>
</section>''',
}

SECTIONS = {
 'ar': {"s1": ("مدخل الدرس: صفة الكفر بالطاغوت وخطة الدرس", "cover"), "s2": ("معنى البغض، وما يتعلق به: عبادة غير الله والطاغوت وأهلها، وصوره", "lugha"),
        "s3": ("العلاقة بين البغض والاعتقاد والترك", "alaqa"), "s4": ("الأدلة الشرعية من الكتاب والسنة ووجه الدلالة منها", "adilla1"),
        "s5": ("البغض وكلمة التوحيد، والأمثلة والتنبيهات والثمرات", "tawhid"), "s6": ("أسئلة المراجعة والخلاصة والخاتمة", "review1")},
 'tr': {"s1": ("Dersin girişi: tâğutu inkârın keyfiyeti ve dersin planı", "cover"), "s2": ("Buğzun anlamı; ilgili olduğu şeyler: Allah’tan başkasına ibadet, tâğut ve ehli; şekilleri", "lugha"),
        "s3": ("Buğzun itikad ve terk ile ilişkisi", "alaqa"), "s4": ("Kitap ve Sünnet’ten şer’î deliller ve delil yönleri", "adilla1"),
        "s5": ("Buğz ve tevhid kelimesi; örnekler, uyarılar ve meyveler", "tawhid"), "s6": ("Tekrar soruları, özet ve kapanış", "review1")},
}
TITLE = {'ar': 'بغض الطاغوت وعبادته وأهله', 'tr': 'Tâğuta, İbadetine ve Ehline Buğz'}

for lang, slides in (('ar', AR), ('tr', TR)):
    assert list(slides) == ORDER, (lang, [k for k in ORDER if k not in slides])
    src = json.load(open(os.path.join(DECKS, f'{lang}2', 'deck.json'), encoding='utf-8'))
    d = os.path.join(DECKS, f'{lang}3')
    shutil.rmtree(os.path.join(d, 'slides'), ignore_errors=True); os.makedirs(os.path.join(d, 'slides'))
    for k, v in slides.items():
        open(os.path.join(d, 'slides', k + '.html'), 'w', encoding='utf-8').write(v.strip() + '\n')
    src['title'] = TITLE[lang]; src['order'] = ORDER
    src['sections'] = {k: {'description': a, 'start': b} for k, (a, b) in SECTIONS[lang].items()}
    json.dump(src, open(os.path.join(d, 'deck.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print(lang, len(slides))
