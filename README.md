Używam PyCharma w wersji Professional (do uzyskania licencji wystarczy zarejestrować się na uczelnianym mailu, professional posiada pełne wsparcie dla Django) i Pythona w wersji 3.4.6 lub nowszej

1) odpalamy PyCharma -> Checkout Project from VCS podajemy dane i pobieramy repo projektu
2) File -> Settings (Ctrl + Alt + S) -> Project -> Project Interpreter, upewniamy się że korzystamy z dobrej wersji Pythona, dodaje libke za pomocą zielonego plusa, wyszukujemy Django i pobieramy, Django powinno pobrać się w wersji 1.11.x
zostałem przy SQLite bo jest natywnie wspierany przez Django, nie trzeba instalować ani konfigurować żadnych libek
3) wszystkie komendy odpalamy najlepiej przez Command Line za pomocą "python manage.py <command>" w głównym projektu
4) w PyCharmie, z prawej strony mamy zakładke 'Database' jeśli nie widnieje tam nasza baza 'db.sqlite3' dodajemy ją przez Add -> Import from Sources -> Test Connection, jeśli nie działa to na dole mamy opcje "Download drivers", po tym powinno wszystko działać i załadować podgląd bazy


SuperUser:
Login:	test
Pass:	testpass

Żeby uruchomić server możemy albo odpalić Shift + F10 w IDE, albo w katalogu projektu: python manage.py runserver
Stroną startową jest: http://localhost:8000/app/

Polecam: https://docs.djangoproject.com/pl/1.11/intro/tutorial01/

Co do gita, to zalecałbym najlepiej rozwijać swoje taski na tworzonych oddzielnie gałęziach, potem mergować do developa, a jak tam będzie działać po złączeniu ze zmianami innych dopiero uaktualniać mastera. 