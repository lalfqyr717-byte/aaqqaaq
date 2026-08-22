# Railway Configuration Solution - Manual GUI Fix

## مشكلة Railway الحالية
Railway في حلقة لا نهائية: "Starting Container → Migrations → Stopping Container" دون بدء الخادم أبداً.

السبب: Railway يستخدم تكويناً مخزناً مؤقتاً في واجهة المستخدم (GUI) ولا يلتقط أي من التغييرات في الملفات.

## الحل النهائي: استخدام Railway GUI

### الخطوة 1: الدخول إلى Railway Console
1. اذهب إلى https://railway.app
2. سجل الدخول باستخدام حسابك
3. اختر مشروع TOX ERP

### الخطوة 2: إعدادات النشر
1. انقر على "Settings"
2. انقر على "Build & Deploy Settings"
3. انقر على "Edit Config"

### الخطوة 3: تغيير Start Command يدوياً
في قسم "Start Command"، أدخل الأمر التالي:

```
python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:$PORT
```

### الخطوة 4: إضافة متغيرات البيئة
1. انقر على "Variables"
2. تأكد من وجود المتغيرات التالية:
   - `ALLOWED_HOSTS`: `127.0.0.1,localhost,moq.up.railway.app,moqq.up.railway.app,healthcheck.railway.app`
   - `TOX_DEBUG`: `False`
   - `DJANGO_SETTINGS_MODULE`: `tox.settings`
   - `PORT`: `8080`

### الخطوة 5: إعادة النشر
1. انقر على "Redeploy"
2. انتظر حتى يكتمل النشر
3. راقب السجلات للتأكد من عدم وجود أخطاء

## لماذا هذا الحل؟
- Railway يستخدم تكويناً مخزناً مؤقتاً في واجهة المستخدم
- تغييرات الملفات (Dockerfile, nixpacks.toml, entrypoint.sh) لا تؤثر على هذا التكوين المخزن
- التعديل المباشر في Railway GUI يتجاوز المشكلة
- Start Command المباشر يضمن التنفيذ الصحيح

## التحقق من النجاح
بعد النشر، يجب أن ترى:
- ✅ Migrations تعمل بنجاح
- ✅ Static files تجمع بنجاح
- ✅ Django server يبدأ على المنفذ 8080
- ✅ Container يستمر في العمل (لا يتوقف)
- ✅ التطبيق يستجيب على `https://moqq.up.railway.app`

## معلومات الدخول
- **اسم المستخدم:** `user`
- **كلمة المرور:** `user123`

## الخطة البديلة: حذف وإعادة إنشاء المشروع
إذا استمرت المشاكل، الحل البديل هو:
1. حذف المشروع الحالي من Railway
2. إنشاء مشروع جديد من GitHub
3. استخدام التكوين الصحيح من البداية

## ملخص
المشكلة ليست في الكود، بل في تكوين Railway المخزن مؤقتاً. الحل الوحيد الموثوق هو التعديل المباشر في Railway GUI.