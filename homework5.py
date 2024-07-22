immutable_var = 1, 3, 8, 'a', 'c', True
print('Immutable tuple: ', immutable_var)
print(type(immutable_var))
# immutable_var[2] = 12 # строка сдержит ошибку "кортеж не поддерживает обращение по элементам"
mutable_list = [1, 3, 8, 'a', 'c', True]
print('Mutable list: ',mutable_list)
print(type(mutable_list))
mutable_list[2] = 12
print('Mutable list: ',mutable_list)

