amount_due = 50
total_inserted = 0

while total_inserted < 50:
    user_input = int(input('Insert Coin: '))

    if user_input in [5, 10, 25]:
        total_inserted = total_inserted + user_input
        amount_due = 50 - total_inserted
        if amount_due > 0:
            print('Amount Due:',amount_due)

    else:
        print('Amount Due:',amount_due)

print('Change Owed:',total_inserted - 50)
