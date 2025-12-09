# 여기 stage에서 ready 끝나면 gamemanager에서 battle.update로 바꿀거임
# 어떤 stage가 와도 같은 방식으로 작동하도록 구현해야함
from pico2d import *
from scene_folder import speedbar
import gamemanager
from gamemanager import WIDTH, HEIGHT
import random
import fade

battle_state = None #None: 배틀중, "win": 승리화면, "lose": 패배화면
#lose_image = load_image(None)
#win_image = load_image(None)
rewards_font = load_font('source\\ui\\DungGeunMo.ttf', 40)

nowTurn = -1  # -1이면 스피드바 진행, 0~3이면 아군 턴, 4~7이면 적군 턴
turnSkillUsed = False # 턴이 시작되고 스킬을 사용중인 걸 판단
skillInform = None # 스킬 마우스로 1번 클릭하면 스킬 설명, 2번 클릭하면 스킬 사용하게끔 해줌
target = [] # 스킬 대상인데 사실상 단일 스킬에만 쓰일 듯.
damageAnimation = False # 데미지
nowChar = None

def Reset():
    global nowTurn, turnSkillUsed, target, skillInform, damageAnimation, battle_state,nowChar
    battle_state = None
    nowTurn = -1
    turnSkillUsed = False
    target.clear()
    skillInform = None
    damageAnimation = False
    speedbar.Reset()
    nowChar = None

