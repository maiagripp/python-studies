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
copy_list = first[:]
copy_list.extend(second)
third = []
x= 0
while x < len(copy_list):
    y = 0
    while y < len(third):
        if copy_list[x] == third[y]:
            break
        y = y + 1
    if y == len(third):
        third.append(copy_list[x])
    x = x + 1

print(third)         