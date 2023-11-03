menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

tot = 0
while True:
   try:
       cfood = input('Item: ')
       food = cfood.lower().title()
       if not food in menu:
           continue
       price = menu[food]
       tot = tot + price
       print(f'Total: ${tot:.2f}')

   except EOFError:
       break









