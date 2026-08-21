import requests
import re

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

print("Testing navigation links in all pages...")
print("=" * 60)

all_pages_ok = True

for page in pages_to_test:
    url = f"{railway_url}{page}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Find all nav-link using regex
            nav_links = re.findall(r'<a class="nav-link[^"]*"[^>]*>([^<]+)</a>', response.text)

            print(f"\n{page}:")
            print(f"  Status: {response.status_code}")
            print(f"  Navigation links found: {len(nav_links)}")

            # Check if all expected links are present
            expected_links = ['المركز الرئيسي', 'المبيعات', 'المنتجات', 'المستودعات', 'المشتريات', 'العملاء', 'الموردين', 'الموظفين', 'الأقساط', 'التقارير', 'الإعدادات']
            missing_links = [link for link in expected_links if link not in nav_links]
            if missing_links:
                print(f"  WARNING: Missing {len(missing_links)} links")
                all_pages_ok = False
            else:
                print(f"  OK: All navigation links present")
        else:
            print(f"\n{page}: FAILED with status {response.status_code}")
            all_pages_ok = False
    except Exception as e:
        print(f"\n{page}: ERROR - {e}")
        all_pages_ok = False

print("\n" + "=" * 60)
if all_pages_ok:
    print("SUCCESS: All pages have complete navigation links!")
else:
    print("WARNING: Some pages have missing navigation links")
print("Navigation test completed!")