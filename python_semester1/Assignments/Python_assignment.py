import turtle as t

square = t.Turtle()
diamond = t.Turtle()
hexagon = t.Turtle()

def draw_square():
    square.fillcolor("red")
    square.begin_fill()

    square.penup()
    square.goto(-300,0)
    square.pendown()

    for i in range (0, 4):
        square.forward(90)
        square.left(90)
    square.end_fill()

def draw_diamond():
    diamond.fillcolor("green")
    diamond.penup()

    diamond.goto(-100,0)
    diamond.pendown()
    diamond.begin_fill()

    for i in range (0,5):
        diamond.forward(90)
        diamond.left(72)
    diamond.end_fill()

def draw_hexagon():
    hexagon.fillcolor("blue")
    hexagon.begin_fill()

    hexagon.penup()
    hexagon.goto(100,0)
    hexagon.pendown()

    for i in range (0, 6):
        hexagon.forward(90)
        hexagon.left(60)
    hexagon.end_fill()


draw_square()
draw_diamond()
draw_hexagon()

def greet():
    print("Hello, What shape do you want?")
    choice = input("1 for Square, 2 for Diamond, 3 for Hexagon: ")
    choice = int(choice)
    if choice == 1:
        draw_square
    elif choice == 2:
        draw_diamond
    elif choice == 3:
        draw_hexagon
    else:
        print("moron!")
