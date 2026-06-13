from turtle import *

screensize(5000,5000)
tracer(0)
r = 30

for i in range(9):
    fd(17*r)
    rt(90)
    fd(20*r)
    rt(90)
up()

fd(3*r)
rt(90)
fd(6*r)
lt(90)

down()
for i in range(9):
    fd(44*r)
    rt(90)
    fd(33*r)
    rt(90)

up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')

update()
