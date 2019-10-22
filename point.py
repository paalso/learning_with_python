class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        x = 0.5 * (self.x + target.x)
        y = 0.5 * (self.y + target.y)
        return Point(x,y)

    def reflect_x(self):
        return Point(self.x, -self.y)

    def reflect_y(self):
        return Point(-self.x, self.y)

    def reflect_origin(self):
        return Point(-self.x, -self.y)

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, target):
        k = (target.y - self.y) / (target.x - self.x)
        b = (self.x * target.y - self.y * target.x) / (self.x - target.x)
        return k, b



p1 = Point(1,2)
p2 = Point(1,9)

print(Point(4, 11).get_line_to(Point(6, 15)))