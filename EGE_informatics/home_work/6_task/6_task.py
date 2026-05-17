from turtle import *
tracer(0)

r= 50

screensize(5000,5000)

for i in range(15):
    fd(7*r)
    rt(30)
    fd(8*r)
    rt(150)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3,'red')
update()
