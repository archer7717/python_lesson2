from turtle import *
tracer(0)
screensize(5000,5000)
r = 40


for i in range(2):
    fd(3*r)
    rt(90)
    fd(20*r)
    rt(90)
up()

bk(8*r)
rt(90)
fd(9*r)
lt(90)
down()

for i in range(2):
    fd(16*r)
    rt(90)
    fd(8*r)
    rt(90)




up()

for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'red')

update()
