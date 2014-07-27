from object import ScreenObject
from obstacle import Obstacle
import curses
import random

import logging
logging.basicConfig(filename='main.log',level=logging.DEBUG)

class ObstacleManager(ScreenObject):

    def __init__(self):
        self.obstacles = []
        self.starting_gap = 20

    def display(self, screen, settings):
        for obstacle in self.obstacles:
            obstacle.display(screen, settings)

    def update(self, screen, frame_count, bottom_limit, settings, points):

        s = screen
        max_y, max_x = s.getmaxyx()

        # First Frame, append a couple of obstacle
        if frame_count == 0:

            x = self.starting_gap
            while x < (max_x + self.starting_gap):
                self.obstacles.append(Obstacle(screen, x, settings, bottom_limit))
                x += self.starting_gap            

        for obstacle in self.obstacles:
            delete_obstacle = obstacle.update()
            if delete_obstacle:
                self.obstacles.pop(0)
                self.obstacles.append(Obstacle(screen, max_x, settings, bottom_limit))
                points += 1

        return points

    def checkCollision(self, screen, rectangle):

        for obstacle in self.obstacles:
            obstacle_collision = obstacle.checkCollision(screen, rectangle)
            if obstacle_collision:
                return True, obstacle_collision['x'], obstacle_collision['y']

        return False, None, None