from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    name = input('Input: ')
    font_name = random.choice(font_list)
    f = Figlet(font=font_name)
    print(f.renderText(name))

elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    if  not sys.argv[1] == '-f' or sys.argv[1] == '--font':
        sys.exit(1)
    name = input('Input: ')
    font_name = sys.argv[2]

    if font_name in font_list:
        f = Figlet(font=font_name)
        print(f.renderText(name))
    else:
        sys.exit(1)

else:
    sys.exit(1)
