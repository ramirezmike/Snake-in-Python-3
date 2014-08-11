from object import Object
from controlComponent import ControlComponent
from moveComponent import MoveComponent
from collisionComponent import CollisionComponent
from tailComponent import TailComponent
import messages

class PlayerObject(Object):
    def __init__(self, parent, content, screen):
        Object.__init__(self, parent, content, screen)

        self.x = 2
        self.y = 2
        self.speed = 5
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        self.controlComponent = ControlComponent()
        self.moveComponent = MoveComponent(self, screen)
        self.collisionComponent = CollisionComponent(self)
        self.tailComponent = TailComponent()
        self.components.append(self.controlComponent)
        self.components.append(self.moveComponent)
        self.components.append(self.collisionComponent)
        self.components.append(self.tailComponent)
        self.tailComponent.addNode(self)

    def update(self):
        self.controlComponent.update(self)
        self.moveComponent.update(self)
        self.tailComponent.update(self)
        self.screen.addToScreen(self.x, self.y, self.content)
