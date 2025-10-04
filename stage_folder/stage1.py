import gamemanager
from gamemanager import WIDTH, HEIGHT
from pico2d import *
from background import BackGround
from stage_base import Stage
from characters import Characters

stage1 = Stage()

ground = load_image('source\\background\\stage1_ground.png')
background = BackGround(load_image('source\\background\\bg_tile_chapter_01_01.png'),WIDTH/2,HEIGHT/2,960,800)
black = load_image('source\\background\\black.png')

choiceChar = None

def UPDATE_overriding(self, dt):
    background.Move(-10 * dt)

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y
            cnt = 1
            for _ in Characters[cnt:]:
                if (cnt-1)*100+50 <= mx <= (cnt-1)*100+150 and 50 <= my <= 150:
                    #gamemanager.party.append(c)
                    global choiceChar
                    if choiceChar == cnt:
                        choiceChar = None
                    else:
                        choiceChar = cnt
                cnt += 1
            for i in gamemanager.partylocate:
                if (i[0]-50 <= mx <= i[0]+50 and i[1]-50 <= my <= i[1]+50) and i[0] != 100:
                    if choiceChar != None:
                        Characters[choiceChar].x = i[0]
                        Characters[choiceChar].y = i[1]
                        gamemanager.party = [c for c in gamemanager.party if not (c.x == i[0] and c.y == i[1])]
                        if Characters[choiceChar] in gamemanager.party:
                            gamemanager.party.remove(Characters[choiceChar])
                        gamemanager.party.append(Characters[choiceChar])
                        choiceChar = None

stage1.Update = UPDATE_overriding.__get__(stage1, Stage)

def Draw_overriding(self):
    background.Draw()
    ground.clip_draw(0, 0, 1024, 252, WIDTH // 2, 300,1200,250)
    black.clip_draw(0, 0, 1200, 800, WIDTH // 2, 50,1200,250)
    cnt = 1
    for c in Characters[cnt:]:
        c.anime[0][0].clip_draw(0,0,100,100,(cnt-1)*100+100,100,100,100)
        cnt += 1
    global choiceChar
    if choiceChar != None:
        Draw_choice(choiceChar)

stage1.Draw = Draw_overriding.__get__(stage1, Stage)

def Draw_choice(n):
    choice_box = load_image('source\\ui\\choice_box.png')
    choice_box.clip_draw(0, 0, 88, 88, (n-1)*100+100, 90, 100, 100)
