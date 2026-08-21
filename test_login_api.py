import requests
import json

url = "http://127.0.0.1:8000/api/auth/login/"
headers = {"Content-Type": "application/json"}
data = {
    "username": "maqi",
    "password": "12345",
    "accountType": "admin"
}

print("Testing login API...")
print(f"URL: {url}")
print(f"Data: {data}")

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        if result.get('ok'):
            print("\nLogin SUCCESS!")
            print(f"User: {result.get('user')}")
        else:
            print(f"\nLogin FAILED: {result.get('reason')}")
    else:
        print(f"\nLogin FAILED with status {response.status_code}")
        
except Exception as e:
    print(f"\nError: {e}")
