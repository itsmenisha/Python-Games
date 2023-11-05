import random
number = random.randint(0, 300)
print(" guess number between 0 to 300")
guess = 0
while guess != number:
    guess = int(input("enter a number"))
    if guess < number:
        print("guess higher")
    elif (guess > number):
        print("guess lower")
    else:
        print("you guessed right")
