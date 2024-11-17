'''Задача "Меньше текста, больше кликов":
Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.
Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и 'Информация'.
Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью 'Рассчитать'
срабатывает функция set_age с которой начинается работа машины состояний для age, growth и weight.'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio

api = ''
bot = Bot( token=api )
dp = Dispatcher( bot, storage=MemoryStorage() )


class UserState( StatesGroup ):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup( resize_keyboard=True )
button1 = KeyboardButton( text='Рассчитать' )
button2 = KeyboardButton( text='Информация' )
kb.add( button1 )
kb.add( button2 )


@dp.message_handler( commands=['start'] )
async def start_message(message):
    await message.answer( f'Привет! Я бот помогающий твоему здоровью.\n'
                          f'Чтобы начать, нажмите "Рассчитать"', reply_markup=kb )


@dp.message_handler( text='Рассчитать' )
async def set_age(message):
    await message.answer( 'Введите свой возраст (полных лет):' )
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
