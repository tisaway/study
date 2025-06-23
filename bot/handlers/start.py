from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, User
from keyboards import ROLE_KEYBOARD

start_router = Router()


@start_router.message(CommandStart(
    deep_link=True, magic=F.args == "help"
))

async def cmd_start_help(message: Message):
    await message.answer("/start")

from create_bot import bot

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    # user_id = message.from_user.id
    # chat_id = message.chat.id
    chat = await bot.get_chat
    # ChatFullInfo = await bot.get_chat(435680352)
    # username = ChatFullInfo.username
    await message.answer('chat_id: ' + str(chat.id), reply_markup=ROLE_KEYBOARD)
    # await bot.send_contact(message.chat.id, '+79142528323', 'Имя')


admin_id = '435680352'
@start_router.message(F.document)
async def echo_gif(message: Message):
    print('kek')
    # await message.answer_document(message.document.file_id)
    await bot.forward_message(chat_id=admin_id, from_chat_id=message.from_user.id, message_id=message.message_id)

@start_router.message()
async def echo(message: Message):
    print('lol')
    # await message.answer(str(message.from_user.id))
    await bot.forward_message(chat_id=admin_id, from_chat_id=message.from_user.id, message_id=message.message_id)

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import CallbackQuery

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

async def kek(id, text='azaza'):
    await bot.send_message(chat_id=id, text=text)

@start_router.callback_query(F.data == 'register_teacher')
async def notify(call: CallbackQuery):
    await kek(call.message.chat.id)
    
    scheduler.add_job(kek, 'cron', second='*', args=[call.message.chat.id, 'kek'], id='smth')
    scheduler.start()
    await call.message.answer("done?")

@start_router.callback_query(F.data == 'smth')
async def smth(call: CallbackQuery):
    scheduler.modify_job(job_id='smth', args=[call.message.chat.id, 'lol'])
    await call.message.answer("done?")
