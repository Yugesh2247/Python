import turtle
t=turtle.Turtle()

s=turtle.Screen()
s.title("Digital Clock")
s.bgcolor('black')
t.speed(0)
t.pencolor('red')
a=1
while True:
    t.fd(a)
    t.left(120)
    t.left(1)
    a+=1
    
tuple.done()