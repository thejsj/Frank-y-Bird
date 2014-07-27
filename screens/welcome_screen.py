import curses
from screen import Screen

class WelcomeScreen(Screen):

    def __init__(self):
        self.name = "Welcome Screen"

    def screen(self, screen):

        s = screen # For brevity

        s1 = "Frank-y Bird"
        s2 = "Press SPACE to jump...       "
        s3 = "Press Q or ESC to quit...    "
        s4 = "Press B for boost...         "
        s5 = "Easy (1), Medium (2), or Hard (3)? "

        s.addstr(5, self.center_x(s, s1), s1)
        s.addstr(7, self.center_x(s, s2), s2)
        s.addstr(8, self.center_x(s, s3), s3)
        s.addstr(9, self.center_x(s, s4), s4)

        # Show Difficuly
        s.addstr(15, 0, s5)

    def events(self, key):
        difficulty = None
        if key == 49:
            difficulty = 1
        elif key == 50:
            difficulty = 2
        elif key == 51:
            difficulty = 3
        return difficulty

