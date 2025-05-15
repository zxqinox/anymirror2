import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from database.db import init_db
from handlers.commands import router as commands_router
from handlers.files import router as files_router
from handlers.setup_template import router as template_router

async def main():
    # Настройка логирования
    logging.basicConfig(level=logging.INFO)

    # Инициализация бота и диспетчера
    bot = Bot(token="YOUR_BOT_TOKEN")  # Замените на ваш токен бота
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрация маршрутизаторов
    dp.include_router(commands_router)
    dp.include_router(files_router)
    dp.include_router(template_router)

    # Инициализация базы данных
    await init_db()

    # Запуск опроса
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
