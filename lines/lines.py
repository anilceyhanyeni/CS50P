import sys

def main():
    lines_of_code()

def lines_of_code():
    complexity = 0
    if len(sys.argv) < 2:
        print("Too few command line arguments")
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("Too many command line arguments")
        sys.exit(1)

    if ".py" not in (sys.argv[1]):
        print("Not a python file")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                if not (line.lstrip()).startswith("#"):
                    complexity += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    print(complexity)

if __name__ == "__main__":
    main()
    