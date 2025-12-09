from pico2d import *
from characters_folder.character_base import *
from skill_folder.kimu_skill.kimu_skill_2 import create_skill_2
from skill_folder.kimu_skill.kimu_skill_3 import create_skill_3


kimu = Character([
    [load_image(f'source\\character\\kimu\\kimu04_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\kimu\\kimu04_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\kimu\\kimu04_0{i}.png') for i in range(5, 8)]
], 100, 400, [],flip = True,name = "키무")

kimu.illust = load_image('source\\character\\kimu\\hero_illust_04_Kimu.png')

kimu.status = {"nowhp": 500, "maxhp":500, "atk": 50, "def":30, "speed": 92, "condition":[], "origin_atk":50, "origin_def" : 30, "origin_speed":92}  # nowhp, maxhp, attack, speed

kimu.skill_1_icon = load_image(f'source\\skill_icon\\kimu\\kimu_0402.png')
kimu.skill_2_icon = load_image(f'source\\skill_icon\\kimu\\kimu_0401.png')
kimu.skill_3_icon = load_image(f'source\\skill_icon\\kimu\\kimu_0404.png')
kimu.skill_1_inform = f"적 단일 공격, {kimu.status["atk"]}의 피해를 줍니다."
kimu.skill_2_inform = f"아군 단일 회복, 아군의 체력을 {kimu.status["atk"]} * 2회복합니다."
kimu.skill_3_inform = f"아군 전체 버프, 아군의 방어력,속도를 10 올립니다."

kimu.skill_2_sound = load_wav('source\\sound\\heal.mp3')
kimu.skill_2_sound.set_volume(32)
kimu.skill_3_sound = load_wav('source\\sound\\buff.mp3')
kimu.skill_3_sound.set_volume(32)

def Skill_2_override(self):
    skill_2 = create_skill_2(self.x, self.y, self.flip)
    self.skill.append(skill_2)
kimu.Skill_2 = Skill_2_override.__get__(kimu, Character)

def Skill_3_override(self):
    skill_3 = create_skill_3(self.x, self.y, self.flip)
    self.skill.append(skill_3)
kimu.Skill_3 = Skill_3_override.__get__(kimu, Character)

def Draw_turn_override(self):
    kimu.illust.clip_draw(0, 550, 1350, 1350, 150, 150, 300, 300)
    kimu.nameBox.clip_draw(125, 0, 125, 33, 150, 25,300,50)
    kimu.namefont.draw(100, 24, self.name, (0, 0, 0))
    kimu.namefont.draw(100, 26, self.name, (0, 0, 0))
    kimu.namefont.draw(99, 25, self.name, (0, 0, 0))
    kimu.namefont.draw(101, 25, self.name, (0, 0, 0))
    kimu.namefont.draw(100, 25, self.name, (230, 230, 230))
    kimu.skill_1_icon.clip_draw(0, 0, 32, 32, 850, 100, 100, 100)
    kimu.skill_2_icon.clip_draw(0, 0, 32, 32, 975, 100, 100, 100)
    kimu.skill_3_icon.clip_draw(0, 0, 32, 32, 1100, 100, 100, 100)
kimu.Draw_turn = Draw_turn_override.__get__(kimu, Character)

def evolution_override(self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\kimu\\kimu0{self.evo}_0{i}.png') for i in range(1, 3)],
        [load_image(f'source\\character\\kimu\\kimu0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\kimu\\kimu0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
kimu.evolution = evolution_override.__get__(kimu, Character)