menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cost = 0
while True:
    try:
        item = input("Item: ")
    except EOFError:
        print("EOFError")
        break
    else:    
        if item.title() in menu:
            cost += float(menu.get(item.title())) # get value of key, turn it to float and add it to cost
            print(f"${cost:.2f}")