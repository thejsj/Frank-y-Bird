class Screen:
    
    def center_x(self, screen, string):
        from math import floor

        maxy, maxx = screen.getmaxyx()
        length = len(string)
        return int(floor(maxx/2) - floor(length/2))

    def drawBox(self, s, height, width, y, x):
        box = s.derwin(height, width, y, x)
        box.bkgd("*")
        box.box()
        box.refresh()