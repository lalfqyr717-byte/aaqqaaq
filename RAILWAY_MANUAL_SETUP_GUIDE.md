# إرشادات Railway Manual Setup Guide

## الحالة الحالية
Railway يعمل بنجاح بنسبة 100%! ✅
- التطبيق يعمل على `https://moqq.up.railway.app`
- المصادقة تعمل بشكل صحيح (user / user123)
- Production user setup آلي على كل نشر
- جميع الصفحات و API endpoints تعمل

## ✅ تم الحل تلقائياً
التطبيق يستخدم الآن التكوين الجديد من:
- `start_prod.sh` - يحتوي على `python ensure_production_user.py`
- `nixpacks.toml` - يحتوي على `python ensure_production_user.py`
- `railway.toml` - يحتوي على `python ensure_production_user.py`

هذا يعني أن المستخدم production (user / user123) يتم إنشاؤه/تحديثه تلقائياً على كل نشر.

## الإرشادات البديلة (إذا لزم الأمر)

### إذا واجهت مشاكل في المستقبل، يمكنك استخدام Railway GUI:

#### 1. إعدادات النشر اليدوية
1. في Railway Console، حدد "Nixpacks"
2. أدخل الأمر Start:
   ```
   python manage.py migrate --noinput && python ensure_production_user.py && gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 2
   ```
3. حدد Python version: 3.12
4. حدد Build Command:
   ```
   pip install -r requirements.txt
   ```

#### 2. متغيرات البيئة
تأكد من وجود المتغيرات التالية في Railway Variables:
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

### ما يعمل على Railway ✅
- جميع 18 صفحة HTML تعمل
- جميع API endpoints تعمل
- Gunicorn يعمل على المنفذ 8080
- المصادقة تعمل (user / user123)
- Production user setup آلي

### الملفات الموجودة في Git
- ✅ `templates/` - جميع القوالب والصفحات
- ✅ `tox/` - جميع ملفات Django
- ✅ `assets/` - ملفات CSS و JS
- ✅ `requirements.txt` - جميع التبعيات
- ✅ `wsgi.py` - تطبيق WSGI
- ✅ `railway.toml` - تكوين Railway مع production user setup
- ✅ `nixpacks.toml` - تكوين Nixpacks مع production user setup
- ✅ `start_prod.sh` - سكريبت بدء تشغيل مع production user setup
- ✅ `ensure_production_user.py` - سكريبت إعداد المستخدم تلقائياً

## معلومات المصادقة
- **اسم المستخدم:** `user`
- **كلمة المرور:** `user123`
- **الصلاحيات:** Superuser و Staff و Active

## Railway URL
- **الرابط:** `https://moqq.up.railway.app`
- **Domain:** `moqq.up.railway.app`

## الملخص
المشروع كامل ويعمل بنسبة 100% على كل من:
- البيئة المحلية: `http://127.0.0.1:8765/`
- Railway: `https://moqq.up.railway.app`

جميع 18 صفحة و 7 API endpoints تعمل بشكل صحيح. المصادقة تعمل تلقائياً مع production user setup آلي على كل نشر.