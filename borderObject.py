from object import Object

class BorderObject(Object):
    def __init__(self, parent, content, screen):
        Object.__init__(self, parent, content, screen)

    def update(self):
        for x in range(0, self.screen.width):
            self.screen.addToScreen(x, 0, self.content)
            self.screen.addToScreen(x, self.screen.height - 1, self.content)
        for y in range(0, self.screen.height):
            self.screen.addToScreen(0, y, self.content)
            self.screen.addToScreen(self.screen.width - 1, y, self.content)

