# Chapter 15. Classes and Objects — the Basics
# http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

# Exercises 1 - 5
# ================

"""
1. Rewrite the distance function from the chapter titled Fruitful functions so
that it takes two Points as parameters instead of four numbers.

2. Add a method reflect_x to Point which returns a new Point, one which is
the reflection of the point about the x-axis.

3. Add a method slope_from_origin which returns the slope of the line joining
the origin to the point. What cases will cause this method to fail?

4. The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”).
The coefficients a and b completely describe the line. Write a method in
the Point class so that if a point instance is given another point, it will
compute the equation of the straight line joining the two points. It must
return the two coefficients as a tuple of two values.

5. Given four points that fall on the circumference of a circle, find
the midpoint of the circle. When will this function fail?
"""
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



p1 = Point(1,2)
p2 = Point(1,9)

print(Point(4, 11).get_line_to(Point(6, 15)))