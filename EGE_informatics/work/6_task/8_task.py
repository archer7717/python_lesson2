from turtle import *
r = 70
tracer(0)
screensize(5000,5000)

for i in range(2):
    goto(xcor()+3*r,ycor()+4*r)
    goto(xcor()-3*r,ycor()+4*r)
    goto(xcor()-3*r,ycor()-4*r)
    goto(xcor()+3*r,ycor()-4*r)




up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'red')
update()
