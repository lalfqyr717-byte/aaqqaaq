import requests
import re

railway_url = "https://moq.up.railway.app"

print("Testing dashboard buttons on main page...")
print("=" * 60)

response = requests.get(railway_url)
if response.status_code == 200:
    # Find all dashboard shortcut links - try different pattern
    shortcuts = re.findall(r'<a class="tox-dashboard-shortcut[^"]*"[^>]*href="([^"]*)"[^>]*>', response.text)

    print(f"Found {len(shortcuts)} dashboard shortcuts:")
    print()

    for href in shortcuts:
        print(f"  Link: {href}")

        # Test if the link works
        full_url = railway_url + href if href.startswith('/') else railway_url + '/' + href
        try:
            test_response = requests.get(full_url)
            if test_response.status_code == 200:
                print(f"  Status: OK (200)")
            else:
                print(f"  Status: FAILED ({test_response.status_code})")
        except Exception as e:
            print(f"  Status: ERROR - {e}")
        print()

    print("=" * 60)
    print("Dashboard buttons test completed!")
else:
    print(f"Failed to load main page: {response.status_code}")