# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 2-c
# =============
# (For the mathematically inclined). In the squares shown here,
# the higher-order drawings become a little larger. (Look at the bottom lines
# of each square - they’re not aligned.) This is because we just halved
# the drawn part of the line for each recursive subproblem. So we’ve “grown”
# the overall square by the width of the tear(s). Can you solve the geometry
# problem so that the total size of the subproblem case (including the tear)
# remains exactly the same size as the original?


import turtle
import turtle_helper


def cesaro(t, order, size):
    """
       Make turtle t draw a Cesaro fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """
    import math

    TEAR_ANGLE = 10

    def helper(t, order, size):

        if order == 0:
            t.forward(size)
            return

        for turn in 90 - TEAR_ANGLE / 2, TEAR_ANGLE - 180, \
                    90 - TEAR_ANGLE / 2, 0:
            helper(t, order - 1, size / 2)
            t.right(turn)

    helper(t, order,
            size / (1 + order * math.sin(math.radians(TEAR_ANGLE / 2))))



def cesaro_snowflake(t, order, size):
    for _ in range(4):
        cesaro(t, order, size)
        t.right(90)


def main():
    wn = turtle_helper.make_window("lightgreen", "Cesàro Fractal")

    move_len = 600

    colors = "black", "red", "blue", "green", "orange"

    line_width = 2
    for order, color in enumerate(colors):
        t = turtle_helper.make_turtle(color, line_width, shape='classic')
        turtle_helper.move(t, -move_len / 2 - 2 * order * line_width,
                            move_len / 2 + 2 * order)
        t.speed(0)
        cesaro_snowflake(t, order, move_len)

    wn.mainloop()


if __name__ == '__main__':
    main()
