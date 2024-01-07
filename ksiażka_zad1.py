import uuid

k = {
    "id" : uuid.uuid4()
}
ksiazka1 = {
    'nazwa': 'Pan Tadeusz',
    'ilość stron': '375',
    'autor': 'Adam Mickiewicz',
    'id': uuid.uuid4()
}
ksiazka2 = {
    'nazwa': 'Pan Tsz',
    'ilość stron': '75',
    'autor': 'Adam Mwicz',
    'id': uuid.uuid4()
}
def informacje(slownik):
    for k,v in slownik.items():
        print(f"{k}:   {v}")
def edytowanie(slownik):
    print("co chcesz edytować?")
    informacje(slownik)
    edytowany_element = input()
    slownik[edytowany_element] = input("Wprowadź nowe dane")

while True:
    print("i - informacje")
    print("e - edytuj dane")
    dzialanie = input()
    if "i" == dzialanie:
        informacje(ksiazka1)
        informacje(ksiazka2)
    elif "e" == dzialanie:
        edytowanie(ksiazka1)



        