def main():
    p = fuel()
    if p == 'F' or p == 'E':
        print(p)
    else:
         print(f'{p}%')





def fuel(i):
    while True:
        try:

            if not '/' in i:
                continue
            for l in i:
                if l == '/' :
                    index = i.index(l)

            r = int(i[0:index])/int(i[index+1:])
            if int(i[0:index]) > int(i[index+1:]):
                continue
            if r >= (99/100):
                return 'F'

            elif r <= (1/100):
                return 'E'
            else:
                return int(round(r*100))
        except (ValueError, ZeroDivisionError):
            continue




main()



