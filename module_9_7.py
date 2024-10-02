# Задание: Декораторы в Python

"""Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и
обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае."""


def is_prime(func):
    def wrapper(a, b, c):

        n = func( a, b, c )
        count = 0

        for i in range( 2, n + 1 ):
            if n % i == 0:
                count += 1
                print( 'Составное' )
            else:
                print( 'Простое' )
            return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three( 2, 3, 8 )
print( result )
