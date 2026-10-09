from pathlib import Path
from pygame.color import Color
import json

ROOT_DIR = Path(__file__).parent.parent
SRC_DIR = ROOT_DIR / 'src'

COLOR_BG = (245, 245, 245)
COLOR_GRID = (220, 220, 220)
COLOR_AXIS = (50, 50, 50)
COLOR_TEXT = (80, 80, 80)

def save_settings(size:tuple=(1280, 720), color:Color=COLOR_BG, fps:int=30):
    settings = {
        'size': size,
        'color': list(color),
        'fps': fps,
    }

    with open(SRC_DIR / 'settings.json', 'w', encoding='UTF-8') as file:
        json.dump(settings, file, indent=4)

def read_settings():
    settings_file = SRC_DIR / 'settings.json'

    if not settings_file.exists():
        save_settings()

    with open(settings_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    data['color'] = Color(*data['color'])
    data['size'] = tuple(data['size'])

    return data