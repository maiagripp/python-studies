expression = input("Type the parentesis sequel to be validate:")
x = 0
stack = []
while x < len(expression):
    if expression[x] == "(":
        stack.append("(")
    if expression[x] == ")":
        if len(stack) > 0:
            top = stack.pop(-1)
        else: 
            stack.append(")")
            break
    x = x + 1
if len(stack) == 0:
    print("Ok")
else:
    print("Not Ok")
