import random

number  = random.randint(1, 10)
max_attempts = 3

a=0
while a < max_attempts:
    guess = int(input(f"Attempt {a + 1}: Enter your number guess: "))
    a += 1

    if guess < number:
        print("Guess is too low!")
    elif guess > number:
        print("Guess is too high!")
    else:
        print(f"Congratulations! You have guessed the correct number {number}.")
        break
else:
    print(f"OOps! You've used all {max_attempts} attempts and all numbers were incorrect . The correct number is  {number}.")
