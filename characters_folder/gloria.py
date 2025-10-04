from pico2d import load_image
from character_base import *
from projectile import Projectile

gloria = Character([
    [load_image(f'source\\character\\gloria01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\gloria01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\gloria01_0{i}.png') for i in range(5, 8)]
], 100, 400, [])

gloria.status = {"hp": 100, "atk": 50, "speed": 100}  # hp, attack, speed


def Skill_1_override(self):
    pass

gloria.Skill_1 = Skill_1_override.__get__(gloria, Character)