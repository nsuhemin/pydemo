import turtle

a = turtle.Turtle()
a.color('red', 'yellow')
a.begin_fill()
while True:
    a.forward(200)
    a.left(170)
    if abs(a.pos()) < 1:
        break
a.end_fill()
turtle.done()