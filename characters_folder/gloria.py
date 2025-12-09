from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.gloria_skill.gloria_skill_2 import create_skill_2
from skill_folder.gloria_skill.gloria_skill_3 import create_skill_3


gloria = Character([
    [load_image(f'source\\character\\gloria\\gloria01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\gloria\\gloria01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\gloria\\gloria01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "글로리아")

gloria.illust = load_image('source\\character\\gloria\\hero_illust_17_Gloria.png')

gloria.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 124, "condition":[], "origin_atk":50, "origin_def" : 30, "origin_speed":120}  # nowhp, maxhp, attack, speed

gloria.skill_1_icon = load_image(f'source\\skill_icon\\gloria\\klat_0802.png')
gloria.skill_2_icon = load_image(f'source\\skill_icon\\gloria\\nor_attck_type.png')
gloria.skill_3_icon = load_image(f'source\\skill_icon\\gloria\\kar_1304.png')
gloria.skill_1_inform = f"적 단일 공격, {gloria.status["atk"]}의 피해를 줍니다."
gloria.skill_2_inform = f"아군 전체 버프, 아군의 공격력을 10 올립니다."
gloria.skill_3_inform = f"적 단일 공격, {gloria.status["atk"]} * 1.5의 피해를 줍니다."

gloria.skill_2_sound = load_wav('source\\sound\\buff.mp3')
gloria.skill_2_sound.set_volume(32)
gloria.skill_3_sound = load_wav('source\\sound\\gloria3.mp3')
gloria.skill_3_sound.set_volume(32)


def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
gloria.Skill_2 = Skill_2_override.__get__(gloria, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
gloria.Skill_3 = Skill_3_override.__get__(gloria, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\gloria\\gloria0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\gloria\\gloria0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\gloria\\gloria0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
gloria.evolution = evolution_override.__get__(gloria, Character)