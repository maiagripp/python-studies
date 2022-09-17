dividendo = int(input('Type a number '))
divisor = int(input('Type a number '))

x = dividendo
quociente = 0

while x >= divisor:
    x = x- divisor
    print(x)
    quociente = quociente + 1