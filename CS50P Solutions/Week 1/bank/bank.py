userinput = input('Greeting: ')

if userinput.lower().strip().startswith('hello'):
    print('$0')

elif userinput.lower().strip().startswith('h'):
    print('$20')

else:
    print('$100')

