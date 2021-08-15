# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 2-b
# =============
# Four lines make a square. Use the code in part a) to draw cesaro squares.
# Varying the angle gives interesting effects — experiment a bit, or perhaps
# let the user input the angle of the tear.


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

    for turn in 90 - TEAR_ANGLE / 2, TEAR_ANGLE - 180, 90 - TEAR_ANGLE / 2, 0:
        cesaro(t, order - 1, size / 2)
        t.right(turn)


def cesaro_snowflake(t, order, size):
    for _ in range(4):
        cesaro(t, order, size)
        t.right(90)


def main():
    wn = turtle_helper.make_window("lightgreen", "Cesàro Fractal")

    move_len = 300

    t = turtle_helper.make_turtle("blue", 2, shape='classic')
    turtle_helper.move(t, -move_len, move_len)
    t.speed(0)

    order = 3
    cesaro_snowflake(t, order, move_len)

    wn.mainloop()


if __name__ == '__main__':
    main()
