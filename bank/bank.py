greeting = input("Greetings: ")

if str.lower(greeting) == "hello":
    print("$0")
elif str.lower(greeting)[0] == "h":
    print("$20")
else:
    print("$100")