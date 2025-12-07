from pico2d import *
from characters_folder.character_base import *
from skill_folder.asha_skill.asha_skill_1 import create_skill_1

asha = Character([
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "아샤", get = True)

# ui에 필요한 리소스들
asha.illust = load_image('source\\character\\asha\\hero_illust_09_Asha.png')
asha.skill_1_icon = load_image(f'source\\skill_icon\\asha\\asha_0904.png')
asha.skill_2_icon = load_image(f'source\\skill_icon\\asha\\asha_0903.png')
asha.skill_3_icon = load_image(f'source\\skill_icon\\asha\\asha_0901.png')

asha.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 300, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":300}  # nowhp, maxhp, attack, speed



def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\asha\\asha0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\asha\\asha0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\asha\\asha0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
asha.evolution = evolution_override.__get__(asha, Character)