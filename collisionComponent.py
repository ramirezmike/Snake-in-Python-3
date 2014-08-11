from component import Component
import messages

class CollisionComponent(Component):
    def eatHandle(self):
        self.parent.sendMessage(messages.APPLE_EATEN)

    def dieHandle(self):
        self.parent.sendMessage(messages.DEADLY_COLLISION)

    def receiveMessage(self, message):
        if (message == messages.PLAYER_MOVE):
            currentSpot = self.parent.screen.grid[self.parent.x][self.parent.y]
            if (currentSpot in self.collisionHandler):
                self.collisionHandler[currentSpot]()

    def __init__(self, parent):
        Component.__init__(self)
        self.parent = parent

        self.collisionHandler = {
            "@": self.eatHandle,
            "X": self.dieHandle,
            "\\u2591": self.dieHandle
        }

