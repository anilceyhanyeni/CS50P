while True:
    try:
        mass = int(input("Enter Mass: "))
        break
    except ValueError:
        print("Enter an integer")

energy = mass * 300000000**2

print(energy)