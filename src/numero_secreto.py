import random
import os

os.system('clear')
print('Número secreto\n')

numero_secreto = random.randint(1, 5)
chute = int(input('Digite um número entre 1 e 5: '))
if chute == numero_secreto:
    print('Você acetou!')
else:
    print(f'Quase... o número secreto era {numero_secreto}')
