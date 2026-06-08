import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
color = ["red","yellow","green","blue","cyan","magenta","orange","purple"][::-1]

for x in range(1000):
    t.color(color[x % len(color)])
    t.circle(x)
    t.left(44)
    t.forward(x)
    t.right(00)
turtle.done()
