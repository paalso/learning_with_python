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
        koch(t, order - 1, size / 3)
        t.left(turn)


def main():
    wn = turtle_helper.make_window("lightgreen", "Koch's curve")

    move_len = 600
    t = turtle_helper.make_turtle("blue", 2, -move_len/2, 0, shape='classic')
    t.speed(0)

    koch(t, 4, move_len)

    wn.mainloop()


if __name__ == '__main__':
    main()

