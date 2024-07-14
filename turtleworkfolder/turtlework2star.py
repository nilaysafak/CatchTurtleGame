import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("dark blue")
drawing_board.title("Star")


turtle_instance = turtle.Turtle()
'''
turtle_instance.left(110)
turtle_instance.forward(200)
turtle_instance.right(210)
turtle_instance.forward(200)
turtle_instance.left(150)
turtle_instance.forward(200)
turtle_instance.left(135)
turtle_instance.forward(200)
turtle_instance.left(139)
turtle_instance.forward(213)
'''
''' 
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(200)

turtle.done()
'''
 #polygon
turtle_instance = turtle.Turtle()
num_sides = 5
angle = 360.0 / num_sides * 2
sides_lenght = 200

for i in range(5):
    turtle_instance.left(angle)
    turtle_instance.forward(sides_lenght)

turtle.done()