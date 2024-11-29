'''
Задача "Продуктовая база":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя
пунктам задачи ниже.

Дополните ранее написанный код для Telegram-бота:
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
 Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
title(название продукта) - текст (не пустой)
description(описание) - текст
price(цена) - целое число (не пустой)
get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи
SQL запроса.

Изменения в Telegram-бот:
В самом начале запускайте ранее написанную функцию get_all_products.
Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной
нумерации продуктов функцию get_all_products. Полученные записи используйте в выводимой
надписи: "Название: <title> | Описание: <description> | Цена: <price>"
Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего
 вывода в чате Telegram-бота.
'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

import crud_function
from config import *
from crud_function import *

# from keyboards import *
# import texts

api = ''
bot = Bot( token=API )
dp = Dispatcher( bot, storage=MemoryStorage() )

kb = ReplyKeyboardMarkup( resize_keyboard=True )
button1 = KeyboardButton( text='Рассчитать' )
button2 = KeyboardButton( text='Информация' )
button3 = KeyboardButton( text='Купить' )
kb.row( button1, button2 )
kb.add( button3 )

kb2 = InlineKeyboardMarkup( resize_keyboard=True )
button_norma = InlineKeyboardButton( text='Рассчитать норму калорий', callback_data='calories' )
button_formula = InlineKeyboardButton( text='Формулы рассчета', callback_data='formulas' )
kb2.add( button_norma )
kb2.add( button_formula )

kb3 = InlineKeyboardMarkup( resize_keyboard=True )
p1 = InlineKeyboardButton( text='Product1', callback_data='product_buying' )
p2 = InlineKeyboardButton( text='Product2', callback_data='product_buying' )
p3 = InlineKeyboardButton( text='Product3', callback_data='product_buying' )
p4 = InlineKeyboardButton( text='Product4', callback_data='product_buying' )
kb3.row( p1, p2, p3, p4 )


class UserState( StatesGroup ):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler( commands=['start'] )
async def start_message(message):
    await message.answer( 'Привет! Я бот помогающий твоему здоровью.', reply_markup=kb )


@dp.message_handler( text='Рассчитать' )
async def main_menu(message):
    await message.answer( 'Выберите опцию:', reply_markup=kb2 )


@dp.message_handler( text='Купить' )
async def get_buying_list(message):
    products = crud_function.get_all_product()
    for product in products:
        await message.answer( f'Название: Product{product[1]} |Описание: описание {product[2]} | Цена: {product[3]}' )
        with open( f'{product[0]}.jpg', 'rb' ) as img:
            await message.answer_photo( img )
    await message.answer( 'Выберите продукт для покупки:', reply_markup=kb3 )


@dp.callback_query_handler( text='product_buying' )
async def send_confirm_message(call):
    await call.message.answer( 'Вы успешно приобрели продукт!' )
    await call.answer()


@dp.callback_query_handler( text='formulas' )
async def get_formulas(call):
    await call.message.answer( f'10 х вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) + 5 - для мужчиню\n'
                               f'10 х вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) - 161 - для женщин' )
    await call.answer()


@dp.callback_query_handler( text='calories' )
async def set_age(call):
    await call.message.answer( "Введите свой возраст:" )
    await UserState.age.set()


@dp.message_handler( state=UserState.age )
async def set_growth(message, state):
    await state.update_data( years=message.text )
    await message.answer( 'Введите свой рост (в сантиметрах):' )
    await UserState.growth.set()


@dp.message_handler( state=UserState.growth )
async def set_weight(message, state):
    await state.update_data( kg=message.text )
    await message.answer( 'Введите свой вес (в килограммах):' )
    await UserState.weight.set()


@dp.message_handler( state=UserState.weight )
async def set_calories(message, state):
    await state.update_data( cm=message.text )
    data = await state.get_data()
    calories_m = float( data['kg'] ) * 10 + float( data['cm'] ) * 6.25 - 5 * float( data['years'] ) + 5
    calories_w = float( data['kg'] ) * 10 + float( data['cm'] ) * 6.25 - 5 * float( data['years'] ) - 161
    await message.answer( f'Ваша суточная норма калорий:\n'
                          f'{calories_m} - для мужчин\n'
                          f'{calories_w} - для женщин' )
    await state.finish()


if __name__ == '__main__':
    executor.start_polling( dp, skip_updates=True )
