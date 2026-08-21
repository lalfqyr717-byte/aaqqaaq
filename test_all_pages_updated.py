import requests

local_url = "http://127.0.0.1:8000"

all_pages = [
    "/",
    "/pages/sales.html",
    "/pages/products.html",
    "/pages/purchases.html",
    "/pages/clients.html",
    "/pages/suppliers.html",
    "/pages/warehouse.html",
    "/pages/employees.html",
    "/pages/installments.html",
    "/pages/sales-invoices.html",
    "/pages/returns.html",
    "/pages/reports.html",
    "/pages/settings.html"
]

print("Testing all pages (13 total)...")
print("=" * 60)

for page in all_pages:
    url = f"{local_url}{page}"
    try:
        response = requests.get(url)
        status = "OK" if response.status_code == 200 else "FAIL"
        print(f"{status} {page}: {response.status_code}")
    except Exception as e:
        print(f"ERROR {page}: {e}")

print("=" * 60)