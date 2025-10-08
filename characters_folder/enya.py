from pico2d import load_image
from character_base import *
from skill import Skill

enya = Character([
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "에냐")

enya.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 110, "condition":[]}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass

enya.Skill_1 = Skill_1_override.__get__(enya, Character)