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


# Function to draw color splash dots
def color_splash():
    for _ in range(80):
        t.penup()
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        t.goto(x, y)
        t.pendown()
        t.dot(random.randint(10, 25), random.choice(colors))

# Function to write colorful HAPPY HOLI
def write_text():
    t.penup()
    t.goto(-250, -40)  # Starting position for big text
    
    for letter in "HAPPY HOLI":
        if letter == " ":
            t.forward(40)
        else:
            t.color(random.choice(colors))
            t.write(letter, font=("Arial", 48, "bold"))
            t.forward(35)

    # Small message below
    t.goto(0, -120)
    t.color("white")
    t.write("May your life be filled with vibrant colors and happiness!",
            align="center",
            font=("Arial", 14, "italic"))

# Main execution
color_splash()

write_text()

turtle.done()