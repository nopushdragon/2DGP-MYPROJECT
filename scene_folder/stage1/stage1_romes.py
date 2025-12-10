from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.romes_skill.romes_skill_2 import create_skill_2
from skill_folder.romes_skill.romes_skill_3 import create_skill_3


romes = Character([
    [load_image(f'source\\character\\romes\\romes04_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\romes\\romes04_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\romes\\romes04_0{i}.png') for i in range(5, 8)]
], 100, 400, [],flip = True, name = "로메스")

romes.illust = load_image('source\\character\\romes\\hero_illust_05_Romes.png')

romes.status = {"nowhp": 370, "maxhp":620, "atk": 50, "def":20, "speed": 110, "condition":[], "origin_atk":100, "origin_def" : 100, "origin_speed":172}  # nowhp, maxhp, attack, speed

romes.skill_1_icon = load_image(f'source\\skill_icon\\romes\\romes_0501.png')
romes.skill_2_icon = load_image(f'source\\skill_icon\\romes\\romes_0502.png')
romes.skill_3_icon = load_image(f'source\\skill_icon\\romes\\kar_1301.png')
romes.skill_1_inform = f"적 단일 공격, {romes.status["atk"]}의 피해를 줍니다."
romes.skill_2_inform = f"적 전체 공격, {romes.status["atk"]}의 피해를 줍니다."
romes.skill_3_inform = f"적 전체 공격, {romes.status["atk"]}의 피해를 줍니다."

romes.skill_2_sound = load_wav('source\\sound\\romes2.mp3')
romes.skill_2_sound.set_volume(32)
romes.skill_3_sound = load_wav('source\\sound\\romes3.mp3')
romes.skill_3_sound.set_volume(32)

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
romes.Skill_2 = Skill_2_override.__get__(romes, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
romes.Skill_3 = Skill_3_override.__get__(romes, Character)

def evolution_override (self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\romes\\romes0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\romes\\romes0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\romes\\romes0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
romes.evolution = evolution_override.__get__(romes, Character)