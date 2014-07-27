import curses
from screen import Screen

class GameOverScreen(Screen):

    def __init__(self):
        self.name = "Welcome Screen"

    def screen(self, screen, points):

        s = screen # For brevity

        max_y, max_x = s.getmaxyx() 

        # Box
        self.border = 15

        height = max_y - (self.border * 2) 
        width  = max_x - (self.border * 2) 
        x      = self.border
        y      = self.border

        box = s.derwin(height, width, y, x)
        box.clear()
        box.box()
        box.refresh()

        # Messages
        s1 = "GAME OVER"
        s2 = "Your Score : " + str(points)
        s3 = "Press ESC or Q to quit"

        s.addstr(max_y / 2 - 2, self.center_x(s, s1), s1)
        s.addstr(max_y / 2, self.center_x(s, s2), s2)
        s.addstr(max_y / 2  + 2, self.center_x(s, s3), s3)