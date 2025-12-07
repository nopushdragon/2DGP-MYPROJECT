from pico2d import load_image
from characters_folder.character_base import *

enya = Character([
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "에냐", get = True)

enya.illust = load_image('source\\character\\enya\\hero_illust_12_Enya.png')

enya.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 110, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":110}  # nowhp, maxhp, attack, speed



def Skill_2_override(self):
    pass
enya.Skill_2 = Skill_2_override.__get__(enya, Character)

def Skill_3_override(self):
    pass
enya.Skill_3 = Skill_3_override.__get__(enya, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\enya\\enya0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\enya\\enya0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\enya\\enya0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
enya.evolution = evolution_override.__get__(enya, Character)