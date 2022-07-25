from turtle import *
r=30
tim=Turtle()

tim.color("Black")
tim.speed(1)
for i in range(20):
    tim.circle(r)
    r=r+30
    tim.right(90)
    tim.penup()
    tim.forward(30)
    tim.left(90)
    tim.pendown()
mscreen= Screen()
print(mscreen.canvheight)
mscreen.exitonclick()

