import requests

# Test accessing pages directory
pages_to_test = [
    "http://127.0.0.1:8000/pages/sales.html",
    "http://127.0.0.1:8000/pages/products.html",
    "http://127.0.0.1:8000/pages/warehouse.html",
]

print("Testing pages directory access...")
for url in pages_to_test:
    print(f"\nTesting: {url}")
    try:
        response = requests.get(url)
        print(f"  Status: {response.status_code}")
        if response.status_code == 200:
            print(f"  SUCCESS")
        elif response.status_code == 404:
            print(f"  NOT FOUND (expected since pages directory is empty)")
        else:
            print(f"  FAILED with status {response.status_code}")
    except Exception as e:
        print(f"  Error: {e}")
