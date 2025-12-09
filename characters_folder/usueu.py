from pico2d import load_image
from characters_folder.character_base import *

from skill_folder.usueu_skill.usueu_skill_2 import create_skill_2
from skill_folder.usueu_skill.usueu_skill_3 import create_skill_3

usueu = Character([
    [load_image(f'source\\character\\usueu\\usueu01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\usueu\\usueu01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\usueu\\usueu01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "우스유")

usueu.illust = load_image('source\\character\\usueu\\hero_illust_20_Usuu.png')

usueu.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 100, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":100}  # nowhp, maxhp, attack, speed

usueu.skill_1_icon = load_image(f'source\\skill_icon\\usueu\\kar_1302.png')
usueu.skill_2_icon = load_image(f'source\\skill_icon\\usueu\\kar_1303.png')
usueu.skill_3_icon = load_image(f'source\\skill_icon\\usueu\\greg_1604.png')
usueu.skill_1_inform = f"적 단일 공격, {usueu.status["atk"]}의 피해를 줍니다."
usueu.skill_2_inform = f"아군 전체 버프, 아군의 공격,방어를 10 올립니다.."
usueu.skill_3_inform = f"적 전체 공격, {usueu.status["atk"]}의 피해를 줍니다."

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
usueu.Skill_2 = Skill_2_override.__get__(usueu, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
usueu.Skill_3 = Skill_3_override.__get__(usueu, Character)

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

def evolution_override (self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\usueu\\usueu0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\usueu\\usueu0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\usueu\\usueu0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
usueu.evolution = evolution_override.__get__(usueu, Character)