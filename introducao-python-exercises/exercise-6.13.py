L = [-10, -8, 0, 1, 2, 5, -2, -4 ]

min = L[0]
max = L[0]

for e in L:
    if e < min:
        min = e
    elif e > max:
        max = e
        
    avg = (max + min)/2
print(f"The min is {min}")
print(f"The max is {max}" )
print(f"The average temp is {avg}")
