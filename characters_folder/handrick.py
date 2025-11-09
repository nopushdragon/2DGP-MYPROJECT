from pico2d import load_image
from characters_folder.character_base import *

handrick = Character([
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "핸드릭")

handrick.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 100, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":100}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass

handrick.Skill_1 = Skill_1_override.__get__(handrick, Character)