import requests

local_url = "http://127.0.0.1:8000"

dashboard_links = [
    ("Sales Invoice", "/pages/sales.html"),
    ("Purchase Invoice", "/pages/purchases.html"),
    ("Add Product", "/pages/products.html"),
    ("Clients", "/pages/clients.html"),
    ("Suppliers", "/pages/suppliers.html"),
    ("Warehouse", "/pages/warehouse.html"),
    ("Employees", "/pages/employees.html"),
    ("Reports", "/pages/reports.html"),
    ("Settings", "/pages/settings.html")
]

print("Verifying dashboard shortcuts links...")
print("=" * 60)

all_ok = True
for name, path in dashboard_links:
    url = f"{local_url}{path}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"OK {name}: {path} (200)")
        else:
            print(f"FAIL {name}: {path} ({response.status_code})")
            all_ok = False
    except Exception as e:
        print(f"ERROR {name}: {path} - {e}")
        all_ok = False

print("=" * 60)
if all_ok:
    print("SUCCESS: All dashboard shortcuts work correctly!")
else:
    print("WARNING: Some dashboard shortcuts have issues")