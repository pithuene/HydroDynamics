import math


ALLOWED_NUM_TYPES = (int, float)


class Vector:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Any):
        if isinstance(other, ALLOWED_NUM_TYPES):
            return Vector(self.x+other, self.y+other)

        return Vector(self.x+other.x, self.y+other.y)

    def __mul__(self, other: Any):
        if isinstance(other, ALLOWED_NUM_TYPES):
            return Vector(self.x*other, self.y*other)

        return Vector(self.x*other.x, self.y*other.y)

    def __sub__(self, other: Any):
        if isinstance(other, ALLOWED_NUM_TYPES):
            return Vector(self.x-other, self.y-other)

        return Vector(self.x-other.x, self.y-other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __truediv__(self, other: Any):
        if isinstance(other, ALLOWED_NUM_TYPES):
            return Vector(self.x/other, self.y/other)

        return Vector(self.x/other.x, self.y/other.y)

    def __floordiv__(self, other: Any):
        if isinstance(other, ALLOWED_NUM_TYPES):
            return Vector(self.x//other, self.y//other)

        return Vector(self.x//other.x, self.y//other.y)

    def __mod__(self, other: Any):
        if isinstance(other, ALLOWED_NUM_TYPES):
            return Vector(self.x % other, self.y % other)

        return Vector(self.x % other.x, self.y % other.y)

    def __eq__(self, other: Any):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Any):
        if not isinstance(other, Vector):
            return True

        return self.x != other.x or self.y != other.y

    def __getitem__(self, index: int):
        return [self.x, self.y][index]

    def __contains__(self, value):
        return value == self.x or value == self.y

    def __len__(self):
        return 2

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Vector [{x}, {y}]".format(x=self.x, y=self.y)

    def copy(self):
        return Vector(self.x, self.y)

    def set(self, other):
        self.x = other.x
        self.y = other.y

    def perp(self):
        return Vector(self.y, -self.x)

    def rotate(self, angle: Union[int, float, Real]):
        return Vector(self.x * math.cos(angle) - self.y * math.sin(angle), self.x * math.sin(angle) + self.y * math.cos(angle))

    def reverse(self):
        return Vector(-self.x, -self.y)

    def int(self):
        return Vector(int(self.x), int(self.y))

    def normalize(self):
        dot = self.ln()
        return self / dot

    def project(self, other):
        amt = self.dot(other) / other.ln2()

        return Vector(amt * other.x,  amt * other.y)

    def project_n(self, other):
        amt = self.dot(other)

        return Vector(amt * other.x, amt * other.y)

    def reflect(self, axis):
        v = Vector(self.x, self.y)
        v = v.project(axis) * 2
        v = -v

        return v

    def reflect_n(self, axis):
        v = Vector(self.x, self.y)
        v = v.project_n(axis) * 2
        v = -v

        return v

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def ln2(self):
        return self.dot(self)

    def ln(self):
        return math.sqrt(self.ln2())

    def toAngle(self):
        normSelf = self.normalize()
        return ((math.atan2(normSelf.x, normSelf.y) * 180) / math.pi)

    def fromAngle(angle):
        radians = math.radians(angle)
        return Vector(round(math.sin(radians),10), round(math.cos(radians),10))
