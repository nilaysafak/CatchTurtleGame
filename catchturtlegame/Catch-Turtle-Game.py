import turtle
import random
screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Catch The Turtle")
FONT = ('Arial', 30 , 'normal')
score = 0

game_over = False
turtle_list = []

count_down_turtle = turtle.Turtle()

#score turtle
score_turtle = turtle.Turtle()
def setupScoreTurtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("black")
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    score_turtle.setposition(0,y)
    score_turtle.write(arg="Score: 0", move=False, align="center",font=FONT)

grid_size= 10



def make_turtle(x,y):
    t = turtle.Turtle()
    def handle_click(x,y):
        global score 
        score += +1
        score_turtle.clear()
        score_turtle.write("Score : {}".format(score), move= False, align="center",font=FONT)
        print(x,y)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark blue")
    t.goto(x*grid_size,y*grid_size)
    t.pendown()
    turtle_list.append(t)


x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height- top_height / 10
    count_down_turtle.penup()
    count_down_turtle.hideturtle()
    count_down_turtle.setposition(0,y - 30)
    count_down_turtle.clear()
    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time),move=False,align="center",font=FONT)
        screen.ontimer(lambda:countdown(time - 1),1000)
    else :
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over!",align="center",font=FONT)


def start_game():
    global game_over
    game_over = False
    turtle.tracer(0)
    setupScoreTurtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10),10)



start_game()
turtle.mainloop()