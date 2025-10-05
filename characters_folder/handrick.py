from pico2d import load_image
from character_base import *
from projectile import Projectile

handrick = Character([
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(5, 8)]
], 100, 400, [])

handrick.status = {"hp": 100, "atk": 50, "speed": 100}  # hp, attack, speed


def Skill_1_override(self):
    pass

handrick.Skill_1 = Skill_1_override.__get__(handrick, Character)