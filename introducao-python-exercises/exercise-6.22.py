a = "AAACTBF"
b = "CBTYU"

c = []
for letra in a:
    if letra in b:
        c.append(letra)
print("".join(c))
