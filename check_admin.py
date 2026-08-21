import os
import sys
import django

sys.path.insert(0, 'C:\\Users\\moktata\\Desktop\\moq-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Delete existing admin user if exists
if User.objects.filter(username='admin').exists():
    User.objects.filter(username='admin').delete()
    print('Existing admin user deleted')

# Create new superuser
admin = User.objects.create_superuser('admin', 'admin@tox.iq', 'admin123')
print(f'Superuser created: {admin.username}')
print(f'Email: {admin.email}')
print(f'Is superuser: {admin.is_superuser}')
print(f'Is staff: {admin.is_staff}')
print(f'Is active: {admin.is_active}')
