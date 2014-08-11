from object import Object

class ScoreObject(Object):
    def __init__(self, parent, content, screen):
        Object.__init__(self, parent, content, screen)
        self.score = 0

    def update(self):
        print("Score: " + str(self.score))

    def addPoint(self):
        self.score = self.score + 1
