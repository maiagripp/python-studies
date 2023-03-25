value = 0
while True:
    code = int(input('Type the code: '))
    if code == 0:
        break
    elif code == 1:
        price = 0.5
    elif code == 2:
        price = 1.0
    elif code == 3:
        price = 4.0
    elif code == 5:
        price = 7.0
    elif code == 9:
        price = 8.0
    else:
        print('invalid code')    
    if price != 0:
        quantity = int(input('Type the quantity: '))
        value = value + (price * quantity)
print(f"Total value ${value:8.2f}")