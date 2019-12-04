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
        return Vector(x, y)
