first_number = float(input("Type the first number "))
second_number = float(input("Type the second number "))

selected_operator = input("Select the operator ")

if selected_operator == "+":
    operation = first_number + second_number
elif selected_operator == "-":
    operation = first_number - second_number
elif selected_operator == "*":
    operation = first_number * second_number
elif selected_operator == "/":
    operation = first_number / second_number
else:
    print("Invalid operator")
    operation = 0

print(operation)
