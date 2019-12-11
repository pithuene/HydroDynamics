import math
from vector import Vector


# Beschreibt eine Gerade
# dabei ist `start` der Startpunkt, und `end` der Endpunkt
class Line:
    __slots__ = ['start', 'end']

    def __init__(self, start: Vector, end: Vector):
        self.start = start
        self.end = end

    def __getitem__(self, index: int):
        return [self.start, self.end][index]

    def __str__(self):
        return "Line from {start} to {end}]".format(start=str(self.start), end=str(self.end))

    def length(self):
        return math.sqrt(
            math.pow((self.end.x - self.start.x),2) +
            math.pow((self.end.y - self.start.y),2)
        )

    def intersects(self: Line, otherLine: Line):
        xdiff = (self[0][0] - self[1][0], otherLine[0][0] - otherLine[1][0])
        ydiff = (self[0][1] - self[1][1], otherLine[0][1] - otherLine[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = (det(*self), det(*otherLine))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div

        def numberBetween(num, start, end):
            numBetweenStartEnd = (start <= num) & (num <= end)
            numBetweenEndStart = (end <= num) & (num <= start)
            return numBetweenEndStart | numBetweenStartEnd

        if numberBetween(x, self.start.x, self.end.x) & numberBetween(y, self.start.y, self.end.y):
            return Vector(x, y)
        return None
