import gamemanager
import start


def DrawAll(dt):
    gamemanager.clear_canvas()

    if gamemanager.nowScene == "start":
        start.Draw()
    else:
        gamemanager.nowstage.Draw()
        for c in gamemanager.party:
            c.Draw(dt)
            for p in c.projectile:
                p.Draw()

    gamemanager.update_canvas()