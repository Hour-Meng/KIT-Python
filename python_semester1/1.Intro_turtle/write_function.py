import turtle as t

user = input("Type something: ")

writer = t.Turtle()
writer.shape("turtle")


writer.write(user, move=True, font=("Arial", 32, "bold"), align="center")

t.done()