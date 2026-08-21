import requests

local_url = "http://127.0.0.1:8000"

print("Testing local Django server...")
print("=" * 60)

try:
    response = requests.get(local_url)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("SUCCESS - Local server is working!")
        print(f"Server is accessible at: {local_url}")
    else:
        print(f"FAILED with status {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

print("=" * 60)