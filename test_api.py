import os
import sys
import django

sys.path.insert(0, 'C:\\Users\\moktata\\Desktop\\moq-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tox.settings')
django.setup()

from django.test import Client
import json

client = Client()

# Test the login API
print("Testing /api/auth/login/ API...")
response = client.post('/api/auth/login/', 
    data=json.dumps({'username': 'maiq', 'password': '12345'}),
    content_type='application/json')

print(f"Status code: {response.status_code}")
print(f"Response content: {response.content.decode()}")

# Test session API
print("\nTesting /api/session/ API...")
response = client.get('/api/session/')
print(f"Status code: {response.status_code}")
print(f"Response content: {response.content.decode()}")
