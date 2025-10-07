from pico2d import load_image
from character_base import *
from skill import Skill

greg = Character([
    [load_image(f'source\\character\\greg\\greg01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\greg\\greg01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\greg\\greg01_0{i}.png') for i in range(5, 8)]
], 100, 400, [])

greg.status = {"hp": 100, "atk": 50, "speed": 100}  # hp, attack, speed


def Skill_1_override(self):
    pass

greg.Skill_1 = Skill_1_override.__get__(greg, Character)