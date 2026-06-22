import emoji

text = input("Input: ")

print(emoji.emojize(text.strip(), language='alias'))