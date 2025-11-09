import gamemanager
from scene_folder import title, speedbar
import battle
from pico2d import *
import fade
from scene_folder.home import home
from scene_folder.shop import shop
from scene_folder.friend import friend


hp_font = load_font('source\\ui\\DungGeunMo.ttf',15)
hp_base = load_image('source\\ui\\hp_base.png')
hp_team = load_image('source\\ui\\hp_team.png')
hp_enemy = load_image('source\\ui\\hp_enemy.png')

def DrawAll(dt):
    gamemanager.clear_canvas()

    if gamemanager.nowScene == "title":
        title.Draw()
    elif gamemanager.nowScene == "home":
        home.Draw()
    elif gamemanager.nowScene == "shop":
        shop.Draw()
    elif gamemanager.nowScene == "friend":
        friend.Draw()
    else:
        if gamemanager.nowScene in "stage1_ready" or "battle":    #나중에 다른 stage도 or로 추가
            if not battle.turnSkillUsed:
                gamemanager.nowstage.Draw_background() #스테이지 배경 그리기
                if not gamemanager.nowScene == "battle": gamemanager.nowstage.Draw_choicechar()
                for c in gamemanager.party: #아군 그리기
                    if c.status["nowhp"] > 0:
                        c.Draw()
                for e in gamemanager.enemy: #적 그리기
                    if e.status["nowhp"] > 0:
                        e.Draw()
                if gamemanager.nowScene == "battle": speedbar.Draw() #speedbar 그리기
                speedbar.Draw_locateguide()
                HpUi_draw() #hp ui 그리기
                if not battle.nowTurn == -1:
                    if battle.nowTurn < 4:
                        gamemanager.party[battle.nowTurn].Draw_turn()
                    else:
                        gamemanager.enemy[battle.nowTurn-4].Draw_turn()
                    skill_inform_draw()
            elif battle.turnSkillUsed:
                skill_cut()

    fade.draw()
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
            gamemanager.enemy[battle.nowTurn-4].Draw()
            if not len(battle.target) == 0:
                for t in battle.target:
                    t.Draw()
            if not gamemanager.enemy[battle.nowTurn - 4].attackMotionEnd:
                for c in gamemanager.enemy[battle.nowTurn - 4].skill:
                    c.Draw()
            gamemanager.enemy[battle.nowTurn - 4].Draw_turn()

def skill_inform_draw():
    informBox = load_image('source\\ui\\skill_choice_box.png')
    if battle.skillInform == "skill_1":
        informBox.clip_draw(0, 0, 88, 88, 850, 100, 110, 110)
    elif battle.skillInform == "skill_2":
        informBox.clip_draw(0, 0, 88, 88, 975, 100, 110, 110)
    elif battle.skillInform == "skill_3":
        informBox.clip_draw(0, 0, 88, 88, 1100, 100, 110, 110)

def HpUi_draw():
    if gamemanager.nowScene == "battle":
        for n in speedbar.spdNums:
            if speedbar.spdNums.index(n) < 4:
                n.image.clip_draw(0, 0, 100, 100, 380, 180 - (50 * speedbar.spdNums.index(n)), 20, 20)
                hp_font.draw(510, 180 - (50 * speedbar.spdNums.index(n)),
                    f'{gamemanager.party[speedbar.spdNums.index(n)].status["nowhp"]}/{gamemanager.party[speedbar.spdNums.index(n)].status["maxhp"]}', (220, 220, 220))
                hp_team.clip_draw(0,0,114,14,
                                  450-((114 - (int)(114 * (gamemanager.party[speedbar.spdNums.index(n)].status["nowhp"] / gamemanager.party[speedbar.spdNums.index(n)].status["maxhp"]))) / 2), 180 - (50 * speedbar.spdNums.index(n)),
                                  (int)(114 * (gamemanager.party[speedbar.spdNums.index(n)].status["nowhp"] / gamemanager.party[speedbar.spdNums.index(n)].status["maxhp"])),14)
            else:
                n.image.clip_draw(0, 0, 100, 100, 580, 180 - (50 * (speedbar.spdNums.index(n) - 4)), 20, 20)
                hp_font.draw(710, 180 - (50 * (speedbar.spdNums.index(n) - 4)),
                    f'{gamemanager.enemy[speedbar.spdNums.index(n) - 4].status["nowhp"]}/{gamemanager.enemy[speedbar.spdNums.index(n) - 4].status["maxhp"]}', (220, 220, 220))
                hp_enemy.clip_draw(0, 0, 114, 14,
                                   650-((114 - (int)(114 * (gamemanager.enemy[speedbar.spdNums.index(n) - 4].status["nowhp"] / gamemanager.enemy[speedbar.spdNums.index(n) - 4].status["maxhp"]))) / 2), 180 - (50 * (speedbar.spdNums.index(n)-4)),
                                   (int)(114 * (gamemanager.enemy[speedbar.spdNums.index(n)-4].status["nowhp"] / gamemanager.enemy[speedbar.spdNums.index(n)-4].status["maxhp"])),14)

