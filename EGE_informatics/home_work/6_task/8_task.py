from turtle import *
tracer(0)

r= 50

screensize(5000,5000)

for i in range(3):
    fd(7*r)
    rt(90)
fd(8*r)
for i in range(3):
    lt(90)
    fd(5*r)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3,'red')
update()
