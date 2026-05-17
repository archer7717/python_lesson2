from turtle import *

tracer(0)
r = 50
screensize(5000,5000)

for i in range(3):
    down()
    for b in range(2):
        fd(7*r)
        rt(90)
        fd(7*r)
        rt(90)
    up()
    fd(6*r)
    rt(90)
    fd(6*r)
    lt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3,'red')

update()
