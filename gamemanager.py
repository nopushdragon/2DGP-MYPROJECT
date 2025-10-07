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
import battle

party = []
party.append(Characters[0])
enemy = []

nowstage = []
partylocate = [(100,400),(200,400),(300,400),(400,400)]
enemylocate = [(800,400),(900,400),(1000,400),(1100,400)]

def GameUpdate(dt):
    nowstage.Update(dt)
    if nowScene == "battle":
        battle.Update(dt)
    for c in party:
        c.Update(dt)
    for e in enemy:
        e.Update(dt)

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