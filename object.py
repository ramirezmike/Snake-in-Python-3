class Object:
    def __init__(self, parent, content, screen):
        self.x = 0
        self.y = 0
        self.parent = parent
        self.content = content
        self.components = []
        self.screen = screen

    def update(self):
        self.screen.addToScreen(self.x, self.y, self.content)

    def sendMessage(self, message):
        for component in self.components:
            component.receiveMessage(message)
        self.parent.receiveMessage(message)
