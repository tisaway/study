from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, CallbackQuery
from aiogram import Router, F
from aiogram.types import Message
from keyboards import ROLE_KEYBOARD

settings_router = Router()

async def contact_keyboard():
    kb_list = [
        [KeyboardButton(text="Отправить гео", request_location=True)],
        [KeyboardButton(text="Поделиться номером", request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   one_time_keyboard=True,
                                   input_field_placeholder="Воспользуйтесь специальной клавиатурой:")
    return keyboard




@settings_router.message(F.data == 'register_role')
async def register_role(message: Message):
    user_first_name = message.from_user.first_name
    await message.answer('Привет, ' + user_first_name + '!\nДля начала выбери, кто ты:', reply_markup=ROLE_KEYBOARD)

@settings_router.callback_query(F.data == 'register_phone')
async def share_number(call: CallbackQuery):
    await call.message.answer("Нажмите на кнопку ниже, чтобы отправить контакт или напишите номер телефона:", reply_markup=await contact_keyboard())

@settings_router.message(F.contact)
async def get_contact(message: Message):
    contact = message.contact
    await message.answer(f"Спасибо, {contact.first_name}.\n"
                         f"Ваш номер {contact.phone_number} был получен",
                         reply_markup=ReplyKeyboardRemove())
    
@settings_router.message(F.phone_number)
async def get_phone(message: Message):
    await message.answer('KEEEEEEEEEEEEEEK')