from pico2d import *
import gamemanager
from scene_folder.background_base import BackGround
from characters import Characters
import ui
import fade
import currency
import random
import sound

get_stack = []
get_event = False #뽑기 이벤트 위한 변수
old_anime = None
new_anime = None
is_event = False #진화 이벤트 위한 변수

def Reset():
    global shop_bg_bg, shop_bg, result_bg, new_char, arrow, evo_max, get_gem
    shop_bg_bg = BackGround(load_image('source\\background\\bg_home_morning.png'),gamemanager.WIDTH/2,gamemanager.HEIGHT/2,1024,800)
    shop_bg = load_image('source\\background\\shop_bg.png')
    result_bg = load_image('source\\background\\shop_result_bg.png')
    new_char = load_image('source\\background\\new_char_get.png')
    arrow = load_image('source\\background\\shop_evo_change.png')
    evo_max = load_image('source\\background\\shop_evo_max.png')
    get_gem = load_image('source\\background\\shop_get_gem.png')

def Update(dt):
    global shop_bg_bg, shop_bg
    shop_bg_bg.Move(-10 * dt)
    handle_events()
    pass

def handle_events():
    global get_event, get_stack, old_anime, new_anime, is_event

    events = get_events()
    for event in events:
        if get_event == False:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                fade.fade_out("home")
            if event.type == SDL_MOUSEBUTTONDOWN:
                mx, my = event.x, gamemanager.HEIGHT - event.y
                if 700 <= mx <= 900 and 40 <= my <= 90 and currency.ticket.quantity >= 1:
                    currency.ticket.quantity -= 1
                    get_stack.append(random.randint(1,150))
                    get_event = True
                elif 940 <= mx <= 1140 and 40 <= my <= 90 and currency.ticket.quantity >= 10:
                    currency.ticket.quantity -= 10
                    for _ in range(10):
                        get_stack.append(random.randint(1, 150))
                    get_event = True
        elif get_event == True:
            if event.type == SDL_MOUSEBUTTONDOWN:
                if get_stack != []:
                    if get_stack[0] <= 15:
                        if Characters[get_stack[0] - 1].get == False:
                            Characters[get_stack[0] - 1].get = True
                    get_stack.pop(0)
                    is_event = False
                    old_anime = None
                    new_anime = None
                    if get_stack == []:
                        get_event = False

def Draw():
    global get_stack, new_char, old_anime, new_anime, is_event, evo_max, get_gem
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
                    if Characters[get_stack[0]-1].evo < 4:
                        if old_anime == None:
                            old_anime = Characters[get_stack[0]-1].anime[0][0]
                        if is_event == False:
                            Characters[get_stack[0]-1].evolution()
                            is_event = True
                        if new_anime == None:
                            new_anime = Characters[get_stack[0]-1].anime[0][1]
                        arrow.clip_draw(0,0,arrow.w,arrow.h,gamemanager.WIDTH/2,gamemanager.HEIGHT/2, gamemanager.WIDTH,gamemanager.HEIGHT)
                        old_anime.clip_draw(0, 0, old_anime.w, old_anime.h, 900, gamemanager.HEIGHT/2 + 150, 200, 200)
                        new_anime.clip_draw(0, 0, new_anime.w, new_anime.h, 900, gamemanager.HEIGHT/2 - 150, 200, 200)
                    elif Characters[get_stack[0]-1].evo >= 4:
                        evo_max.clip_draw(0,0,evo_max.w,evo_max.h,gamemanager.WIDTH/2,gamemanager.HEIGHT/2, gamemanager.WIDTH,gamemanager.HEIGHT)
                        if is_event == False:
                            currency.ticket.quantity += 10
                            is_event = True
            else:
                get_gem.clip_draw(0,0,get_gem.w,get_gem.h,gamemanager.WIDTH/2,gamemanager.HEIGHT/2, gamemanager.WIDTH,gamemanager.HEIGHT)
                if is_event == False:
                    currency.upgrade_stone.quantity += 1
                    is_event = True
