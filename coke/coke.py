#In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
coin_list = [5,10,25]
amount_due = 50
while True:
    coin = int(input("Insert 5, 10 or 25 cents: "))
    if coin in coin_list:
        amount_due -= coin
        if amount_due <= 0:
            print(f"Change Owed:{-amount_due}")
            break
        else:
            print(f"Amount due:{amount_due}" )
        

    
