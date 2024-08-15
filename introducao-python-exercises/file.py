file = open("number.txt", "w")
for line in range(1, 101):
    file.write(f"{line}\n")
file.close()