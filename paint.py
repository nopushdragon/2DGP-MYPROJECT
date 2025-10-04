import gamemanager
import start


def DrawAll(dt):
    gamemanager.clear_canvas()

    if gamemanager.nowScene == "start":
        start.Draw()
    else:
        gamemanager.hometown.Draw()
        gamemanager.gunman.Draw(dt)
        for b in gamemanager.gunman.projectile:
            b.Draw()

    gamemanager.update_canvas()