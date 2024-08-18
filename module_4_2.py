# Домашнее задание по уроку "Пространство имен"

def test_function():
    def inner_function():
        d = 'Я в области видимости функции test_function'
        print(d)
    inner_function()

test_function()

#inner_function() #При вызове из этой строки не работает потому, что находится вне области видимости ф-ции test_function

