import turtle

turtle.speed(11)

turtle.penup()

turtle.goto(0,-75)

turtle.pendown()

turtle.color("#FEDC5F")

turtle.begin_fill()

turtle.circle(200)

turtle.end_fill()

turtle.penup()

turtle.goto(-90,150)


def draw_eye():
    turtle.color("#000000")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


draw_eye()

turtle.penup()

turtle.goto(90,150)

turtle.pendown()

draw_eye()

turtle.penup()

turtle.goto(-15,125)


def draw_nose():
    turtle.color("#000000")
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(40)
        turtle.right(120)
    turtle.end_fill()


draw_nose()

turtle.penup()

turtle.goto(-50,20)

turtle.pendown()

turtle.pencolor("#000000")

turtle.width(15)

turtle.forward(100)

turtle.width(1)

turtle.penup()

turtle.goto(-110,330)



turtle.exitonclick()