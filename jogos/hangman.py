print('*******************************')
print('**Bem vindo ao jogo da Forca!**')
print('*******************************')

secret_word = 'banana'
right_letters = ['_', '_', '_', '_', '_', '_']

right = False
hanged = False
errors = 0

print(right_letters)
while(not right and not hanged):
    guess = input('Qual a letra?')

    if(guess in secret_word):
        position = 0 
    for letter in secret_word:
        if(guess.upper() == letter.upper()):
            right_letters[position] = letter
            position += 1
            print(right_letters)
        else:
            errors += 1

    right = '_' not in right_letters
    hanged = errors == 6
    print(right_letters)

if(right):
    print('Você acertou!')
else:
    print('Você perdeu!')
print('Fim do jogo')