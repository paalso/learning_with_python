##http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

##6. Use for loops to make a turtle draw these regular polygons
##(regular means all sides the same lengths, all angles the same):
##An equilateral triangle
##A square
##A hexagon (six sides)
##An octagon (eight sides)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.width(3)
tess.color("black")

##An arbitrary triangle in fact
n = int(input("Input number of angles of the polygon to draw: "))

for i in range(n):
    tess.forward(100)
    tess.left(360 / n)

wn.mainloop()