import requests

railway_url = "https://moq.up.railway.app"
installments_url = f"{railway_url}/pages/installments.html"

print("Testing Railway installments page...")
try:
    response = requests.get(installments_url)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("SUCCESS - Installments page accessible")
        print(f"Contains section: {'<section' in response.text}")
        print(f"Contains sidebar: {'<aside' in response.text}")
    else:
        print(f"FAILED with status {response.status_code}")
except Exception as e:
    print(f"Error: {e}")