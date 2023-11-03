import random
def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        attempts = 0

        while attempts < 3:
            print(f'{x} + {y} = ', end='')
            sol = input()
            try:
                sol = int(sol)

                if sol == result:
                    score = score + 1
                    break
                else:
                    attempts = attempts + 1
                    print('EEE')
                    if attempts < 3:
                        print(f'{x} + {y} ={result}')

                        pass
            except ValueError:
                print('EEE')
                pass




    print(score)






def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if not 1 <= level <= 3:
                continue
        except:
            continue
        else:
            return level




def generate_integer(digits):

    if digits == 1:
        x = random.randint(0,9)

    elif digits == 2:
        x = random.randint(10,99)

    elif digits == 3:
        x = random.randint(100,999)


    return x





if __name__ == "__main__":
    main()
