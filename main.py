import turtle

t = turtle.Pen()

t.fillcolor("#FFD700")
t.begin_fill()

t.circle(500,15)

t.left(75)
t.forward(80)

t.right(35)
t.forward(80)

t.left(155)
t.forward(130)

t.right(90)
t.forward(150)

t.left(120)
t.forward(150)

t.right(90)
t.forward(130)

t.left(155)
t.forward(80)

t.right(35)
t.forward(80)

t.left(75)

t.circle(500, 17.7)
t.end_fill()

t.fillcolor("#FFD700")
t.begin_fill()

t.up()
t.goto(29, 160)
t.down()

t.left(30)
t.forward(80)

t.right(123)
t.forward(85)

t.right(60)
t.forward(38)

t.right(90)
t.forward(70)

t.end_fill()

t.fillcolor("#FFD700")
t.begin_fill()

t.up()
t.goto(-50,160)
t.down()

t.left(28.5)
t.forward(80)

t.left(121.5)
t.forward(85)

t.left(60)
t.forward(38)

t.left(91)
t.forward(70)

t.end_fill()

t.fillcolor("#3CB371")
t.begin_fill()

t.up()
t.goto(-80,40)
t.down()

t.circle(15)

t.end_fill()

t.fillcolor("#3CB371")
t.begin_fill()

t.up()
t.goto(80,40)
t.down()

t.circle(15)

t.end_fill()

t.up()
t.goto(-10,75)
t.down()

t.fillcolor("#3CB371")
t.begin_fill()

t.left(122)
t.shape("circle")
t.shapesize(6,3.5,2)

t.end_fill()

turtle.done()