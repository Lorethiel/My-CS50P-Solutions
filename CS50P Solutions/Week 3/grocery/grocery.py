grocery_dict = {}

while True:
    try:
        item = input().upper()
        if not item in grocery_dict:
            grocery_dict[item] = 1
        else:
            grocery_dict[item] = grocery_dict[item] + 1

    except EOFError:
        break


for key,value in sorted(grocery_dict.items()):
    print(value,key)




