from pico2d import *
import gamemanager
from scene_folder.background_base import BackGround
import ui
import fade
import currency
import random

def Reset():
    global shop_bg_bg, shop_bg
    shop_bg_bg = BackGround(load_image('source\\background\\bg_home_morning.png'),gamemanager.WIDTH/2,gamemanager.HEIGHT/2,1024,800)
    shop_bg = load_image('source\\background\\shop_bg.png')

def Update(dt):
    global shop_bg_bg, shop_bg
    shop_bg_bg.Move(-10 * dt)
    handle_events()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            fade.fade_out("home")
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, gamemanager.HEIGHT - event.y
            if 700 <= mx <= 900 and 40 <= my <= 90 and currency.ticket.quantity >= 1:
                currency.ticket.quantity -= 1
            elif 940 <= mx <= 1140 and 40 <= my <= 90 and currency.ticket.quantity >= 10:
                currency.ticket.quantity -= 10

def Draw():
    global shop_bg_bg, shop_bg
    shop_bg_bg.Draw()
    shop_bg.clip_draw(0,0,1200,800,gamemanager.WIDTH/2,gamemanager.HEIGHT/2,gamemanager.WIDTH,gamemanager.HEIGHT)
    ui.draw()