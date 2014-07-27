import curses
from screen import Screen
from point_screen import PointScreen
from objects.obstacle_manager import ObstacleManager
from objects.flappy_bird import FlappyBird

KEY = "KEY"
K_B = ord("b")
K_Q = ord("q")
K_SPACE = ord(" ")
K_ESCAPE = 27

class GameScreen(Screen):

    def __init__(self):
        self.name = "Game Screen"

        self.frames = 0
        self.points = 0
        self.done = False
        self.final_x = None
        self.final_y = None

        # Visual Variables
        self.bottom_limit = 4

        self.flappy_bird = FlappyBird()

        self.points_screen = PointScreen()

        self.obstacles = ObstacleManager()

    def initGame(self, settings):
        # Set Other Stuff
        self.obsTime = (settings.get('obsWidth') + settings.get('obsSpacing')) / 2

    def screen(self, screen, settings):

        s = screen # For brevity   

        maxy, maxx = s.getmaxyx() 

        # Display Flappy Bird
        self.flappy_bird.display(screen, settings)

        # Display Obstacles
        self.obstacles.display(screen, settings)

        # Display Points Screen
        self.points_screen.display(screen, settings, self.points)

        if self.done:
            s.addstr(self.final_y, self.final_x, "#", curses.color_pair(1))

    def update(self, screen, settings):

        # Udate Flappy Bird
        if not self.done:
            self.flappy_bird.update()

            # Update Obstacles
            self.points = self.obstacles.update(screen, self.frames, self.bottom_limit, settings, self.points)
            self.done, _x, _y  = self.obstacles.checkCollision(screen, self.flappy_bird.rectangle())

            if self.done:
                self.final_x = _x
                self.final_y = _y

            # Increase number of frames
            self.frames += 1            

        return self.done, self.points

    def events(self, key):
        if key == K_SPACE:
            self.flappy_bird.pushUp()

