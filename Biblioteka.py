# Zad1. Napisz analogiczny słownik (książka) który pozwoli ci edytować dane ;)
# Funkcje umieść w 2 pliku i zaimportuj funkcje do main.py. Jak dobrze opanujesz co się dzieje w twoim pierwszym skrypcie dopiero potem przejdź do Zad2 . 

# Zad 2. Hej a co powiesz na listę słowników! Napisz program biblioteka który pozwoli ci w pełni edytować listę słowników jak i same książki ;
#im więcej posiedzidzisz i popłaczesz nad zad 2 tym lepiej zrozumiesz materiał ;). Podziel program na pliki:
import time


def generate_unix_id():
    unix_id = int(time.time())
    return unix_id


unique_unix_id = generate_unix_id()


ksiazka1 = {
    'nazwa': 'Pan Tadeusz',
    'ilość stron': '375',
    'autor': 'Adam Mickiewicz',
    'id': generate_unix_id()
}

ksiazka2 = {
    'nazwa': 'Balladyna',
    'ilość stron': '170',
    'autor': 'Juliusz Słowacki',
    'id': generate_unix_id()
}
ksiazka3 = {
    'nazwa': 'Upiorny pociąg. Wiggott przedstawia fantastyczny woskowy świat',
    'ilość stron': '384',
    'autor': 'Terry Deary',
    'id': generate_unix_id()
}
biblioteka = [ksiazka1,ksiazka2,ksiazka3]

def informacje(lista:list)->None:
    for slownik in lista:
        for k,v in slownik.items():
            print(f"{k}:   {v}")
        print("==="*20)
def dodaj_ksiazke(lista):
    x = input("podaj tytuł")
    y = input("podaj liczbe stron")
    z = input("podaj autora")
    ksiazka = {
        'nazwa': x,
        'ilość stron': y,
        'autor': z,
        'id': generate_unix_id()
    }
    lista.append(ksiazka)
def usun(lista):
    id = input("Co chcesz usunac ")
    del lista[id]
def edytowanie(slownik, lista):
    print("co chcesz edytować?")
    informacje(lista)
    edytowany_element = input()
    slownik[edytowany_element] = input("Wprowadź nowe dane")

while True:
    print("i - informacje")
    print("e - edytuj dane")
    print("d - dodaj ksiazke")
    print("u - usun ksiazke")
    dzialanie = input()
    if "i" == dzialanie:
        informacje(biblioteka)
    elif "e" == dzialanie:
        x = input("Wybierz ksiazke")
        edytowanie(ksiazka1, biblioteka)
    elif "u" == dzialanie:
        usun(biblioteka)
    elif "d" == dzialanie:
        dodaj_ksiazke(biblioteka)