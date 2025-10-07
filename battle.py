# 여기 stage에서 ready 끝나면 gamemanager에서 battle.update로 바꿀거임
# 어떤 stage가 와도 같은 방식으로 작동하도록 구현해야함
from pico2d import *
import speedbar
import gamemanager
from gamemanager import WIDTH, HEIGHT
import random

nowTurn = -1  # -1이면 스피드바 진행, 0~3이면 아군 턴, 4~7이면 적군 턴
turnSkillUsed = False # 턴이 시작되고 스킬을 사용중인 걸 판단
target = None

def Update(dt):
    global nowTurn, turnSkillUsed,target

    if nowTurn == -1:
        speedbar.Update(dt)
        turnSkillUsed = False
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
                        nowChar.state = "skill_1"
                        nowChar.Skill_1()
                        turnSkillUsed = True
                    elif (925 <= mx <= 1025 and 50 <= my <= 150):
                        nowChar.state = "skill_2"
                        nowChar.Skill_2()
                        turnSkillUsed = True
                    elif (1050 <= mx <= 1150 and 50 <= my <= 150):
                        nowChar.state = "skill_3"
                        nowChar.Skill_3()
                        turnSkillUsed = True
                    nowChar.frameTimer = 0.0

        if target == None:
            if nowChar.flip:  # 적군 턴
                target = random.choice(gamemanager.party)
            else:  # 아군 턴
                target = random.choice(gamemanager.enemy)

        if not len(nowChar.skill) == 0 and not nowChar.attackMotionEnd:
            for p in nowChar.skill[::-1]:
                p.Update(dt,target.x,target.y)
                if not p.visible:
                    nowChar.skill.remove(p)
                if len(nowChar.skill) == 0:
                    nowChar.state = "idle"
                    nowChar.frame = 0

        if len(nowChar.skill) == 0 and nowChar.state == "idle" and turnSkillUsed:
            speedbar.spdNums[nowTurn].x = 1000
            nowTurn = -1
            target = None