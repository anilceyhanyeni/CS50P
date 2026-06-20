#In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    text = input("Input:")
    print(omit_vowels(text))

def omit_vowels(text):
    vowels = ["a","e","i","o","u"]
    omit_text=""
    for char in text:
        if str.lower(char) in vowels:
            pass
        else:
            omit_text += char
    return omit_text

if __name__ == "__main__":
    main()    