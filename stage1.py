from gamemanager import WIDTH, HEIGHT
from pico2d import *
from background import BackGround
from stage import Stage
from characters import Characters

stage1 = Stage()

ground = load_image('source\\background\\stage1_ground.png')
background = BackGround(load_image('source\\background\\bg_tile_chapter_01_01.png'),WIDTH/2,HEIGHT/2,960,800)
black = load_image('source\\background\\black.png')

def UPDATE_overriding(self, dt):
    background.Move(-10 * dt)

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, HEIGHT - event.y


stage1.Update = UPDATE_overriding.__get__(stage1, Stage)

def Draw_overriding(self):
    background.Draw()
    ground.clip_draw(0, 0, 1024, 252, WIDTH // 2, 300,1200,250)
    black.clip_draw(0, 0, 1200, 800, WIDTH // 2, 50,1200,250)
    cnt = 1
    for c in Characters[cnt:]:
        c.anime[0][0].clip_draw(0,0,100,100,(cnt-1)*100+100,100,100,100)
        cnt += 1
stage1.Draw = Draw_overriding.__get__(stage1, Stage)