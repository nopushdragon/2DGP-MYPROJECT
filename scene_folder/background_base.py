from gamemanager import WIDTH, HEIGHT

class BackGround:
    def __init__(self, image, x, y,width, height, flip=False):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.flip = flip

    def Draw(self):
        if self.flip:
            self.image.clip_draw(0, 0, self.width, self.height, self.x, self.y)
            self.image.clip_composite_draw(0, 0, self.width, self.height, 0, 'h', self.x - self.width, self.y,self.width,self.height)
            self.image.clip_composite_draw(0, 0, self.width, self.height, 0, 'h', self.x + self.width, self.y,self.width,self.height)
        else:
            self.image.clip_draw(0, 0, self.width, self.height, self.x, self.y)
            self.image.clip_draw(0, 0, self.width, self.height, self.x - self.width, self.y)
            self.image.clip_draw(0, 0, self.width, self.height, self.x + self.width, self.y)

    def Move(self, mx):
        self.x += mx
        if self.x > WIDTH:
            self.x -= self.width
        elif self.x < 0:
            self.x += self.width