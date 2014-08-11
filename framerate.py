import time

class Framerate:
    def __init__(self):
        self.start = time.time()
        self.end = time.time()
        self.avgFPS = 0
        self.frameCount = 0

    def render(self):
        self._print()
        self.frameCount = self.frameCount + 1
        self.end = time.time()
        if (self.end - self.start > 1):
            self.start = time.time()
            self.avgFPS = self.frameCount
            self.frameCount = 0

    def _print(self):
        print((self.avgFPS))
