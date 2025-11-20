from pico2d import load_image
from characters_folder.character_base import *

usueu = Character([
    [load_image(f'source\\character\\usueu\\usueu01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\usueu\\usueu01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\usueu\\usueu01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],flip=True)

usueu.illust = load_image('source\\character\\usueu\\hero_illust_20_Usuu.png')

usueu.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 98, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":98}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass

usueu.Skill_1 = Skill_1_override.__get__(usueu, Character)