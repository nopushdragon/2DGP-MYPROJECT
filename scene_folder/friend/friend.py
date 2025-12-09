from pico2d import *
import ui
from gamemanager import WIDTH, HEIGHT
from scene_folder.background_base import BackGround
from characters import Characters
import fade
import sound

bbackground = BackGround(load_image('source\\background\\bg_home_morning.png'),WIDTH/2,HEIGHT/2,1024,800)
background = BackGround(load_image('source\\background\\bg_friend.png'),WIDTH/2,HEIGHT/2,1024,800)
unknown = load_image('source\\character\\unknown.png')
choice_box = load_image('source\\ui\\choice_box.png')
card = load_image('source\\ui\\card.png')
card_char_bg = load_image('source\\ui\\card_char_bg.png')
card_char = load_image('source\\ui\\card_char.png')
nameBox = load_image('source\\ui\\namebox.png')
font = load_font('source\\ui\\DungGeunMo.ttf', 40)

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
    choice_char_draw()
    ui.draw()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            cnt = 0
            global choiceChar
            for cnt, c in enumerate(Characters):
                col = cnt % 3
                row = cnt // 3
                # 화면에 표시되는 최대 행(0..4)만 처리
                if row >= 5:
                    continue

                # draw에서 사용한 중심 좌표와 크기에 맞춤
                center_x = col * 160 + 800  # 기존 draw: cnt * 160 + 800
                center_y = 600 - row * 100  # 기존 draw: 600,500,400,300,200
                half_w = 50  # draw에서 사용한 폭 100 -> 반폭 50
                half_h = 50  # draw에서 사용한 높이 100 -> 반높이 50

                if center_x - half_w <= mx <= center_x + half_w and center_y - half_h <= my <= center_y + half_h:
                    sound.click_sound.play(1)
                    if choiceChar == cnt:
                        choiceChar = None
                    else:
                        if c.get == True:
                            choiceChar = cnt
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                fade.fade_out("home")

def char_draw():
    card.clip_draw(0,0,375,496,WIDTH - 250, HEIGHT/2, 500, 800)
    card_char_bg.clip_draw(0,0,470,699,350, HEIGHT/2, 700, 800)
    card_char.clip_draw(0,0,375,496,WIDTH - 250, HEIGHT/2, 500, 800)
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

def choice_char_draw():
    global choiceChar
    if choiceChar != None:
        Characters[choiceChar].illust.clip_draw(0,0,Characters[choiceChar].illust.w,Characters[choiceChar].illust.h,200,570,300,400)
        nameBox.clip_draw(0,0,nameBox.w,nameBox.h,200,400,300,50)
        font.draw(150, 399, Characters[choiceChar].name, (0, 0, 0))
        font.draw(150, 401, Characters[choiceChar].name, (0, 0, 0))
        font.draw(149, 400, Characters[choiceChar].name, (0, 0, 0))
        font.draw(151, 400, Characters[choiceChar].name, (0, 0, 0))
        font.draw(150, 400, Characters[choiceChar].name, (230, 230, 230))
        font.draw(475, 700, '능력치', (255, 255, 255))
        font.draw(450, 600, f'체력: {Characters[choiceChar].status["maxhp"]}', (230, 230, 230))
        font.draw(450, 550, f'공격력: {Characters[choiceChar].status["origin_atk"]}', (230, 230, 230))
        font.draw(450, 500, f'방어력: {Characters[choiceChar].status["origin_def"]}', (230, 230, 230))
        font.draw(450, 450, f'속도: {Characters[choiceChar].status["origin_speed"]}', (230, 230, 230))
        if Characters[choiceChar].skill_1_icon != None:
            Characters[choiceChar].skill_1_icon.clip_draw(0,0,Characters[choiceChar].skill_1_icon.w,Characters[choiceChar].skill_1_icon.h,150,200,150,150)
        if Characters[choiceChar].skill_2_icon != None:
            Characters[choiceChar].skill_2_icon.clip_draw(0,0,Characters[choiceChar].skill_2_icon.w,Characters[choiceChar].skill_2_icon.h,350,200,150,150)
        if Characters[choiceChar].skill_3_icon != None:
            Characters[choiceChar].skill_3_icon.clip_draw(0,0,Characters[choiceChar].skill_3_icon.w,Characters[choiceChar].skill_3_icon.h,550,200,150,150)