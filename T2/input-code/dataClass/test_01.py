# data class contains information of a pixel point
class Point:
    def __init__(self, posX, posY, grey):
        self.posX = posX
        self.posY = posY
        self.gre = grey
    def getX(self):
        return self.posX
    def setX(self, posX):
        self.posX = posX

