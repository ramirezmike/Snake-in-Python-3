from playerObject import PlayerObject
from borderObject import BorderObject
from appleObject import AppleObject
from scoreObject import ScoreObject
import messages

class GameController:
    def eatHandle(self):
        self.gameObjects["score"].addPoint() 
        self.gameObjects["player"].sendMessage(messages.ADD_NODE)
        self.gameObjects["apple"].moveApple()

    def dieHandle(self):
        self.newGame()

    def update(self):
        for key, obj in list(self.gameObjects.items()):
            obj.update()

    def newGame(self):
        self.gameObjects["score"] = ScoreObject(self, 0, screen)
        self.gameObjects["player"] = PlayerObject(self, '\u2591', self.screen)
        self.gameObjects["apple"].moveApple()
        self.gameObjects["player"].sendMessage(messages.MOVE_RIGHT)

    def receiveMessage(self, message):
        if (message in self.eventHandlers):
            self.eventHandlers[message]()

    def __init__(self, screen):
        self.gameObjects = {}
        self.screen = screen

        self.eventHandlers = {
            messages.APPLE_EATEN: self.eatHandle,
            messages.DEADLY_COLLISION: self.dieHandle
        }
        self.gameObjects["score"] = ScoreObject(self, 0, screen)
        self.gameObjects["player"] = PlayerObject(self, '\u2591', screen)
        self.gameObjects["apple"] = AppleObject(self, "@", screen)
        self.gameObjects["border"] = BorderObject(self, '\u2591', screen)
        self.gameObjects["player"].sendMessage(messages.MOVE_RIGHT)
