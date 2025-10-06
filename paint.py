import gamemanager
import start
import speedbar

def DrawAll(dt):
    gamemanager.clear_canvas()

    if gamemanager.nowScene == "start":
        start.Draw()
    elif gamemanager.nowScene == "stage1_ready":
        gamemanager.nowstage.Draw()
        for c in gamemanager.party: #아군 그리기
            c.Draw(dt)
            for p in c.projectile:
                p.Draw()
        for e in gamemanager.enemy: #적 그리기
            e.Draw(dt)
            for p in e.projectile:
                p.Draw()
        speedbar.Draw()
        speedbar.DrawLocateGuide()

    gamemanager.update_canvas()