import requests

railway_url = "https://moq.up.railway.app"

print("Testing Railway home page...")
print(f"URL: {railway_url}")

try:
    response = requests.get(railway_url)
    print(f"Status Code: {response.status_code}")
    print(f"Content length: {len(response.text)}")
    
    if response.status_code == 200:
        print("\nHome page access SUCCESS!")
        print(f"Contains login form: {'data-login-form' in response.text}")
        print(f"Contains dashboard: {'tox-dashboard' in response.text}")
        print(f"Contains TOX branding: {'TOX' in response.text}")
    else:
        print(f"\nHome page access FAILED with status {response.status_code}")
        
except Exception as e:
    print(f"Error: {e}")