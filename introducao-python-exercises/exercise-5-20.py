while True:
    operation = input(f'''Choose an operation: p for plus,\n m for minus,\n d for division,
                      \n m for multiplication,\n e for exit: ''').lower()
    
    if operation == 'e':
        break

    n = int(input('Type a number'))
    c = 1
    if operation == 'p':
        while c <= 10:
            sum = n + c
            print(f'The sum of {n} and {c} is equal to {sum}')
            c += 1
        break    
    elif operation == 's':
        while c <= 10:
            minus = n - c
            print(f'The subtraction of {n} and {c} is equal to {minus}')
            c += 1
        break
    elif operation == 'd':
        while c <= 10:
            if n == 0 or c == 0:
                print('We cant divide for zero')
                break 
            division = n / c
            print(f'The divison of {n} and {c} is equal to {division}')
            c += 1
        break
    elif operation == 'm':
        while c <= 10:
            multiplication = n * c
            print(f'The sum of {n} and {c} is equal to {multiplication}')
            c += 1
        break
    else:
        print('Invalid operation')

