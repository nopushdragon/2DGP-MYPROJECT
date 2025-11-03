
from gamemanager import WIDTH, HEIGHT
from pico2d import *
import fade

titleBackground = load_image('source\\background\\home.png')

def Update():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            if( 0 <= mx <= WIDTH//2 and HEIGHT//2 <= my <= HEIGHT): fade.fade_out("hotel")
            elif( WIDTH//2 <= mx <= WIDTH and HEIGHT//2 <= my <= HEIGHT): fade.fade_out("upgrade")
            elif( 0 <= mx <= WIDTH//2 and 0 <= my <= HEIGHT//2): fade.fade_out("shop")
            elif( WIDTH//2 <= mx <= WIDTH and 0 <= my <= HEIGHT//2): fade.fade_out("stage1")

def Draw():
    titleBackground.clip_draw(0, 0, 1200, 800, WIDTH // 2, HEIGHT // 2)