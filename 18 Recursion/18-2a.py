# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 2-a
# =============
# Draw a Cesaro torn line fractal, of the order given by the user.
# We show four different lines of orders 0,1,2,3. In this example,
# the angle of the tear is 10 degrees.


import turtle
import turtle_helper


def cesaro(t, order, size):
    """
       Make turtle t draw a Cesaro fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """
    TEAR_ANGLE = 10

    if order == 0:
        t.forward(size)
        return

    for turn in 90 - TEAR_ANGLE, 2 * TEAR_ANGLE - 180, 90 - TEAR_ANGLE, 0:
        cesaro(t, order - 1, size / 2)
        t.right(turn)


def main():
    wn = turtle_helper.make_window("lightgreen", "Cesàro Fractal")

    move_len = 300

    t = turtle_helper.make_turtle("blue", 2, shape='classic')
    turtle_helper.move(t, -move_len * 1.2, move_len * 0.6)
    t.speed(0)

    order = 5
    cesaro(t, order, move_len)

    wn.mainloop()


if __name__ == '__main__':
    main()
