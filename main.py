from gamemanager import *
import sound

if __name__ == '__main__':
    sound.play_main_bgm()
    gamemanager.nowScene = "title"
    main()
