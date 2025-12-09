from pico2d import *

main_bgm = load_music('source\\sound\\main2.mp3')
stage1_bgm = load_music('source\\sound\\main4.mp3')

def play_main_bgm():
    main_bgm.set_volume(40)
    main_bgm.repeat_play()

def play_stage1_bgm():
    stage1_bgm.set_volume(40)
    stage1_bgm.repeat_play()

click_sound = load_wav('source\\sound\\click.mp3')
click_sound.set_volume(32)

start_sound = load_wav('source\\sound\\시작합니다.mp3')
start_sound.set_volume(32)

friend_sound = load_wav('source\\sound\\친구탭.mp3')
friend_sound.set_volume(32)

shop_sound = load_wav('source\\sound\\상점탭.mp3')
shop_sound.set_volume(32)

upgrade_sound = load_wav('source\\sound\\강화탭.mp3')
upgrade_sound.set_volume(32)

battle_start_sound = load_wav('source\\sound\\전투하러가시죠.mp3')
battle_start_sound.set_volume(32)