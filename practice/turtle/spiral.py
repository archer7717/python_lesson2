from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(200):
    t = (i/10)* pi
    print(t)
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)
