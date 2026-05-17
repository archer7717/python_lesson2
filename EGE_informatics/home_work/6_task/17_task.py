from turtle import *

tracer(0)

r = 50
screensize(5000,5000)

def vec(x,y):
    goto(xcor()+x*r, ycor()+y*r)

for i in range(5):
    vec(6,8)
    vec(-8,4)
    vec(2,-12)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')

update()
