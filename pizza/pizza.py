import csv
import tabulate
import sys

def pizza():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if not ".csv" in sys.argv[1]:
        print("File is not a csv file")
        sys.exit(1)

    try:
        file =  open(sys.argv[1], "r")
        menu = csv.reader(file)        
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    pizzas = []
    for row in menu:
        pizzas.append([row[0],row[1],row[2]])

    print(tabulate.tabulate(pizzas, headers="firstrow", tablefmt="grid"))


pizza()