''' ДЗ по теме "Методы Юнит-тестирования"

Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список
участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты
всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта
класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается
метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и
предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его
работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
Пример результата выполнения тестов:
Вывод на консоль:
{1: Усэйн, 2: Ник}
{1: Андрей, 2: Ник}
{1: Андрей, 2: Усэйн, 3: Ник}

Ran 3 tests in 0.001s
OK
'''
from runner_and_tournament import Runner, Tournament

import unittest


class TournamentTest( unittest.TestCase ):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # словарь с результатами всех тестов

    def setUp(self):
        self.runner_1 = Runner( 'Усэйн', 10 )
        self.runner_2 = Runner( 'Андрей', 9 )
        self.runner_3 = Runner( 'Ник', 3 )

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print( show_result )

    def test_run_1(self):
        self.tournament_1 = Tournament( 90, self.runner_1, self.runner_3 )  # создаем объект класса Забег

        self.all_results = self.tournament_1.start()  # в словарь all_result записываем результат функции (место:участн)

        last_runner_name = self.all_results[max( self.all_results.keys() )].name  # записываем имя с максимальным местом
        self.assertTrue( last_runner_name == 'Ник' )  # вызываем юнит-метод сравнения

        TournamentTest.all_results[1] = self.all_results  # записываем словарь с ключом 1

    def test_run_2(self):
        self.tournament_2 = Tournament( 90, self.runner_2, self.runner_3 )  # создаем объект класса Забег

        self.all_results = self.tournament_2.start()  # в словарь all_result записываем результат функции (место:участн)

        last_runner_name = self.all_results[max( self.all_results.keys() )].name  # записываем имя с максимальным местом
        self.assertTrue( last_runner_name == 'Ник' )  # вызываем юнит-метод сравнения

        TournamentTest.all_results[2] = self.all_results  # записываем словарь с ключом 2

    def test_run_3(self):
        self.tournament_3 = Tournament( 90, self.runner_1, self.runner_2, self.runner_3 )  # создаем объект класса Забег

        self.all_results = self.tournament_3.start()  # в словарь all_result записываем результат функции (место:участн)

        last_runner_name = self.all_results[max( self.all_results.keys() )].name  # записываем имя с максимальным местом
        self.assertTrue( last_runner_name == 'Ник' )  # вызываем юнит-метод сравнения

        TournamentTest.all_results[3] = self.all_results  # записываем словарь с ключом 3

    if __name__ == '__main__':
        unittest.main()
