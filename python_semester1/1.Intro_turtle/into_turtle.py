#import the turtle Module / Library
import turtle as t
import time

# Create a turtle object to control
fine_line = turtle.Turtle()

# Draw around using turtle methods
def star():
    for i in range(1,10):
        fine_line.forward(200) #Instruct computer to draw line forward in 200pixel distance
        time.sleep(1)
        fine_line.right(200)
    t.done()
    # Prevent the output screen from closing turtle.done()

def square(far):
    for _ in range(4):
        fine_line.forward(far)
        fine_line.right(90)

def circle(far):
    fine_line.circle(far)

def forward(far):
    fine_line.forward(far)

def backward(far):
    fine_line.backward(far)

def left(far):
    fine_line.left(far)

def right(far):
    fine_line.right(far)


"""circle(45)
forward(90)
circle(45)
backward(68)
left(90)
forward(180)      #dih
right(90)
forward(45)
right(90)
forward(180)
turtle.done()"""
