import os

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screenContainer = [[" " for i in range(height)] for j in range(width)]
        self.grid = [[" " for i in range(height)] for j in range(width)]

    def clear(self):
        #os.system("clear")
        os.system("cls")
        self.grid = self.screenContainer
        self.screenContainer = [[" " for i in range(self.height)] for j in range(self.width)]

    def render(self):
        self._printScreen()

    def _printScreen(self):
        for y in range(0, self.height):
            line = ""
            for x in range(0,self.width):
                line = line + self.screenContainer[x][y]
            print(line)

    def getFromScreen(self, x, y):
        return self.screenContainer[x][y]

    def addToScreen(self, x, y, content):
        self.screenContainer[x][y] = content
