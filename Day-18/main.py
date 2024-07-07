from turtle1 import Turtle, Screen

tim = Turtle()

# Solution-1
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# Solution -2
for _ in range(4):
    tim.forward(100)
    tim.right(90)




screen =  Screen()
screen.exitonclick()