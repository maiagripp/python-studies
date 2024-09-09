def validate_input(message, options):
    options = options.lower()
    while True:
        choice = input(message)
        if choice.lower() in options:
            break
        print("Wrong choice. Choose again\n")
    return choice


print(validate_input("Choose an option:", "abcde"))