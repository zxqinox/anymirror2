from aiogram import Bot
from aiogram.client import bot
from aiogram.methods import (
    SetMyName,
    SetMyDescription,
    SetMyShortDescription,
    SetMyCommands,
    SetChatMenuButton,
    SetMyDefaultAdministratorRights
)
from aiogram.types import (
    BotCommand,
    BotMenuButton,
    BotCommandScopeAllPrivateChats
)

async def configure_bot_api(token: str, template: dict):
    try:
        async with Bot(token=token) as bot:
            # Основные настройки
            await bot(SetMyName(name=template['name']))
            await bot(SetMyDescription(description=template['description']))
            await bot(SetMyShortDescription(short_description=template['about_text']))
            
            # Команды
            commands = [BotCommand(command=cmd['command'], description=cmd['description']) 
                       for cmd in template['commands']]
            await bot(SetMyCommands(commands=commands, scope=BotCommandScopeAllPrivateChats()))
            
            # Настройка меню
            menu_button = BotMenuButton(type="commands")
            await bot(SetChatMenuButton(menu_button=menu_button))
            
            # Права администратора
            if template['settings'].get('admin_rights'):
                await bot(SetMyDefaultAdministratorRights(
                    rights=template['settings']['admin_rights']
                ))
            
            logger.info(f"Bot @{await bot.get_me().username} configured successfully")
            return True
    except Exception as e:
        logger.error(f"Bot API configuration failed: {e}")
        return False
