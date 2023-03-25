import random

secret_key = random.randint(1,100)
spin = 0

while spin is not secret_key:
    spin = int(input('Spin the dial \n'))
    if spin == 0:
        print('You have to spin unleast one time')
    else:    
        print(f'You spun the dial {spin} times')
        if(spin == secret_key):
            print('GREEN')
        elif(spin < secret_key):
            print('RED')
            print(f"You have to spin the dial {secret_key - spin} positions foward")
        elif(spin > secret_key):
            print(f"You have to spin the dial {spin - secret_key} positions backwards")
