import currency
from pico2d import *

class Stage :
    ticket = 0
    upgrade_stone = 0

    def __init__(self):
        pass

    def Reset(self):
        pass

    def Update(self, dt):
        pass

    def Draw_background(self):
        pass

    def Draw_choicechar(self):
        pass

    def get_rewards(self):
        currency.ticket += self.ticket
        currency.upgrade_stone += self.upgrade_stone