from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.isli_skill.isli_skill_2 import create_skill_2
from skill_folder.isli_skill.isli_skill_3 import create_skill_3


isli = Character([
    [load_image(f'source\\character\\isli\\isli04_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\isli\\isli04_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\isli\\isli04_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "이즐리", get = True,flip = True)

isli.illust = load_image('source\\character\\isli\\hero_illust_03_Islil.png')

isli.status = {"nowhp": 100, "maxhp":720, "atk": 50, "def":20, "speed": 125, "condition":[], "origin_atk":102, "origin_def" : 65, "origin_speed":155}  # nowhp, maxhp, attack, speed

isli.skill_1_icon = load_image(f'source\\skill_icon\\isli\\islil_0302.png')
isli.skill_2_icon = load_image(f'source\\skill_icon\\isli\\nor_shoot_type.png')
isli.skill_3_icon = load_image(f'source\\skill_icon\\isli\\islil_0304.png')
isli.skill_1_inform = f"적 단일 공격, {isli.status["atk"]}의 피해를 줍니다."
isli.skill_2_inform = f"아군 전체 버프, 아군의 speed를 10 올립니다."
isli.skill_3_inform = f"적 전체 공격, {isli.status["atk"]}의 피해를 줍니다."

isli.skill_2_sound = load_wav('source\\sound\\buff.mp3')
isli.skill_2_sound.set_volume(32)
isli.skill_3_sound = load_wav('source\\sound\\isli3.mp3')
isli.skill_3_sound.set_volume(32)

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
isli.Skill_2 = Skill_2_override.__get__(isli, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
isli.Skill_3 = Skill_3_override.__get__(isli, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\isli\\isli0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\isli\\isli0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\isli\\isli0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
isli.evolution = evolution_override.__get__(isli, Character)