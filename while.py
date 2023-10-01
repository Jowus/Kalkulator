
import math


# print("9-=-"*10)
# numbers = [1,1,1,2,2,5]


# i = -1
# while i >= -len(numbers):
#     print(numbers[i])
#     i-= 1


# # 2.


# print("9-=-"*10)
# numbers = [1,1,1,2,2,5]
# inp = int(input())
# if inp in numbers:
#     print("Tak")
# else:
#     print("Nie")


# # 3.


# print("9-=-"*10)
# numbers = [1,1,1,2,2,5]
# inp = int(input())
# i = 0
# while i < len(numbers):
#     if inp == numbers[i]:
#         print(i)
#         break
#     i += 1


# # 4.


# print("9-=-"*10)
# numbers = [1,1,1,2,2,5,11]
# ile = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > 10:
#         ile += 1


#     i += 1
# print(ile)


# # 5.


# print("9-=-"*10)
# numbers = [11,2,10,3,1,2,4]
# numbers.sort(reverse=True)
# print(numbers)


# # 6.


# print("9-=-"*10)
# numbers = [11,2,10,3,1,2,4,11]


# max1 = float('-inf')
# max2 = float('-inf')


# i = 0
# while i < len(numbers):
#     if numbers[i] > max1:
#         max2 = max1
#         max1 = numbers[i]
#     elif numbers[i] > max2 and numbers[i] != max1:
#         max2 = numbers[i]
#     i += 1


# print(f"max1 {max1}")
# print(f"max2 {max2}")


   





# # 7.


# print("9-=-"*10)
# numbers = [1,1,2,2,3,3,4,4,10,10,10,10]
# doubled_numbers = []


# i = 0
# while i < len(numbers):
#     doubled_numbers.append(numbers[i]*2)
#     i += 1
# print(doubled_numbers)    


# # 8.


# print("9-=-"*10)
# numbers = [1,1,2,2,3,3,4,4,10,10,10,10]
# i = 0
# inp = float(input("-"))
# ile = 0
# while i < len(numbers):
#     if numbers[i] == inp:
#         ile += 1
#     i += 1
# print(ile)


# # 9. 


# print("9-=-"*10)
# numbers = [1,1,2,2,3,3,4,4,10,10,10,10]


# i = 0
# while i < len(numbers):
#     print(f"{i} {numbers[i]}")
#     i += 1

# # Napisz program który na każde zadane pytanie odpowiada “perhaps”
# while True:
#     pytanie = str(input("zadaj pytanie "))
#     print("perhaps")

# Napiszmy program który wyświetli nam wszystkie liczby podzielne przez 9. Do wartości podanej przez użytkownika.

# do_ktorej_liczby = int(input("do której liczby wyświetlicz liczby podzielne przez 9 "))
# i = 0
# n9 = []
# while i <= do_ktorej_liczby:
#     if i % 9 == 0:
#         n9.append(i)
#     i += 1
# print(n9)
# # Napisz program który z wypisze wszystkie liczby które NIE są podzielne przez 3.  Do wartości podanej przez użytkownika.

# do_ktorej_liczby = int(input("do której liczby wyświetlicz liczby niepodzielne przez 3 "))
# i = 0
# n3 = []
# while i <= do_ktorej_liczby:
#     if i % 3 != 0:
#         n3.append(i)
#     i += 1
# print(n3)
# # Napisz program który wyświetli n potęg liczby 2.
# n = int(input())
# i = 0
# n20 = []
# while i <= n:
#     n20.append(math.pow(2,i))
#     i += 1
# print(n20)
     


# # Zsumuj wszystkie liczby które są są podzielne przez 5 do wartości podanej przez użytkownika. 
# i = 0
# do_ktorej_liczby = int(input("do której liczby podzielne przez 5 "))
# n5 = []
# while i <= do_ktorej_liczby:
#     if i % 5 == 0:
#         n5.append(i)
# suma = 0
# print(n5)

# for i in n5:
#     suma += i
# print(suma)
# # Wyświetl n razy Kocham programować!

# n = int(input())
# i = 0
# while i <= n:
#     print("kocham programowac")
#     i += 1
# # Sprawdzić czy zapytana x liczba liczba jest liczbą pierwszą?
# x = int(input("podaj liczbe"))
# i = 0
# while i <= x:
#     if x % i == 0:
#         print("false")
# print("true")
# # Stwórz listę zawierającą x liczb wprowadzonych przez użytkownika od (1 do 200)
# x = int(input())
# n200 = []
# i = 0
# while i <= x:
#     n200.append(i)
# print(n200)

# # Napisz program co wprowadzi x ocen (1 do 6) a następnie obliczy nam średnią  arytmetyczną. Jeśli ktoś wprowadzi liczby inne niż 1 i 6 niech program wyświetli m….
# # podałeś złe liczby Nobie!
# i = 0
# suma = 0

# g = int(input())
# while i <= g:
#     h = int(input())

#     if h <= 6 and h >= 1:
#         suma += h
#     else:
#         print("podałeś złe liczby Nobie!")
# print(suma / g)

    

# Napisz program do którego możemy wprowadzić dowolne zdanie. Niech nasz program wyświetli:
# Ile mamy samogłosek:
samogłoski = ["a" , "ą", "e", "ę", "i", "o", "u", "y"]
zdanie = str(input())
i = 0
j = 0
suma = 0
for i in zdanie:
    for j in samogłoski:
        if zdanie[i] == samogłoski[j]:
            suma += 1
print(suma)
