from pico2d import *
from currency import *
from gamemanager import WIDTH, HEIGHT

ticket = TICKET()
upgrade_stone = UPGRADE_STONE()
option = load_image('source\\ui\\option.png')


def draw():
    back_bar.clip_draw(0, 0, 114, 14, WIDTH - 150, HEIGHT - 25, 150, 30)
    ticket.image.clip_draw(0, 0, 21, 21, WIDTH - 200, HEIGHT - 25)
    back_bar.clip_draw(0, 0, 114, 14, WIDTH - 320, HEIGHT - 25, 150, 30)
    upgrade_stone.image.clip_draw(0, 0, 32, 32, WIDTH - 370, HEIGHT - 25)

    font = load_font('source\\ui\\DungGeunMo.TTF', 20)
    font.draw(WIDTH - 150, HEIGHT - 25, f" {ticket.quantity}", (255, 255, 255))
    font.draw(WIDTH - 320, HEIGHT - 25, f" {upgrade_stone.quantity}", (255, 255, 255))

    option.clip_draw(0, 0, 62, 62, WIDTH - 35, HEIGHT - 25, 40, 40)
