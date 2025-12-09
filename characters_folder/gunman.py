from pico2d import *
from characters_folder.character_base import *
from skill_folder.gunman_skill.gunman_skill_2 import create_skill_2
from skill_folder.gunman_skill.gunman_skill_3 import create_skill_3

gunman = Character([
    [load_image(f'source\\character\\hope\\hope01_0{i}.png')for i in range(1, 3)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "건 맨", get = True)

gunman.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 130, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":130}  # nowhp, maxhp, attack, speed

# ui에 필요한 리소스들
gunman.illust = load_image('source\\character\\hope\\hero_illust_11_Hope.png')
gunman.skill_1_icon = load_image(f'source\\skill_icon\\gunman\\hope_1103.png')
gunman.skill_2_icon = load_image(f'source\\skill_icon\\gunman\\hope_1101.png')
gunman.skill_3_icon = load_image(f'source\\skill_icon\\gunman\\hope_1102.png')
gunman.skill_1_inform = f"적 단일 공격, {gunman.status["atk"]}의 피해를 줍니다."
gunman.skill_2_inform = f"적 전체 공격, {gunman.status["atk"]}의 피해를 줍니다."
gunman.skill_3_inform = f"적 전체 공격, {gunman.status["atk"]} * 1.2의 피해를 줍니다."

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
gunman.Skill_2 = Skill_2_override.__get__(gunman, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
gunman.Skill_3 = Skill_3_override.__get__(gunman, Character)

def evolution_override (self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\hope\\hope0{self.evo}_0{i}.png')for i in range(1, 3)],
        [load_image(f'source\\character\\hope\\hope0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\hope\\hope0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
gunman.evolution = evolution_override.__get__(gunman, Character)