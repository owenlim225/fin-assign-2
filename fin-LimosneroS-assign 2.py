import turtle
import time

t = turtle.Turtle()

#cirlce
t.pen(pencolor="crimson", fillcolor="#FFE7A7", pensize=10, speed=9)
t.begin_fill()
t.circle(100)
t.end_fill()

#body
t.pen(pencolor="yellow", fillcolor="gold", pensize=10, speed=9)
t.rt(90)
t.fd(200)

#left legs
t.rt(30)
t.fd(150)

#right leg
t.begin_fill()
t.pen(pencolor="navy", fillcolor="gold", pensize=10, speed=9)
t.end_fill()
t.backward(150)
t.rt(-60)
t.fd(150)

#back to the body
t.backward(150)
t.rt(210)
t.penup()
t.fd(150)

#left arm
t.rt(65)
t.pendown()
t.fd(100)

#right arm
t.backward(100)
t.rt(-130)
t.fd(100)

#right eye
t.penup()
t.backward(100)
t.rt(80)
t.fd(160)
t.pendown()
t.begin_fill()
t.pen(pencolor="navy", fillcolor="black", pensize=10, speed=9)
t.end_fill()
t.circle(10)


#left eye
t.penup()
t.rt(-95)
t.fd(70)
t.pendown()
t.begin_fill()
t.pen(pencolor="navy", fillcolor="black", pensize=10, speed=9)
t.end_fill()
t.circle(10)

#lips
t.penup()
t.rt(-100)
t.fd(30)
t.fd(20)
t.rt(-90)
t.pendown()
t.fd(60)
t.penup()


#Alien
t.fd(20)
t.rt(-120)
t.fd(150)
t.pendown()
t.fd(30)
t.circle(7)

t.penup()
t.rt(-180)
t.fd(20)
t.pendown()
t.fd(30)
t.circle(7)


#Name
t.penup()
t.fd(350)
t.write("Sherwin P. Limosnero", font="100")
t.hideturtle()
time.sleep(3)