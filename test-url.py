#!/usr/bin/env python3

import time
import requests
from datetime import datetime

url = "http://www.apple.com"
logfile = "curl.log"

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Equivalent to: curl -sSf
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        print(f"Connection to {url} successful at {timestamp}")

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response else "unknown"

        if status_code == 404:
            print(
                f"Connection to {url} failed with 404 error at {timestamp}",
                file=sys.stderr
            )
            with open(logfile, "a") as f:
                f.write(f"HTTP Status Code: {status_code}\n")
                f.write(f"Response headers:\n{e.response.headers}\n")
                f.write(f"Response body:\n{e.response.text}\n\n")
        else:
            print(
                f"Connection to {url} failed at {timestamp}",
                file=sys.stderr
            )
            with open(logfile, "a") as f:
                f.write(f"HTTP Status Code: {status_code}\n")
                if e.response:
                    f.write(f"Response headers:\n{e.response.headers}\n")
                    f.write(f"Response body:\n{e.response.text}\n\n")

    except requests.exceptions.RequestException as e:
        # Network errors, DNS, timeouts, etc.
        print(
            f"Connection to {url} failed at {timestamp}",
            file=sys.stderr
        )
        with open(logfile, "a") as f:
            f.write(f"Request error: {e}\n\n")

    time.sleep(1)

