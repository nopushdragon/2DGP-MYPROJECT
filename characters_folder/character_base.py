from pico2d import *

class Character:
    evo = 1 #진화 단계
    illust = None
    nameBox = load_image('source\\ui\\namebox.png')
    namefont = load_font('source\\ui\\DungGeunMo.ttf', 40)
    #skill_1_icon = None
    #skill_2_icon = None
    #skill_3_icon = None
    skill_1_icon = load_image(f'source\\skill_icon\\gunman\\hope_1103.png')
    skill_2_icon = load_image(f'source\\skill_icon\\gunman\\hope_1101.png')
    skill_3_icon = load_image(f'source\\skill_icon\\gunman\\hope_1102.png')

    def __init__(self, anime, x, y, skill, status = None,frame=0, frameTimer=0.0, state="idle", flip=False, name = None, get = False):
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
        self.name = name
        # 현재 애니메이션 인덱스 저장용
        self.anim_idx = 0
        self.get = get


    def Update(self, dt):
        self.frameTimer += dt
        if self.state == "idle":
            waitTime = 1.0
            idx = 0
        elif self.state == "walk":
            waitTime = 0.2
            idx = 1
        elif self.state == "skill_1" or self.state == "skill_2" or self.state == "skill_3":
            self.attackMotionEnd = True
            waitTime = 0.3
            idx = 2
        else:
            waitTime = 2.0
            idx = 0

        # 현재 상태에 맞는 애니메이션 인덱스 저장
        self.anim_idx = idx

        if (self.state == "skill_1" or self.state == "skill_2" or self.state == "skill_3") and self.frame == len(self.anime[2]) - 1:
            #self.attackMotionEnd = True
            pass

        if self.attackMotionEnd:
            self.attackMotionEndTimer += dt
            if self.attackMotionEndTimer >= 1.0 + waitTime * 2:
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


    def Draw(self):
        # Update는 GameUpdate에서 한 번만 호출되도록 변경했으므로 Draw에서는 상태를 바꾸지 않습니다.
        if self.flip:
            self.anime[self.anim_idx][self.frame].clip_composite_draw(0, 0, 100, 100, 0, 'h', self.x, self.y, 200, 200)
        else:
            self.anime[self.anim_idx][self.frame].clip_draw(0, 0, 100, 100, self.x, self.y, 200, 200)

    def Skill_1(self):
        pass

    def Skill_2(self):
        pass

    def Skill_3(self):
        pass

    def Draw_turn(self):
        self.illust.clip_draw(0, 500, self.illust.w, self.illust.h, 150, 150, 300, 300)
        self.nameBox.clip_draw(125, 0, 125, 33, 150, 25, 300, 50)
        self.namefont.draw(100, 24, self.name, (0, 0, 0))
        self.namefont.draw(100, 26, self.name, (0, 0, 0))
        self.namefont.draw(99, 25, self.name, (0, 0, 0))
        self.namefont.draw(101, 25, self.name, (0, 0, 0))
        self.namefont.draw(100, 25, self.name, (230, 230, 230))
        self.skill_1_icon.clip_draw(0, 0, self.skill_1_icon.w, self.skill_1_icon.h, 850, 100, 100, 100)
        self.skill_2_icon.clip_draw(0, 0, self.skill_1_icon.w, self.skill_1_icon.h, 975, 100, 100, 100)
        self.skill_3_icon.clip_draw(0, 0, self.skill_1_icon.w, self.skill_1_icon.h, 1100, 100, 100, 100)

    def evolution(self, new_anime, new_illust, new_nameBox, new_namefont, new_skill_icons, new_status):
        pass

    def reset(self):
        self.anim_idx = 0
        self.frame = 0
        self.frameTimer = 0.0
        self.state = "idle"
        self.skill = []
        self.attackMotionEnd = False
        self.attackMotionEndTimer = 0.0
        self.status["nowhp"] = self.status["maxhp"]
        self.status["atk"] = self.status["origin_atk"]
        self.status["def"] = self.status["origin_def"]
        self.status["speed"] = self.status["origin_speed"]
        self.status["condition"] = []
