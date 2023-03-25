numbers = []

while len(numbers) < 3:
    number = int(input('Type a number:'))
    numbers.append(number)
      
print(f'The largest number its {max(numbers)}')
print(f'The smallest number its {min(numbers)}')
