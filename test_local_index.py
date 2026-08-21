import requests

local_url = "http://127.0.0.1:8000"
urls_to_test = [
    f"{local_url}/",
    f"{local_url}/index.html",
]

print("Testing local index.html redirect...")
for url in urls_to_test:
    print(f"\nTesting: {url}")
    try:
        response = requests.get(url, allow_redirects=False)
        print(f"  Status: {response.status_code}")
        if response.status_code == 302:
            print(f"  Redirect to: {response.headers.get('Location', 'unknown')}")
            print(f"  SUCCESS - Redirecting")
        elif response.status_code == 200:
            print(f"  SUCCESS - Direct access")
        else:
            print(f"  FAILED with status {response.status_code}")
    except Exception as e:
        print(f"  Error: {e}")