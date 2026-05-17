from turtle import *
tracer(0)

screensize(5000,5000)

r = 25

for i in range(2):
    fd(23*r)
    lt(90)
    bk(27*r)
    lt(90)
up()

bk(5*r)
rt(90)
fd(11*r)
lt(90)

down()

for i in range(2):
    fd(26*r)
    rt(90)
    fd(32*r)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')

update()
