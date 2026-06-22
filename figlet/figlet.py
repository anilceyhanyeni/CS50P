from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    random_font = random.choice(fonts)
    figlet.setFont(font = random_font)
    print(figlet.renderText(text))
elif len(sys.argv) == 3:

    if not sys.argv[1] == ("-f" or "-font"):
        sys.exit("Invalid usage")

    if not sys.argv[2] in fonts:
        sys.exit("Invalid usage")
        
    text = input("Input: ")
    f = sys.argv[2]
    figlet.setFont(font = f)
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")
