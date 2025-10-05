from pico2d import *
from gamemanager import WIDTH

class SpeedNum:
    def __init__(self,image,x=1000,y=700,speed =0):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed

    def Update(self):
        self.x -= self.speed

    def Draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y, 20, 20)

speedBar = load_image('source\\ui\\speedbar.png')
p1 = SpeedNum(load_image('source\\ui\\p1.png'))
p2 = SpeedNum(load_image('source\\ui\\p2.png'))
p3 = SpeedNum(load_image('source\\ui\\p3.png'))
p4 = SpeedNum(load_image('source\\ui\\p4.png'))
e1 = SpeedNum(load_image('source\\ui\\e1.png'))
e2 = SpeedNum(load_image('source\\ui\\e2.png'))
e3 = SpeedNum(load_image('source\\ui\\e3.png'))
e4 = SpeedNum(load_image('source\\ui\\e4.png'))
spdNums = [p1,p2,p3,p4,e1,e2,e3,e4]

class Speedbar:
    def Update(self):
        for n in spdNums:
            n.Update()
            # 여기에 속도 도착했을때 처리하고 battle에 아마 캐릭터 턴 넘겨줘야 할듯

    def Draw(self):
        speedBar.clip_draw(0, 0, 1200, 800, WIDTH // 2, 700, 800, 20)
        for n in spdNums:
            if not n.speed == 0:
                n.Draw()