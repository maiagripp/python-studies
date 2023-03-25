income = float(input('Type the employee actual income '))

if income > 1250:
    income = income + (income * 0.1)
    print(income)
elif income <= 1250:
    income = income + (income * 0.15)
    print(income)