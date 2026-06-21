def main():
    print(fuel())

def fuel():
    while True:
        try:
            x, y = input("Enter fuel in X/Y format:").split("/")
            x,y = int(x), int(y) #check if x and y are available to be cast to actual integers
            if y == 0:
                raise ZeroDivisionError
            if (x < 0 or y < 0) or ( x > y) : # raises ValueError if x or y is negative or x is greater than y
                raise ValueError  #this will make except block for valueError work
            nearest_integer = round(100 * x / y)
            
        except ValueError:
            print("X and Y must be integers, y must be greater than x and neither of them can be negative:")
        except ZeroDivisionError:
            print("Y can't be 0:")
        else:
            if nearest_integer <= 1:
                return "E"
            elif nearest_integer >= 99:
                return "F"
            else:
                return "%"+str(nearest_integer)
    
if __name__ == "__main__":
    main()
    



