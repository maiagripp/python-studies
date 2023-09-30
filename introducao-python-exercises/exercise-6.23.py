a = "CTA"
b = "ABC"

c = []

for letra in a:
    if letra not in b:
        c.append(letra)
for letra in b:
    if letra not in a and letra not in c:
        c.append(letra)
print("".join(c))
