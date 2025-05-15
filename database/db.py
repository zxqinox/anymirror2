import aiosqlite
from config import config

async def get_connection():
    return await aiosqlite.connect(config.DB_PATH)

async def init_db():
    async with await get_connection() as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                about_text TEXT,
                commands JSON,
                cities JSON,
                photo_dir TEXT,
                bot_username TEXT,
                settings JSON
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS bot_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_id INTEGER,
                tokens TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()
