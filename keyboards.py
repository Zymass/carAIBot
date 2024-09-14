from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram import Router, F, Bot


router = Router()


first_kb_buttons = [
    [InlineKeyboardButton(text='Да!', callback_data='yes')]
]


first_kb = InlineKeyboardMarkup(inline_keyboard=first_kb_buttons)


url_buttons = [
    [InlineKeyboardButton(text='CarVisionAi Channel Link', url='https://t.me/carvisionai', callback_data='Sub')]
]

url_to_channel = InlineKeyboardMarkup(inline_keyboard=url_buttons)