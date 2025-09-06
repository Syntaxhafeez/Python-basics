# create a random number guessing game with python

import random
num = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))

    if guess == num:
        print("congrats! your guess is correct: ", num)
        break
    elif guess > num:
        print("Too high! enter small number")
    else:
        print("Too small! enter big number")