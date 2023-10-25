for i in range(11):
    print(i)

print('*'*20)

for i in range(10, 21):
    print(i)

print('*'*20)

for i in range(10, 21, 2):
    print(i)
print('*'*20)

lista_de_carros = ['Uno', 'Gol', 147]
for carro in lista_de_carros:
    print(carro)
print('*'*20)

for i, carro in enumerate(lista_de_carros):
    print(f'posicao:{i} | carro: {carro}')