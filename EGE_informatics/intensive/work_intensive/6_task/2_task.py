from turtle import *


tracer(0)
screensize(5000,5000)
r = 45

rt(45)
for i in range(7):
    fd(6*r)
    rt(45)
    fd(12*r)
    rt(135)

up()

for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'red')
update()
