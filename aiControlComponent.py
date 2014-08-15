import messages
from component import Component
from pathService import PathService

class AIControlComponent(Component):
    def handleAI(self):
        self.aquireTarget()
        #path = self.pathService._toTarget(self.parent, self.target)
        path = self.decidePath()
        self.parent.sendMessage(path)

    def decidePath(self):
        
        potentialPath = self.pathService.to(self.parent, self.target)
        if (potentialPath in self.pathHandling):
            checkX = self.parent.x + self.pathHandling[potentialPath]["x"]
            checkY = self.parent.y + self.pathHandling[potentialPath]["y"]
            if (self.screen.getFromScreen(checkX, checkY) == self.parent.content):
                target = { "x": checkX, "y": checkY }
                potentialPath = self.pathService.away(self.parent, target)
        return potentialPath

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
        self.initialCoolDown = 1
        self.coolDown = self.initialCoolDown
        self.target = { "x":0, "y":0 }
        self.messageHandling = {
            messages.APPLE_EATEN: self.aquireTarget,
        }
        self.pathHandling = {
            messages.MOVE_LEFT: { "x": -1, "y": 0 },
            messages.MOVE_RIGHT: { "x": 1, "y": 0 },
            messages.MOVE_UP: { "x": 0, "y": -1 },
            messages.MOVE_DOWN: { "x": 0, "y": 1 }
        }

