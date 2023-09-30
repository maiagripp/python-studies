dict = {}

frase = ("O rato").lower()

for e in frase:
    if e in dict:
        dict[e] = dict[e] + 1
    else:
        dict[e] = 1
print(dict)