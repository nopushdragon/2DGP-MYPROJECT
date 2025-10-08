# 여기 stage에서 ready 끝나면 gamemanager에서 battle.update로 바꿀거임
# 어떤 stage가 와도 같은 방식으로 작동하도록 구현해야함
from pico2d import *
import speedbar
import gamemanager
from gamemanager import WIDTH, HEIGHT
import random

nowTurn = -1  # -1이면 스피드바 진행, 0~3이면 아군 턴, 4~7이면 적군 턴
turnSkillUsed = False # 턴이 시작되고 스킬을 사용중인 걸 판단
skillInform = None # 스킬 마우스로 1번 클릭하면 스킬 설명, 2번 클릭하면 스킬 사용하게끔 해줌
target = [] # 스킬 대상인데 사실상 단일 스킬에만 쓰일 듯.
damageAnimation = False # 데미지

def Update(dt):
    global nowTurn, turnSkillUsed,target, skillInform, skillBuffer

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
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEBUTTONDOWN:
                    mx, my = event.x, HEIGHT - event.y
                    print(mx, my)
                    if (800 <= mx <= 900 and 50 <= my <= 150):
                        if skillInform == "skill_1":
                            nowChar.state = "skill_1"
                            nowChar.Skill_1()
                            turnSkillUsed = True
                            nowChar.frameTimer = 0.0
                        else:
                            skillInform = "skill_1"
                    elif (925 <= mx <= 1025 and 50 <= my <= 150):
                        if skillInform == "skill_2":
                            nowChar.state = "skill_2"
                            nowChar.Skill_2()
                            turnSkillUsed = True
                            nowChar.frameTimer = 0.0
                        else:
                            skillInform = "skill_2"
                    elif (1050 <= mx <= 1150 and 50 <= my <= 150):
                        if skillInform == "skill_3":
                            nowChar.state = "skill_3"
                            nowChar.Skill_3()
                            turnSkillUsed = True
                            nowChar.frameTimer = 0.0
                        else:
                            skillInform = "skill_3"

        if len(target) == 0:
            if nowChar.flip:  # 적군 턴
                if nowChar.skill and nowChar.skill[0].type == "enemy_solo":
                    target = [random.choice(gamemanager.party)]
                elif nowChar.skill and nowChar.skill[0].type == "enemy_all":
                    target = gamemanager.party[:]
                elif nowChar.skill and nowChar.skill[0].type == "party_solo":
                    target = [random.choice(gamemanager.enemy)]
                elif nowChar.skill and nowChar.skill[0].type == "party_all":
                    target = gamemanager.enemy[:]
            else:  # 아군 턴
                if nowChar.skill and nowChar.skill[0].type == "enemy_solo":
                    target = [random.choice(gamemanager.enemy)]
                elif nowChar.skill and nowChar.skill[0].type == "enemy_all":
                    target = gamemanager.enemy[:]
                elif nowChar.skill and nowChar.skill[0].type == "party_solo":
                    target = [random.choice(gamemanager.party)]
                elif nowChar.skill and nowChar.skill[0].type == "party_all":
                    target = gamemanager.party[:]

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