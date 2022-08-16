import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor("green")
a=0
t.speed(0)
while True:
    for i in range(4):
      t.fd(100)
      t.right(90)
    t.right(5)
    a+=1
    if a>=360/5:
        break
t.hideturtle()
turtle.done()