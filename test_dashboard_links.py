import requests

local_url = "http://127.0.0.1:8000"

print("Testing home page and checking links...")
try:
    response = requests.get(local_url)
    print(f"Home page status: {response.status_code}")
    
    if response.status_code == 200:
        # Check if links are absolute
        has_absolute_links = 'href="/pages/' in response.text
        has_relative_links = 'href="pages/' in response.text
        
        print(f"Has absolute links (/pages/): {has_absolute_links}")
        print(f"Has relative links (pages/): {has_relative_links}")
        
        if has_absolute_links and not has_relative_links:
            print("SUCCESS - All links updated to absolute paths")
        else:
            print("ISSUE - Some links still using relative paths")
            
except Exception as e:
    print(f"Error: {e}")

print("\nTesting specific page links...")
test_links = [
    f"{local_url}/pages/sales.html",
    f"{local_url}/pages/products.html",
    f"{local_url}/pages/settings.html",
]

for url in test_links:
    print(f"\nTesting: {url}")
    try:
        response = requests.get(url)
        print(f"  Status: {response.status_code}")
        if response.status_code == 200:
            print(f"  SUCCESS - Page accessible")
    except Exception as e:
        print(f"  Error: {e}")