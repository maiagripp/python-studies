name = input('Enter your name: \n')

print('Your name is: ' + name.capitalize())

age = input('Enter your age: \n')

print('Your age is: {}'.format(age))

print('Your name is {} and your age is {}'.format(name.capitalize(), age))

#formatter
x = 3.14159
print('{:.2f}'.format(x))