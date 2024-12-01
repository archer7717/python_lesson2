import turtle

turtle.shape('turtle')

f = 20
l = 90
p = 0
while  p <=9:
    turtle.forward(f)
    turtle.left(90)
    turtle.forward(f)
    turtle.left(90)
    turtle.forward(f)
    turtle.left(90)
    turtle.forward(f)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)

    turtle.backward(10)
    turtle.pendown()
    p+=1
    f+=20

    

