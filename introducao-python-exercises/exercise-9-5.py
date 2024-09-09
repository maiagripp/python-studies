with open("evens.txt", "r") as evens:
    evens_numbers = evens.readlines()

    evens_numbers = [int(even_number.strip()) for even_number in evens_numbers]

    reversed_evens = evens_numbers[::-1]

with open("reversed_evens.txt", "w") as file:
    for number in reversed_evens:
        file.write(f"{number}\n")
