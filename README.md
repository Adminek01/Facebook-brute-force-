# Facebook-brute-force-
Brute force Facebook "używajcie w calch edukacji" nie ponoszę odpowiedźi

Program jest cały czas w rozwoju i udoskonalania proszę o zrozumienie 
_____________________________________________
**Jak użyć programu**

Aby użyć programu, musisz umieścić go w katalogu domowym i uruchomić go w następujący sposób:

```
python brute_force.py
```

Program poprosi Cię o podanie nazwy użytkownika i listy haseł. Możesz podać nazwę użytkownika ręcznie lub skorzystać z polecenia `whois`.

**Podanie nazwy użytkownika ręcznie:**

```
python brute_force.py
Podaj nazwę użytkownika: 100041219380500@gmail.com
```

**Użycie polecenia whois:**

```
whois 100041219380500@gmail.com
```

Skopiuj nazwę użytkownika z wyników polecenia whois i wprowadź ją do programu.

**Podanie listy haseł ręcznie:**

```
python brute_force.py
Podaj nazwę użytkownika: ...@gmail.com
Podaj listę haseł:
hasło1
hasło2
hasło3
...
```

**Użycie listy haseł z pliku:**

```
python brute_force.py
Podaj nazwę użytkownika: 100041219380500@gmail.com
Podaj nazwę pliku z listą haseł: hasła.txt
```

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
