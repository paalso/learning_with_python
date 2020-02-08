# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 1
# ===========
# Modify the Koch fractal program so that it draws a Koch snowflake


import turtle
import turtle_helper


def cesaro(t, order, size, tear_angle = 10):
    """
       Draws a Cesaro torn line fractal, of the order given by the user.
    """
    if order == 0:
        t.forward(size)
        return

    for angle in 0, 90 - tear_angle / 2, tear_angle - 180, 90 - tear_angle / 2:
        t.right(angle)
        cesaro(t, order - 1, size / 2, tear_angle)


def cesaro_square(t, order, size, angle = 10):
    """
    """
    for i in range(4):
        cesaro(t, order, size, angle)
        t.right(90)


def main():
    wn = turtle_helper.make_window("lightgreen", "Cesaro's curve")
    t = turtle_helper.make_turtle("blue", 2, -250, 200)
    t.speed(0)

    cesaro_square(t, 4, 300, 10)

##    turtle_helper.move(t, -250, 200)
##    t.color('red')
##    cesaro_square(t, 1, 300, 10)

    wn.mainloop()


if __name__ == '__main__':
    main()
