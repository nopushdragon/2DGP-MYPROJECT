import gamemanager
import speedbar
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



def Reset():
    global choiceChar
    choiceChar = None
    gamemanager.party = gamemanager.party[:1]
    pass

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
        Draw_choiceBox(choiceChar)

stage1.Draw = Draw_overriding.__get__(stage1, Stage)

def Draw_choiceBox(n):
    choice_box = load_image('source\\ui\\choice_box.png')
    choice_box.clip_draw(0, 0, 88, 88, (n-1)*100+100, 90, 100, 100)

def ready_overriding(self):
    gamemanager.nowScene = "battle"
    gamemanager.nowstage = gamemanager.Stages[0]

    new_party = []  #party와 partylocate 순서 맞추기
    for loc in gamemanager.partylocate:
        found = None
        for c in gamemanager.party:
            if (c.x, c.y) == loc:
                found = c
                break
        new_party.append(found)
    gamemanager.party = new_party

    # 게임 완료하면 speedbar에 spdNum의 speed 바에 각 캐릭터에 맞는 speed 넣어줌
    '''cnt = 0
    for n in gamemanager.party:
        speedbar.spdNums[cnt].speed = gamemanager.party[cnt].speed
        cnt += 1
    for n in gamemanager.enemy:
        speedbar.spdNums[cnt].speed = gamemanager.enemy[cnt - 4].speed
        cnt += 1'''