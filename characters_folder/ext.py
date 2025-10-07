from pico2d import load_image
from character_base import *
from skill import Skill

ext = Character([
    [load_image(f'source\\character\\ext\\ext01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\ext\\ext01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\ext\\ext01_0{i}.png') for i in range(5, 8)]
], 100, 400, [])

ext.status = {"hp": 100, "atk": 50, "speed": 100}  # hp, attack, speed


def Skill_1_override(self):
    pass

ext.Skill_1 = Skill_1_override.__get__(ext, Character)