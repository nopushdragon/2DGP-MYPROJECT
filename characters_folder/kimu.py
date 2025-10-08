from pico2d import load_image
from character_base import *
from skill import Skill

kimu = Character([
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "키무")

kimu.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 86, "condition":[]}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass

kimu.Skill_1 = Skill_1_override.__get__(kimu, Character)