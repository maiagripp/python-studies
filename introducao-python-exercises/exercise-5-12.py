initial_deposit = float(input('What is the initial deposit? '))
monthly_deposit = float(input('What is the monthly deposit? '))
rate_interest = float(input('What is the rate interest of the saving? '))

balance = initial_deposit
month = 1
while month <= 24:
   balance = balance + monthly_deposit + (balance * (rate_interest/100))
   print(f"Balance of the month {month} é de R${balance:5.2f}.")
   month = month + 1
    
print(f"The final balance with the income was R${balance-initial_deposit-(monthly_deposit*24):8.2f}.")
   
   