import requests

local_url = "http://127.0.0.1:8000"
pages_to_test = [
    f"{local_url}/pages/sales.html",
    f"{local_url}/pages/products.html",
    f"{local_url}/pages/purchases.html",
    f"{local_url}/pages/clients.html",
    f"{local_url}/pages/suppliers.html",
    f"{local_url}/pages/warehouse.html",
    f"{local_url}/pages/employees.html",
    f"{local_url}/pages/reports.html",
    f"{local_url}/pages/settings.html",
]

print("Testing pages availability...")
for url in pages_to_test:
    print(f"\nTesting: {url}")
    try:
        response = requests.get(url)
        print(f"  Status: {response.status_code}")
        if response.status_code == 200:
            print(f"  SUCCESS - Page accessible")
            print(f"  Contains section: {'<section' in response.text}")
            print(f"  Contains sidebar: {'<aside' in response.text}")
        else:
            print(f"  FAILED with status {response.status_code}")
    except Exception as e:
        print(f"  Error: {e}")