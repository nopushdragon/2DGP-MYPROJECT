
from gamemanager import WIDTH, HEIGHT
from pico2d import *
import fade

titleBackground = load_image('source\\background\\ai_start.png')
startButton = load_image('source\\background\\button1.png')
startFont = load_font('source\\ui\\DungGeunMo.ttf')

start_twinkle = False
timer = 0.0
def Update(dt):
    global start_twinkle, timer
    timer += dt
    if timer > 0.5:
        timer = 0.0
        start_twinkle = not start_twinkle
    handle_events()
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            if( WIDTH / 2 - 200 <= mx <= WIDTH//2 + 200 and HEIGHT / 2 - 325 <= my <= HEIGHT//2 - 275):
                fade.fade_out("home")
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            quit()

def Draw():
    titleBackground.clip_draw(0, 0, 1024, 1024, WIDTH / 2, HEIGHT / 2,1200,1000)
    startButton.clip_draw(0, 0, 600, 118, WIDTH / 2, HEIGHT / 2 - 300,400,50)
    if start_twinkle: startFont.draw(WIDTH / 2 - 50, HEIGHT / 2 - 300, "GAME START", (255, 255, 255))
