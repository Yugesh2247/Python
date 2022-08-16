import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('green')
r=100
a=0
t.speed(0)
while True:
   t.circle(r)
   t.right(10)
   a+=1
   if a>=360/5:
       break
   t.hideturtle()
turtle.done()