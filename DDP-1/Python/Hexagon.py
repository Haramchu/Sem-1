import turtle
turtle.getscreen()
turtle.pensize(5)

turtle.pencolor("#0000FF")
turtle.penup()

turtle.setposition(-50,-50)

turtle.pendown()
turtle.fillcolor("#FFFF00")
turtle.begin_fill()

turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)

turtle.hideturtle()
turtle.end_fill()
turtle.done()