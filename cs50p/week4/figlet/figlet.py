from pyfiglet import Figlet
import random
import sys


fonts = Figlet().getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit('Invalid usage')


else:
    sys.exit('Invalid usage')


text = input('Input: ')
print('output:\n', Figlet(font=font).renderText(text))
