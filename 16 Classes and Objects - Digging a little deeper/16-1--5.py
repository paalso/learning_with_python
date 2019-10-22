# http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html

# Exercises 1 - 5
# ================

from point import *
from segment import *
from testtools import *

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h
        posn is bottom-left (!) corner of the rectangle """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        """ Returns the area of the instance """
        return  self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of the instance """
        return  2 * (self.width + self.height)

    def flip(self):
        """ Swaps the width and the height of the instance """
        self.width, self.height = self.height, self.width

    def x_projection(self):
        """ Gets the x-projection of the instance as a LineSegment """
        return LineSegment(self.corner.x, self.corner.x + self.width)

    def y_projection(self):
        """ Gets the y-projection of the instance as a LineSegment """
        return LineSegment(self.corner.y, self.corner.y + self.height)

    def contains(self, point):
        """ Test if a given Point falls within the instance rectangle """
        x, y = point.x, point.y
        x0, y0 = self.corner.x, self.corner.y
        return x0 <= x < x0 + self.width and y0 <= y < y0  + self.height

    def collides(self, rect):
        """ Test if a given Rectangle collides within the instance rectangle """
        self_x_pr, self_y_pr  = self.x_projection(), self.y_projection()
        x_pr, y_pr  = rect.x_projection(), rect.y_projection()
        return self_x_pr.collides(x_pr) and self_y_pr.collides(y_pr)


r = Rectangle(Point(0, 0), 6, 3)

test(r.collides(Rectangle(Point(0, 0), 2, 2)))
test(r.collides(Rectangle(Point(-2, 2), 4, 2)))
test(r.collides(Rectangle(Point(5, 1), 4, 2)))
test(r.collides(Rectangle(Point(6, 0), 4, 2)))
test(r.collides(Rectangle(Point(2, 1), 1, 1)))
test(r.collides(Rectangle(Point(1, 3), 1, 1)))
test(r.collides(Rectangle(Point(-1, -1), 10, 5)))
test(not r.collides(Rectangle(Point(1, 4), 1, 1)))
test(not r.collides(Rectangle(Point(-3, 0), 2, 2)))
test(not r.collides(Rectangle(Point(0, -4), 2, 2)))
test(not r.collides(Rectangle(Point(7, 1), 3, 1)))
