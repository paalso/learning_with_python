class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        x = 0.5 * (self.x + target.x)
        y = 0.5 * (self.y + target.y)
        return Point(x,y)

    def reflect_x(self):
        """ Returns a new Point, which is the reflection of the point
        about the x-axis """
        return Point(self.x, -self.y)

    def reflect_y(self):
        """ Returns a new Point, which is the reflection of the point
        about the y-axis """
        return Point(-self.x, self.y)

    def reflect_origin(self):
        """ Returns a new Point, which is the reflection of the point
        about the origin"""
        return Point(-self.x, -self.y)

    def slope_from_origin(self):
        """ Returns the slope of the line joining the origin to the point.
        The case self.x == 0 will cause this method to fail """
        return self.y / self.x

    def get_line_to(self, target):
        """ Compute the equation of the straight line joining the two points -
        self and target. Return the two coefficients as a tuple of two values.
        """
        k = (target.y - self.y) / (target.x - self.x)
        b = (self.x * target.y - self.y * target.x) / (self.x - target.x)
        return k, b
