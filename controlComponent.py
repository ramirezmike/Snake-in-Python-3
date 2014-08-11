import msvcrt
import messages
from component import Component

class ControlComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self.controls = {
            'M': messages.MOVE_RIGHT,
            'K': messages.MOVE_LEFT,
            'H': messages.MOVE_UP,
            'P': messages.MOVE_DOWN,
            'x': messages.ADD_NODE
        }

    def update(self, parent):
        key = ''
        if (msvcrt.kbhit()):
            key = msvcrt.getch()
        if (key in self.controls):
            parent.sendMessage(self.controls[key])
