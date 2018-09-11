import turtle


turtle.penup()

turtle.goto(0,-75)

turtle.pendown()

turtle.color("#FEDC5F")

turtle.begin_fill()

turtle.circle(200)

turtle.end_fill()

turtle.penup()

turtle.goto(-90,150)


def draweye():
    turtle.color("#000000")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


draweye()

turtle.penup()

turtle.goto(90,150)

turtle.pendown()

draweye()










turtle.exitonclick()