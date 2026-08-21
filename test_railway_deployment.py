import requests

railway_url = "https://moq.up.railway.app"

pages_to_test = [
    "/",
    "/pages/sales.html",
    "/pages/products.html",
    "/pages/purchases.html",
    "/pages/clients.html",
    "/pages/suppliers.html",
    "/pages/warehouse.html",
    "/pages/employees.html",
    "/pages/installments.html",
    "/pages/reports.html",
    "/pages/settings.html"
]

print("Testing Railway deployment status...")
print("=" * 50)

for page in pages_to_test:
    url = f"{railway_url}{page}"
    try:
        response = requests.get(url)
        status = "OK" if response.status_code == 200 else "FAIL"
        print(f"{status} {page}: {response.status_code}")
    except Exception as e:
        print(f"ERROR {page}: {e}")

print("=" * 50)