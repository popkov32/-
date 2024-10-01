#Задача:
"""Напишите функцию-генератор all_variants(text), которая принимает строку
 text и возвращает объект-генератор, при каждой итерации которого будет
 возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации."""

def all_variants(text):
    n = len(text)
    for i in range(n):
        for j in range(n - i):
            yield text[j:j + i + 1]

a = all_variants("казбек")
for i in a:
    print(i)