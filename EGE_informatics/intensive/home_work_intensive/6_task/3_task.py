from turtle import *
tracer(0)
screensize(5000,5000)
r = 40


for i in range(4):
    fd(10*r)
    rt(270)
up()

fd(3*r)
rt(270)
fd(5*r)
rt(90)

down()

for i in range(2):
    fd(10*r)
    rt(270)
    fd(12*r)
    rt(270)




up()

for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'red')

update()
