
WIDTH = 1200
HEIGHT = 800

nowScene = None #start, main, stage1, stage2, stage3...

from pico2d import *
open_canvas(WIDTH, HEIGHT)
from background import *
from paint import *
from characters import *
from deltatime import *
from start import *
from stages import Stages

party = []
party.append(Characters[0])
enemy = []

nowstage = Stages[0]
partylocate = [(100,400),(200,400),(300,400),(400,400)]
enemylocate = [(800,400),(900,400),(1000,400),(1100,400)]

def GameUpdate(dt):
    nowstage.Update(dt)
    for c in party:
        c.Update(dt)
    for e in enemy:
        e.Update(dt)
    '''for b in gunman.projectile[::-1]:
        b.Update(dt)
        if not b.visible:
            gunman.projectile.remove(b)'''


'''def InputKey():
    events = get_events()
    if not gunman.state == "attack":
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT or event.key == ord("a") or event.key == ord("A"):
                    gunman.state = "walk"
                    gunman.flip = True
                elif event.key == SDLK_RIGHT or event.key == ord("d") or event.key == ord("D"):
                    gunman.state = "walk"
                    gunman.flip = False
                elif event.key == SDLK_SPACE:
                    gunman.frameTimer = 0.0
                    gunman.frame = 0
                    gunman.state = "attack"
                elif event.key == SDLK_ESCAPE:
                    quit()
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT and gunman.flip == True or event.key == SDLK_RIGHT and gunman.flip == False:
                    gunman.state = "idle"
'''

def main():
    while True:
        dt = DeltaTime()

        if nowScene == "start":
            start.Update()
        else:
            GameUpdate(dt)

        DrawAll(dt)

        if dt < 1 / 60:
            delay((1 / 60) - dt)
    close_canvas()