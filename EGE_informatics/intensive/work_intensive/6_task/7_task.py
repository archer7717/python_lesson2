from turtle import *

screensize(5000,5000)
tracer(0)
r = 20


for i in range(2):
    fd(8*r)
    rt(90)
    fd(18*r)
    rt(90)

up()

fd(4*r)
rt(90)
fd(10*r)

lt(90)

down()

for i in range(2):
    fd(17*r)
    rt(90)
    fd(7*r)
    rt(90)

up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3, 'red')
update()
