'''
Задача "Заморозка кейсов":
Подготовка:
В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
Часть 1. TestSuit.
Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с
произвольным названием.
Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
Создайте объект класса TextTestRunner, с аргументом verbosity=2.
Часть 2. Пропуск тестов.
Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение
'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
'''

import unittest
# from runner import Runner
from runner_and_tournament import Runner, Tournament


class RunnerTest( unittest.TestCase ):
    is_frozen = False

    @unittest.skipIf( is_frozen == True, "Тесты в этом кейсе заморожены" )
    def test_walk(self):
        runner_1 = Runner( 'Den' )
        for i in range( 10 ):
            runner_1.walk()
        self.assertEqual( runner_1.distance, 50 )

    @unittest.skipIf( is_frozen == True, "Тесты в этом кейсе заморожены" )
    def test_run(self):
        runner_1 = Runner( 'Den' )
        for i in range( 10 ):
            runner_1.run()
        self.assertEqual( runner_1.distance, 100 )

    @unittest.skipIf( is_frozen == True, "Тесты в этом кейсе заморожены" )
    def test_challenge(self):
        runner_1 = Runner( 'Den' )
        runner_2 = Runner( 'Max' )
        for i in range( 10 ):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual( runner_1.distance, runner_2.distance )


class TournamentTest( unittest.TestCase ):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner( 'Усэйн', 10 )
        self.runner_2 = Runner( 'Андрей', 9 )
        self.runner_3 = Runner( 'Ник', 3 )

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print( f'Тест: {test_key}' )
            for key, value in test_value.items():
                print( f'{key}: {value.name}' )

    @unittest.skipIf( is_frozen == True, "Тесты в этом кейсе заморожены" )
    def test_turn1(self):
        turn_1 = Tournament( 90, self.runner_1, self.runner_3 )
        result = turn_1.start()
        self.assertTrue( result[list( result.keys() )[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник' )
        self.all_results['test_turn1'] = result

    @unittest.skipIf( is_frozen == True, "Тесты в этом кейсе заморожены" )
    def test_turn2(self):
        turn_2 = Tournament( 90, self.runner_2, self.runner_3 )
        result = turn_2.start()
        self.assertTrue( result[list( result.keys() )[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник' )
        self.all_results['test_turn2'] = result

    @unittest.skipIf( is_frozen == True, "Тесты в этом кейсе заморожены" )
    def test_turn3(self):
        turn_3 = Tournament( 90, self.runner_1, self.runner_2, self.runner_3 )
        result = turn_3.start()
        self.assertTrue( result[list( result.keys() )[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник' )
        self.all_results['test_turn3'] = result


if __name__ == "__main__":
    unittest.main()
