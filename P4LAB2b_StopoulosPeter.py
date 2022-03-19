# Initials P S

import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title('P4Lab2b')

pete = turtle.Turtle()
pete.color("green")
pete.pensize(6)
# Making P
pete.left(90)
pete.forward(100)
for i in [0,1,2,3]:
    pete.right(90)
    pete.forward(40)
# Moving pen
pete.penup()
pete.right(90)
pete.forward(150)
pete.pendown()
# Making S
pete.right(180)
pete.forward(40)
for i in [0,1]:
    pete.left(90)
    pete.forward(33)
for i in [0,1]:
    pete.right(90)
    pete.forward(33)

