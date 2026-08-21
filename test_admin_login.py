import requests
from requests.auth import HTTPBasicAuth

# Test Django admin login
admin_url = "http://127.0.0.1:8000/admin/"
admin_login_url = "http://127.0.0.1:8000/admin/login/"

print("Testing Django admin login...")
session = requests.Session()

# Get the admin login page to get CSRF token
print("Step 1: Get admin login page...")
try:
    response = session.get(admin_login_url)
    print(f"Admin page status: {response.status_code}")
    
    # Try to login
    print("\nStep 2: Login to admin...")
    login_data = {
        "username": "maqi",
        "password": "12345",
        "next": "/admin/"
    }
    
    login_response = session.post(admin_login_url, data=login_data)
    print(f"Login status: {login_response.status_code}")
    
    # Check if redirected to admin
    if login_response.status_code == 302:
        print(f"Redirected to: {login_response.headers.get('Location', 'unknown')}")
        
        # Follow redirect
        admin_response = session.get(admin_url)
        print(f"Admin page after login status: {admin_response.status_code}")
        
        if admin_response.status_code == 200 and "logout" in admin_response.text:
            print("\nDjango admin login SUCCESS!")
        else:
            print("\nDjango admin login FAILED!")
    else:
        print(f"Admin login response: {login_response.text[:200]}...")
        
except Exception as e:
    print(f"Error: {e}")
