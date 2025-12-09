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

win_sound = load_wav('source\\sound\\승리.mp3')
win_sound.set_volume(32)

lose_sound = load_wav('source\\sound\\패배.mp3')
lose_sound.set_volume(32)

upgrade_stone_sound = load_wav('source\\sound\\강화석.mp3')
upgrade_stone_sound.set_volume(32)

hero_sound = load_wav('source\\sound\\영웅이닷.mp3')
hero_sound.set_volume(32)

fight_start_sound = load_wav('source\\sound\\배틀시작.mp3')
fight_start_sound.set_volume(32)

upgrade_button = load_wav('source\\sound\\upgrade.mp3')
upgrade_button.set_volume(32)

skill_1_sound = load_wav('source\\sound\\스킬1.mp3')
skill_1_sound.set_volume(32)