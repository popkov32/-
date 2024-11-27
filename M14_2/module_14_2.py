'''
Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователей.
Решение этого задание со строки 40
'''

import sqlite3  # импорт библиотеки SQLite3

connection = sqlite3.connect( 'not_telegram.db' )  # подключение к БД
cursor = connection.cursor()  # создание виртуальной мышки "cursor"

cursor.execute( ''' 
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL, 
age INTEGER,
balance INTEGER NOT NULL
)
''' )

# Заполнение базы данных 10 записями
# for i in range(1, 11 ):
#     cursor.execute( ' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                     (f'User{i}', f'example{i}@gmail.com', (i) * 10, 1000) )
#
# Обновление баланса у каждой 2й записи на 500
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}')) # обновление в БД элементов
#
# Удаление каждой 3ей записи начиная с 1й
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',)) #удаление из БД элементов

# Удаление из БД записи с id = 6
# cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчет общего кол-ва записей
cursor.execute( 'SELECT COUNT(*) FROM Users' )
total_id = cursor.fetchone()[0]
# print(total_id)

# Подсчет суммы всех балансов и среднего баланса
cursor.execute( 'SELECT SUM(balance) FROM Users' )
total_balance = cursor.fetchone()[0]
cursor.execute( 'SELECT AVG(balance) FROM Users' )
total_balance_avg = cursor.fetchone()[0]
# print(total_balance)
# print(total_balance / total_id)
print( total_balance_avg )

# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]}| Почта: {user[1]}| Возраст: {user[2]}| Баланс: {user[3]}')
connection.commit()  # сохранение изменений в БД
connection.close()  # закрытие соединения с БД
