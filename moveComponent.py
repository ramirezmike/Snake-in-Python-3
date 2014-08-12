from component import Component
import messages

class MoveComponent(Component):
    def update(self, parent):
        self.moveDelay = self.moveDelay - 1
        if (self.moveDelay < 0):
            self.move()
            self.moveDelay = parent.speed

    def move(self):
        self.parent.x = self.parent.x + self.moveX
        self.parent.y = self.parent.y + self.moveY
        self.parent.sendMessage(messages.PLAYER_MOVE)

    def receiveMessage(self, message):
        if (message in self.messageHandling):
            self.messageHandling[message]()

    def moveUp(self):
        if (self.moveY != 1):
            self.moveY = -1
            self.moveX = 0
    def moveDown(self):
        if (self.moveY != -1):
            self.moveY = 1
            self.moveX = 0
    def moveLeft(self):
        if (self.moveX != 1):
            self.moveY = 0
            self.moveX = -1
    def moveRight(self):
        if (self.moveX != -1):
            self.moveY = 0
            self.moveX = 1

    def __init__(self, parent):
        Component.__init__(self)
        self.parent = parent
        self.moveDelay = parent.speed
        self.moveX = 0
        self.moveY = 0
        self.messageHandling = {
            messages.MOVE_RIGHT : self.moveRight,
            messages.MOVE_LEFT : self.moveLeft,
            messages.MOVE_UP : self.moveUp,
            messages.MOVE_DOWN : self.moveDown
        }
