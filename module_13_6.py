'''Задача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'
Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.
Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
По итогу получится следующий алгоритм:
Вводится команда /start
На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

api = ''
bot = Bot( token=api )
dp = Dispatcher( bot, storage=MemoryStorage() )




kb = ReplyKeyboardMarkup( resize_keyboard=True )
button1 = KeyboardButton( text='Рассчитать' )
button2 = KeyboardButton( text='Информация' )
kb.row( button1, button2 )

kb2 = InlineKeyboardMarkup( resize_keyboard=True )
button_norma = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formula = InlineKeyboardButton( text='Формулы рассчета', callback_data='formulas' )
kb2.add( button_norma )
kb2.add( button_formula )

class UserState( StatesGroup ):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler( commands=['start'] )
async def start_message(message):
    await message.answer( 'Привет! Я бот помогающий твоему здоровью.', reply_markup=kb )



@dp.message_handler( text='Рассчитать' )
async def set_age(message):
    await message.answer( 'Выберите опцию:', reply_markup=kb2)



@dp.callback_query_handler( text='formulas' )
async def set_formulas(call):
    await call.message.answer( f'10 х вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) + 5 - для мужчиню\n'
                               f'10 х вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) - 161 - для женщин')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
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
