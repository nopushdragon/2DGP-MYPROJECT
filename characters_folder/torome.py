from pico2d import load_image
from characters_folder.character_base import *

torome = Character([
    [load_image(f'source\\character\\torome\\torome01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\torome\\torome01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\torome\\torome01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "토로메")

torome.illust = load_image('source\\character\\torome\\hero_illust_07_Torome.png')

torome.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 120, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":120}  # nowhp, maxhp, attack, speed



def Skill_2_override(self):
    pass
torome.Skill_2 = Skill_2_override.__get__(torome, Character)

def Skill_3_override(self):
    pass
torome.Skill_3 = Skill_3_override.__get__(torome, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\torome\\torome0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\torome\\torome0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\torome\\torome0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
torome.evolution = evolution_override.__get__(torome, Character)