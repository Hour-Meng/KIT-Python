
'''number_input = t.numinput("Math quizzzz", "what is 2+2")

print(number_input)



if number_input == 4:

    writer.shape("turtle")

    writer.write("great", move=True, font=("Arial", 32, "bold"), align="center")

    t.done()
else:
    writer.write("You are gay", move=True, font=("Arial", 32, "bold"), align="center")
'''

import turtle as t
import random
import time

balance = 10
writer = t.Turtle()


def show_balance():

    writer.shape("turtle")

    writer.write(f"Welcome to my Casino", move=True, font=("Arial", 32, "bold"), align="center")
    time.sleep(0.5)
    writer.clear()
    writer.write(f"Your balance is: ${balance}", move=True, font=("Arial", 32, "bold"), align="right")

    t.done()

def ran():
    random.randint(0,10)

while balance > 0:
    show_balance()



"""import turtle as t

username = t.textinput("What is your name?", "Give me your name")

print(username)

writer = t.Turtle()

writer.write(username, font=("Arial", 30, "bold"), align="center")

t.done()

"""