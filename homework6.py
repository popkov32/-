my_dict = {'Igor': 1970, 'Olga': 1970, 'Petr': 1946}
print( 'First dict:', my_dict )
print( 'Existing value:', my_dict['Igor'] )
print( 'Not existing value:',
       my_dict.get( 'Slava' ) )  # для вывода значения по остутствующему в словарю ключу используется метод get
my_dict['Misha'] = 1994
my_dict['Anton'] = 1999
b = my_dict.pop( 'Misha' )
print( 'Deleted value:', b )
print( 'Modified dictionary:', my_dict )
print()
my_set_1 = {1, 2, 3, 4, 5, 'Night', 3.14159, 3, 2, 2, 1}  # создание множества my_set и присвоение ему значений
print( 'Set_1:', my_set_1 )  # вывод созданного множества на экран
my_set_1 = {1, 2, 3, 4, (8, 12), 'Night', 3.14159, 3, 2, 2, 1, 5}  # добавление значений во множество
list_ = my_set_1
print( list_.discard( 5 ) )
print( 'Modified set:', list_ )
