# Задача "За честь и отвагу!":

# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.


from threading import Thread
from time import sleep


class Knight( Thread ):
    enemies = 100
    days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print( f'{self.name}, на нас напали!' )
        while self.enemies > 0:
            sleep( 1.0 )
            self.enemies -= self.power
            self.days += 1
            # sleep( 1.1 )
            if self.enemies > 0:
                print( f'{self.name}: сражается {self.days} день (дня, дней), осталось {self.enemies} воинов' )
        print( f'{self.name} одержал победу спустя {self.days} день (дня, дней)!' )


first_knight = Knight( 'Sir Lancelot', 15 )
second_knight = Knight( "Sir Galahad", 20 )

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print( 'Все битвы закончились!' )
