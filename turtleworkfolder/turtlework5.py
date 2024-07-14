import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("#8166F0")
drawing_board.title("Direction")



turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotation_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
    #turtle_instance.right(100)

def rotation_left():
    turtle_instance.setheading(turtle_instance.heading()+10)
    #turtle_instance.left(100)

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotation_right,key = "Up")
drawing_board.onkey(fun=rotation_left,key="Down")
turtle.mainloop()