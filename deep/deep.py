answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
print(answer)
print(type(answer))

if str.lower(answer) in ["42", "forty two", "forty-two"]:
        print("Yes")
else:
        print("No")
