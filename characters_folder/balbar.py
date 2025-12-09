from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.balbar_skill.balbar_skill_2 import create_skill_2
from skill_folder.balbar_skill.balbar_skill_3 import create_skill_3


balbar = Character([
    [load_image(f'source\\character\\balbar\\balbar01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\balbar\\balbar01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\balbar\\balbar01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "발바")

balbar.illust = load_image('source\\character\\balbar\\hero_illust_06_Balbar.png')

balbar.status = {"nowhp": 100, "maxhp":100, "atk": 20, "def":20, "speed": 85, "condition":[], "origin_atk":20, "origin_def" : 20, "origin_speed":85}  # nowhp, maxhp, attack, speed

balbar.skill_1_icon = load_image(f'source\\skill_icon\\balbar\\balbar_0601.png')
balbar.skill_2_icon = load_image(f'source\\skill_icon\\balbar\\balbar_0602.png')
balbar.skill_3_icon = load_image(f'source\\skill_icon\\balbar\\balbar_0603.png')
balbar.skill_1_inform = f"적 단일 공격, {balbar.status["atk"]}의 피해를 줍니다."
balbar.skill_2_inform = f"적 전체 공격, {balbar.status["atk"]}의 피해를 줍니다."
balbar.skill_3_inform = f"아군 전체 회복, 아군의 체력을 {balbar.status["atk"]} 회복합니다."

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
balbar.Skill_2 = Skill_2_override.__get__(balbar, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
balbar.Skill_3 = Skill_3_override.__get__(balbar, Character)

def skill_2_sound_override(self):
    sound = load_wav('source\\sound\\sword.mp3')
    sound.set_volume(64)
    sound.play(1)
asha.skill_2_sound = skill_2_sound_override.__get__(asha, Character)

def skill_3_sound_override(self):
    sound = load_wav('source\\sound\\buff.mp3')
    sound.set_volume(64)
    sound.play(1)
asha.skill_3_sound = skill_3_sound_override.__get__(asha, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\balbar\\balbar0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\balbar\\balbar0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\balbar\\balbar0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
balbar.evolution = evolution_override.__get__(balbar, Character)