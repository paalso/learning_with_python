##http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

##11. Write a program to draw a shape like this: <Five-pointed star>

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.width(3)
tess.color("black")

tess.right(90 + 18)

for i in range(5):
    tess.forward(200)
    tess.left(180 - 36)

wn.mainloop()