# Задача "Потоковая запись в файлы":

# Необходимо создать функцию write_words(word_count, file_name), где word_count - количество
# записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий
# файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её:
# from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для
# функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи
# join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано
# в лекции к домашнему заданию.

from time import sleep
from datetime import datetime
from threading import Thread

def whrite_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}' + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start1 = datetime.now()
whrite_words(10, 'example1.txt')
whrite_words(30, 'example2.txt')
whrite_words(200, 'example3.txt')
whrite_words(100, 'example4.txt')
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)

time_start2 = datetime.now()
thr_1 = Thread(target=whrite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=whrite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=whrite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=whrite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)