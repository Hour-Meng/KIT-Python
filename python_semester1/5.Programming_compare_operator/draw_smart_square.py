import turtle as t

ds = t.Turtle()

#This one is user input short for ust
# ustl = user input for lenght

ustl =  int(t.numinput("pease bro make is less than 200", "Please enter the lenght of your square: ")) # float
# the first one is title and the sencond one is description t.numinput("title", "description")
ustt = t.textinput("color option", "write it in small letters")

def ds_1(s_lenght: int, color: str):
    ds.begin_fill()
    ds.fillcolor(color)

    ds.hideturtle()

    for _ in range(4):
        ds.forward(s_lenght)
        ds.left(90)

    ds.end_fill()

if ustt is not str:
    ds.write("You stupid idiot!", font=("Arial", 20, "bold"))
    t.done()

if ustl < 200:

    ds_1(ustl, ustt)

else:

    ds.write("You got it wrong bro")  # If it doesn't work then it will pop up this message instead

t.done()
