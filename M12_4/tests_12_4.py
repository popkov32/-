'''
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано
отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с
сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с
сообщением "Неверный тип данных для объекта Runner".
'''

import logging
import unittest
import traceback

logging.basicConfig( level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                     format='%(asctime)s | %(levelname)s | %(message)s' )


class Runner:
    def __init__(self, name, speed=5):
        if isinstance( name, str ):
            self.name = name
        else:
            raise TypeError( f'Имя может быть только строкой, передано {type( name ).__name__}' )
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError( f'Скорость не может быть отрицательной, сейчас {speed}' )

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance( other, str ):
            return self.name == other
        elif isinstance( other, Runner ):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list( participants )

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove( participant )

        return finishers


class RunnerTest( unittest.TestCase ):
    def test_walk(self):
        try:
            runner_1 = Runner( 'Den', speed=-3 )
            if runner_1.speed > 0:

                for i in range( 10 ):
                    runner_1.walk()
                self.assertEqual( runner_1.distance, 50 )
                logging.INFO( '"test_walk" выполнен успешно' )
        except Exception:
            logging.warning( 'Неверная скорость для Runner' )
            logging.warning( traceback.format_exc() )

    def test_run(self):
        try:
            runner_1 = Runner( 'Den', 25 )
            for i in range( 10 ):
                runner_1.run()
            self.assertEqual( runner_1.distance, 100 )
            logging.INFO( '"test_run" выполнен успешно' )
        except Exception:
            logging.warning( 'Неверный тип данных для объекта Runner' )
            logging.warning( traceback.format_exc() )