def Update(dt):
    global nowTurn, turnSkillUsed,target, skillInform, battle_state,nowChar
    events = get_events()
    do_events()

    if battle_state == None: battle_state = game_end() #게임 끝 판단

    if battle_state == None:
        if nowTurn == -1:
            speedbar.Update(dt)
            turnSkillUsed = False
            skillInform = None
        else:
            if nowTurn < 4:
                nowChar = gamemanager.party[nowTurn]
            else:
                nowChar = gamemanager.enemy[nowTurn - 4]

            if not turnSkillUsed:
                if nowTurn < 4:  # 아군 턴
                    for event in events:
                        if event.type == SDL_MOUSEBUTTONDOWN:
                            mx, my = event.x, HEIGHT - event.y
                            print(mx, my)
                            if (800 <= mx <= 900 and 50 <= my <= 150):
                                if skillInform == "skill_1":
                                    nowChar.state = "skill_1"
                                    nowChar.Skill_1()
                                    nowChar.frame = 0
                                    nowChar.frameTimer = 0.0
                                    nowChar.attackMotionEnd = False
                                    nowChar.attackMotionEndTimer = 0.0
                                    turnSkillUsed = True
                                    skillInform = None
                                else:
                                    skillInform = "skill_1"
                            elif (925 <= mx <= 1025 and 50 <= my <= 150):
                                if skillInform == "skill_2":
                                    nowChar.state = "skill_2"
                                    nowChar.Skill_2()
                                    nowChar.frame = 0
                                    nowChar.frameTimer = 0.0
                                    nowChar.attackMotionEnd = False
                                    nowChar.attackMotionEndTimer = 0.0
                                    turnSkillUsed = True
                                    skillInform = None
                                else:
                                    skillInform = "skill_2"
                            elif (1050 <= mx <= 1150 and 50 <= my <= 150):
                                if skillInform == "skill_3":
                                    nowChar.state = "skill_3"
                                    nowChar.Skill_3()
                                    nowChar.frame = 0
                                    nowChar.frameTimer = 0.0
                                    nowChar.attackMotionEnd = False
                                    nowChar.attackMotionEndTimer = 0.0
                                    turnSkillUsed = True
                                    skillInform = None
                                else:
                                    skillInform = "skill_3"
                else:
                    rd_skill = random.randint(1,3)
                    if rd_skill == 1:
                        nowChar.state = "skill_1"
                        nowChar.Skill_1()
                    elif rd_skill == 2:
                        nowChar.state = "skill_2"
                        nowChar.Skill_2()
                    elif rd_skill == 3:
                        nowChar.state = "skill_3"
                        nowChar.Skill_3()

                    nowChar.frame = 0
                    nowChar.frameTimer = 0.0
                    nowChar.attackMotionEnd = False
                    nowChar.attackMotionEndTimer = 0.0
                    turnSkillUsed = True
                    skillInform = None

            if len(target) == 0:
                if nowChar.flip:  # 적군 턴
                    if nowChar.skill and nowChar.skill[0].type == "enemy_solo":
                        target = [random.choice(gamemanager.party)]
                        while not target[0].status["nowhp"] > 0:
                            target = [random.choice(gamemanager.party)]
                    elif nowChar.skill and nowChar.skill[0].type == "enemy_all":
                        target = [p for p in gamemanager.party if p.status["nowhp"] > 0]
                    elif nowChar.skill and nowChar.skill[0].type == "party_solo":
                        target = [random.choice(gamemanager.enemy)]
                        while not target[0].status["nowhp"] > 0:
                            target = [random.choice(gamemanager.enemy)]
                    elif nowChar.skill and nowChar.skill[0].type == "party_all":
                        target = [e for e in gamemanager.enemy if e.status["nowhp"] > 0]
                else:  # 아군 턴
                    if nowChar.skill and nowChar.skill[0].type == "enemy_solo":
                        target = [random.choice(gamemanager.enemy)]
                        while not target[0].status["nowhp"] > 0:
                            target = [random.choice(gamemanager.enemy)]
                    elif nowChar.skill and nowChar.skill[0].type == "enemy_all":
                        target = [e for e in gamemanager.enemy if e.status["nowhp"] > 0]
                    elif nowChar.skill and nowChar.skill[0].type == "party_solo":
                        target = [random.choice(gamemanager.party)]
                        while not target[0].status["nowhp"] > 0:
                            target = [random.choice(gamemanager.party)]
                    elif nowChar.skill and nowChar.skill[0].type == "party_all":
                        target = [p for p in gamemanager.party if p.status["nowhp"] > 0]

            if nowChar.skill and not nowChar.attackMotionEnd:
                for p in nowChar.skill[::-1]:
                    if not len(target) == 0:
                        if p.type in ["enemy_solo", "party_solo"]:
                            p.Update(dt, target[0].x, target[0].y)
                        elif p.type in ["enemy_all", "party_all"]:
                            avg_x = sum(t.x for t in target) / len(target)
                            avg_y = sum(t.y for t in target) / len(target)
                            p.Update(dt, avg_x, avg_y)
                        else:
                            p.Update(dt, target[0].x, target[0].y)
                    if not p.visible:
                        nowChar.skill[0].apply_effect(target,nowChar.status["atk"])
                        nowChar.skill.remove(p)
                    if len(nowChar.skill) == 0:
                        nowChar.state = "idle"
                        nowChar.frame = 0

            if len(nowChar.skill) == 0 and nowChar.state == "idle" and turnSkillUsed:
                speedbar.spdNums[nowTurn].x = 1000
                nowTurn = -1
                target.clear()
                nowChar = None

def do_events():
    for event in get_events():
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE: #esc
            fade.fade_out("home")

def game_end():
    end_flag = True
    for c in gamemanager.party:  # 패배
        if c.status["nowhp"] > 0:
            end_flag = False
    if end_flag == True:
        return "lose"

    end_flag = True
    for e in gamemanager.enemy:  # 승리
        if e.status["nowhp"] > 0:
            end_flag = False
    if end_flag == True:
        gamemanager.nowstage[0].get_rewards()
        return "win"

    return None #싸우는 중

def lose_draw():
    #lose_image.clip_draw(0,0,lose_image.w,lose_image.h, WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)
    pass

def win_draw():
    #win_image.clip_draw(0, 0, lose_image.w, lose_image.h, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    rewards_font.draw(0,0, f"+ {gamemanager.nowstage[0].ticket}",(0,0,0))
    rewards_font.draw(0,0, f"+ {gamemanager.nowstage[0].upgrade_stone}",(0,0,0))
    pass