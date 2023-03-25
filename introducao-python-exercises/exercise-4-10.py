kwh_consumed = float(input('What was the kWh consumed? '))

instalation = (input('Whats your instalation? R for residential, I for industries and C for stores ')).upper()

if instalation == 'R' and kwh_consumed <= 500:
    bill = kwh_consumed * 0.4
    print(f'Your bill was ${bill:.2f}')
elif instalation == 'R' and kwh_consumed > 500:
    bill = kwh_consumed * 0.65
    print(f'Your bill was ${bill:.2f}')
elif instalation == 'C' and kwh_consumed <= 1000:
    bill = kwh_consumed * 0.55
    print(f'Your bill was ${bill:.2f}')
elif instalation == 'C' and kwh_consumed > 1000:
    bill = kwh_consumed * 0.60
    print(f'Your bill was ${bill:.2f}')
elif instalation == 'I' and kwh_consumed <= 5000:
    bill = kwh_consumed * 0.55
    print(f'Your bill was ${bill:.2f}')
elif instalation == 'C' and kwh_consumed > 5000:
    bill = kwh_consumed * 0.60
    print(f'Your bill was ${bill:.2f}')
else:
    print('Error! Instalation dont exist!')