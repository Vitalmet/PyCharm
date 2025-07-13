# This program draws a pattern using repeating lines.
import turtle

# Named constants.
START_X = - 200     # Start X coordinate.
START_Y = 0         # Start Y coordinate.
NUM_LINES = 36      # Number of lines to draw.
LINE_LENGTH = 400   # Length of each line.
ANGLE = 170         # Rotation angle.
ANIMATION_SPEED = 0 # Animation speed.

# Move turtle to start position.
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

# Set animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, tilting the turtle
# 170 degrees after each circle has been drawn.
for x in range(NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)

turtle.done()