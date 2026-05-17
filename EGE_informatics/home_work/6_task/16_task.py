from turtle import *

r = 40
tracer(0)
screensize(5000,5000)


def vec(x,y):
    goto(xcor()+x*r,ycor()+y*r)
    


for i in range(10):
    vec(3,6)
    vec(7,-2)
    vec(-10,-4)
up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')

    
update()
