from turtle import Turtle, Screen
import random

timmy= Turtle()
# timmy.shape("turtle")

colors =["CornflowerBlue","IndianRed","DarkOrchid","SeaGreen","LightSeaGreen","Wheat","SlateGray","DeepSkyBlue"]
def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)



for shape_sides in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shapes(shape_sides)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
#
# for _ in range(5):
#     timmy.forward(100)
#     timmy.right(72)
#
# for _ in range(6):
#     timmy.forward(100)
#     timmy.right(60)
#
# for _ in range(7):
#     timmy.forward(100)
#     timmy.right(51.43)
#
# for _ in range(8):
#     timmy.forward(100)
#     timmy.right(45)
#
# for _ in range(9):
#     timmy.forward(100)
#     timmy.right(40)
#
# for _ in range(10):
#     timmy.forward(100)
#     timmy.right(36)


screen = Screen()
screen.exitonclick()