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


def main():
    wn = turtle_helper.make_window("lightgreen", "Koch's curve")
    t = turtle_helper.make_turtle("blue", 2, -250, 0)
    t.speed(0)

    koch(t, 4, 600)

    wn.mainloop()


if __name__ == '__main__':
    main()

