import sqlite3  # импорт библиотеки SQLite3

connection = sqlite3.connect( 'products.db' )  # подключение к БД products.db
cursor = connection.cursor()  # создание виртуальной мышки "cursor"

# Создание таблицы Products
cursor.execute( ''' 
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT, 
price INT NOT NULL
);
''' )


# Заполнение базы данных Products
def initiate_db():
    for i in range( 1, 5 ):
        cursor.execute( 'INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                        (f'{i}', f'Продукт{i}', f'Описание{i}', f'{i * 100}') )
        connection.commit()


initiate_db()


#
def get_all_product():
    connection = sqlite3.connect( 'Products.db' )
    cursor = connection.cursor()
    cursor.execute( 'SELECT * FROM Products' )
    products = cursor.fetchall()
    connection.commit()
    return products


connection.commit()  # сохранение изменений в БД
connection.close()  # закрытие соединения с БД

# Создание таблицы Users

connection = sqlite3.connect( 'users.db' )  # подключение к БД Users.db
cursor = connection.cursor()  # создание виртуальной мышки "cursor"

cursor.execute( '''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NO NULL,
age INT NOT NULL,
balance INT NOT NULL
);
''' )


# Ф-ция добавления польз-ля
def add_user(username, email, age):
    connection = sqlite3.connect( 'Users.db' )
    cursor = connection.cursor()
    cursor.execute( 'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (f'{username}', f'{email}', f'{age}', f'{1000}') )
    connection.commit()


# Ф-ция проверки наличия польз-ля в БД
def is_included(username):
    connection.sqlite3.connect( 'Users.db' )
    cursor = connection.cursor()
    check_username = cursor.execute( 'SELECT * FROM Users WHERE username = ?', (username,) )
    if check_username.fetchone() is None:
        return False
    else:
        return True


connection.commit()  # сохранение изменений в БД
connection.close()  # закрытие соединения с БД
