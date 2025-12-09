from pico2d import *
from characters_folder.character_base import *

kimu = Character([
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\kimu\\kimu01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],flip= True, name = "키무")

kimu.illust = load_image('source\\character\\kimu\\hero_illust_04_Kimu.png')
kimu.skill_1_icon = load_image(f'source\\skill_icon\\asha\\asha_0904.png')
kimu.skill_2_icon = load_image(f'source\\skill_icon\\asha\\asha_0903.png')
kimu.skill_3_icon = load_image(f'source\\skill_icon\\asha\\asha_0901.png')

kimu.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 140, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":140}  # nowhp, maxhp, attack, speed
