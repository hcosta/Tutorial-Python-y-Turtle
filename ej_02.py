import turtle as t

t.setup(500,500)
t.shape("turtle")
t.color("green")

t.penup()
t.forward(200)  # Nos posicionamos a la derecha
t.pendown()
t.left(90)
t.forward(150)  # Dibujamos la mitad hacia arriba
t.left(90)
t.forward(400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(400)
t.left(90)
t.forward(150)  # Última mitad hacia arriba

t.done()
t.bye() 
