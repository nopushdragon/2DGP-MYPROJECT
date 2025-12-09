from pico2d import load_image
from characters_folder.character_base import *
from skill_folder.torome_skill.torome_skill_2 import create_skill_2
from skill_folder.torome_skill.torome_skill_3 import create_skill_3


torome = Character([
    [load_image(f'source\\character\\torome\\torome01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\torome\\torome01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\torome\\torome01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "토로메")

torome.illust = load_image('source\\character\\torome\\hero_illust_07_Torome.png')

torome.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 120, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":120}  # nowhp, maxhp, attack, speed

torome.skill_1_icon = load_image(f'source\\skill_icon\\torome\\torome_0703.png')
torome.skill_2_icon = load_image(f'source\\skill_icon\\torome\\torome_0701.png')
torome.skill_3_icon = load_image(f'source\\skill_icon\\torome\\myau_1501.png')
torome.skill_1_inform = f"적 단일 공격, {torome.status["atk"]}의 피해를 줍니다."
torome.skill_2_inform = f"적 단일 디버프, 적의 공격력을 20 낮춥니다."
torome.skill_3_inform = f"적 전체 공격, {torome.status["atk"]}의 피해를 줍니다."

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
torome.Skill_2 = Skill_2_override.__get__(torome, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
torome.Skill_3 = Skill_3_override.__get__(torome, Character)

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
        [load_image(f'source\\character\\torome\\torome0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\torome\\torome0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\torome\\torome0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
torome.evolution = evolution_override.__get__(torome, Character)