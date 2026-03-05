import turtle
import random
import math
#setup screen
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Holi")

#create turtle
t=turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

colors=["red","yellow","blue","green","magenta","orange","cyan","pink"]

def draw_layer(radius,petals):
    angle=360/petals
    for _ in range(petals):
        t.color(random.choice(colors))
        t.circle(radius)
        t.left(angle)
t.penup()
t.goto(0,-50)
t.pendown()
for r in range(40,180,30):
    draw_layer(r,12)
t.penup()
t.goto(0,-20)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()            

#write happy holi text

turtle.done()