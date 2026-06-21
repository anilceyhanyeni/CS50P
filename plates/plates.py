def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    while True:
        #check alpha-numeric
        for char in s:
            if not char.isalnum:
                #print("NON-ALPHANUM")
                return False
        #check length
        if not  2<= len(s) <= 6:
            #print("LENGTH")
            return False 
        #check first two letter
        for char in s[0:2]:
            if not char.isalpha():
                #print("FİRST TWO")
                return False
        #no 0 after letter and no letter after a number
        number_start = False
        for char in s:
            if number_start == False and char == "0": 
                #print("ZERO")
                return False # this will return false only if 0 is the first number
            if char.isdigit():
                number_start = True
            if number_start == True and char.isdigit() == False:
                #print("LETTER AFTER NUMBER")
                return False


        return True
            
if __name__ == "__main__":
    main()
