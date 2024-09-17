# Задание "Записать и запомнить"

from pprint import pprint


def custom_write(file_name, strings):  # ф-ция принимает название файла для записи и список строк для записи
    string_position = {}  # начальный пустой словарь
    file = open( file_name, 'a', encoding='utf-8' )
    for i, j in enumerate( strings ):
        key = (i + 1, file.tell())
        string_position[key] = j
        file.write( j + '\n' )
    file.close()
    return string_position  # возврат получившегося словаря


def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write( 'test.txt', info )
    for elem in result.items():
        print( elem )


if __name__ == '__main__':
    main()
