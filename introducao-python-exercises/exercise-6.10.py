l = [15, 7, 27, 39]
p = int(input("Type the p_value to search "))
v = int(input("Type the v_value to search "))

x = 0
found_p = -1
found_v = -1
found_first = 0
while x < len(l):
    if l[x] == p:
        found_p = x
    if l[x] == v:
        found_v = x
    x += 1
if found_p != -1:
    print(f"p: {p} founded in position {found_p}")
else:
    print(f"p: {p} not founded")
if found_v != -1:
    print(f"p: {v} founded in position {found_v}")
else:
    print(f"p: {v} not founded")
if found_p != -1 and found_v != -1:
    if found_p <= found_v:
        print(f"p was found before v")
    else:
        print(f"v was found before p")
