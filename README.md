# Facebook-brute-force-
Brute force Facebook "używajcie w calch edukacji" nie ponoszę odpowiedźi

Program jest cały czas w rozwoju i udoskonalania proszę o zrozumienie 

zalecam częsta reinstalacji cały czas udoskonalania programu 
_____________________________________________
**Jak użyć programu**

Aby użyć programu, musisz umieścić go w katalogu domowym i uruchomić go w następujący sposób:

```
python brute_force.py
```
(rootkalpython3 brute_force.py                                 
---------- Welcome To Facebook BruteForce ----------

Password file is not exist:  passwords.txt
(rootkali)-[~/Facebook-brute-force-]
# ls
LICENSE    app.py          password.txt
README.md  brute_force.py  update.py
(rootkali)-[~/Facebook-brute-force-]
# mv password.txt passwords.txt
(rootkali)-[~/Facebook-brute-force-]
# python3 brute_force.py

---------- Welcome To Facebook BruteForce ----------

Password file selected:  passwords.txt
Enter Email/Username to target:
_____________________________________________


```bash
pip install requests
```

Po uruchomieniu kodu Pythona, wprowadź odpowiednie dane, a program powinien używać serwera Tor jako proxy do wykonywania zapytań.
_____________________________________________

Program poprosi Cię o podanie nazwy użytkownika i listy haseł. Możesz podać nazwę użytkownika ręcznie lub skorzystać z polecenia `whois`.

**Podanie nazwy użytkownika ręcznie:**

```
python brute_force.py
Podaj nazwę użytkownika: ...@gmail.com
Podaj nazwę id konta : 
```

Skopiuj nazwę użytkownika z wyników polecenia whois i wprowadź ją do programu.

**Podanie listy haseł ręcznie:**

```
python brute_force.py

Podaj nazwę użytkownika: ...@gmail.com
Podaj nazwę id konta
Podaj listę haseł:



**Użycie listy haseł z pliku:**

```
python brute_force.py
Podaj nazwę użytkownika: ...@gmail.com
Podaj nazwę id konta
Podaj nazwę pliku z listą haseł: hasła.txt


Po podaniu nazwy użytkownika i listy haseł program rozpocznie próbowanie logowania się do konta Facebook. Jeśli logowanie się powiedzie, program wydrukuje znalezione hasło. W przeciwnym razie program kontynuuje próbowanie kolejnych haseł.

**Wymagania**

Program wymaga następujących rzeczy:

* Instalacji Python3
* Instalacji biblioteki requests

Aby zainstalować Python3, możesz użyć następującego polecenia:

```
sudo apt install python3
```

Aby zainstalować bibliotekę requests, możesz użyć następującego polecenia:

```
pip3 install requests
```

**Uwagi**

* Program może zostać zablokowany przez Facebooka, jeśli będzie próbował logować się zbyt wiele razy. Aby uniknąć blokady, ustaw odpowiedni czas oczekiwania między próbami logowania.
* Program nie jest gwarantowany, że znajdzie hasło do konta Facebook.
* Program służy wyłącznie do celów edukacyjnych i testu bezpieczeństwa. Nie należy go wykorzystywać do nielegalnych działań.
