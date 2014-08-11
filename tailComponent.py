from object import Object
from component import Component
import messages

class TailComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self.tailNodes = []
        self.previousHeadX = 1
        self.previousHeadY = 1
        self.tailIndex = 0
        self.addNodeOnUpdate = False

    def update(self, parent):
        for i in range(0, len(self.tailNodes)):
            self.tailNodes[i].update()
        self.previousHeadX = parent.x
        self.previousHeadY = parent.y
        if (self.addNodeOnUpdate):
            self.addNode(parent)
            self.addNodeOnUpdate = False

    def addNode(self, parent):
        newNode = Object(self, parent.content, parent.screen)
        newNode.x = self.previousHeadX
        newNode.y = self.previousHeadY
        self.tailNodes.append(newNode)

    def receiveMessage(self, message):
        if (message == messages.PLAYER_MOVE):
            self.moveTail()
        if (message == messages.ADD_NODE):
            self.addNodeOnUpdate = True

    def moveTail(self):
        self.tailNodes[self.tailIndex].x = self.previousHeadX
        self.tailNodes[self.tailIndex].y = self.previousHeadY
        self.moveIndex()

    def moveIndex(self):
        self.tailIndex = self.tailIndex - 1
        if (self.tailIndex < 0):
            self.tailIndex = len(self.tailNodes) - 1
