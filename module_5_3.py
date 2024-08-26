# Задача "Нужно больше этажей"
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor and new_floor <= self.number_of_floors:
            for i in range( 1, new_floor + 1 ):
                print( i )
        else:
            print( 'Такого этажа не существует' )

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance( value, int ):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance( value, int ):
            self.number_of_floors += value
            return self


h1 = House( 'ЖК Эльбрус', 10 )
h2 = House( 'Акация', 20 )
# h1.go_to( 5 )
# h2.go_to( 10 )

# __str__
print( h1 )
print( h2 )

# __len__
# print( len( h1 ) )
# print( len( h2 ) )

# __eq__
print( h1 == h2 )

h1 = h1 + 10  # __add__
print( h1 )
print( h1 == h2 )

h1 += 10  # __iadd__
print( h1 )

h2 = 10 + h2  # __radd__
print( h2 )

print( h1 > h2 )  # __gt__
print( h1 >= h2 )  # __ge__
print( h1 < h2 )  # __lt__
print( h1 <= h2 )  # __le__
print( h1 != h2 )  # __ne__

