from pico2d import load_image
from character_base import *
from skill import Skill

asha = Character([
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "아샤")

asha.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 100, "condition":[]}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass

asha.Skill_1 = Skill_1_override.__get__(asha, Character)