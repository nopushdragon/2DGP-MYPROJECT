from pico2d import load_image
from characters_folder.character_base import *

myau = Character([
    [load_image(f'source\\character\\myau\\myau01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\myau\\myau01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\myau\\myau01_0{i}.png') for i in range(5, 8)]
], 100, 400, [],flip=True,name = "먀우")

myau.illust = load_image('source\\character\\myau\\hero_illust_15_Myau.png')

myau.status = {"nowhp": 100, "maxhp":100, "atk": 50, "def":20, "speed": 89, "condition":[], "origin_atk":50, "origin_def" : 20, "origin_speed":89}  # nowhp, maxhp, attack, speed

