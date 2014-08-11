import msvcrt
import messages
from component import Component

class ControlComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self.controls = {
            b'M': messages.MOVE_RIGHT,
            b'K': messages.MOVE_LEFT,
            b'H': messages.MOVE_UP,
            b'P': messages.MOVE_DOWN,
            b'x': messages.ADD_NODE
        }

    def update(self, parent):
        key = ''
        if (msvcrt.kbhit()):
            key = msvcrt.getch()
        if (key in self.controls):
            parent.sendMessage(self.controls[key])
