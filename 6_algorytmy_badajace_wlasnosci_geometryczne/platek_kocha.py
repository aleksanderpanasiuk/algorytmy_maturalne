import turtle

def koch(a, n):
    if n == 1:
        t.fd(a)
    else:
        koch(a/3, n-1)
        t.left(60)
        koch(a/3, n-1)
        t.right(120)
        koch(a/3, n-1)
        t.left(60)
        koch(a/3, n-1)


def platek(a, n):
    for i in range(3):
        koch(a, n)
        t.right(120)


window = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.speed(100)
t.bk(200)
t.left(90)
t.fd(200)
t.right(90)
t.pendown()

platek(400, 5)

window.exitonclick()
