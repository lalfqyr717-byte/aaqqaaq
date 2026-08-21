import os
import sys
import django

sys.path.insert(0, 'C:\\Users\\moktata\\Desktop\\moq-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

print("=" * 60)
print("Database User Check")
print("=" * 60)

# Show all users
print("\nAll users:")
for user in User.objects.all():
    print(f"  - username: {user.username}, email: {user.email}, is_active: {user.is_active}, is_staff: {user.is_staff}, is_superuser: {user.is_superuser}")

# Check for maqi user
print("\nChecking maqi user:")
maqi_user = User.objects.filter(username='maqi').first()
if maqi_user:
    print(f"  - exists: Yes")
    print(f"  - email: {maqi_user.email}")
    print(f"  - is_active: {maqi_user.is_active}")
    print(f"  - is_staff: {maqi_user.is_staff}")
    print(f"  - is_superuser: {maqi_user.is_superuser}")
    print(f"  - password hash: {maqi_user.password[:20]}...")
else:
    print(f"  - exists: No")

# Test authentication
print("\nAuthentication test:")
test_cases = [
    ('maqi', '12345'),
    ('admin', 'admin123'),
    ('user', 'user123'),
]

for username, password in test_cases:
    print(f"  - {username}/{password}: ", end='')
    user = authenticate(username=username, password=password)
    if user:
        print(f"SUCCESS")
    else:
        print(f"FAILED")

# Test set_password
print("\nTesting set_password:")
if maqi_user:
    print(f"  - Resetting maqi password to 12345")
    maqi_user.set_password('12345')
    maqi_user.save()
    print(f"  - Saved")
    
    # Test again
    print(f"  - Testing authentication after reset: ", end='')
    user = authenticate(username='maqi', password='12345')
    if user:
        print(f"SUCCESS")
    else:
        print(f"FAILED")
