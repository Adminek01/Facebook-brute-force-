import requests
import time
import random
import threading
from requests.auth import HTTPProxyAuth

# Tor proxy details
tor_proxy_ip = "127.0.0.1"
tor_proxy_port = "9050"
tor_proxy_auth = HTTPProxyAuth('your_tor_proxy_username', 'your_tor_proxy_password')  # Modify with your Tor proxy credentials if needed

# Function to perform brute force attack using Tor as a proxy
def brute_force(username, fb_id, passwords):
    for password in passwords:
        # Use the requests library with SOCKS proxy
        proxies = {'http': f'socks5h://{tor_proxy_ip}:{tor_proxy_port}',
                   'https': f'socks5h://{tor_proxy_ip}:{tor_proxy_port}'}

        try:
            # Example: Make a request to Shodan using Tor as a proxy
            result = requests.get(f'https://api.shodan.io/shodan/host/{tor_proxy_ip}?key=YOUR_SHODAN_API_KEY',
                                  proxies=proxies, timeout=10, auth=tor_proxy_auth)
            # Process result as needed
            print(result.text)
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")

        # Rest of your brute-force logic
        # ...

# Function to read passwords from a file
def read_passwords(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Function to execute the main brute-force attack
def main():
    username = input("Enter email address (as username): ")
    fb_id = input("Enter Facebook ID: ")
    password_file = input("Enter the password file name: ")

    # Read passwords from file
    passwords = read_passwords(password_file)

    # Perform brute-force attack
    brute_force(username, fb_id, passwords)

if __name__ == '__main__':
    main()
