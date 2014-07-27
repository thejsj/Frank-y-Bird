import curses
from screen import Screen

class PointScreen(Screen):

    def __init__(self):
        self.name = "Game Screen"

    def display(self, screen, settings, points):

        s = screen

        maxy, maxx = s.getmaxyx()

        # Display line
        line = self.generateLine(maxx)
        s.addstr(maxy - 4, 0, line, curses.color_pair(2))

        # Display Score
        s.addstr(maxy - 2, 5, "Points: " + str(points), curses.color_pair(2))

    def generateLine(self, length):
        return "".join([ "-" if i % 2 == 0 else " " for i in range(length)])