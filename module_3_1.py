calls = 0 # создание переменной количества вызова ОСТАЛЬНЫХ ф-ций
def count_calls (): # создание ф-ции подстчета calls
    global calls # определение calls как глобальной переменной
    calls+=1 # логика count_calls
def string_info (string): # создание ф_ции string_info с параметром string
    count_calls() # вызов ф-ции count_calls
    return (len(string), string.upper(), string.lower()) #логика работы string_info
def is_contains (string, list_to_search): #создание ф-ции is_contains с двумя параметрами string и list_to_search
    count_calls() # вызов ф-ции count_calls
    return string.upper() in [s.upper() for s in list_to_search] #логика работы is_contains

print(string_info('Capybara')) # вывод результата работы string_info
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)