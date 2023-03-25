l = [15, 7, 27, 39]
p = int(input("Type the p_value to search "))
v = int(input("Type the v_value to search "))

x = 0
found_p = False
found_v = False
found_first = 0
while x < len(l):
    if l[x] == p:
        found_p = True
        if not found_v:
            found_first = 1
    if l[x] == v:
        found_v = True
        if not found_p:
            found_first = 2
    x += 1
if found_p:
    print(f"p: {p} founded")
else:
    print(f"p: {p} not founded")
if found_v:
    print(f"p: {v} founded")
else:
    print(f"p: {v} not founded")
if found_first == 1:
    print(f"p was found before v")
elif found_first == 2:
    print(f"v was found before p")
