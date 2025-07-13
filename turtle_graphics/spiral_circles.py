# This program draws a pattern using repeating circles.
import turtle

# Named constants
NUM_CIRCLES = 36     # Number of circles to draw.
RADIUS = 100         # Radius of each circle
ANGLE = 10           # Rotation angle.
ANIMATION_SPEED = 0  # Animation speed.

# Set animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, tilting the turtle
# 10 degrees after each circle has been drawn.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()