my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a <= len(my_list): # проверка нахождения внутри списка
    if my_list[a] > 0 and my_list != 0: #проверка положительного числа
        print(my_list[a])
    if my_list[a] < 0: # проверка отрицательного числа
        break
    a = a + 1 # увеличение текущего индекса



