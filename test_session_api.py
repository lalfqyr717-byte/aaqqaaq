import requests

# First login to create session
login_url = "http://127.0.0.1:8000/api/auth/login/"
session_url = "http://127.0.0.1:8000/api/session/"

print("Step 1: Login...")
session = requests.Session()
login_data = {
    "username": "maqi",
    "password": "12345",
    "accountType": "admin"
}

try:
    login_response = session.post(login_url, json=login_data)
    print(f"Login Status: {login_response.status_code}")
    print(f"Login Response: {login_response.text[:200]}...")
    
    if login_response.status_code == 200:
        print("\nStep 2: Check session...")
        session_response = session.get(session_url)
        print(f"Session Status: {session_response.status_code}")
        print(f"Session Response: {session_response.text}")
        
        if session_response.status_code == 200:
            result = session_response.json()
            if result.get('authenticated'):
                print("\nSession authentication SUCCESS!")
            else:
                print("\nSession authentication FAILED!")
    
except Exception as e:
    print(f"Error: {e}")
