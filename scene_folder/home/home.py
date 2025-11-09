
from gamemanager import WIDTH, HEIGHT
from pico2d import *
from scene_folder.background_base import BackGround
import fade
from characters import Characters
import random

#titleBackground = load_image('source\\background\\home.png')
background = BackGround(load_image('source\\background\\bg_home_morning.png'),WIDTH/2,HEIGHT/2,1024,800,flip=False)
ground = load_image('source\\background\\home_ground.png')
black = load_image('source\\background\\black.png')

chars = []
def Reset():
    for c in Characters:
        if c.get == True:
            c.x = random.randint(100, WIDTH - 100)
            c.y = 300
            chars.append(c)

def Update(dt):
    background.Move(-10 * dt)
    handle_events()
    for c in chars:
        c.Update(dt)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            if( 0 <= mx <= WIDTH//2 and HEIGHT//2 <= my <= HEIGHT): fade.fade_out("hotel")
            elif( WIDTH//2 <= mx <= WIDTH and HEIGHT//2 <= my <= HEIGHT): fade.fade_out("upgrade")
            elif( 0 <= mx <= WIDTH//2 and 0 <= my <= HEIGHT//2): fade.fade_out("shop")
            elif( WIDTH//2 <= mx <= WIDTH and 0 <= my <= HEIGHT//2): fade.fade_out("stage1")
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                fade.fade_out("title")

def Draw():
    background.Draw()
    ground.clip_draw(0, 0, 1024, 252, WIDTH // 2, 200, 1200, 250)
    black.clip_draw(0, 0, 1200, 800, WIDTH // 2, -50, 1200, 250)
    for c in chars:
        c.Draw()