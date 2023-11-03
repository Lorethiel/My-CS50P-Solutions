userinput = input('enter: ').split(' ')

num1 = int(userinput[0])
num2 = int(userinput[2])

if userinput[1] == '+':
    print(float(num1 + num2))

elif userinput[1] == '-':
    print(float(num1 - num2))

elif userinput[1] == '*':
    print(float(num1 * num2))

elif userinput[1] == '/':
    print(float(num1 / num2))
