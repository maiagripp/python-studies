property_value = float(input('Whats the property value? '))

income = float(input('Whats the income? '))

years = int(input('How many years paying? '))
installments = years * 12

installment_value = property_value / installments
max_value_installment = income * 0.3

if installment_value > max_value_installment:
    print('Your loan wasnt approved')
else:
        print(f'''
          Your income its {income}, the property value its {property_value},
          the installments value its {installment_value}.
          So your loan was approved! 
          ''')