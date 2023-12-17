import time


def generate_unix_id():
    unix_id = int(time.time())
    return unix_id


unique_unix_id = generate_unix_id()


k = {
    "id" : generate_unix_id()
}
ksiazka1 = {
    'nazwa': 'Pan Tadeusz',
    'ilość stron': '375',
    'autor': 'Adam Mickiewicz',
    'id': generate_unix_id()
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
    elif "e" == dzialanie:
        edytowanie(ksiazka1)



        