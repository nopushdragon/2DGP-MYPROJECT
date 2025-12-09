from skill_folder.skill_base import Skill
from pico2d import *


def create_skill_2(x, y, flip):
    skill = Skill(
        [load_image(f'source\\skill\\enya\\enya_bird0{i}.png') for i in range(1, 4)],
        x + 100 - (200 * int(flip)), y - 30, 80, 20, 5,
        0, 500, 0, 0.0, 0.1, flip, True, "enemy_solo")

    def Update_override(self, dt, target_x, target_y):
        if self.visible:
            self.frameTimer += dt

            # 이동 방향 처리
            if not self.flip:
                self.x += self.speed * dt
                if self.x > target_x:
                    self.visible = False
            else:
                self.x -= self.speed * dt
                if self.x < target_x:
                    self.visible = False

            # 프레임 전환 처리
            if self.frameTimer >= self.waitTime:
                self.frameTimer = 0.0
                '''if self.frame < len(self.anime) - 1:
                     self.frame += 1'''
                self.frame = (self.frame + 1) % len(self.anime)
    skill.Update = Update_override.__get__(skill, Skill)

    def Draw_override(self):
        if self.visible:
            if self.flip == False:
                self.anime[self.frame].clip_draw(0, 0, self.anime[self.frame].w, self.anime[self.frame].h, self.x, self.y, 100, 100)
            elif self.flip == True:
                self.anime[self.frame].clip_composite_draw(0, 0, self.anime[self.frame].w, self.anime[self.frame].h, 0, 'h', self.x, self.y, 100, 100)
    skill.Draw = Draw_override.__get__(skill, Skill)

    def apply_effect_override(self, target, atk):
        for t in target:
            damage = atk - t.status["def"]
            if damage <= 10:
                damage = 10
            t.status["nowhp"] -= damage
            if t.status["nowhp"] < 0:
                t.status["nowhp"] = 0
    skill.apply_effect = apply_effect_override.__get__(skill, Skill)


    return skill