import magic
from aiogram.types import Message
from config import config
from utils.validators import validate_media_type
from utils.logger import logger

async def process_media(message: Message):
    try:
        file = await message.bot.get_file(message.document.file_id)
        mime_type = magic.from_buffer(await message.document.download()), mime=True)
        
        if not validate_media_type(mime_type):
            await message.answer("❌ Неподдерживаемый тип файла!")
            return None
            
        file_path = f"{config.FILES_DIR}/{message.from_user.id}_{message.document.file_name}"
        await message.bot.download_file(file.file_path, destination=file_path)
        
        logger.info(f"Media saved: {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"Media processing error: {e}")
        return None
