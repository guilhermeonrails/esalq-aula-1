print('IMC\n')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso /altura ** 2
imc = round(imc, 2)

print(f'\nSeu IMC é {imc}')