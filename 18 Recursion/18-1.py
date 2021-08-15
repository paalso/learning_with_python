# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 1
# ===========
# Modify the Koch fractal program so that it draws a Koch snowflake


import turtle
import turtle_helper


def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """
    if order == 0:
        t.forward(size)
        return

    for turn in (60, -120, 60, 0):
        koch(t, order - 1, size // 3)
        t.left(turn)


def koch_snowflake(t, order, size):
    """
       Make turtle t draw a Koch fractal snowflake of 'order' and 'size'.
    """
    for i in range(3):
        koch(t, order, size)
        t.right(120)


def main():
    wn = turtle_helper.make_window("lightgreen", "Koch's curve")

    move_len = 600

    t = turtle_helper.make_turtle("blue", 2, shape='classic')
    turtle_helper.move(t, -move_len / 2, move_len / (2 * 3 ** 0.5))
    t.speed(0)

    order = 2
    koch_snowflake(t, order, move_len)

    wn.mainloop()


if __name__ == '__main__':
    main()
