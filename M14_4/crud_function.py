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


# Заполнение базы данных
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
