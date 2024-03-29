from turtle import *
from random import randint

def finish(Harry, Dobbi, Mike):
    if abs(Harry.xcor()) > 200 or abs(Harry.ycor()) > 200 or abs(Dobbi.xcor()) > 200 or abs(Dobbi.ycor()) > 200 or abs(Mike.xcor()) > 200 or abs(Mike.ycor()) > 200:
        return False
    else:
        return True

def run(x,y):
    Harry.goto(randint(-50,50), randint(-50,50))
    Harry.left(randint(10,360))


def run2(x,y):
    Dobbi.goto(randint(-50,50), randint(-50,50))
    Dobbi.left(randint(10,360))

def run3(x,y):
    Mike.goto(randint(-50,50), randint(-50,50))
    Mike.left(randint(10,360))

Dobbi = Turtle()
Harry = Turtle()
Mike = Turtle()

Dobbi.shape('turtle')
Harry.shape('turtle')
Mike.shape('turtle')

Dobbi.penup()
Dobbi.goto(-10,0)

Harry.penup()
Harry.goto(0,10)

Mike.penup()
Mike.goto(10,0)

Harry.left(90)
Dobbi.right(140)
Mike.right(20)

Harry.color('yellow')
Dobbi.color('green')
Mike.color('blue')

Harry.pendown()
Dobbi.pendown()
Mike.pendown()

Harry.onclick(run)
Dobbi.onclick(run2)
Mike.onclick(run3)
    
while finish(Harry, Dobbi, Mike):
    Harry.forward(2)
    Dobbi.forward(2)
    Mike.forward(2)

Harry.penup()
Harry.goto(-30,0)
Harry.pendown()
Harry.write('you lose', font=('Arial', 40, 'normal'))


hideturtle()
exitonclick()