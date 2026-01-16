import turtle as t
import time

from numpy import power

#dwr stands for drawer
dwr = t.Turtle()
dwr.hideturtle()

choices = ["triangle", "square", "circle"]

#ustc stands for user input choice
#urng
#usts stands for user input size

ustc  = t.textinput("Please select one", "Triangle, Square, Circle")


#sqm stands for square maker
def sqm(size):
    for _ in range(4):
        dwr.forward(size)
        dwr.left(90)

#tm stands for triangle maker
def tm(size):
    for _ in range(3):
        dwr.forward(size)
        dwr.left(120)

#crm stands for circle maker

def crm(size):
    dwr.circle(size)


#This is the decision making

while ustc is None or ustc.lower() not in choices:

    dwr.write("That is not valid", font=("Arial", 20, "bold"), align="center")

    time.sleep(1.5)
    ustc  = t.textinput("Please select one", "Triangle, Square, Circle")
else:
    dwr.clear()
    usts = int(t.numinput("Size", "Please enter the size"))

    urng = t.textinput("Color option", "What color do you want?")
    
    if urng is None or urng.strip() == "":
        urng = "black"  # Default color if user cancels or didn't enter anything

    dwr.begin_fill()
    dwr.fillcolor(urng.lower())

    if ustc.lower() == "triangle":
        tm(usts)

    elif ustc.lower() == "square":
        sqm(usts)

    elif ustc.lower() == "circle":
        crm(usts)

    else:
        print("Invalid Please try again")

dwr.end_fill()




t.done()