from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.handrick_skill.handrick_skill_2 import create_skill_2
from skill_folder.handrick_skill.handrick_skill_3 import create_skill_3


handrick = Character([
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\handrick\\handrick01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "핸드릭")

handrick.illust = load_image('source\\character\\handrick\\hero_illust_02_Handrick.png')

handrick.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 88, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":100}  # nowhp, maxhp, attack, speed

handrick.skill_1_icon = load_image(f'source\\skill_icon\\handrick\\handrick_0202.png')
handrick.skill_2_icon = load_image(f'source\\skill_icon\\handrick\\handrick_0204.png')
handrick.skill_3_icon = load_image(f'source\\skill_icon\\handrick\\handrick_0203.png')
handrick.skill_1_inform = f"적 단일 공격, {handrick.status["atk"]}의 피해를 줍니다."
handrick.skill_2_inform = f"아군 전체 버프, 아군의 공격력을 10 올립니다."
handrick.skill_3_inform = f"적 단일 공격, {handrick.status["atk"]} * 1.5의 피해를 줍니다."

handrick.skill_2_sound = load_wav('source\\sound\\buff.mp3')
handrick.skill_2_sound.set_volume(32)
handrick.skill_3_sound = load_wav('source\\sound\\greg3.mp3')
handrick.skill_3_sound.set_volume(32)

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
handrick.Skill_2 = Skill_2_override.__get__(handrick, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
handrick.Skill_3 = Skill_3_override.__get__(handrick, Character)

def evolution_override (self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\handrick\\handrick0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\handrick\\handrick0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\handrick\\handrick0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
handrick.evolution = evolution_override.__get__(handrick, Character)