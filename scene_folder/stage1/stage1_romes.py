from pico2d import load_image
from characters_folder.character_base import *

romes = Character([
    [load_image(f'source\\character\\romes\\romes01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\romes\\romes01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\romes\\romes01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],flip=True)

romes.illust = load_image('source\\character\\romes\\hero_illust_05_Romes.png')

romes.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 101, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":101}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass

romes.Skill_1 = Skill_1_override.__get__(romes, Character)