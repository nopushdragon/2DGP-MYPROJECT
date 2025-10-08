from pico2d import *
from character_base import *
from skill_folder.gunman_skill.gunman_skill_1 import create_skill_1

# ui에 필요한 리소스들
illust = load_image('source\\skill_icon\\gunman\\hero_illust_11_Hope.png')
nameBox = load_image('source\\ui\\namebox.png')
namefont = load_font('source\\ui\\DungGeunMo.ttf', 40)
skill_1_icon = load_image(f'source\\skill_icon\\gunman\\hope_1103.png')
skill_2_icon = load_image(f'source\\skill_icon\\gunman\\hope_1101.png')
skill_3_icon = load_image(f'source\\skill_icon\\gunman\\hope_1102.png')

gunman = Character([
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "건 맨")

gunman.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 500, "condition":[]}  # nowhp, maxhp, attack, speed

def Skill_1_override(self):
    skill_1 = create_skill_1(self.x, self.y, self.flip)
    self.skill.append(skill_1)
gunman.Skill_1 = Skill_1_override.__get__(gunman, Character)

def Skill_2_override(self):
    pass
gunman.Skill_2 = Skill_2_override.__get__(gunman, Character)

def Skill_3_override(self):
    pass
gunman.Skill_3 = Skill_3_override.__get__(gunman, Character)

def Draw_turn_override(self):
    global illust, nameBox, namefont, skill_1_icon, skill_2_icon, skill_3_icon

    illust.clip_draw(0, 550, 1350, 1350, 150, 150, 300, 300)
    nameBox.clip_draw(125, 0, 125, 33, 150, 25,300,50)
    namefont.draw(100, 24, self.name, (0, 0, 0))
    namefont.draw(100, 26, self.name, (0, 0, 0))
    namefont.draw(99, 25, self.name, (0, 0, 0))
    namefont.draw(101, 25, self.name, (0, 0, 0))
    namefont.draw(100, 25, self.name, (230, 230, 230))
    skill_1_icon.clip_draw(0, 0, 32, 32, 850, 100, 100, 100)
    skill_2_icon.clip_draw(0, 0, 32, 32, 975, 100, 100, 100)
    skill_3_icon.clip_draw(0, 0, 32, 32, 1100, 100, 100, 100)

gunman.Draw_turn = Draw_turn_override.__get__(gunman, Character)