import os
import sys
import django

sys.path.insert(0, 'C:\\Users\\moktata\\Desktop\\moq-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("Checking all users...")
for user in User.objects.all():
    print(f"Username: {user.username}, Email: {user.email}, Is Superuser: {user.is_superuser}, Is Staff: {user.is_staff}, Is Active: {user.is_active}")

print("\nTesting login with maiq/12345...")
from django.contrib.auth import authenticate
user = authenticate(username='maiq', password='12345')
if user:
    print(f"Login successful: {user.username}")
else:
    print("Login failed")

print("\nTesting login with admin/admin123...")
user = authenticate(username='admin', password='admin123')
if user:
    print(f"Login successful: {user.username}")
else:
    print("Login failed")
