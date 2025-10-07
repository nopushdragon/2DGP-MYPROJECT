from pico2d import load_image
from character_base import *
from skill_folder.gunman_skill_1 import create_skill_1

gunman = Character([
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(5, 8)]
], 100, 400, [])

gunman.status = {"hp": 100, "atk": 50, "speed": 140}  # hp, attack, speed

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

def Draw_SkillIcon_override(self):
    skill_1_icon = load_image(f'source\\skill_icon\\gunman\\hope_1103.png')
    skill_1_icon.clip_draw(0, 0, 32, 32, 850, 100, 100, 100)
    skill_2_icon = load_image(f'source\\skill_icon\\gunman\\hope_1101.png')
    skill_2_icon.clip_draw(0, 0, 32, 32, 975, 100, 100, 100)
    skill_3_icon = load_image(f'source\\skill_icon\\gunman\\hope_1102.png')
    skill_3_icon.clip_draw(0, 0, 32, 32, 1100, 100, 100, 100)
gunman.Draw_Icon = Draw_SkillIcon_override.__get__(gunman, Character)