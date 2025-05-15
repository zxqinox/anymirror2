from aiogram import Router, F
from aiogram.types import Message
from services.file_processor import process_txt, process_zip

router = Router()

@router.message(F.document.file_name.endswith('.txt'))
async def handle_txt(message: Message, bot: Bot):
    await process_txt(message, bot)

@router.message(F.document.file_name.endswith('.zip'))
async def handle_zip(message: Message, bot: Bot):
    await process_zip(message, bot)
