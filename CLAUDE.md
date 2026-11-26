# مشروع «وتواصوا بالحق» · tevhidim.com

موقع تعليمي بالعربية والتركية، يُنشر عبر GitHub Pages على https://tevhidim.com/

## قبل أي عمل

اقرأ مجلد [`guide/`](guide/README.md): فيه دليل إنتاج الدرس (`lesson-production.md`)، ودليل الأسلوب والمصطلحات (`style-and-terms.md`)، وخريطة كل سلسلة في `series/`. وتفاصيل ترتيب المستودع في [`README.md`](README.md).

## قواعد ثابتة

- **كل ما يُضاف بالعربية يُضاف مثله بالتركية.** لا يُنشر شيء بلغة واحدة.
- **التعديل في `src/` فقط.** مجلد `docs/` هو الموقع المولَّد، لا يُعدَّل يدويًا (عدا رفع الفيديوهات إلى `docs/media/`).
- رسائل الـ commit تُكتب بالعربية، وصفًا لما تغيّر من جهة القارئ.
- الموقع يُنشر من فرع `main`؛ فلا يظهر تعديل للناس حتى يُدمج فيه.

## البناء والفحص

```
pip install markdown segno
python3 src/build.py                                  # يولّد الموقع كاملًا في docs/
python3 -m http.server 8765 --directory docs &        # ثم الفحص قبل الرفع:
python3 src/tools/test.py http://localhost:8765/
```

بعد تعديل ملخص (`summaries.py`) أو عنوان درس: تُولَّد ملفات PDF والصور من جديد — الأوامر في README.
