a = [0, 1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7, 8, 9, 10]

c_1 = set(a)
c_2 = set(b)

print(c_1 & c_2)
print(c_2 - c_1)
print(c_1 - c_2)
