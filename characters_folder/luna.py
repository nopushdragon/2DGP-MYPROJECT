from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.luna_skill.luna_skill_2 import create_skill_2
from skill_folder.luna_skill.luna_skill_3 import create_skill_3


luna = Character([
    [load_image(f'source\\character\\luna\\luna01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\luna\\luna01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\luna\\luna01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "루나")

luna.illust = load_image('source\\character\\luna\\hero_illust_10_Luna.png')

luna.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 104, "condition":[], "origin_atk":50, "origin_def" : 15, "origin_speed":100}  # nowhp, maxhp, attack, speed

luna.skill_1_icon = load_image(f'source\\skill_icon\\luna\\klat_0804.png')
luna.skill_2_icon = load_image(f'source\\skill_icon\\luna\\luna_1002.png')
luna.skill_3_icon = load_image(f'source\\skill_icon\\luna\\luna_1001.png')
luna.skill_1_inform = f"적 단일 공격, {luna.status["atk"]}의 피해를 줍니다."
luna.skill_2_inform = f"적 전체 디버프, 적의 방어력을 10 낮춥니다."
luna.skill_3_inform = f"적 전체 공격, {luna.status["atk"]}의 피해를 줍니다."

luna.skill_2_sound = load_wav('source\\sound\\debuff.mp3')
luna.skill_2_sound.set_volume(32)
luna.skill_3_sound = load_wav('source\\sound\\luna3.mp3')
luna.skill_3_sound.set_volume(32)

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
luna.Skill_2 = Skill_2_override.__get__(luna, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
luna.Skill_3 = Skill_3_override.__get__(luna, Character)

def evolution_override (self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\luna\\luna0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\luna\\luna0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\luna\\luna0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
luna.evolution = evolution_override.__get__(luna, Character)