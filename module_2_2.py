# modul2_2_2.py
print( 'введите любое целое число', end='\n' )
first = int( input() )
print( 'введите любое целое число', end='\n' )
second = int( input() )
print( 'введите любое целое число', end='\n' )
third = int( input() )
if first == second and first == third and second == third:
    print( 3 )
elif first == second or first == third or second == third:
    print( 2 )
else:
    print( 0 )
