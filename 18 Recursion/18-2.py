# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 2
# ===========
# a. Draw a Cesaro torn line fractal, of the order given by the user.
#
# b. Four lines make a square. Use the code in part a) to draw cesaro squares.
# Varying the angle gives interesting effects — experiment a bit, or perhaps
# let the user input the angle of the tear.
#
# c. or the mathematically inclined). In the squares shown here,
# the higher-order drawings become a little larger. (Look at the bottom lines of
# each square - they’re not aligned.) This is because we just halved the drawn
# part of the line for each recursive subproblem. So we’ve “grown” the overall
# square by the width of the tear(s). Can you solve the geometry problem so
# that the total size of the subproblem case (including the tear) remains
# exactly the same size as the original?


import turtle
import turtle_helper
import math


def cesaro(t, order, size, tear_angle = 10):
    """
       Draws a Cesaro torn line fractal, of the order given by the user.
    """
    size = size / (1 + order * math.sin(math.radians(tear_angle / 2)))
##    - order * t.width()

    turn_angles = 0, 90 - tear_angle / 2, tear_angle - 180, 90 - tear_angle / 2

    def drawer(t, order, size):
        if order == 0:
            t.forward(size)
            return

        for angle in turn_angles:
            t.right(angle)
            drawer(t, order - 1, size / 2)

    drawer(t, order, size)


def cesaro_square(t, order, size, angle = 10):
    """
        Draws a Cesaro torn line square fractal, of the order given by the user.
    """
    for i in range(4):
        cesaro(t, order, size, angle)
        t.right(90)


def main():
    wn = turtle_helper.make_window("lightgreen", "Cesaro's curve")
    t = turtle_helper.make_turtle("black", 3, -250, 200)
    t.speed(0)

    size = 400
    tear_angle = 10

    print(t.width())

    order = 0
    cesaro_square(t, order, size, tear_angle)

    order = 1
    turtle_helper.move(t, -250, 200)
    t.color('red')
    cesaro_square(t, order, size, tear_angle)

    order = 2
    turtle_helper.move(t, -250, 200)
    t.color('blue')
    cesaro_square(t, order, size, tear_angle)

    order = 3
    turtle_helper.move(t, -250, 200)
    t.color('green')
    cesaro_square(t, order, size, tear_angle)
##
##    order = 4
##    turtle_helper.move(t, -250, 200)
##    t.color('brown')
##    cesaro_square(t, order, size, tear_angle)

    wn.mainloop()


if __name__ == '__main__':
    main()