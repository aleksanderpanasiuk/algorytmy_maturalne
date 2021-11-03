import turtle

def dywan_sierpinskiego(a, n):
    if n == 0:
        for i in range(0, 4):
            t.fd(a)
            t.left(90)
    else:
        a /= 3
        dywan_sierpinskiego(a, n-1)
        t.fd(a)
        dywan_sierpinskiego(a, n-1)
        t.fd(a)
        dywan_sierpinskiego(a, n-1)
        t.left(90)
        t.fd(a)
        t.left(90)
        t.fd(a*2)
        t.right(180)
        dywan_sierpinskiego(a, n-1)
        t.fd(a*2)
        dywan_sierpinskiego(a, n-1)
        t.left(90)
        t.fd(a)
        t.left(90)
        t.fd(a*2)
        t.right(180)
        dywan_sierpinskiego(a, n-1)
        t.fd(a)
        dywan_sierpinskiego(a, n-1)
        t.fd(a)
        dywan_sierpinskiego(a, n-1)
        t.fd(a)
        t.right(90)
        t.fd(a*2)
        t.right(90)
        t.fd(a*3)
        t.left(180)



window = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.speed(100)
t.bk(200)
t.right(90)
t.fd(200)
t.left(90)
t.pendown()
dywan_sierpinskiego(300, 4)

window.exitonclick()

