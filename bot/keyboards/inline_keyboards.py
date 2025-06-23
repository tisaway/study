from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

admin_username = 'Gremm3666'
ROLE_KEYBOARD_BUTTONS = [
    [InlineKeyboardButton(text='Я учитель 🧑‍🏫', callback_data='register_teacher')],
    [InlineKeyboardButton(text='Я smth 🧑‍🏫', callback_data='smth')],
    [InlineKeyboardButton(text='Я ученик 🧑‍🎓', url=f"https://t.me/{admin_username.lstrip('@')}")],
    [InlineKeyboardButton(text='Я родитель 🧑‍💼', web_app=WebAppInfo(url='https://tisaway.pythonanywhere.com/students'))]
]
ROLE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=ROLE_KEYBOARD_BUTTONS)

ROLE_KEK = [
    [InlineKeyboardButton(text='TESTING', web_app=WebAppInfo(url='https://tisaway.pythonanywhere.com/students'))]
]
ROLE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=ROLE_KEK)