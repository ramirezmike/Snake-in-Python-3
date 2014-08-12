import messages

class PathService():
    def toTarget(self, currentPosition, target):
        curX = currentPosition.x
        curY = currentPosition.y
        tarX = target["x"]
        tarY = target["y"]
        result = ""

        verDistance = tarY - curY
        hozDistance = tarX - curX
        if (self.lastMoveHorizontal):
            if (verDistance > 0):
                self.lastMoveHorizontal = False
                result = messages.MOVE_DOWN
            elif (verDistance < 0):
                self.lastMoveHorizontal = False
                result = messages.MOVE_UP
        else:
            if (hozDistance > 0):
                self.lastMoveHorizontal = True 
                result = messages.MOVE_RIGHT
            elif (hozDistance < 0):
                self.lastMoveHorizontal = True 
                result = messages.MOVE_LEFT
        return result
            
    def __init__(self, parent, screen):
        self.parent = parent
        self.screen = screen
        self.lastMoveHorizontal = True
