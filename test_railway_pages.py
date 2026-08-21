import requests

railway_url = "https://moq.up.railway.app"
pages_to_test = [
    f"{railway_url}/pages/sales.html",
    f"{railway_url}/pages/products.html",
    f"{railway_url}/pages/warehouse.html",
    f"{railway_url}/pages/settings.html",
]

print("Testing Railway pages redirect...")
for url in pages_to_test:
    print(f"\nTesting: {url}")
    try:
        response = requests.get(url, allow_redirects=False)
        print(f"  Status: {response.status_code}")
        if response.status_code == 302:
            print(f"  Redirect to: {response.headers.get('Location', 'unknown')}")
            print(f"  SUCCESS - Redirecting to home")
        elif response.status_code == 200:
            print(f"  SUCCESS - Direct access to home")
        else:
            print(f"  FAILED with status {response.status_code}")
    except Exception as e:
        print(f"  Error: {e}")

print(f"\nTesting home page directly...")
try:
    response = requests.get(railway_url)
    print(f"  Status: {response.status_code}")
    if response.status_code == 200:
        print(f"  SUCCESS - Home page accessible")
except Exception as e:
    print(f"  Error: {e}")