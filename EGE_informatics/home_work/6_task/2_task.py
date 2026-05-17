from turtle import *
tracer(0)
screensize(5000,5000)
r = 120

for i in range(16):
    lt(36)
    fd(4*r)
    lt(36)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r,y*r)
        dot(3,'green')

    
update()
