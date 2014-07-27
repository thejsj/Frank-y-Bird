import curses
from screen import Screen

class WelcomeScreen(Screen):

    def __init__(self):
        self.name = "Welcome Screen"

    def screen(self, screen):

        s = screen # For brevity
        max_y, max_x = s.getmaxyx() 

        s1 = "Frank-y Bird"
        s2 = "Press SPACE to jump...            "
        s3 = "Press Q or ESC to quit...         "
        s4 = "Press B for boost...              "
        s5 = "Easy (1), Medium (2), or Hard (3)?"

        # Box
        self.border = 15

        height = max(20, max_y - (self.border * 2))
        width  = max_x - (self.border * 2) 
        x      = self.border
        y      = (max_y - height) / 2

        box = s.derwin(height, width, y, x)
        box.clear()
        box.box()
        box.refresh()

        s.addstr(max_y / 2 - 7, self.center_x(s, s1), s1)
        s.addstr(max_y / 2 - 3, self.center_x(s, s2), s2)
        s.addstr(max_y / 2 - 1, self.center_x(s, s3), s3)
        s.addstr(max_y / 2 + 1, self.center_x(s, s4), s4)
        s.addstr(max_y / 2 + 5, self.center_x(s, s5), s5)

    def events(self, key):
        difficulty = None
        if key == 49:
            difficulty = 1
        elif key == 50:
            difficulty = 2
        elif key == 51:
            difficulty = 3
        return difficulty

