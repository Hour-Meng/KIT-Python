import turtle as t

square = t.Turtle()
square_write = t.Turtle()
diamond = t.Turtle()
diamond_write = t.Turtle()
hexagon = t.Turtle()
hexagon_write = t.Turtle()

def draw_square():
    square.fillcolor("red")
    square.begin_fill()
    
    square.penup()
    square.goto(-300,0)
    square.pendown()

    square_write.penup()
    square_write.goto(-300,-50)
    square_write.pendown()

    for i in range (0, 4):
        square.forward(90)
        square.left(90)
    square.end_fill()

    square_write.write("Square", font=("Arial", 20, "bold"))

def draw_diamond():
    diamond.fillcolor("green")
    diamond.begin_fill()

    diamond.penup()
    diamond.goto(-100,0)
    diamond.pendown()
    
    diamond_write.penup()
    diamond_write.goto(-100,-50)
    diamond_write.pendown()

    for i in range (0,5):
        diamond.forward(90)
        diamond.left(72)
    diamond.end_fill()

    diamond_write.write("Diamond", font=("Arial", 20, "bold"))

def draw_hexagon():
    hexagon.fillcolor("blue")
    hexagon.begin_fill()

    hexagon.penup()
    hexagon.goto(100,0)
    hexagon.pendown()

    hexagon_write.penup()
    hexagon_write.goto(100,-50)
    hexagon_write.pendown()

    for i in range (0, 6):
        hexagon.forward(90)
        hexagon.left(60)
    hexagon.end_fill()

    hexagon_write.write("Hexagon", font=("Arial", 20, "bold"))


draw_square()
draw_diamond()
draw_hexagon()
t.done()