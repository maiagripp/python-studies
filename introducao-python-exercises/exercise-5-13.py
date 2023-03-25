initial_debt = float(input("Debt: "))
rate = float(input("Rate: "))
monthly_payment = float(input("Monthly payment: "))
month = 1
if (initial_debt * (rate/100) > monthly_payment):
    print("Your debt wasnt going to be payed, cause the rate is bigger than the monthly payment")
else:
    balance = initial_debt
    payed_rate = 0
    while balance > monthly_payment:
        rate = balance * rate / 100
        balance = balance + rate - monthly_payment
        payed_rate = payed_rate + rate
        print(f"Balance of the debt on month {month} was R${balance:6.2f}.")
        month = month + 1
    print(f'''To pay a debt of R${initial_debt:8.2f}, in a rate of {rate:5.2f}% , you will need {month - 1} months, \n
          paying a total of ${payed_rate:8.2f} rate. \n
         On the last month, you will have a residual balance of ${balance:8.2f} to pay.''')