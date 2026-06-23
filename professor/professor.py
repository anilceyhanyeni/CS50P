import random

def main():
    level = get_level()
    generate_integer(level)

    score = 0
    for i in range(10):
        x0, y0 = generate_integer(level), generate_integer(level)
        print(f"{x0} + {y0} = ")
        result = x0 + y0
        tries = 3 
        while tries != 0:
            guess = input()
            if int(guess) == result:
                score += 1
                break
            else:
                print("EEE")
                tries -= 1
    print(score)


#####################################
def get_level():
    while True:
        level = int(input("Level:"))
        if not level in [1,2,3]:
            continue
        else:
            return level
#####################################
def generate_integer(level):
        try:
            if not level in [1,2,3]:
                raise ValueError
        except ValueError:
            ValueError
        else:
            x = random.randint(1, 10 ** level -1 )
            return x
#####################################

if __name__ == "__main__":
    main()