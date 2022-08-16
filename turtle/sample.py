import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('white')
a=1
while True:
    t.fd(a)
    t.left(30)
    t.right(30)
    a+=3
turtle.done()