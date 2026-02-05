import random

num = random.randint(1, 100)
guesses = 0
max_guesses = 7

print("I have chosen a number between 1 and 100.")
print("You have 7 attempts.")

while guesses < max_guesses:
    n = int(input("Enter your guess: "))
    guesses += 1

    if n > num:
        print("Too high")
    elif n < num:
        print("Too low")
    else:
        print("You guessed right! ")
        print("Number of guesses:", guesses)
        break
else:
    print("Out of guesses! ")
    print("The number was:", num)
