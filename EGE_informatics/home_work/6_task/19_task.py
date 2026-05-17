from turtle import *
tracer(0)
r =15

screensize(5000,5000)

def vec(x,y):
    goto(xcor()+x*r, ycor()+y*r)

for i in range(5):
    vec(5,4)
    vec(4,-4)
    vec(-7,-2)
    vec(-2,2)
update()
