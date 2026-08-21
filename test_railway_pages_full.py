import requests

railway_url = "https://moq.up.railway.app"
pages_to_test = [
    f"{railway_url}/pages/sales.html",
    f"{railway_url}/pages/products.html",
    f"{railway_url}/pages/purchases.html",
    f"{railway_url}/pages/clients.html",
    f"{railway_url}/pages/suppliers.html",
    f"{railway_url}/pages/warehouse.html",
    f"{railway_url}/pages/employees.html",
    f"{railway_url}/pages/reports.html",
    f"{railway_url}/pages/settings.html",
]

print("Testing Railway pages availability...")
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