from pico2d import load_image
from characters_folder.character_base import *

balbar = Character([
    [load_image(f'source\\character\\balbar\\balbar01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\balbar\\balbar01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\balbar\\balbar01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "발바")

balbar.illust = load_image('source\\character\\balbar\\hero_illust_06_Balbar.png')

balbar.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 85, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":85}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    pass
balbar.Skill_1 = Skill_1_override.__get__(balbar, Character)

def Skill_2_override(self):
    pass
balbar.Skill_2 = Skill_2_override.__get__(balbar, Character)

def Skill_3_override(self):
    pass
balbar.Skill_3 = Skill_3_override.__get__(balbar, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\balbar\\balbar0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\balbar\\balbar0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\balbar\\balbar0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
balbar.evolution = evolution_override.__get__(balbar, Character)