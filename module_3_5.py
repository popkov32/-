# Задача "Рекурсивное умножение цифр".
def get_multiplied_digits(number): #Определение ф-ции с параметром
    str_number = str(number) #Создание переменной со строковым представлением параметра number
    first = int( str_number[0] ) #Создание переменной, в который будет вноситься первый символ из str_number в int
    if len(str_number) > 1: #Условие вызова ф-ции
        #print(first)
        #print(int(str_number[1:]))
        return first * get_multiplied_digits(int(str_number[1:])) #Логика работы ф-ции
    else:
        return int(str_number) #Окончание рекурсивного вызова
result = get_multiplied_digits(40203)
print(result)
