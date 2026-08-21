import requests

railway_url = "https://moq.up.railway.app"
urls_to_test = [
    f"{railway_url}/",
    f"{railway_url}/index.html",
]

print("Testing Railway index.html redirect...")
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