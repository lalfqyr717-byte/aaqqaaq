import requests

# Test accessing the home page
home_url = "http://127.0.0.1:8000/"

print("Testing home page access...")
try:
    response = requests.get(home_url)
    print(f"Status Code: {response.status_code}")
    print(f"Content length: {len(response.text)}")
    
    if response.status_code == 200:
        print("\nHome page access SUCCESS!")
        print(f"Contains login form: {'data-login-form' in response.text}")
        print(f"Contains dashboard: {'tox-dashboard' in response.text}")
    else:
        print(f"\nHome page access FAILED with status {response.status_code}")
        
except Exception as e:
    print(f"Error: {e}")
