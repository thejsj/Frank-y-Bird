class Difficulty:

    def __init__(self, callback):
        self.value = None
        self.callback = callback

    def __nonzero__(self):
        if self.value is None:
            return False
        else:
            return True

    def __int__(self) :
        if self.value is None:
            return 0
        else:
            return int(self.value)

    def set(self, value) :
        try:
            if int(value) == value and value > 0 and value < 4:
                self.value = value
                self.callback()
            else:
                self.value = None 
        except TypeError:
            self.value = None

    def getHTime(self):
        if self.value == 1:
            return 0.5
        elif self.value == 2:
            return 0.2
        elif self.value == 2:
            return 0.1
        return 0.5