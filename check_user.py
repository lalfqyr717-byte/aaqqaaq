import os
import sys
import django

sys.path.insert(0, 'C:\\Users\\moktata\\Desktop\\moq-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("Checking admin user...")
admin_user = User.objects.filter(username='admin').first()
if admin_user:
    print(f"User found: {admin_user.username}")
    print(f"Email: {admin_user.email}")
    print(f"Is superuser: {admin_user.is_superuser}")
    print(f"Is staff: {admin_user.is_staff}")
    print(f"Is active: {admin_user.is_active}")
    print(f"Password check: {admin_user.check_password('admin123')}")
else:
    print("No admin user found")
