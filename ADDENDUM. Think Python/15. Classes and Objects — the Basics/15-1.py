'''
Exercise 15.1. Write a definition for a class named Circle with attributes
center and radius, where center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at
(150, 100) and radius 75.
Write a function named point_in_circle that takes a Circle and a Point and
returns True if the Point lies in or on the boundary of the circle.
Write a function named rect_in_circle that takes a Circle and a Rectangle and
returns True if the Rectangle lies entirely in or on the boundary of the circle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle
and returns True if any of the corners of the Rectangle fall inside the circle.
Or as a more challenging version, return True if any part of the Rectangle
falls inside the circle. Solution: http://thinkpython2.com/code/Circle.py
'''

from figures import Circle, Point, Rectangle


c = Circle(Point(0, 0), 7)

r1 = Rectangle(Point(6, 5), 1, 1)
print(c.rect_circle_overlap(r1) == False)

r2 = Rectangle(Point(8, 5), 10, 10)
print(c.rect_circle_overlap(r2) == False)

r3 = Rectangle(Point(-8, 8), 16, 16)
print(c.rect_circle_overlap(r3) == True)

r4 = Rectangle(Point(5, 6), 1, 1)
print(c.rect_circle_overlap(r4) == False)

r5 = Rectangle(Point(4, 7), 5, 1)
print(c.rect_circle_overlap(r5) == False)

r6 = Rectangle(Point(-7, 2), 7, 2)
print(c.rect_circle_overlap(r6) == True)

r7 = Rectangle(Point(-7, 4), 1, 4)
print(c.rect_circle_overlap(r7) == True)

r8 = Rectangle(Point(-1, -7), 1, 1)
print(c.rect_circle_overlap(r8) == True)

r9 = Rectangle(Point(-4, 4), 5, 5)
print(c.rect_circle_overlap(r9) == True)
