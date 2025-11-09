from pico2d import *
import ui
from gamemanager import WIDTH, HEIGHT
from scene_folder.background_base import BackGround
from characters import Characters
import fade

bbackground = BackGround(load_image('source\\background\\bg_home_morning.png'),WIDTH/2,HEIGHT/2,1024,800)
background = BackGround(load_image('source\\background\\bg_friend.png'),WIDTH/2,HEIGHT/2,1024,800)
unknown = load_image('source\\character\\unknown.png')
choice_box = load_image('source\\ui\\choice_box.png')
card = load_image('source\\ui\\card.png')

choiceChar = None

def Reset():
    global choiceChar
    choiceChar = None

def Update(dt):
    bbackground.Move(-10 * dt)
    handle_events()

def Draw():
    bbackground.Draw()
    background.Draw()
    char_draw()
    ui.draw()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            cnt = 0
            for _ in Characters:
                if ((cnt < 3 and cnt * 160 + 750 <= mx <= cnt * 160 + 850 and 550 <= my <= 650) or
                        (cnt < 6 and (cnt - 3) * 160 + 750 <= mx <= (cnt - 3) * 160 + 850 and 450 <= my <= 550)or
                        (cnt < 9 and (cnt - 6) * 160 + 750 <= mx <= (cnt - 6) * 160 + 850 and 350 <= my <= 450)or
                        (cnt < 12 and (cnt - 9) * 160 + 750 <= mx <= (cnt - 9) * 160 + 850 and 250 <= my <= 350)or
                        (cnt < 15 and (cnt - 12) * 160 + 750 <= mx <= (cnt - 12) * 160 + 850 and 150 <= my <= 250)):
                    global choiceChar
                    if choiceChar == cnt:
                        choiceChar = None
                    else:
                        if (Characters[cnt].get == True):
                            choiceChar = cnt
                cnt += 1
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                fade.fade_out("home")

def char_draw():
    card.clip_draw(0,0,375,496,WIDTH - 250, HEIGHT/2, 500, 800)
    cnt = 0
    for c in Characters:  # 캐릭터 선택창
        if cnt < 3:
            if (c.get == False):
                unknown.clip_draw(0, 0, 70, 80, cnt * 160 + 800, 590, 70, 80)
            else:
                c.anime[0][0].clip_draw(0, 0, 100, 100, cnt * 160 + 800, 600, 100, 100)
        elif cnt < 6:
            if (c.get == False):
                unknown.clip_draw(0, 0, 70, 80, (cnt - 3) * 160 + 800, 490, 70, 80)
            else:
                c.anime[0][0].clip_draw(0, 0, 100, 100, (cnt - 3) * 160 + 800, 500, 100, 100)
        elif cnt < 9:
            if (c.get == False):
                unknown.clip_draw(0, 0, 70, 80, (cnt - 6) * 160 + 800, 390, 70, 80)
            else:
                c.anime[0][0].clip_draw(0, 0, 100, 100, (cnt - 6) * 160 + 800, 400, 100, 100)
        elif cnt < 12:
            if (c.get == False):
                unknown.clip_draw(0, 0, 70, 80, (cnt - 9) * 160 + 800, 290, 70, 80)
            else:
                c.anime[0][0].clip_draw(0, 0, 100, 100, (cnt - 9) * 160 + 800, 300, 100, 100)
        else:
            if (c.get == False):
                unknown.clip_draw(0, 0, 70, 80, (cnt - 12) * 160 + 800, 190, 70, 80)
            else:
                c.anime[0][0].clip_draw(0, 0, 100, 100, (cnt - 12) * 160 + 800, 200, 100, 100)
        cnt += 1

    global choiceChar
    if choiceChar != None:
        Draw_choiceBox(choiceChar)

def Draw_choiceBox(n):
    if n < 3:
        choice_box.clip_draw(0, 0, 88, 88, n * 160 + 800, 590, 100, 100)
    elif n < 6:
        choice_box.clip_draw(0, 0, 88, 88, (n - 3) * 160 + 800, 490, 100, 100)
    elif n < 9:
        choice_box.clip_draw(0, 0, 88, 88, (n - 6) * 160 + 800, 390, 100, 100)
    elif n < 12:
        choice_box.clip_draw(0, 0, 88, 88, (n - 9) * 160 + 800, 290, 100, 100)
    else:
        choice_box.clip_draw(0, 0, 88, 88, (n - 12) * 160 + 800, 190, 100, 100)