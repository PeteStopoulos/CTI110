# Square Triangle

import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title('P4Lab2b')

pete = turtle.Turtle()
pete.color("green")
pete.pensize(6)
for i in [0,1,2,3]:
    pete.forward(50)
    pete.right(90)
pete.penup()
pete.right(180)
pete.forward(100)
pete.pendown()
for i in[0,1,2]:
    pete.right(120)
    pete.forward(50)