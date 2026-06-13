from turtle import *

tracer(0)
screensize(5000,5000)
r = 50

rt(90)

for i in range(3):
    rt(45)
    fd(10*r)
    rt(45)

rt(315)
fd(10*r)

for i in range(2):
    rt(90)
    fd(10*r)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3, 'red')
update()
    
