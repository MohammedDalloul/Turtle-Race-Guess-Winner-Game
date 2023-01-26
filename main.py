import random
from turtle import Turtle, Screen
race_off = True
screen = Screen()
screen.setup(width = 800, height = 600)
player_choice = screen.textinput(title="Welcom to our race", prompt="guess the winner color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# def running():
#     n.speed(random.randint(1, 4))
#     n.fd(20)

if player_choice:
    race_off = False

num = 0
h = 170
turtles_list = []
for n in colors:
    abood = Turtle("turtle")
    abood.color(colors[num])
    abood.penup()
    abood.goto(x=-380, y=h)
    num+=1
    h-=65
    turtles_list.append(abood)

while race_off == False:

    for tur in turtles_list:
        if tur.xcor() > 350:
            race_off = True
            winning_color = tur.pencolor()
            if winning_color == player_choice:
                print(f"You've won! Congrats!")
            else:
                print(f"the {winning_color}-turtle had won, You've lost!")
        step = random.randint(15, 25)
        vilo = random.randint(2, 5)
        tur.speed(vilo)
        tur.fd(step)



screen.exitonclick()

# abood = Turtle()
# abood.shape("turtle")
# abood.penup()
# abood.goto(x=-380, y=200)
#
# mahmoud = Turtle()
# mahmoud.shape("turtle")
# mahmoud.penup()
# mahmoud.goto(x=-380, y=100)
#
# tasneem = Turtle()
# tasneem.shape("turtle")
# tasneem.penup()
# tasneem.goto(x=-380, y=0)
#
# amal = Turtle()
# amal.shape("turtle")
# amal.penup()
# amal.goto(x=-380, y=-100)
#
# rawan = Turtle()
# rawan.shape("turtle")
# rawan.penup()
# rawan.goto(x=-380, y=-200)




