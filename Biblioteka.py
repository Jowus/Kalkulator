# Zad1. Napisz analogiczny słownik (książka) który pozwoli ci edytować dane ;)
# Funkcje umieść w 2 pliku i zaimportuj funkcje do main.py. Jak dobrze opanujesz co się dzieje w twoim pierwszym skrypcie dopiero potem przejdź do Zad2 . 

# Zad 2. Hej a co powiesz na listę słowników! Napisz program biblioteka który pozwoli ci w pełni edytować listę słowników jak i same książki ;
#im więcej posiedzidzisz i popłaczesz nad zad 2 tym lepiej zrozumiesz materiał ;). Podziel program na pliki:
import uuid


ksiazka1 = {
    'nazwa': 'Pan Tadeusz',
    'ilość stron': '375',
    'autor': 'Adam Mickiewicz',
    'id': uuid.uuid4()
}

ksiazka2 = {
    'nazwa': 'Balladyna',
    'ilość stron': '170',
    'autor': 'Juliusz Słowacki',
    'id': uuid.uuid4()
}
ksiazka3 = {
    'nazwa': 'Upiorny pociąg. Wiggott przedstawia fantastyczny woskowy świat',
    'ilość stron': '384',
    'autor': 'Terry Deary',
    'id': uuid.uuid4()
}
biblioteka = [ksiazka1,ksiazka2,ksiazka3]
# informacje o liscie / dziala
def informacje(lista:list)->None:
    for slownik in lista:
        for k,v in slownik.items():
            print(f"{k}:   {v}")
        print("==="*20)
#dodawanie ksiazek do listy / dziala
def dodaj_ksiazke(lista):
    x = input("podaj tytuł")
    y = input("podaj liczbe stron")
    z = input("podaj autora")
    ksiazka = {
        'nazwa': x,
        'ilość stron': y,
        'autor': z,
        'id': uuid.uuid4()
    }
    lista.append(ksiazka)
#usuwanie slownikow z listy / dziala juz
def istnieje(lst: list, id: str):
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id:
            return True
    return False

def index(lista: list, id: str):
    for i in range(len(lista)):
        if str(lista[i]["id"]) == id:
            return i
    return -1  

def usun(lista: list) -> None:
    inp = input("Podaj id książki: ")
    if istnieje(lista, inp):
        index = index(lista, inp)
        if index != -1:
            lista.pop(index)
            print("Ksiażka usunięta")
        else:
            print("Nie ma takiej książki")
    else:
        print("Nie ma takiej książki")
#edytowanie danych w slownikach 
def edytowanie(lista:list):
    x = input("Którą książkę chcesz edytować?(podaj id)")
    if istnieje(lista, x):
        idd = index(lista, x)
        z = input("Co chcesz edytować?")
        lista[idd][z] = input("wprwadź dane ")
        print(lista[idd][z])

while True:
    print("i - informacje")
    print("e - edytuj dane")
    print("d - dodaj ksiazke")
    print("u - usun ksiazke")
    dzialanie = input()
    if "i" == dzialanie:
        informacje(biblioteka)
    elif "e" == dzialanie:
        edytowanie(biblioteka)
    elif "u" == dzialanie:
        usun(biblioteka)
    elif "d" == dzialanie:
        dodaj_ksiazke(biblioteka)

