user_input = input('enter variable in camel case: ')
new_string = ''

for char in user_input:
    if char.isupper():
        new_string = new_string + '_' + char.lower()
    else:
        new_string = new_string + char

print('snake_case:',new_string)
