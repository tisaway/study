import asyncio
from create_bot import bot, dp
from handlers import start_router

async def main():
    dp.include_router(start_router)

    print('Bot is runninng.')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())