with open("odds.txt", "w") as odds, open("evens.txt", "w") as evens:
    for n in range(0, 1000):
        if n % 2 == 0:
            odds.write(f"{n}\n")
        else:
            evens.write(f"{n}\n")