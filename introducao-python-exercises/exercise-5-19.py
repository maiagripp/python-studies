while True:
    value = float(input("Type the payment value:"))
    if value == 0:
        break
    notes = 0
    actual_value = 100
    pay_value = value
    while True:
        if actual_value <= pay_value:
            pay_value -= actual_value
            notes += 1
        else:
            if actual_value >= 1:
                print(f"{notes} note of ${actual_value}")
            else:
                print(f"{notes} coin(s) of ${actual_value:5.2f}")
            if pay_value < 0.01:
                break
            elif actual_value == 100:
                actual_value = 50
            elif actual_value == 50:
                actual_value = 20
            elif actual_value == 20:
                actual_value = 10
            elif actual_value == 10:
                actual_value = 5
            elif actual_value == 5:
                actual_value = 1
            elif actual_value == 1:
                actual_value = 0.5
            elif actual_value == 0.5:
                actual_value = 0.1
            elif actual_value == 0.1:
                actual_value = 0.05
            elif actual_value == 0.05:
                actual_value = 0.02
            elif actual_value == 0.02:
                actual_value = 0.01
            notes = 0
    break