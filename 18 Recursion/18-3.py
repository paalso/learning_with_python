# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 3
# ===========
# A Sierpinski triangle of order 0 is an equilateral triangle.
# An order 1 triangle can be drawn by drawing 3 smaller triangles
# (shown slightly disconnected here, just to help our understanding).
# Higher order 2 and 3 triangles are also shown. Draw Sierpinski triangles
# of any order input by the user.


import turtle
import turtle_helper


def triangle(t, size):
    for i in range(3):
        t.forward(size)
        t.left(120)


def sierpinski(t, order, size):
    print(f'Order: {order}')

    if order == 0:
        triangle(t, size)
        return

    sierpinski(t, order - 1, size / 2)
    t.forward(size / 2)
    sierpinski(t, order - 1, size / 2)
    t.left(120)
    t.forward(size / 2)
    t.right(120)
    sierpinski(t, order - 1, size / 2)
    t.right(120)
    t.forward(size / 2)
    t.left(120)


def main():
    wn = turtle_helper.make_window("lightgreen", "Cesaro's curve")
    t = turtle_helper.make_turtle("blue", 2, -300, -200)
    t.speed(0)

    sierpinski(t, 5, 550)

    wn.mainloop()


if __name__ == '__main__':
    main()