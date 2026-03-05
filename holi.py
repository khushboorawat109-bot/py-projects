import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Holi 🌸")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

colors = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "cyan"]

# Function to draw rangoli pattern
def draw_rangoli():
    for i in range(36):
        t.color(random.choice(colors))
        t.circle(120)
        t.left(10)

# Function to draw color splash dots
def color_splash():
    for _ in range(80):
        t.penup()
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        t.goto(x, y)
        t.pendown()
        t.dot(random.randint(10, 25), random.choice(colors))

# Write Happy Holi text
def write_text():
    t.penup()
    t.goto(0, -30)
    t.color("white")
    t.write("HAPPY HOLI", align="center", font=("Arial", 36, "bold"))

# Main execution
color_splash()

write_text()

turtle.done()