# data class contains information of a pixel point
class Point:
    def __init__(self, posX, posY, grey):
        self.posX = posX
        self.posY = posY
        self.grey = grey
    def distance(self):
        return ((self.posX ** 2) + (self.posY ** 2)) ** 0.5
