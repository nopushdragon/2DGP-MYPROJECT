
from gamemanager import WIDTH, HEIGHT
from pico2d import *
import fade

titleBackground = load_image('source\\background\\start.png')
startButton = load_image('source\\background\\start_button.png')

def Update():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            if( WIDTH//2 - 200 <= mx <= WIDTH//2 + 200 and HEIGHT//2 - 50 <= my <= HEIGHT//2 + 50):
                fade.fade_out("home")

def Draw():
    titleBackground.clip_draw(0, 0, 1200, 800, WIDTH // 2, HEIGHT // 2)
    startButton.clip_draw(0, 0, 400, 100, WIDTH // 2, HEIGHT // 2, )