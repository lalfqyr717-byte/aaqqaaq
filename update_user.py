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
    print('Old admin user deleted')

# Create new superuser with requested credentials
new_user = User.objects.create_superuser('maiq', 'maiq@tox.iq', '12345')
print(f'New superuser created: {new_user.username}')
print(f'Email: {new_user.email}')
print(f'Is superuser: {new_user.is_superuser}')
print(f'Is staff: {new_user.is_staff}')
print(f'Is active: {new_user.is_active}')
print('\nLogin credentials:')
print(f'Username: maiq')
print(f'Password: 12345')
