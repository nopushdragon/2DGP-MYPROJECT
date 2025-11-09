WIDTH = 1200
HEIGHT = 800

nowScene = None #start, main, stage1, stage2, stage3...

from pico2d import *
open_canvas(WIDTH, HEIGHT)
from paint import *
from characters import *
from scene_folder.title import *
from scene_folder.home import *
from scene_folder.shop import *
import battle
import fade

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

TARGET_FPS = 60.0
TARGET_DT = 1.0 / TARGET_FPS

def main():
    while True:
        frame_start = get_time()
        dt = TARGET_DT

        if nowScene == "title":
            title.Update(dt)
        elif nowScene == "home":
            home.Update(dt)
        elif nowScene == "shop":
            shop.Update(dt)
        else:
            GameUpdate(dt)
        fade.update(dt)

        DrawAll(dt)

        frame_time = get_time() - frame_start
        sleep_time = TARGET_DT - frame_time
        if sleep_time > 0:
            delay(sleep_time)
    close_canvas()