points = 0
question = 1

while question <= 3:
    answer = input(f"Answers question {question} ")
    if question == 1 and (answer == 'b' or answer == 'B'):
        points = points + 1
    if question == 2 and (answer == 'a' or answer == 'A'):
        points = points + 1
    if question == 3 and (answer == 'd' or answer == 'D'):
        points = points + 1
    question += 1
print(f"The student scored {points} points")
    