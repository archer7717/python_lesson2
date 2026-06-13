from turtle import *

tracer(0)
screensize(5000,5000)
r = 40

for i in range(4):
    fd(19*r)
    rt(90)
    fd(30*r)
    rt(90)
up()

fd(2*r)
rt(90)
fd(8*r)
lt(90)
down()

for i in range(4):
    fd(93*r)
    rt(90)
    fd(97*r)
    rt(90)


up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3, 'red')

update()
