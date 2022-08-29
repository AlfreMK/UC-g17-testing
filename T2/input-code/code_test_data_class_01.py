# data class contains information of a pixel point
class Point:
    def __init__(self, x, y, grey):
        self.x = x
        self.y = y
        self.grey = grey
    def setGrey(self, grey):
        self.grey = grey
    def getGrey(self):
        return self.grey
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self):
        return self.y
