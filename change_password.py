import os
import sys
import django

sys.path.insert(0, 'C:\\Users\\moktata\\Desktop\\moq-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Find admin user and change password
admin_user = User.objects.filter(username='admin').first()
if admin_user:
    admin_user.set_password('maiq 12345')
    admin_user.save()
    print(f"Password changed successfully for user: {admin_user.username}")
    print(f"New password: maiq 12345")
else:
    print("Admin user not found")
