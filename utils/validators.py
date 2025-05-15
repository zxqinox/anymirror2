from config import config

def validate_media_type(mime_type: str) -> bool:
    return mime_type in config.ALLOWED_MEDIA_TYPES

def validate_bot_commands(commands: list) -> bool:
    if len(commands) > 100:
        return False
    for cmd in commands:
        if len(cmd['command']) > 32 or len(cmd['description']) > 256:
            return False
    return True
