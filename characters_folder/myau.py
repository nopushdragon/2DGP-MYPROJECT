from pico2d import load_image
from characters_folder.character_base import *

myau = Character([
    [load_image(f'source\\character\\myau\\myau01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\myau\\myau01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\myau\\myau01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "먀우")

myau.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 100, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":100}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass

myau.Skill_1 = Skill_1_override.__get__(myau, Character)