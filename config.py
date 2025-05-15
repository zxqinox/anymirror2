from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).parent

# Конфигурация базы данных
DB_PATH = BASE_DIR / "database" / "bot_factory.db"

# Директории для хранения файлов
FILES_DIR = BASE_DIR / "uploads"
PHOTO_DIR = FILES_DIR / "photos"

# Разрешённые типы медиа для загрузки
ALLOWED_MEDIA_TYPES = [
    "text/plain",
    "application/zip",
]

# Настройки шаблона по умолчанию для создания ботов
TEMPLATE_DEFAULTS = {
    "name": "MyBot",
    "description": "Бот, созданный с помощью Bot Factory",
    "about_text": "Добро пожаловать в мой бот!",
    "commands": [
        {"command": "/start", "description": "Запустить бот"},
        {"command": "/help", "description": "Получить помощь"},
    ],
    "cities": ["Москва", "Лондон", "Нью-Йорк"],
    "photo_dir": str(PHOTO_DIR),
    "bot_username": "@MyBot",
    "settings": {
        "admin_rights": {
            "can_delete_messages": True,
            "can_restrict_members": True,
            "can_pin_messages": True,
        },
        "inline_mode": True,
        "group_mode": True,
        "privacy_mode": True,
        "welcome_message": "Добро пожаловать в {bot_name}!",
        "language": "ru",
        "timezone": "UTC",
    },
}

# Создание директорий, если они не существуют
import os
os.makedirs(FILES_DIR, exist_ok=True)
os.makedirs(PHOTO_DIR, exist_ok=True)
