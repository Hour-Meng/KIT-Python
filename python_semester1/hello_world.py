import random

balance = 10

while balance > 0:
    print(f"Current balance is ${balance}")
    print("Pick a number between 0 to 10")
    game = input("Guess the number bro: ")
    ran = random.randint(0,10)

    if ran == game:
        balance += 1
        print("You win!")
        print(f"{ran} and your is {game}")
    else:
        balance -= 1
        print("You lost")
        print(f"{ran} and your is {game}")