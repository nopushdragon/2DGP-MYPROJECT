from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.enya_skill.enya_skill_2 import create_skill_2
from skill_folder.enya_skill.enya_skill_3 import create_skill_3


enya = Character([
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\enya\\enya01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "에냐", get = True)

enya.illust = load_image('source\\character\\enya\\hero_illust_12_Enya.png')

enya.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 110, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":110}  # nowhp, maxhp, attack, speed

enya.skill_1_icon = load_image(f'source\\skill_icon\\enya\\enya_1202.png')
enya.skill_2_icon = load_image(f'source\\skill_icon\\enya\\enya_1201.png')
enya.skill_3_icon = load_image(f'source\\skill_icon\\enya\\enya_1204.png')
enya.skill_1_inform = f"적 단일 공격, {enya.status["atk"]}의 피해를 줍니다."
enya.skill_2_inform = f"적 단일 공격, {enya.status["atk"]}의 피해를 줍니다."
enya.skill_3_inform = f"적 전체 공격, {enya.status["atk"]}의 피해를 줍니다."

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
enya.Skill_2 = Skill_2_override.__get__(enya, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
enya.Skill_3 = Skill_3_override.__get__(enya, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\enya\\enya0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\enya\\enya0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\enya\\enya0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
enya.evolution = evolution_override.__get__(enya, Character)