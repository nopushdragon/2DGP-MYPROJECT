from pico2d import load_image
from characters_folder.character_base import *

isli = Character([
    [load_image(f'source\\character\\isli\\isli01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\isli\\isli01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\isli\\isli01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "이즐리", get = True)

isli.illust = load_image('source\\character\\isli\\hero_illust_03_Islil.png')

isli.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 100, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":100}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass
isli.Skill_1 = Skill_1_override.__get__(isli, Character)

def Skill_2_override(self):
    pass
isli.Skill_2 = Skill_2_override.__get__(isli, Character)

def Skill_3_override(self):
    pass
isli.Skill_3 = Skill_3_override.__get__(isli, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\isli\\isli0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\isli\\isli0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\isli\\isli0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
isli.evolution = evolution_override.__get__(isli, Character)