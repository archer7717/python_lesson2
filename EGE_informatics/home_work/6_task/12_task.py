from turtle import *
r = 45
tracer(0)
screensize(5000,5000)

lt(255)
for i in range(3):
    lt(30)
    for b in range(4):
        fd(10*r)
        lt(90)


up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r,y*r)
        dot(3,'red')
        



update()
