from turtle import *

tracer(0)

screensize(5000,5000)
r = 55

rt(270)

for i in range(8):
    fd(10*r)
    rt(45)
    fd(10*r)
    rt(135)
for i in range(4):
    fd(4*r)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50,50):
        goto(x*r, y*r)
        dot(3,'red')

update()
