
from gamemanager import WIDTH, HEIGHT
from pico2d import *
from scene_folder.background_base import BackGround
import fade
from characters import Characters
import random
import ui

background = BackGround(load_image('source\\background\\bg_home_morning.png'),WIDTH/2,HEIGHT/2,1024,800)
ground = load_image('source\\background\\home_ground.png')
black = load_image('source\\background\\home_black.png')
dungeon_button = load_image('source\\ui\\dungeon_button.png')
friend_button = load_image('source\\ui\\friend_button.png')
shop_button = load_image('source\\ui\\shop_button.png')
upgrade_button = load_image('source\\ui\\upgrade_button.png')

chars = []
active_timer = []
def Reset():
    global chars, active_timer
    chars.clear()
    active_timer.clear()
    for c in Characters:
        if c.get == True:
            c.x = random.randint(100, WIDTH - 100)
            c.y = 300
            c.frameTimer = random.uniform(0, 1)
            c.frame = random.randint(0,1)
            chars.append(c)
            active_timer.append(random.randint(0,5))

def Update(dt):
    background.Move(-10 * dt)
    handle_events()
    char_update(dt)

def char_update(dt):
    global chars, active_timer
    for c in chars:
        idx = chars.index(c)
        active_timer[idx] += dt
        if active_timer[idx] > 4:
            active_timer[idx] = 0.0
            c.frameTimer = 0.0
            c.frame = 0
            if random.randint(0,2) == 0:
                c.state = "idle"
            elif random.randint(0,2) == 1:
                c.state = "walk"
                c.flip = False
            elif random.randint(0,2) == 2:
                c.state = "walk"
                c.flip = True
        if c.state == "walk" and c.flip == False:
            c.x += 30 * dt
            if c.x > WIDTH - 50:
                c.flip = True
        elif c.state == "walk" and c.flip == True:
            c.x -= 30 * dt
            if c.x < 50:
                c.flip = False
        c.Update(dt)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            if( 30 <= mx <= 190 and 40 <= my <= 110): fade.fade_out("friend")
            elif( 230 <= mx <= 390 and 40 <= my <= 110): fade.fade_out("shop")
            elif( 430 <= mx <= 590 and 40 <= my <= 110): fade.fade_out("upgrade")
            elif( 980 <= mx <= 1180 and 40 <= my <= 100): fade.fade_out("stage1")
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                fade.fade_out("title")

def Draw():
    background.Draw()
    ground.clip_draw(0, 0, 1024, 252, WIDTH // 2, 200, 1200, 250)
    black.clip_draw(0, 0, 1200, 800, WIDTH // 2, -50, 1200, 250)
    for c in chars:
        c.Draw()
    dungeon_button.clip_draw(0, 0, 306, 90, 1080, 70, 200, 60)
    friend_button.clip_draw(0, 0, 131, 87, 110, 70, 160, 80)
    shop_button.clip_draw(0, 0, 131, 87, 310, 70, 160, 80)
    upgrade_button.clip_draw(0, 0, 131, 87, 510, 70, 160, 80)
    ui.draw()