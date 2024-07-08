import turtle
import turtle as t
import random

tim = t.Turtle()
tim.pensize(10)
t.colormode(255)

# Custom color palate
# colors =["CornflowerBlue","IndianRed","DarkOrchid","SeaGreen","LightSeaGreen","Wheat","SlateGray","DeepSkyBlue"]
directions = [0, 90, 180, 270]
tim.speed("fastest")

# Random Colorpalate
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r, g, b)
    return rand_color



for _ in range(200):
    tim.forward(30)
    tim.color(random_color())
    # when custom color palate
    # tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
