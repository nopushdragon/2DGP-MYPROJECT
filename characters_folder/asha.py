from pico2d import *
from characters_folder.character_base import *
from skill_folder.asha_skill.asha_skill_2 import create_skill_2
from skill_folder.asha_skill.asha_skill_3 import create_skill_3

asha = Character([
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "아샤", get = True)

asha.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 150, "condition":[], "origin_atk":50, "origin_def" : 12, "origin_speed":150}  # nowhp, maxhp, attack, speed

# ui에 필요한 리소스들
asha.illust = load_image('source\\character\\asha\\hero_illust_09_Asha.png')
asha.skill_1_icon = load_image(f'source\\skill_icon\\asha\\asha_0904.png')
asha.skill_2_icon = load_image(f'source\\skill_icon\\asha\\asha_0903.png')
asha.skill_3_icon = load_image(f'source\\skill_icon\\asha\\asha_0901.png')
asha.skill_1_inform = f"적 단일 공격, {asha.status["atk"]}의 피해를 줍니다."
asha.skill_2_inform = f"적 단일 공격, {asha.status["atk"]}의 피해를 줍니다."
asha.skill_3_inform = f"아군 전체 버프, 아군의 speed를 10 올립니다."

asha.skill_2_sound = load_wav('source\\sound\\sword.mp3')
asha.skill_2_sound.set_volume(32)
asha.skill_3_sound = load_wav('source\\sound\\buff.mp3')
asha.skill_3_sound.set_volume(32)


def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
asha.Skill_2 = Skill_2_override.__get__(asha, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
asha.Skill_3 = Skill_3_override.__get__(asha, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\asha\\asha0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\asha\\asha0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\asha\\asha0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
asha.evolution = evolution_override.__get__(asha, Character)