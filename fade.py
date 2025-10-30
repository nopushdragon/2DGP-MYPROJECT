from pico2d import *
from stages import Stages
import gamemanager

black_fade_image = load_image('source\\background\\fade_black.png')

STATE_IDLE = 0
STATE_FADING_OUT = 1
STATE_FADING_IN = 2

FADE_SPEED = 0.02

fade_state = STATE_IDLE  # 현재 페이드 상태
fade_alpha = 0.0        # 현재 알파 값

next_scene = ""


def fade_out(scene):
    global next_scene, fade_state, fade_alpha

    fade_alpha = 0.0
    next_scene = scene
    fade_state = STATE_FADING_OUT


def update():
    global fade_alpha, fade_state

    if not fade_state == STATE_IDLE:
        if fade_state == STATE_FADING_OUT:
            fade_alpha += FADE_SPEED
            if fade_alpha >= 1.0:
                fade_alpha = 1.0

                if "stage" in next_scene:
                    Stages[int(next_scene[-1]) - 1].Reset()
                    gamemanager.nowScene = f"{next_scene}_ready"
                    gamemanager.nowstage = Stages[int(next_scene[-1]) - 1]

                fade_state = STATE_FADING_IN
        elif fade_state == STATE_FADING_IN:
            fade_alpha -= FADE_SPEED
            if fade_alpha <= 0.0:
                fade_alpha = 0.0
                fade_state = STATE_IDLE  # 페이드 완료


def draw():
    if fade_state != STATE_IDLE:
        black_fade_image.opacify(fade_alpha)
        print(fade_alpha)
        # clip_draw 사용하여 전체 화면에 그립니다.
        black_fade_image.clip_draw(0, 0, 120, 80, gamemanager.WIDTH // 2, gamemanager.HEIGHT // 2,1200,800)

