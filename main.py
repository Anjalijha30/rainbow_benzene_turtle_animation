import turtle

c=["red","purple","blue","green","orange","yellow"]
t = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(c[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

t.exitonclick()
