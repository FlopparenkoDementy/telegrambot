import asyncio

from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart, Command 
import keyboards as kb

router = Router()

@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer("Версия менеджера паролей 0.0.1. Для получения большей информации напишите /info")

@router.message(Command('info'))
async def get_info(message: Message):
    await message.answer("Какая то краткая информация о проекте...")

@router.message(Command('get_passwords'))
async def get_password(message: Message):
    await message.answer("Выберите что вам нужно", reply_markup=kb.main)
