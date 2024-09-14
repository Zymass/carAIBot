import asyncio
import logging
from aiogram import Bot, Dispatcher
TOKEN = '6772074338:AAGYYNSC946YQHEoRdPZ7C2mAzAN0Sc4XKo'
import handlers


logging = logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')


# Функция конфигурирования и запуска бота
async def main() -> None:
    # Инициализируем бот и диспетчер

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    #Регистрируем роутеры
    dp.include_router(handlers.router)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "callback_query"])



asyncio.run(main())