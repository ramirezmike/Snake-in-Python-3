from framerate import Framerate
from screen import Screen
from gameController import GameController

width = 20#60
height = 20#35

screen = Screen(width,height)
gameController = GameController(screen)
framerate = Framerate()

while True:
    screen.clear()
    gameController.update()
    framerate.render()
    screen.render()
