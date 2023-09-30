a = "TTAAC"

c = {}

for letra in a:
    c[letra] = c.get(letra, 0) + 1

for key, value in c.items():
    print(f"{key}: {value}xs")
