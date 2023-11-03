import random
import sys

while True:
    try:
        n = int(input('Level: '))
        if not n >= 1:
            continue
        x = int(input('Guess: '))
        if x < 1 or x > n:
            continue
        random_number = random.randint(1, n)
        if x == random_number:
            print('Just Right!')
            sys.exit()
        elif x > random_number:
            print('Too Large!')
        elif x < random_number:
            print('Too Small!')
    except ValueError:
        continue
