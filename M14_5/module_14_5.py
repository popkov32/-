from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio
import logging

import crud_function
from config import *

# from keyboards import *
# import texts
logging.basicConfig( level=logging.INFO )
api = ''
bot = Bot( token=API )
dp = Dispatcher( bot, storage=MemoryStorage() )

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton( text='Регистрация' ),
            KeyboardButton( text='Информация' )
        ],
        [
            KeyboardButton( text='Рассчитать' ),
            KeyboardButton( text='Купить' )
        ]
    ], resize_keyboard=True
)

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


class RegistrationState( StatesGroup ):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler( commands=['start'] )
async def start_message(message):
    await message.answer( 'Привет! Я бот помогающий твоему здоровью.\n'
                          'Чтобы начать, пройдите регистрацию', reply_markup=start_menu )


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


@dp.message_handler( text='Регистрация' )
async def sing_up(message):
    await message.answer( 'Введите имя пользователя (только латиницей):' )
    await  RegistrationState.username.set()


@dp.message_handler( state=RegistrationState.username )
async def set_username(message, state):
    new_user = crud_function.is_included( message.text )
    if new_user is True:
        await message.answer( 'Пользователь с таким именем уже существует. Введите другое имя' )
    else:
        await state.update_data( username=message.text )
        await message.answer( 'Ведите свой email:' )
        await RegistrationState.email.set()


@dp.message_handler( state=RegistrationState.email )
async def set_email(message, state):
    await state.update_data( email=message.text )
    await message.answer( 'Введите свой возраст:' )
    await RegistrationState.age.set()


@dp.message_handler( state=RegistrationState.age )
async def set_age(message, state):
    await state.update_data( age=message.text )
    data = await state.get_data()
    crud_function.add_user( data['username'], data['email'], data['age'] )
    await message.answer( 'Вы зарегистрированы.' )
    await state.finish()


if __name__ == '__main__':
    executor.start_polling( dp, skip_updates=True )
