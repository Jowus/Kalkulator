# 1. Wyświetl liczby od 1 do 10.
for i in range(10):
    print(i)
# 2. Oblicz sumę liczb od 1 do 100.
suma = 0
for i in range(100):
    i += 1
    suma += i
print(suma)
# 3. Wyświetl wszystkie parzyste liczby od 1 do 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
        i += 0
# 4. Oblicz iloczyn liczb od 1 do 5.
print(1*2*3*4*5)
# 5. Wyświetl odwróconą wersję napisu "Hello World!".
j = "Hello World!"
k = ""
for char in j:
    k = char + k
print(k)
# 6. Wyświetl wszystkie litery z podanego słowa.
inp = input()
for el in inp: #element z inputa
    print(el)
# 7. Oblicz sumę elementów listy liczb.
lista = [2,3,4,5,2,5,7,86]
suma = 0
for el in lista:
    suma += el
print(suma)

# 8. Wyświetl wszystkie liczby od 20 do 30, które są podzielne przez 3.
for i in range(21, 31):
    if i % 3 == 0:
        print(i)
# 9. Znajdź największą liczbę w liście.
lista2 = [2,4,6,2,33]
najwieksza = lista2[0]
for number in lista2:
    if najwieksza > number:
        najwieksza = number
print(number)
# 10. Wyświetl wszystkie liczby od 1 do 100, które są podzielne jednocześnie przez 3 i 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
            print(i)
# 11. Oblicz średnią arytmetyczną z listy liczb.
lista = [2,3,5,64,2,5,1]
suma = 0
for number in lista:
    suma += number
print(suma/len(lista))
# 12. Wyświetl wszystkie litery z podanego zdania, pomijając spacje.
inp = input()
spacja = " "
for i in inp:
    if i == " ":
        continue
    spacja += i
print(spacja)
# 13. Oblicz silnię liczby podanej przez użytkownika.
inp = int(input())
s = 1
for i in range(1,inp+1):
    s *= i
print(s)
# 14. Wyświetl tabliczkę mnożenia (od 1 do 20).
for i in range(1, 21):
    for w in range(1, 21):
        res = i * w
        print(f" {res:3} ", end=" ")
    print("\n")
# 15. Sprawdź, czy podane słowo jest palindromem.
inp = input()
palindromem = True
for i in range(len(inp)//2):
    if inp[i] != inp[-i - 1]:
        palindromem = False
        break
print(palindromem)
# 16. Zamień wszystkie litery w podanym napisie na wielkie litery.
t = 0
for el in inp:
    t += el.upper()
print(t)
# 17. Wyświetl liczby od 1 do 10 w odwrotnej kolejności.
for i in range(10,0,-1):
    print(-i)