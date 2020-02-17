# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 4
# ===========
# Adapt the above program to change the color of its three sub-triangles
# at some depth of recursion.


import turtle
import turtle_helper


def triangle(t, size):
    for i in range(3):
        t.forward(size)
        t.left(120)


def sierpinski(t, order, size, color_change_depth = -1):

##    print(color_change_depth)

    if order == 0:
        triangle(t, size)
        return

    if color_change_depth == 0:
        t.color('red')
    sierpinski(t, order - 1, size / 2, color_change_depth - 1)
    t.penup()
    t.forward(size / 2)
    t.pendown()

    if color_change_depth == 0:
        t.color('blue')
    sierpinski(t, order - 1, size / 2, color_change_depth - 1)
    t.left(120)
    t.penup()
    t.forward(size / 2)
    t.pendown()
    t.right(120)

    if color_change_depth == 0:
        t.color('green')
    sierpinski(t, order - 1, size / 2, color_change_depth - 1)
    t.penup()
    t.right(120)
    t.forward(size / 2)
    t.left(120)
    t.pendown()


def main():
    wn = turtle_helper.make_window("lightgreen", "Cesaro's curve")
    t = turtle_helper.make_turtle("black", 2, -300, -200)
    t.speed(0)

    sierpinski(t, 5, 550, 2)

    wn.mainloop()


if __name__ == '__main__':
    main()