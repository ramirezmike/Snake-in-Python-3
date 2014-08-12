import messages
from component import Component
from pathService import PathService

class AIControlComponent(Component):
    def handleAI(self):
        self.aquireTarget()
        path = self.pathService.toTarget(self.parent, self.target)
        self.parent.sendMessage(path)

    def handleCooldown(self):
        self.coolDown = self.coolDown - 1
        if (self.coolDown < 0):
            self.handleAI()
            self.coolDown = self.initialCoolDown

    def update(self, parent):
        self.handleCooldown()

    def receiveMessage(self, message):
        if (message in self.messageHandling):
            self.messageHandling[message]()

    def aquireTarget(self):
        #temporary method - eventually have apple broadcast location
        target = self.parent.parent.gameObjects["apple"]
        self.target["x"] = target.x
        self.target["y"] = target.y

    def __init__(self, parent, screen):
        Component.__init__(self)
        self.parent = parent
        self.screen = screen
        self.pathService = PathService(self, screen)
        self.initialCoolDown = 10
        self.coolDown = self.initialCoolDown
        self.target = { "x":0, "y":0 }
        self.messageHandling = {
            messages.APPLE_EATEN: self.aquireTarget,
        }

