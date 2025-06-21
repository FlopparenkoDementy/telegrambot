import asyncio

from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.filters import CommandStart, Command 
from handlers import router
from config import BOT_TOKEN

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("БОТ ВЫКЛЮЧЕН")