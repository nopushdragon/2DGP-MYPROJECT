from pico2d import *
from characters_folder.character_base import *
from skill_folder.asha_skill.asha_skill_1 import create_skill_1

asha = Character([
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\asha\\asha01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "아샤", get = True)

# ui에 필요한 리소스들
asha.illust = load_image('source\\character\\asha\\hero_illust_09_Asha.png')
asha.nameBox = load_image('source\\ui\\namebox.png')
asha.namefont = load_font('source\\ui\\DungGeunMo.ttf', 40)
asha.skill_1_icon = load_image(f'source\\skill_icon\\asha\\asha_0904.png')
asha.skill_2_icon = load_image(f'source\\skill_icon\\asha\\asha_0903.png')
asha.skill_3_icon = load_image(f'source\\skill_icon\\asha\\asha_0901.png')

asha.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 300, "condition":[]}  # nowhp, maxhp, attack, speed


def Skill_1_override(self):
    skill_1 = create_skill_1(self.x, self.y, self.flip)
    self.skill.append(skill_1)
asha.Skill_1 = Skill_1_override.__get__(asha, Character)

def Draw_turn_override(self):
    asha.illust.clip_draw(0, 550, 1350, 1350, 150, 150, 300, 300)
    asha.nameBox.clip_draw(125, 0, 125, 33, 150, 25,300,50)
    asha.namefont.draw(100, 24, self.name, (0, 0, 0))
    asha.namefont.draw(100, 26, self.name, (0, 0, 0))
    asha.namefont.draw(99, 25, self.name, (0, 0, 0))
    asha.namefont.draw(101, 25, self.name, (0, 0, 0))
    asha.namefont.draw(100, 25, self.name, (230, 230, 230))
    asha.skill_1_icon.clip_draw(0, 0, 32, 32, 850, 100, 100, 100)
    asha.skill_2_icon.clip_draw(0, 0, 32, 32, 975, 100, 100, 100)
    asha.skill_3_icon.clip_draw(0, 0, 32, 32, 1100, 100, 100, 100)
asha.Draw_turn = Draw_turn_override.__get__(asha, Character)