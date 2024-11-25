from turtle import Turtle, Screen
from typing import final

import heroes

tim=Turtle()

tim.shape("turtle")
tim.color("black")
tim.pencolor("black")
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)

import heroes as h

tom=heroes.gen()
print(tom)





screen=Screen()
screen.exitonclick()

