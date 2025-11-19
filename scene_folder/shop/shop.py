from pico2d import *
import gamemanager
from scene_folder.background_base import BackGround
from characters import Characters
import ui
import fade
import currency
import random

get_stack = []
get_event = False

def Reset():
    global shop_bg_bg, shop_bg, result_bg, new_char
    shop_bg_bg = BackGround(load_image('source\\background\\bg_home_morning.png'),gamemanager.WIDTH/2,gamemanager.HEIGHT/2,1024,800)
    shop_bg = load_image('source\\background\\shop_bg.png')
    result_bg = load_image('source\\background\\shop_result_bg.png')
    new_char = load_image('source\\background\\new_char_get.png')

def Update(dt):
    global shop_bg_bg, shop_bg
    shop_bg_bg.Move(-10 * dt)
    handle_events()
    pass

def handle_events():
    global get_event, get_stack

    events = get_events()
    for event in events:
        if get_event == False:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                fade.fade_out("home")
            if event.type == SDL_MOUSEBUTTONDOWN:
                mx, my = event.x, gamemanager.HEIGHT - event.y
                if 700 <= mx <= 900 and 40 <= my <= 90 and currency.ticket.quantity >= 1:
                    currency.ticket.quantity -= 1
                    get_stack.append(random.randint(1,200))
                    get_event = True
                elif 940 <= mx <= 1140 and 40 <= my <= 90 and currency.ticket.quantity >= 10:
                    currency.ticket.quantity -= 10
                    for _ in range(10):
                        get_stack.append(random.randint(1, 200))
                    get_event = True
        elif get_event == True:
            if event.type == SDL_MOUSEBUTTONDOWN:
                if get_stack != []:
                    if get_stack[0] <= 15:
                        if Characters[get_stack[0] - 1].get == False:
                            Characters[get_stack[0] - 1].get = True
                    get_stack.pop(0)
                elif get_stack == []:
                    get_event = False

def Draw():
    global shop_bg_bg, shop_bg, result_bg, get_stack, new_char
    shop_bg_bg.Draw()
    shop_bg.clip_draw(0,0,1200,800,gamemanager.WIDTH/2,gamemanager.HEIGHT/2,gamemanager.WIDTH,gamemanager.HEIGHT)
    ui.draw()
    if get_event == True:
        result_bg.clip_draw(0,0,result_bg.w,result_bg.h,gamemanager.WIDTH/2,gamemanager.HEIGHT/2,gamemanager.WIDTH,gamemanager.HEIGHT)
        if get_stack != []:
            if get_stack[0] <= 15:
                Characters[get_stack[0]-1].illust.clip_draw(0, 0, Characters[get_stack[0]-1].illust.w, Characters[get_stack[0]-1].illust.h, 312, gamemanager.HEIGHT/2, 500, 700)
                if Characters[get_stack[0]-1].get == False:
                    new_char.clip_draw(0,0,new_char.w,new_char.h,gamemanager.WIDTH/2,gamemanager.HEIGHT/2, gamemanager.WIDTH,gamemanager.HEIGHT)
                elif Characters[get_stack[0]-1].get == True:
                    pass
