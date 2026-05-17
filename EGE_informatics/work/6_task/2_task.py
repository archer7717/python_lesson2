from turtle import *
tracer(0)
screensize(5000,5000)
r = 30
for i in range(5):
    rt(45)
    fd(10*r)
    rt(45)
for i in range(6):
    fd(20*r)
    rt(90)
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*r,y*r)
        dot(3,'red')

update()
