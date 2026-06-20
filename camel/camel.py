# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
def main():

    camel_case = input("camelCase: ")
    print(camel_to_snake(camel_case))

def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        #print(char)
        #print(type(char))
        if char == str.upper(char):
            snake_case = snake_case +  "_" + str.lower(char)
        else:
            snake_case = snake_case + char
    return snake_case


if __name__ == "__main__":
    main()