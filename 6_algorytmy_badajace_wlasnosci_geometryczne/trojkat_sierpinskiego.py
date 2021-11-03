import turtle


def trojkat_sierpinskiego(a, n):
    if n == 0:
        for i in range(0, 3):
            t.fd(a)
            t.left(120)
    else:
        trojkat_sierpinskiego(a/2, n-1)
        t.fd(a/2)
        
        trojkat_sierpinskiego(a/2, n-1)
        t.bk(a/2)
        t.left(60)
        t.fd(a/2)
        t.right(60)
        
        trojkat_sierpinskiego(a/2, n-1)
        t.left(60)
        t.bk(a/2)
        t.right(60)


window = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.speed(100)
t.bk(200)
t.right(90)
t.fd(200)
t.left(90)
t.pendown()
trojkat_sierpinskiego(400, 4)

window.exitonclick()
