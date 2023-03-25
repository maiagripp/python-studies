l = [15, 7, 27, 39]
p = int(input("Type the value to search"))

x = 0
while x < len(l):
    if l[x] == p:
        break
    x += 1
if x < len(l):
    print(f"{p} found in {x} position")
else: 
    print(f"{p} not found")
