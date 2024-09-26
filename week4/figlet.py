from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fonts = figlet.getFonts() 

if len(sys.argv) == 1:
    text = input('Input: ')
    figlet.setFont(font=choice(fonts))
    print(f"Output: {figlet.renderText(text)}")

elif len(sys.argv) == 3:
    if sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in fonts:
        sys.exit('Invalid usage')
    else:
        text = input('Input: ')
        figlet.setFont(sys.argv[2])
        print(f"Output: {figlet.renderText(text)}")



