import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Keep asking for guesses
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except:
        pass
