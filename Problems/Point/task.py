import math


class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def dist(self, p2):
        return math.sqrt((self.x1 - p2.x1) ** 2 + (self.y1 - p2.y1) ** 2)

