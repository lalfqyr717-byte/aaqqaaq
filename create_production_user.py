import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("Creating production user...")

# Delete existing maqi user if exists
if User.objects.filter(username='maqi').exists():
    User.objects.filter(username='maqi').delete()
    print("Deleted existing maqi user")

# Create new maqi user
maqi_user = User.objects.create_superuser('maqi', 'maqi@tox.iq', '12345')

print(f"Successfully created maqi user")
print(f"Username: {maqi_user.username}")
print(f"Email: {maqi_user.email}")
print(f"Is superuser: {maqi_user.is_superuser}")
print(f"Is staff: {maqi_user.is_staff}")
print(f"Is active: {maqi_user.is_active}")
print("Login credentials: maqi / 12345")