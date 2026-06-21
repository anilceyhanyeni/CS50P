grocery_list = {}
while True:
    try:
        item = input() #get input
        if item not in grocery_list: #if input not in list
            grocery_list.update({item : 1}) #add item with amount 1
        else:   #if item in list
            value = int(grocery_list.get(item)) #get value of item
            grocery_list.update({ item : value + 1}) #update value of item by increasing it by 1 
    except EOFError:
        break

for x in sorted(grocery_list):
    print(str.upper(f"{grocery_list.get(x)} {x}"))
