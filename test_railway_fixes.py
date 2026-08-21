#!/usr/bin/env python3
"""Test script to verify Railway deployment fixes"""

import requests
import sys

BASE_URL = "http://127.0.0.1:8765"

def test_endpoints():
    """Test all fixed endpoints"""
    endpoints = [
        ('/api/state/', 'api_state'),
        ('/api/analytics/dashboard/', 'api_analytics_dashboard'),
        ('/favicon.ico', 'favicon_redirect'),
    ]
    
    all_passed = True
    for endpoint, name in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
            status = response.status_code
            if status == 200:
                print(f"[OK] {endpoint} - {name} (200)")
            elif status == 404:
                print(f"[FAIL] {endpoint} - {name} (404 - Not Found)")
                all_passed = False
            else:
                print(f"[WARN] {endpoint} - {name} ({status})")
        except requests.exceptions.ConnectionError:
            print(f"[FAIL] {endpoint} - {name} (Connection error)")
            all_passed = False
        except Exception as e:
            print(f"[FAIL] {endpoint} - {name} ({e})")
            all_passed = False
    
    if all_passed:
        print("\nSUCCESS: All Railway endpoints are accessible")
    else:
        print("\nFAILED: Some endpoints are not accessible")
    
    return all_passed

if __name__ == "__main__":
    success = test_endpoints()
    sys.exit(0 if success else 1)