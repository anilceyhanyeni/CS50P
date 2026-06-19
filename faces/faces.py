def main():
    text = input(str("Enter emote: "))
    print(convert(text))

def convert(text: str):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

main()