value = int(input("Type the payment value:"))
notes = 0
actual_value = 50
pay_value = value
while True:
    if actual_value <= pay_value:
        pay_value -= actual_value
        notes += 1
    else:
        print(f"{notes} note of ${actual_value}")
        if pay_value == 0:
            break
        elif actual_value == 50:
            actual_value = 20
        elif actual_value == 20:
            actual_value = 10
        elif actual_value == 10:
            actual_value = 5
        elif actual_value == 5:
            actual_value = 1
        notes = 0