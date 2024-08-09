# Задача "Однокоренные".

def single_root_words(root_word, *other_root_words): #Определение ф-ции с обязат парам-м и парам-м с неогр посл-стью
    same_words = [] #Создание пустого списка для последующего заполнения в рез-те работы ф-ции
    for i in other_root_words: #Запуск цикла перебора последовальности other_root_words
        if root_word.upper() in i.upper() or i.upper() in root_word.upper(): #Условие для проверки однокоренных слов
            same_words.append(i) #Добавление однокоренных слов в список same_words
    return same_words #Возврат рез-та работы ф-ции

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)