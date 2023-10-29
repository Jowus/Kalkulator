
# 10. Utwórz listę słów i napisz funkcję która wypisze tylko te słowa, które mają więcej niż 5 znaków.
lista = ["ala", "bartek", "krzysztof"]
def k(lista, ile):
    for el in lista:
        if len(el) > ile:
            print(f" {el}", end = " ")
    print("\n")
k(lista,5)
# 11. Napisz funkcję, która zamienia wszystkie litery w danym łańcuchu znaków na duże litery.
def z(string):
    print(string.upper())
z("rower jedzie chodniiem")
# 12. Utwórz listę liczb i napisz funkcję która znajduje drugą najmniejszą wartość w tej liście.
def j(lista):
    list.sort(lista)
    return(lista[lista2])
lista2 = [1,2,432,1,3,432,3,41,63,2]
# print(j(lista2))
# 13. Napisz funkcję, która liczy wystąpienia danego znaku w danym łańcuchu znaków.
def q(słowo, znak):
    ile = 0
    for el in słowo:
        if el == znak:
            ile += 1
        return ile
print(q("Komin", "k"))
# 14. Utwórz listę liczb i napisz funkcję która obliczy sumę wszystkich liczb podzielnych przez 3.
def g(lista):
    suma = 0
    for el in lista:
        if el % 3 == 0:
            suma += el
    return suma
print(g(lista2))
# 15. Napisz funkcję, która usuwa duplikaty z danej listy.
def f(lista):
    r = []
    for el in lista:
        if el not in r:
            r.append(el)
    return r
print(f([1,234,456,23,456]))
# 16. Utwórz listę liczb i napisz funkcję która  znajdzie najczęściej występujący element w tej liście.
def b(lista):
    ile = 0
    naj = lista[0]
    for el in lista:
        if ile < lista.count(el):
            ile = lista.count(el)
            naj = ile
    return naj
print(b(lista2))
# 17. Napisz funkcję, która odwraca kolejność elementów w danej liście.
def t(inp):
    return inp[::-1]
print(t("kotek"))

# 18. Utwórz dwie listy i napisz funkcję która połączy je w jedną, tak aby elementy były posortowane rosnąco.
def h(lista1,lista):
    lista.extend(lista1)
    return sorted(lista)
print(h(lista2, [1,2,4,2,5,21,234]))
# 19. Utwórz listę liczb i napisz funkcję która znajdzie drugą największą wartość w tej liście.
def p(lista):
    lista = sorted(lista)
    return lista[-2]
print(p(lista2))