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
            gamemanager.nowstage.Draw()
            for c in gamemanager.party: #아군 그리기
                c.Draw(dt)
            for e in gamemanager.enemy: #적 그리기
                e.Draw(dt)
            speedbar.Draw()
            skill_cut(dt)
            if not battle.nowTurn == -1:
                gamemanager.party[battle.nowTurn].Draw_Icon()

    gamemanager.update_canvas()

def skill_cut(dt):
    if battle.turnSkillUsed:
        balck = load_image('source\\background\\black.png')
        balck.clip_draw(0, 0, 1200, 800, gamemanager.WIDTH // 2, gamemanager.HEIGHT // 2)
        if battle.nowTurn < 4:
            gamemanager.party[battle.nowTurn].Draw(dt)
            if gamemanager.party[battle.nowTurn].skill and gamemanager.party[battle.nowTurn].skill[0].type == "enemy_solo":
                if battle.target is not None:
                    battle.target.Draw(dt)
            elif gamemanager.party[battle.nowTurn].skill and gamemanager.party[battle.nowTurn].skill[0].type == "party_solo":
                if battle.target is not None:
                    battle.target.Draw(dt)
            elif gamemanager.party[battle.nowTurn].skill and gamemanager.party[battle.nowTurn].skill[0].type == "enemy_all":
                for e in gamemanager.enemy:
                    e.Draw(dt)
            elif gamemanager.party[battle.nowTurn].skill and gamemanager.party[battle.nowTurn].skill[0].type == "party_all":
                for c in gamemanager.party:
                    c.Draw(dt)

            if not gamemanager.party[battle.nowTurn].attackMotionEnd:
                for c in gamemanager.party[battle.nowTurn].skill:
                    c.Draw()
        else:
            if gamemanager.enemy[battle.nowTurn - 4].skill and gamemanager.enemy[battle.nowTurn - 4].skill[0].type == "enemy_solo":
                gamemanager.enemy[battle.nowTurn - 4].Draw(dt)
                if battle.target is not None:
                    battle.target.Draw(dt)
            elif gamemanager.enemy[battle.nowTurn - 4].skill and gamemanager.enemy[battle.nowTurn - 4].skill[0].type == "party_solo":
                gamemanager.enemy[battle.nowTurn - 4].Draw(dt)
                if battle.target is not None:
                    battle.target.Draw(dt)
            elif gamemanager.enemy[battle.nowTurn - 4].skill and gamemanager.enemy[battle.nowTurn - 4].skill[0].type == "enemy_all":
                gamemanager.enemy[battle.nowTurn - 4].Draw(dt)
                for c in gamemanager.party:
                    c.Draw(dt)
            elif gamemanager.enemy[battle.nowTurn - 4].skill and gamemanager.enemy[battle.nowTurn - 4].skill[0].type == "party_all":
                gamemanager.enemy[battle.nowTurn - 4].Draw(dt)
                for e in gamemanager.enemy:
                    e.Draw(dt)

            if not gamemanager.enemy[battle.nowTurn - 4].attackMotionEnd:
                for c in gamemanager.enemy[battle.nowTurn - 4].skill:
                    c.Draw()