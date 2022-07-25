import turtle
from turtle import Turtle, Screen
import random
import turtle

timmy=Turtle()
tom=Turtle()
print(timmy)
r=5
m=3
timmy.shape("turtle")
tom.shape("turtle")
colors=["blue","green","red","coral","black","yellow","brown","pink"]
timmy.speed(100)

for i in range(1,1000):
    rcolor=random.choice(colors)
    timmy.color(rcolor)
    r=r+3
    timmy.forward(r)
    timmy.left(90)
    rrcolor=random.choice(colors)
    tom.color(rrcolor)
    tom.speed(100)
    m=m+4
    tom.circle(m)
mscreen= Screen()
print(mscreen.canvheight)
mscreen.exitonclick()
