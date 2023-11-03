def main():
    userinput = input('enter emoji: ')
    print(convert(userinput))




def convert(userinput):
    userinput = userinput.replace(':)', '🙂').replace(':(', '🙁')
    return userinput

main()

