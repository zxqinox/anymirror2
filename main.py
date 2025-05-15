import asyncio
from aiogram import Bot, Dispatcher
from config import config
from database.db import init_db
from handlers import commands, files, setup_template

async def main():
    await init_db()
    
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_routers(
        commands.router,
        files.router,
        setup_template.router
    )
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
