from turtle import *
r = 30
tracer(0)
screensize(5000,5000)

def vec(x,y):
    goto(xcor()+x*r,ycor()+y*r)
    
vec(0, 12)
vec(5, -12)
vec(-10, 0)
vec(5, 12)
vec(0,4)
vec(3,-4)
vec(-6,0)
vec(3,4)
up()

for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*r,y*r)
        dot(3, 'pink')
        


update()
