import os
import logging
from pathlib import Path

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DB_PATH = "database/bot_factory.db"
    FILES_DIR = "user_files"
    LOGS_DIR = "logs"
    ALLOWED_MEDIA_TYPES = ['image/jpeg', 'image/png', 'application/zip']
    
    def setup_dirs(self):
        Path(self.FILES_DIR).mkdir(exist_ok=True)
        Path("database").mkdir(exist_ok=True)
        Path(self.LOGS_DIR).mkdir(exist_ok=True)

config = Config()
config.setup_dirs()
