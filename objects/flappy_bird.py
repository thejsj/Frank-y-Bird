from object import ScreenObject
import curses

class FlappyBird(ScreenObject):

    def __init__(self):
        self.str = "0>"
        self.x = 5
        self.y = 10
        self.width = len(self.str)
        self.height = 1

    def update(self):
        self.y += 1

    def pushUp(self):
        self.y -= 4

    def display(self, screen, settings):
        s = screen
        s.addstr(self.y, self.x, self.str, curses.color_pair(2))

    def rectangle(self):
        return {
            'x'      : self.x,
            'y'      : self.y,
            'width'  : self.width,
            'height' : self.height,
            'left'   : self.x,
            'right'  : self.x + self.width,
            'top'    : self.y,
            'bottom' : self.y + self.height
        }