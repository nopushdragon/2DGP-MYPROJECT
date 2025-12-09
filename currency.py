from pico2d import *

back_bar = load_image('source\\ui\\hp_base.png')

class TICKET: #21, 21
    quantity = 20
    image = load_image('source\\ui\\ticket.png')

class UPGRADE_STONE: #32, 32
    quantity = 100
    image = load_image('source\\ui\\upgrade_stone.png')

ticket = TICKET()
upgrade_stone = UPGRADE_STONE()