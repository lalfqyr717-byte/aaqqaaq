import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth.models import User

# Ensure production user exists with correct password
if User.objects.filter(username='user').exists():
    user = User.objects.get(username='user')
    user.set_password('user123')
    user.is_superuser = True
    user.is_staff = True
    user.email = 'user@tox.iq'
    user.save()
    print("Updated existing production user")
else:
    user = User.objects.create_superuser('user', 'user@tox.iq', 'user123')
    print("Created new production user")

print(f"Username: {user.username}")
print(f"Email: {user.email}")
print(f"Is superuser: {user.is_superuser}")
print(f"Is staff: {user.is_staff}")
print(f"Is active: {user.is_active}")
print("Login credentials: user / user123")
