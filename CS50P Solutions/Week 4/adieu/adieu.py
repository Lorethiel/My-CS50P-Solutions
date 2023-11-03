import inflect
import sys

p = inflect.engine()

adieu = 'Adieu, adieu, to '
name_list = []

while True:
    try:
        names = input('Name: ').title()
        name_list.append(names)
        name_tup = tuple(name_list)




    except EOFError:
        break
        print()

print(adieu+p.join(name_tup))
