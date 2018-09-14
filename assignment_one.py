# Flint Eller
# 9/13/18
# Draws a face



import turtle

turtle.speed(11)

turtle.penup()

turtle.goto(0,-75)

turtle.pendown()

turtle.color("#FEDC5F")

turtle.begin_fill()
# This draws a yellow face
turtle.circle(200)

turtle.end_fill()

turtle.penup()

turtle.goto(-90,150)


# This creates a function so I can just call it instead of drawing a whole new eye
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

turtle.goto(-20,125)


# This draws a balck tringle for the nose
turtle.color("#000000")
turtle.begin_fill()
for w in range(3):
    turtle.forward(50)
    turtle.right(120)
turtle.end_fill()


turtle.penup()

turtle.goto(-50,20)

turtle.pendown()

turtle.pencolor("#000000")

turtle.width(15)
# This draw a mouth
turtle.forward(100)

turtle.width(1)

turtle.penup()

turtle.goto(-55,330)

# This draws a series of brown triangles for the hair
turtle.color("#9C6503")
turtle.begin_fill()
for x in range(5):
    for y in range(3):
        turtle.right(120)
        turtle.forward(40)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
turtle.end_fill()


turtle.penup()

turtle.goto(-90,320)

turtle.pendown()


# This makes a single brown triangle to add next to the hair
def draw_one_hair():
    turtle.color("#9C6503")
    turtle.begin_fill()
    for z in range(3):
        turtle.right(120)
        turtle.forward(40)
    turtle.end_fill()


draw_one_hair()

turtle.penup()

turtle.goto(140,320)

turtle.pendown()

draw_one_hair()


turtle.exitonclick()