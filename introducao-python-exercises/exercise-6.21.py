a = "AABBEFAAT"
b = "BE"

p = 0
while p > -1:
    p = a.find(b, p)
    if p >= 0:
        print(f"Posição: {p}")
        p += 1
