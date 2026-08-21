import requests

local_url = "http://127.0.0.1:8000"

new_pages = [
    "/pages/sales-invoices.html",
    "/pages/returns.html"
]

print("Testing new pages...")
print("=" * 60)

for page in new_pages:
    url = f"{local_url}{page}"
    try:
        response = requests.get(url)
        status = "OK" if response.status_code == 200 else "FAIL"
        print(f"{status} {page}: {response.status_code}")
    except Exception as e:
        print(f"ERROR {page}: {e}")

print("=" * 60)