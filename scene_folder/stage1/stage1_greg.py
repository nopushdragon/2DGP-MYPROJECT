from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.greg_skill.greg_skill_2 import create_skill_2
from skill_folder.greg_skill.greg_skill_3 import create_skill_3

greg = Character([
    [load_image(f'source\\character\\greg\\greg04_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\greg\\greg04_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\greg\\greg04_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "그렉",flip = True)

greg.illust = load_image('source\\character\\greg\\hero_illust_16_Greg.png')

greg.status = {"nowhp": 100, "maxhp":820, "atk": 50, "def":20, "speed": 123, "condition":[], "origin_atk":100, "origin_def" : 80, "origin_speed":155}  # nowhp, maxhp, attack, speed

greg.skill_1_icon = load_image(f'source\\skill_icon\\greg\\greg_1601.png')
greg.skill_2_icon = load_image(f'source\\skill_icon\\greg\\greg_1602.png')
greg.skill_3_icon = load_image(f'source\\skill_icon\\greg\\greg_1603.png')
greg.skill_1_inform = f"적 단일 공격, {greg.status["atk"]}의 피해를 줍니다."
greg.skill_2_inform = f"적 단일 공격, {greg.status["atk"]}의 피해를 줍니다."
greg.skill_3_inform = f"적 단일 공격, {greg.status["atk"]} * 1.5의 피해를 줍니다."

greg.skill_2_sound = load_wav('source\\sound\\greg2.mp3')
greg.skill_2_sound.set_volume(32)
greg.skill_3_sound = load_wav('source\\sound\\greg3.mp3')
greg.skill_3_sound.set_volume(32)

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
greg.Skill_2 = Skill_2_override.__get__(greg, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
greg.Skill_3 = Skill_3_override.__get__(greg, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\greg\\greg0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\greg\\greg0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\greg\\greg0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
greg.evolution = evolution_override.__get__(greg, Character)