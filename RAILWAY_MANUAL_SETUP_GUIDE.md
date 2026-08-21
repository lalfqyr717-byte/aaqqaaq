# إرشادات Railway Manual Setup Guide

## المشكلة الحالية
Railway يستخدم تكويناً مخزناً مؤقتاً (cached configuration) في واجهة المستخدم يحدد استخدام `./start_prod.sh`. هذا التكوين لا يتغير بتغييرات الملفات في Git.

## الحل: إعداد Railway يدوياً

### الخطوة 1: الدخول إلى Railway Console
1. اذهب إلى https://railway.app
2. سجل الدخول باستخدام حسابك
3. اختر مشروع TOX ERP الخاص بك

### الخطوة 2: إعدادات النشر (Deployment Settings)
1. في صفحة المشروع، انقر على "Settings"
2. اختر "Variables"
3. تأكد من وجود المتغيرات التالية:
   - `ALLOWED_HOSTS`: `127.0.0.1,localhost,moq.up.railway.app,moqq.up.railway.app,healthcheck.railway.app`
   - `TOX_DEBUG`: `False`
   - `TOX_SECRET_KEY`: قيمة سرية عشوائية

### الخطوة 3: إعداد Start Command يدوياً
1. في صفحة المشروع، انقر على "Settings"
2. اختر "Nixpacks" أو "Build & Deploy Settings"
3. في قسم "Start Command"، أدخل الأمر التالي:
   ```
   python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 2
   ```
4. احفظ التغييرات

### الخطوة 4: إعادة النشر
1. انقر على "Redeploy" في صفحة المشروع
2. انتظر حتى يكتمل النشر
3. راقب السجلات (Logs) للتأكد من عدم وجود أخطاء

### الخطوة 5: التحقق من النشر
1. افتح الرابط المقدم من Railway
2. تأكد من أن الصفحة الرئيسية تعمل
3. تأكد من أن جميع الصفحات تعمل

## الخطة البديلة: استخدام Railway GUI فقط

### إذا استمرت المشاكل، يمكنك استخدام Railway GUI بالكامل:

#### 1. إلغاء الملفات المشكلة من Git
حذف هذه الملفات من المستودع المحلي:
- `start_prod.sh`
- `scripts/start_prod.sh`
- `Procfile` (إذا كان موجوداً)
- `railway.toml`
- `nixpacks.toml`

#### 2. استخدام Railway Console للإعداد الكامل
1. في Railway Console، حدد "Buildpacks" أو "Nixpacks"
2. أدخل الأمر Start:
   ```
   python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 2
   ```
3. حدد Python version: 3.12
4. حدد Build Command:
   ```
   pip install -r requirements.txt
   ```

#### 3. متغيرات البيئة
أضف المتغيرات التالية في Railway Variables:
```
ALLOWED_HOSTS=127.0.0.1,localhost,moq.up.railway.app,moqq.up.railway.app,healthcheck.railway.app
TOX_DEBUG=False
DJANGO_SETTINGS_MODULE=tox.settings
```

## حالة المشروع الحالية

### ما يعمل محلياً ✅
- جميع 18 صفحة HTML تعمل
- جميع API endpoints تعمل
- Django runserver يعمل على المنفذ 8765
- جميع التبعيات مثبتة

### الملفات الموجودة في Git
- ✅ `templates/` - جميع القوالب والصفحات
- ✅ `tox/` - جميع ملفات Django
- ✅ `assets/` - ملفات CSS و JS
- ✅ `requirements.txt` - جميع التبعيات
- ✅ `wsgi.py` - تطبيق WSGI
- ✅ `railway.toml` - تكوين Railway
- ✅ `nixpacks.toml` - تكوين Nixpacks
- ⚠️ `start_prod.sh` - موجود لكن متجاهل
- ❌ `Procfile` - محذوف

## المشكلة الأساسية
Railway يستخدم تكويناً مخزناً مؤقتاً في واجهة المستخدم (GUI) يحدد استخدام `./start_prod.sh`. هذا التكوين:
- لا يتغير بتغييرات الملفات في Git
- لا يتغير بحذف الملفات
- لا يتغير بتعديل الملفات
- يمكن تغييره فقط من Railway GUI

## الحل النهائي المقترح
استخدم Railway GUI لتعديل Start Command مباشرة:
1. انتقل إلى Railway Console
2. ابحث عن "Start Command" أو "Deployment Settings"
3. غيره من `./start_prod.sh` إلى:
   ```
   python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 2
   ```
4. احفظ وأعد النشر

هذا يتجاوز مشكلة التكوين المخزن مؤقتاً عن طريق التعديل المباشر في Railway GUI.