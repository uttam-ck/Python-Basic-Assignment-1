
# Write a Python script that checks the uptime of provided URLs and notifies the user if any of the URLs return 4xx or 5xx HTTP status codes (indicating client or server errors). For demonstration purposes, you can use the following URLs as inputs:
# 4xx (Client Error):
# http://www.example.com/nonexistentpage or
# http://httpstat.us/404
# 5xx (Server Error):
# http://httpstat.us/500
# 200 (Successful Response):
# https://www.google.com/
# Requirements:
# URL Check: The script should check the provided URLs and get their HTTP status codes.
# Handle Multiple URLs: The script should be able to handle multiple URLs at once, checking each one.
# Error Detection: If the status code of any URL is either 4xx or 5xx, the program should:
# Notify the user via a print message.
# Alternatively, you can implement more advanced logging methods, (log in any log file).
# Loop and Monitor: You should set up a simple loop that continuously monitors the URLs for a certain interval (e.g., every 10 seconds) to simulate a basic uptime monitoring system.
# Status Message: For each URL, the script should output the URL and its current HTTP status code (e.g., 200 OK, 404 Not Found).

import requests
import time

def check_url_status(url):
    """Checks the HTTP status of a given URL."""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.RequestException:
        return None

def log_error(url, status_code):
    """Logs URL errors to a file."""
    with open("url_errors.log", "a") as log_file:
        log_file.write(f"Error: {url} returned {status_code}\n")

def monitor_urls(urls, interval=10):
    """Continuously monitors the list of URLs at the given interval."""
    while True:
        print("Checking URLs...")
        for url in urls:
            status_code = check_url_status(url)
            if status_code:
                print(f"{url} -> {status_code}")
                if 400 <= status_code < 600:
                    print(f"ALERT: {url} returned an error ({status_code})!")
                    log_error(url, status_code)
            else:
                print(f"ALERT: {url} is unreachable!")
                log_error(url, "Unreachable")
        print("Waiting for next check...")
        time.sleep(interval)

if __name__ == "__main__":
    urls_to_check = [
        "http://www.example.com/nonexistentpage",
        "http://httpstat.us/404",
        "http://httpstat.us/500",
        "https://www.google.com/"
    ]
    monitor_urls(urls_to_check)
