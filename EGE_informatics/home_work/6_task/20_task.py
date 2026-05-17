from turtle import *

tracer(0)

r = 15

screensize(5000,5000)

def vec(x,y):
    goto(xcor()+x*r,ycor()+y*r)




for i in range(2):
    vec(6,2)
    vec(0,-2)

for i in range(3):
    vec(2,-1)
    vec(-2, -1)

for i in range(6):
    vec(-2,1)


update()
