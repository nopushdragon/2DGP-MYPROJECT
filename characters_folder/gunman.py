from pico2d import *
from characters_folder.character_base import *
from skill_folder.gunman_skill.gunman_skill_1 import create_skill_1

gunman = Character([
    [load_image(f'source\\character\\hope\\hope01_0{i}.png')for i in range(1, 3)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\hope\\hope01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],name = "건 맨", get = True)

# ui에 필요한 리소스들
gunman.illust = load_image('source\\character\\hope\\hero_illust_11_Hope.png')
gunman.nameBox = load_image('source\\ui\\namebox.png')
gunman.namefont = load_font('source\\ui\\DungGeunMo.ttf', 40)
gunman.skill_1_icon = load_image(f'source\\skill_icon\\gunman\\hope_1103.png')
gunman.skill_2_icon = load_image(f'source\\skill_icon\\gunman\\hope_1101.png')
gunman.skill_3_icon = load_image(f'source\\skill_icon\\gunman\\hope_1102.png')

gunman.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 250, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":250}  # nowhp, maxhp, attack, speed

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
    gunman.illust.clip_draw(0, 550, 1350, 1350, 150, 150, 300, 300)
    gunman.nameBox.clip_draw(125, 0, 125, 33, 150, 25,300,50)
    gunman.namefont.draw(100, 24, self.name, (0, 0, 0))
    gunman.namefont.draw(100, 26, self.name, (0, 0, 0))
    gunman.namefont.draw(99, 25, self.name, (0, 0, 0))
    gunman.namefont.draw(101, 25, self.name, (0, 0, 0))
    gunman.namefont.draw(100, 25, self.name, (230, 230, 230))
    gunman.skill_1_icon.clip_draw(0, 0, 32, 32, 850, 100, 100, 100)
    gunman.skill_2_icon.clip_draw(0, 0, 32, 32, 975, 100, 100, 100)
    gunman.skill_3_icon.clip_draw(0, 0, 32, 32, 1100, 100, 100, 100)
gunman.Draw_turn = Draw_turn_override.__get__(gunman, Character)

def evolution_override (self):
    self.evo += 1
    self.anime = [
        [load_image(f'source\\character\\hope_evo\\hope_evo0{self.evo}_0{i}.png')for i in range(1, 3)],
        [load_image(f'source\\character\\hope_evo\\hope_evo0{self.evo}_0{i}.png') for i in range(3, 5)],
        [load_image(f'source\\character\\hope_evo\\hope_evo0{self.evo}_0{i}.png') for i in range(5, 8)]
    ]
gunman.evolution = evolution_override.__get__(gunman, Character)