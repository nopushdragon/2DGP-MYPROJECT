from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.myau_skill.myau_skill_2 import create_skill_2
from skill_folder.myau_skill.myau_skill_3 import create_skill_3


myau = Character([
    [load_image(f'source\\character\\myau\\myau04_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\myau\\myau04_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\myau\\myau04_0{i}.png') for i in range(5, 8)]
], 100, 400, [],flip =True,name = "먀우")

myau.illust = load_image('source\\character\\myau\\hero_illust_15_Myau.png')

myau.status = {"nowhp": 500, "maxhp":500, "atk": 50, "def":20, "speed": 100, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":100}  # nowhp, maxhp, attack, speed

myau.skill_1_icon = load_image(f'source\\skill_icon\\myau\\myau_1504.png')
myau.skill_2_icon = load_image(f'source\\skill_icon\\myau\\klat_0801.png')
myau.skill_3_icon = load_image(f'source\\skill_icon\\myau\\myau_1502.png')
myau.skill_1_inform = f"적 단일 공격, {myau.status["atk"]}의 피해를 줍니다."
myau.skill_2_inform = f"적 전체 디버프, 적의 속도를 10 낮춥니다."
myau.skill_3_inform = f"아군 전체 버프, 아군의 공격,속도,방어력을 10 올립니다."

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
myau.Skill_2 = Skill_2_override.__get__(myau, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
myau.Skill_3 = Skill_3_override.__get__(myau, Character)

def evolution_override (self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\myau\\myau0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\myau\\myau0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\myau\\myau0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
myau.evolution = evolution_override.__get__(myau, Character)