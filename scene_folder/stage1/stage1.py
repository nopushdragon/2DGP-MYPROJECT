import gamemanager
from .. import speedbar
from gamemanager import WIDTH, HEIGHT
from pico2d import *
from scene_folder.background_base import BackGround
from scene_folder.stage_base import Stage
from characters import Characters
import fade
import currency
import sound
import random

from .stage1_enemys import enemys

stage1 = Stage()

ground = load_image('source\\background\\stage1_ground.png')
#background = BackGround(load_image('source\\background\\bg_tile_chapter_01_01.png'),WIDTH/2,HEIGHT/2,960,800)
background = BackGround(load_image('source\\background\\bg_home_morning.png'),WIDTH/2,HEIGHT/2,1024,800)
black = load_image('source\\background\\black.png')
unknown = load_image('source\\character\\unknown.png')
choice_box = load_image('source\\ui\\choice_box.png')
battleBox_off = load_image('source\\ui\\mainmenu_0003_mainmenuEN2-copy.png')
battleBox_on = load_image('source\\ui\\mainmenu_0004_mainmenuEN2.png')
choiceChar = None

def Reset(self):
    self.ticket = 10
    self.upgrade_stone = 50
    global choiceChar
    choiceChar = None
    import gamemanager
    gamemanager.party = gamemanager.party[:1]
    gamemanager.party[0].x = gamemanager.partylocate[0][0]
    gamemanager.party[0].y = gamemanager.partylocate[0][1]
    gamemanager.enemy.clear()
    enemy_random_idx = random.sample(range(len(enemys)), 4)
    cnt = 0
    for e in enemy_random_idx:
        gamemanager.enemy.append(enemys[e])
        enemys[e].x = gamemanager.enemylocate[cnt][0]
        enemys[e].y = gamemanager.enemylocate[cnt][1]
        enemys[e].reset()
        cnt += 1


# Bind Reset as an instance method so Stage instances have Reset()
stage1.Reset = Reset.__get__(stage1, Stage)

def UPDATE_overriding(self, dt):
    background.Move(-10 * dt)

    if not gamemanager.nowScene == "battle":
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                mx, my = event.x, HEIGHT - event.y
                cnt = 1
                for _ in Characters[cnt:]:
                    if (cnt < 8 and (cnt-1)*100+50 <= mx <= (cnt-1)*100+150 and 120 <= my <= 220) or (cnt >= 8 and (cnt-8)*100+50 <= mx <= (cnt-8)*100+150 and 20 <= my <= 120):
                        global choiceChar
                        if choiceChar == cnt:
                            choiceChar = None
                        else:
                            if(Characters[cnt].get == True):
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
                if(1100 - 75 <= mx <= 1100 + 75 and 100 - 75 <= my <= 100 + 75):
                    if len(gamemanager.party) == 4:
                        Ready()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                sound.play_main_bgm()
                fade.fade_out("home")
stage1.Update = UPDATE_overriding.__get__(stage1, Stage)

def Draw_background_overriding(self):
    background.Draw()
    ground.clip_draw(0, 0, 1024, 252, WIDTH // 2, 300,1200,250)
    black.clip_draw(0, 0, 1200, 800, WIDTH // 2, 50,1200,250)
stage1.Draw_background = Draw_background_overriding.__get__(stage1, Stage)

def Draw_choicechar_overriding(self):
    cnt = 1
    for c in Characters[cnt:]:# 캐릭터 선택창
        if cnt < 8:
            if(c.get == False): unknown.clip_draw(0,0,70,80,(cnt-1)*100+100,160,70,80)
            else: c.anime[0][0].clip_draw(0,0,100,100,(cnt-1)*100+100,170,100,100)
        else:
            if (c.get == False): unknown.clip_draw(0,0,70,80,(cnt-8)*100+100,60,70,80)
            else: c.anime[1][0].clip_draw(0,0,100,100,(cnt-8)*100+100,70,100,100)
        cnt += 1

    global choiceChar   # 선택된 캐릭터 테두리
    if choiceChar != None:
        Draw_choiceBox(choiceChar)
    if len(gamemanager.party) < 4:
        battleBox_off.clip_draw(0, 0, 82, 82, 1100, 100, 150, 150)
    else:
        battleBox_on.clip_draw(0, 0, 82, 82, 1100, 100, 150, 150)
stage1.Draw_choicechar = Draw_choicechar_overriding.__get__(stage1, Stage)

def Draw_choiceBox(n):
    if n < 8:
        choice_box.clip_draw(0, 0, 88, 88, (n-1)*100+100, 160, 100, 100)
    else:
        choice_box.clip_draw(0, 0, 88, 88, (n-8)*100+100, 60, 100, 100)

def Ready():
    gamemanager.nowScene = "battle"
    sound.fight_start_sound.play(1)

    new_party = []  #party와 partylocate 순서 맞추기
    for loc in gamemanager.partylocate:
        found = None
        for c in gamemanager.party:
            if (c.x, c.y) == loc:
                found = c
                break
        new_party.append(found)
    gamemanager.party = new_party

    for p in gamemanager.party:
        p.reset()

    # 게임 완료하면 speedbar에 spdNum의 speed 바에 각 캐릭터에 맞는 speed 넣어줌
    cnt = 0
    for n in gamemanager.party:
        speedbar.spdNums[cnt].speed = gamemanager.party[cnt].status["speed"]
        cnt += 1
    for n in gamemanager.enemy:
        speedbar.spdNums[cnt].speed = gamemanager.enemy[cnt - 4].status["speed"]
        cnt += 1