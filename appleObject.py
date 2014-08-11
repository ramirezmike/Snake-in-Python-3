from object import Object
from random import randrange

class AppleObject(Object):
    def __init__(self, parent, content, screen):
        Object.__init__(self, parent, content, screen)
        self.moveApple()

    def moveApple(self):
        self.x = randrange(1, self.screen.width)
        self.y = randrange(1, self.screen.height)

