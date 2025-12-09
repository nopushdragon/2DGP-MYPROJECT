from pico2d import *

main_bgm = load_music('source\\sound\\main2.mp3')
stage1_bgm = load_music('source\\sound\\main4.mp3')

def play_main_bgm():
    main_bgm.set_volume(64)
    main_bgm.repeat_play()

def play_stage1_bgm():
    stage1_bgm.set_volume(64)
    stage1_bgm.repeat_play()

click_sound = load_wav('source\\sound\\click.wav')