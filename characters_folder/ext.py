from pico2d import load_image
from characters_folder.character_base import *

ext = Character([
    [load_image(f'source\\character\\ext\\ext01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\ext\\ext01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\ext\\ext01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "EXT")

ext.illust = load_image('source\\character\\ext\\hero_illust_14_Ext.png')

ext.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 100, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":100}  # nowhp, maxhp, attack, speed

ext.skill_1_icon = load_image(f'source\\skill_icon\\ext\\ext_1401.png')
ext.skill_2_icon = load_image(f'source\\skill_icon\\ext\\ext_1403.png')
ext.skill_3_icon = load_image(f'source\\skill_icon\\ext\\balbar_0604.png')
ext.skill_1_inform = f"적 단일 공격, {ext.status["atk"]}의 피해를 줍니다."
ext.skill_2_inform = f"적 전체 공격, {ext.status["atk"]}의 피해를 줍니다."
ext.skill_3_inform = f"적 전체 공격, {ext.status["atk"]}의 피해를 줍니다."

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
ext.Skill_2 = Skill_2_override.__get__(ext, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
ext.Skill_3 = Skill_3_override.__get__(ext, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\ext\\ext0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\ext\\ext0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\ext\\ext0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
ext.evolution = evolution_override.__get__(ext, Character)