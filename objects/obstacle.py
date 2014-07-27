from object import ScreenObject
import curses
import random

class Obstacle(ScreenObject):

    def __init__(self, screen, x, settings, bottom_limit):

        s = screen
        max_y, max_x = s.getmaxyx() 

        self.x = x
        self.y = 0

        self.holeHeight = settings.get('obsHoleHeigth')

        self.gap_area = 12
        self.y_gap_start = random.randint(0 + self.gap_area, (max_y - self.holeHeight - self.gap_area))
        self.y_gap_end = self.y_gap_start + self.holeHeight

        self.bottom_limit = bottom_limit

        self.width = settings.get('obsWidth')        

    def update(self):
        self.x = self.x - 1
        # Check if item should be DELETED - True for deleted
        if (self.x + self.width) < 0:
            return True
        else:
            return False

    def display(self, screen, settings):

        s = screen
        max_y, max_x = s.getmaxyx()

        x, width = self.getMaxXAndWidth(max_x)

        if x + width > 0 and self.x < max_x:
            # Second Box
            bottom_box = self.getBottomBox(max_y, max_x)
            self.drawBox(s, bottom_box['height'], bottom_box['width'], bottom_box['y'], bottom_box['x'])

            # First Box
            top_box = self.getTopBox(max_y, max_x)
            self.drawBox(s, top_box['height'], top_box['width'], top_box['y'], top_box['x'])

    def getMaxXAndWidth(self, max_x):
        # Make sure width doesn't overflow
        x     = self.x if (self.x) >= 0 else 0
        width = self.width if (self.x + self.width) < max_x else (max_x - self.x)
        width = width if (self.x) >= 0 else width + self.x

        return x, width

    def getTopBox(self, max_y, max_x):

        x, width = self.getMaxXAndWidth(max_x)
        y      = 0
        height = self.y_gap_start

        return {
            'x'      : x,
            'y'      : y,
            'width'  : width, 
            'height' : height,
            'left'   : x,
            'right'  : x + width,
            'top'    : y,
            'bottom' : y + height
        }

    def getBottomBox(self, max_y, max_x):
    
        x, width = self.getMaxXAndWidth(max_x)
        y      = self.y_gap_end
        height = max_y - self.bottom_limit - self.y_gap_end

        return {
            'x'      : x,
            'y'      : y,
            'width'  : width,
            'height' : height,
            'left'   : x,
            'right'  : x + width,
            'top'    : y,
            'bottom' : y + height
        }

    def drawBox(self, s, height, width, y, x):
        box = s.derwin(height, width, y, x)
        box.bkgd("*", curses.color_pair(2))
        box.box()
        box.refresh()

    def checkCollisionForSingleBox(self, r1, r2):

        def range_overlap(a_min, a_max, b_min, b_max):
            '''Neither range is completely greater than the other'''

            if (b_min < a_max) and (b_min > a_min):
                return b_min
            elif (a_min < b_max) and (a_min > b_min):
                return a_min
            else:
                return False

        range_overlap_horizontal = range_overlap(r1['left'], r1['right'], r2['left'], r2['right'])
        range_overlap_vertical   = range_overlap(r1['top'], r1['bottom'], r2['top'], r2['bottom'])

        if range_overlap_horizontal is not False and range_overlap_vertical is not False:
            return {
                'x' : range_overlap_horizontal,
                'y' : range_overlap_vertical
            }
        else:
            return False

    def checkCollision(self, screen, input_rectangle):

        s = screen
        max_y, max_x = s.getmaxyx()

        if input_rectangle['right'] >= self.x and input_rectangle['x'] <= self.x + self.width:
            top_box    = self.getTopBox(max_y, max_x)           
            bottom_box = self.getBottomBox(max_y, max_x)  

            top_box_intersecting = self.checkCollisionForSingleBox(input_rectangle, top_box)
            bottom_box_intersecting = self.checkCollisionForSingleBox(input_rectangle, bottom_box)

            if top_box_intersecting is not False:
                return top_box_intersecting

            if bottom_box_intersecting is not False:
                return bottom_box_intersecting

        return False




