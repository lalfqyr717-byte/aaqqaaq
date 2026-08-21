#!/usr/bin/env python3
"""Test script to verify super-admin page is accessible"""

import requests
import sys

BASE_URL = "http://127.0.0.1:8765"

def test_super_admin_page():
    """Test that super-admin page returns 200"""
    try:
        response = requests.get(f"{BASE_URL}/pages/super-admin.html", timeout=5)
        if response.status_code == 200:
            print("SUCCESS: super-admin page is accessible (status 200)")
            print(f"Content length: {len(response.content)} bytes")
            return True
        else:
            print(f"FAILED: super-admin page returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("FAILED: Could not connect to server. Make sure the server is running.")
        return False
    except Exception as e:
        print(f"FAILED: Error occurred: {e}")
        return False

if __name__ == "__main__":
    success = test_super_admin_page()
    sys.exit(0 if success else 1)