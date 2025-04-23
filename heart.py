import turtle
import time

# Setup turtle
turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)
turtle.color('pink', 'pink')

# Function to draw one side of the heart
def draw_half_heart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

# Start filling the heart with color
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)

# Draw left half
draw_half_heart()

turtle.left(120)

# Draw right half
draw_half_heart()

turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

# Pause before closing
time.sleep(5)
turtle.done()
