from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить пароль", url="https://google.com")], 
    [InlineKeyboardButton(text="Просмотреть существующие пароли", url="https://google.com")]
])