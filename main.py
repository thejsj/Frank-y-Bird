#! /usr/bin/env python

import sys
import time
import curses
from collections import namedtuple

import logging
logging.basicConfig(filename='main.log',level=logging.DEBUG)

# Import Screens
from screens.welcome_screen import WelcomeScreen
from screens.game_screen import GameScreen
from difficulty import Difficulty
from settings import Settings

KEY = "KEY"
K_B = ord("b")
K_Q = ord("q")
K_SPACE = ord(" ")
K_ESCAPE = 27
#fix freezes [issue#1]
KEYS = [K_B, K_Q, K_SPACE, K_ESCAPE]

class App(object):

    def __init__(self):
        # Define all game state variables
        self.welcome_screen = WelcomeScreen()
        self.game_screen = GameScreen()
        self.difficulty = Difficulty(self.setOptions)
        self.done = False

        self.settings = Settings()
        self.settings.set('hTime', 0.3)

        # Define all the Curses stuff
        curses.initscr()
        curses.start_color()
        # curses.use_default_colors()

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        self.screen = curses.newwin(0, 0)
        self.screen.keypad(1)
        self.screen.nodelay(1)
        
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

    def setOptions(self):
        self.settings.set('hTime', self.difficulty.getHTime())
        self.settings.set('obsWidth',10)
        self.settings.set('obsHoleHeigth', 7)
        self.settings.set('obsSpacing',15)

        self.game_screen.initGame(self.settings) 

    def deinit(self):
        self.screen.nodelay(0)
        self.screen.keypad(0)
        curses.flash()
        curses.beep()
        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        curses.endwin()
        sys.exit(1)

    # Event Loop Functions

    def events(self):
        # Global Events
        key = self.screen.getch()
        if key == K_ESCAPE or key is K_Q:
            self.deinit()

        # State-depent events
        if not self.difficulty:
            self.difficulty.set(self.welcome_screen.events(key))
        else:
            self.game_screen.events(key)

    def update(self):
        if self.difficulty:
            self.done = self.game_screen.update(self.screen, self.settings)

        if self.done:
            self.difficulty.set(None)
            # self.deinit()

    def render(self):
        self.screen.erase()

        # Render Current State
        if not self.difficulty:
            self.welcome_screen.screen(self.screen)
        elif not self.done:
            self.game_screen.screen(self.screen, self.settings)
        else:
            pass

        # Refresh and Loop
        self.screen.refresh()
        time.sleep(self.settings.get('hTime'))

    def loop(self):
        while True:
            self.events()
            self.update()
            self.render()

def main():
    app = App()
    app.loop()

if __name__ == "__main__":
    main()

