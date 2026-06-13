from turtle import *
tracer(0)
screensize(5000,5000)
r = 55

fd(9*r)
rt(90)

for i in range(2):
    fd(3*r)
    rt(90)
    fd(3*r)
    rt(270)

for i in range(2):
    fd(3*r)
    rt(90)
fd(9*r)

up()

for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'red')

update()
