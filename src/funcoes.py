def soma():
    print(40+2)

soma()

def soma_com_argumentos(a, b):
    print(a + b)

soma_com_argumentos(40,2)

def soma_com_argumentos_e_retorno(a, b):
    return a + b 

resultado = soma_com_argumentos_e_retorno(40, 2)
print(resultado)

def quadrado(a):
    return a*a

print(quadrado(3))

def diga_oi(nome, caps=False):
    if caps:
        nome = nome.upper()
    return f'oi {nome}'

print(diga_oi('gui', True))