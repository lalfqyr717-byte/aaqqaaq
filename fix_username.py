import os
import sys
import django

sys.path.insert(0, 'C:\\Users\\moktata\\Desktop\\moq-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("Fixing username issue...")

# Delete existing maiq user (without 'c')
if User.objects.filter(username='maiq').exists():
    User.objects.filter(username='maiq').delete()
    print("Deleted old user: maiq")

# Create new maqi user (with 'c')
maqi_user = User.objects.create_superuser('maqi', 'maqi@tox.iq', '12345')
print(f"Created new user: {maqi_user.username}")
print(f"Email: {maqi_user.email}")
print(f"Is superuser: {maqi_user.is_superuser}")
print(f"Is staff: {maqi_user.is_staff}")
print(f"Is active: {maqi_user.is_active}")

print("\nTest authentication...")
from django.contrib.auth import authenticate
user = authenticate(username='maqi', password='12345')
if user:
    print(f"Authentication SUCCESS for maqi/12345")
else:
    print(f"Authentication FAILED for maqi/12345")

print("\nLogin credentials:")
print(f"Username: maqi")
print(f"Password: 12345")
