import random

while True:
    try:
        level = int(input("Level: "))
        if not level > 0:
            raise ValueError    
    except ValueError:
        #print("Enter positive integer!")
        continue
    else:
        break

number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess:"))
        if guess <= 0:
            raise ValueError
    except ValueError:
        #print("Enter positive integer!")
        continue
    else:
        if guess < number:
            print("Too small")
        elif guess > number:
            print("Too large")
        else:
            print("Just Right!")
            break