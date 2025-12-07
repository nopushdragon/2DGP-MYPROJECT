from pico2d import *
from characters_folder.character_base import *

kimu = Character([
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "키무")

kimu.illust = load_image('source\\character\\kimu\\hero_illust_04_Kimu.png')
kimu.nameBox = load_image('source\\ui\\namebox.png')
kimu.namefont = load_font('source\\ui\\DungGeunMo.ttf', 40)
kimu.skill_1_icon = load_image(f'source\\skill_icon\\asha\\asha_0904.png')
kimu.skill_2_icon = load_image(f'source\\skill_icon\\asha\\asha_0903.png')
kimu.skill_3_icon = load_image(f'source\\skill_icon\\asha\\asha_0901.png')

kimu.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 86, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":86}  # nowhp, maxhp, attack, speed


def Skill_2_override(self):
    pass
kimu.Skill_2 = Skill_2_override.__get__(kimu, Character)

def Skill_3_override(self):
    pass
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