x, y, z = input("Write number1, operator and number2 with spaces between them: ").split()
print(x,y,z)
x = float(x)
z = float(z)

match y:
    case "+":
        result = float(x + z)
    case "-":
        result = float(x - z)
    case "*":
        result = float(x * z)
    case "/":
        result = float(x / z)
print(f"{result:.1f}")