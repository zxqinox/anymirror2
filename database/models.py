from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Template:
    id: int
    user_id: int
    name: str
    description: str
    about_text: str
    commands: List[Dict]
    cities: List[str]
    photo_dir: str
    bot_username: str
    settings: Dict
