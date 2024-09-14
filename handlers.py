import time
import json
from requests_funcs import get_img_from_txt
import keyboards
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from aiogram import Router, F, Bot
from additional_funcs import check_sub_channel


router = Router()


@router.message(CommandStart())
async def say_hello(message: Message, bot: Bot):
    user_status = await bot.get_chat_member(chat_id=-1002199731984, user_id=message.from_user.id)
    if check_sub_channel(user_status):
        await message.answer(text='Привет! 🚗\n\n'
                                  'Я генерирую картинки машин по твоему описанию\n'
                                  'Опиши авто — и получи изображение!\n'
                                  'Начинаем? 🚗✨',reply_markup=keyboards.first_kb)
        await bot.send_message(chat_id=-1002223414416, text='Пользователь подписался на канал и использует бота\n'
                                                             'id - {}\nusername - {}'.format(message.from_user.id, message.from_user.username))
    else:
        await message.answer(text='Сначала подпишитесь на наш канал - там много интересного!\n\nПосле этого '
                                  'возвращатесь и нажимайте👇🏼\n\n/start\n/start\n/start',
                             reply_markup=keyboards.url_to_channel)


@router.callback_query(F.data == 'yes')
async def send_example(callback: CallbackQuery):
    await callback.message.answer(text='Запрос должен быть на английском языке\n'
                                       '(Используй переводчик)\n'
                                       'Например - Chevrolet Cruze.\n\nОтправляю результат такого запроса:')
    await callback.message.answer_photo(photo='https://iimg.su/i/J0xJC', caption='Результат')
    await callback.answer()
    time.sleep(2)
    await callback.message.answer(text='Жду твой запрос!')


@router.message()
async def send_user_img(message:Message, bot: Bot):
    link = await get_img_from_txt(message.text)
    print(link)
    if link != 'Ошибка выполнения запроса!':
        await message.answer('🚗✨ Вот ваше изображение! Наслаждайтесь результатом! 🎨\n\n'
                             '*Если ссылка не открывается, подождите 10 секунд, изображение дорабатывается\n{}'
                             '\n\nhttps://t.me/carvisionai'.format(link))
    else:
        await message.answer('Ошибка!')