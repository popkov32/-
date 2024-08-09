# Задача "Распаковка"

# 1. Ф-ция с параметрами по умолчанию.

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params() #Вызов ф-ции со значениями по умолчанию
print_params(8,'String', False) #Вызов ф-ции с тремя аргументами
print_params(12, 'Terracot') #Вызов ф-ции с параметром (c) по умолчанию
print_params(b = 'garbage') #Вызов ф-ции с параметром (b) и двумя по умолчанию
print_params(b = 25) #Проверка работы ф-ции при b = 25
print_params(c = [1, 2, 3]) #Проверка работы ф-ции при c = [1, 2, 3]

# 2. Распаковка параметров.

values_list = [3, 'Abracadabra', False] #Список с тремя элементами разных типов
value_dict = {'a': 386, 'b': 'IBM', 'c': True} #Словарь с тремя ключами и значениями разных типов
print_params(*values_list) #Распаковка списка
print_params(**value_dict) #Распаковка словаря

# 3. Распаковка + отдельные параметры.

value_list_2 = [54.32, 'Строка'] #Список с двумя элементами разных типов
print_params(*value_list_2, 42) #Проверка распаковки списка

