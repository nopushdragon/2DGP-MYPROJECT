
class Character:
    def __init__(self, anime, x, y, skill, status = None,frame=0, frameTimer=0.0, state="idle", flip=False):
                     # anime[0] = idle, anime[1] = walk, anime[2] = attack
        self.anime = anime
        self.x = x
        self.y = y
        self.frame = frame
        self.frameTimer = frameTimer
        self.state = state
        self.flip = flip
        self.skill = skill
        self.status = status
        self.attackMotionEnd = False
        self.attackMotionEndTimer = 0.0


    def Update(self, dt):
        self.frameTimer += dt
        if self.state == "idle":
            waitTime = 2.0
            idx = 0
        elif self.state == "walk":
            waitTime = 0.2
            idx = 1
        elif self.state == "skill_1" or self.state == "skill_2" or self.state == "skill_3":
            self.attackMotionEnd = True
            waitTime = 1.0
            idx = 2
        else:
            waitTime = 2.0
            idx = 0

        if (self.state == "skill_1" or self.state == "skill_2" or self.state == "skill_3") and self.frame == len(self.anime[2]) - 1:
            #self.attackMotionEnd = True
            pass

        if self.attackMotionEnd:
            self.attackMotionEndTimer += dt
            if self.attackMotionEndTimer >= 3.0:
                self.attackMotionEndTimer = 0.0
                self.frame = 0
                self.attackMotionEnd = False
                '''if self.state == "skill_1":
                    self.Skill_1()
                elif self.state == "skill_2":
                    self.Skill_2()
                elif self.state == "skill_3":
                    self.Skill_3()'''
                self.state = "using_skill"

        if not ((self.state == "skill_1" or self.state == "skill_2" or self.state == "skill_3") and self.frame == len(self.anime[2]) - 1):
            if self.frameTimer >= waitTime:
                self.frameTimer = 0.0
                self.frame = (self.frame + 1) % len(self.anime[idx])

        return idx  # 상태에 맞는 인덱스 반환


    def Draw(self, dt):
        if self.flip:
            self.anime[self.Update(dt)][self.frame].clip_composite_draw(0, 0, 100, 100, 0, 'h', self.x, self.y, 200, 200)
        else:
            self.anime[self.Update(dt)][self.frame].clip_draw(0, 0, 100, 100, self.x, self.y, 200, 200)

    def Skill_1(self):
        pass

    def Skill_2(self):
        pass

    def Skill_3(self):
        pass