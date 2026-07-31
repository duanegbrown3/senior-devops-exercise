#!/usr/bin/env python3

import requests

SERVICES = {
    "Auth Service": "http://localhost:8080/health",
    "Main App": "http://localhost:3000/health"
}


def check(name, url):

    try:

        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            print(f"✓ {name} OK")
        else:
            print(f"✗ {name} returned {r.status_code}")

    except Exception as e:

        print(f"✗ {name}: {e}")


for name, url in SERVICES.items():

    check(name, url)