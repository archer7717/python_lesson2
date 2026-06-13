from turtle import *
tracer(0)
screensize(5000,5000)
r = 55

rt(30)
for i in range(3):
    rt(150)
    fd(6*r)
    rt(30)
    fd(12*r)

up()

for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'red')

update()
