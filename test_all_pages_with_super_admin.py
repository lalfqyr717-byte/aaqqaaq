#!/usr/bin/env python3
"""Test script to verify all 18 pages are accessible (including super-admin)"""

import requests
import sys

BASE_URL = "http://127.0.0.1:8765"

pages = [
    "/",
    "/pages/sales.html",
    "/pages/products.html",
    "/pages/product-alerts.html",
    "/pages/warehouse.html",
    "/pages/purchases.html",
    "/pages/purchase-invoices.html",
    "/pages/clients.html",
    "/pages/suppliers.html",
    "/pages/employees.html",
    "/pages/super-admin.html",
    "/pages/finance.html",
    "/pages/installments.html",
    "/pages/sales-invoices.html",
    "/pages/returns.html",
    "/pages/reports.html",
    "/pages/settings.html",
    "/pages/labels.html"
]

def test_all_pages():
    """Test that all pages return 200"""
    all_passed = True
    for page in pages:
        try:
            response = requests.get(f"{BASE_URL}{page}", timeout=5)
            if response.status_code == 200:
                print(f"[OK] {page} - 200")
            else:
                print(f"[FAIL] {page} - {response.status_code}")
                all_passed = False
        except requests.exceptions.ConnectionError:
            print(f"[FAIL] {page} - Connection error")
            all_passed = False
        except Exception as e:
            print(f"[FAIL] {page} - {e}")
            all_passed = False
    
    if all_passed:
        print(f"\nSUCCESS: All {len(pages)} pages are accessible")
    else:
        print(f"\nFAILED: Some pages are not accessible")
    
    return all_passed

if __name__ == "__main__":
    success = test_all_pages()
    sys.exit(0 if success else 1)