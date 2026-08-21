import requests
import json

railway_url = "https://moq.up.railway.app"
login_url = f"{railway_url}/api/auth/login/"
session_url = f"{railway_url}/api/session/"

print("Testing Railway login API...")
print(f"URL: {login_url}")

headers = {"Content-Type": "application/json"}
data = {
    "username": "maqi",
    "password": "12345",
    "accountType": "admin"
}

try:
    # Test login
    print("\nStep 1: Testing login...")
    response = requests.post(login_url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    
    if response.status_code == 200:
        result = response.json()
        if result.get('ok'):
            print("\nLogin SUCCESS!")
            print(f"User: {result.get('user')}")
            
            # Test session
            print("\nStep 2: Testing session...")
            session = requests.Session()
            session.post(login_url, headers=headers, json=data)
            session_response = session.get(session_url)
            print(f"Session Status: {session_response.status_code}")
            print(f"Session Response: {session_response.text[:200]}...")
            
            if session_response.status_code == 200:
                session_result = session_response.json()
                if session_result.get('authenticated'):
                    print("\nSession authentication SUCCESS!")
                else:
                    print("\nSession authentication FAILED!")
        else:
            print(f"\nLogin FAILED: {result.get('reason')}")
    else:
        print(f"\nLogin FAILED with status {response.status_code}")
        
except Exception as e:
    print(f"\nError: {e}")