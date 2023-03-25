speed = int(input('The driver speed was:'))


if speed > 80:
    value = (speed - 80) * 5
    print(f'You got a traffic ticket. The fine its ${value}')
    
else:
    print("Your speed its ok! Have a safe travel!")