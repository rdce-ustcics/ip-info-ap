#!/usr/bin/env python3
"""
ip_info.py - Fetch public IP + geolocation using ipapi.co
Requires: requests
"""
import requests
import sys
import json

URL = "https://ipapi.co/json/"

def fetch(url=URL, timeout=10):
    headers = {"User-Agent": "ip-info-script/1.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e, file=sys.stderr)
        return None

def main():
    data = fetch()
    if not data:
        sys.exit(1)
    print("Public IP:", data.get("ip", "N/A"))
    print("City:", data.get("city", "N/A"))
    print("Region:", data.get("region", "N/A"))
    print("Country:", f"{data.get('country_name','N/A')} ({data.get('country_code','N/A')})")
    print("ISP/Org:", data.get("org", "N/A"))
    print("\nFull JSON response:")
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
