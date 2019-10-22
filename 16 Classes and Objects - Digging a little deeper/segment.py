# http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html

# Exercises 1 - 5
# ================

from testtools import *

class LineSegment:
    """ A class to manufacture line segment objects """

    def __init__(self, start = 0, end = 1):
        """ Initializes a line segment at the point 'start',
        with a given 'length' """
        self.start = start
        self.end = end

    def __str__(self):
        return  "([{0}, {1}])".format(self.start, self.end)


    def collides(self, segment):
        """ Test if a given Line Segment collides with the segment """
        return not (segment.end < self.start or self.end < segment.start)


s = LineSegment(0, 5)
print(s)

test(s.collides(LineSegment(0, 3)))
test(s.collides(LineSegment(1, 3)))
test(s.collides(LineSegment(-2, 8)))
test(s.collides(LineSegment(-2, 4)))
test(s.collides(LineSegment(4, 4)))
test(s.collides(LineSegment(5, 6)))
test(not s.collides(LineSegment(-5, -1)))
test(not s.collides(LineSegment(6, 7)))
