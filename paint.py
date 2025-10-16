import gamemanager
import start
import speedbar
import battle
from pico2d import *


def DrawAll(dt):
    gamemanager.clear_canvas()

    if gamemanager.nowScene == "start":
        start.Draw()
    else:
        if gamemanager.nowScene in "stage1_ready" or "battle":    #나중에 다른 stage도 or로 추가
            if not battle.turnSkillUsed:
                gamemanager.nowstage.Draw() #스테이지 배경 그리기
                for c in gamemanager.party: #아군 그리기
                    c.Draw()
                for e in gamemanager.enemy: #적 그리기
                    e.Draw()
                speedbar.Draw()
                HpUi_draw()
                if not battle.nowTurn == -1:
                    if battle.nowTurn < 4:
                        gamemanager.party[battle.nowTurn].Draw_turn()
                    else:
                        gamemanager.enemy[battle.nowTurn-4].Draw_turn()
                    skill_inform_draw()
            elif battle.turnSkillUsed:
                skill_cut()

    gamemanager.update_canvas()

def skill_cut(dt=None):
    if battle.turnSkillUsed:
        black = load_image('source\\background\\black.png')
        black.clip_draw(0, 0, 1200, 800, gamemanager.WIDTH // 2, gamemanager.HEIGHT // 2)
        if battle.nowTurn < 4:
            gamemanager.party[battle.nowTurn].Draw()
            if not len(battle.target) == 0:
                for t in battle.target:
                    t.Draw()
            if not gamemanager.party[battle.nowTurn].attackMotionEnd:
                for c in gamemanager.party[battle.nowTurn].skill:
                    c.Draw()
            gamemanager.party[battle.nowTurn].Draw_turn()
        else:
            gamemanager.party[battle.nowTurn-4].Draw()
            if not len(battle.target) == 0:
                for t in battle.target:
                    t.Draw()
            if not gamemanager.enemy[battle.nowTurn - 4].attackMotionEnd:
                for c in gamemanager.enemy[battle.nowTurn - 4].skill:
                    c.Draw()
            gamemanager.enemy[battle.nowTurn - 4].Draw_turn()

def skill_inform_draw():
    informBox = load_image('source\\ui\\choice_box.png')
    if battle.skillInform == "skill_1":
        informBox.clip_draw(0, 0, 88, 88, 850, 100, 110, 110)
    elif battle.skillInform == "skill_2":
        informBox.clip_draw(0, 0, 88, 88, 975, 100, 110, 110)
    elif battle.skillInform == "skill_3":
        informBox.clip_draw(0, 0, 88, 88, 1100, 100, 110, 110)

hp_font = load_font('source\\ui\\DungGeunMo.ttf',25)
def HpUi_draw():
    if gamemanager.nowScene == "battle":
        for n in speedbar.spdNums:
            if speedbar.spdNums.index(n) < 4:
                n.image.clip_draw(0, 0, 100, 100, 380, 180-(50*speedbar.spdNums.index(n)), 20, 20)
                hp_font.draw(400,180-(50*speedbar.spdNums.index(n)),
                    f'{gamemanager.party[speedbar.spdNums.index(n)].status["nowhp"]}/{gamemanager.party[speedbar.spdNums.index(n)].status["maxhp"]}', (220, 220, 220))
            else:
                n.image.clip_draw(0, 0, 100, 100, 580, 180-(50*(speedbar.spdNums.index(n)-4)), 20, 20)
                hp_font.draw(600,180-(50*(speedbar.spdNums.index(n)-4)),
                    f'{gamemanager.enemy[speedbar.spdNums.index(n)-4].status["nowhp"]}/{gamemanager.enemy[speedbar.spdNums.index(n)-4].status["maxhp"]}', (220, 220, 220))