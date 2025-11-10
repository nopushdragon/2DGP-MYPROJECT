from pico2d import *
import gamemanager
from scene_folder.background_base import BackGround
import ui
import fade

def Reset():
    global shop_bg
    shop_bg = BackGround('source\\background\\shop_background.png')

def Update(dt):
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            fade.fade_out("home")

def Draw():
    ui.draw()