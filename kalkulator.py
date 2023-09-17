import math

a = float(input("wprowadź liczbę a: "))
b = float(input("wprowadź liczbę b: "))

co = input().lower()

if co == "a":
    print(a+b)
elif co == "b":
    print(a-b)
elif co == "c":
    print(a/b)
elif co == "d":
    print(a*b)
elif co == "e":
    print(a**b)
elif co == "f":
    print(a%b)
else:
    print("nie ma takiej opcji")


def kwadrat():
    a = int(input("długość: "))
    pk = pow(a, 2)
    print("Pole = " + str(pk))

def prostokąt():
    a = int(input("długość boku a: "))
    b = int(input("długość boku b: "))
    pp = a*b
    print("Pole = " + pp)

def trójkąt():
    a = int(input("długość podstawy: "))
    h = int(input("wysokość: "))
    pt = (a*h)/2
    print("Pole = " + pt)

def równoległobok():
    a = int(input("długość podstawy: "))
    h = int(input("wysokośc: "))
    prl = a*h
    print("Pole = " + prl)

def romb():
    e = int(input("przekątna1: "))
    f = int(input("przekątna2: "))
    prp = (e*f)/2
    print("Pole = " + prp)

def rombv2():
    a = int(input("długość: "))
    h = int(input("wysokość: "))
    prb = a*h
    print("Pole = " + prb)

def koło():
    r = int(input("promień: "))
    pko = math.pi*r**2
    print("Pole = " + pko)

def trapez():
    a = int(input("długość podstawy a: "))
    b = int(input("długość podstawy b: "))
    h = int(input("wysokość: "))
    ptra = (a+b)*h/2
    print("Pole = " + ptra)

def trójkąt_równoboczny():
    a = int(input("długość boków: "))
    ptr = a**2(math.sqrt(3))/4
    print("Pole = " + ptr)

w = input("wybierz pole ")

if w == "kwadrat":
    kwadrat()
elif w == "prostokąt":
    prostokąt()
elif w == "trójkąt":
    trójkąt()
elif w == "trójkąt_równoboczny":
    trójkąt_równoboczny()
elif w == "równoległobok":
    równoległobok()
elif w == "romb":
    romb()
elif w == "rombv2":
    rombv2()
elif w == "koło":
    koło()
elif "trapez":
    trapez()
else:
    trójkąt_równoboczny()