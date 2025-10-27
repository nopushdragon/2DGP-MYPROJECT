from gamemanager import WIDTH

class Skill:
    def __init__(self, anime, x, y, width, height,maxCooltime,nowCooltime=0,speed=0,frame=0, frameTimer=0.0, waitTime=0.1, flip = False, visible = False, type = None):
        self.anime = anime
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.maxCooltime = maxCooltime
        self.nowCooltime = nowCooltime
        self.speed = speed
        self.frame = frame
        self.frameTimer = frameTimer
        self.waitTime = waitTime
        self.flip = flip
        self.visible = visible
        self.type = type # party_solo, enemy_solo, party_all, enemy_all

    def Update(self, dt):
        pass

    def Draw(self):
        if self.visible:
            if self.flip == False:
                self.anime[self.frame].clip_draw(0, 0, self.width, self.height, self.x, self.y, 100, 30)
            elif self.flip == True:
                self.anime[self.frame].clip_composite_draw(0, 0, self.width, self.height, 0, 'h', self.x, self.y, 100, 30)

    def apply_effect(self, target, damage):
        pass
