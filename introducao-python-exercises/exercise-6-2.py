first = []
second = []
while True:
    e = int(input("Type a value for the first list (0 to end): "))
    if e == 0:
        break
    first.append(e)
while True:
    e = int(input("Type a value for the second list (0 to end): "))
    if e == 0:
        break
    second.append(e)
third = first[:]  # Copia os elementos da primeira lista
third.extend(second)
x = 0
while x < len(third):
    print(f"{x}: {third[x]}")
    x = x + 1