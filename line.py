from vector import Vector


# Beschreibt die Vektorgleichung für eine Gerade in Parameterform,
# dabei ist `start` der Ortsvektor, und `direction` der Richtungsvektor
class Line:
    __slots__ = ['start', 'direction']

    def __init__(self, start: Vector, direction: Vector):
        self.start = start
        self.direction = direction

    def __getitem__(self, index: int):
        return [self.start, self.direction][index]

    def __str__(self):
        return "Line from {start} to {direction}]".format(start=str(self.start), direction=str(self.direction))

    def intersects(self: Line, otherLine: Line):
        line1 = Line(self.start, self.start + self.direction)
        line2 = Line(otherLine.start, otherLine.start + otherLine.direction)

        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return Vector(x, y)
