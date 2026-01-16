import turtle as t

square = t.Turtle()
writer = t.Turtle()

def square_maker(size: int|float, fill_color: str, x_cordinate:int|float):

    square.pensize(10)
    square.pencolor("black")
    
    square.color(fill_color)
    square.begin_fill()

    square.penup()
    square.goto(x_cordinate,0)
    square.pendown()

    for i in range(0,4):
        square.forward(size)
        square.left(90)
        
    square.end_fill()
    square.hideturtle()

# Writert
writer.penup()
writer.goto(0, 180)
writer.pendown()
writer.write("A frame of Squares",align=("center"), font=("Arila", 30, "bold") )
writer.hideturtle()

square_maker(45, "green", -150 )
square_maker(90, "orange", -50 )
square_maker(135, "blue", 120 )

t.done()