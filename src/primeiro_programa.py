import os

def exibir_nome_do_jogo():
    print('''
▄▀█ █░░ █░█ █▀█ █▀▀ █▀▀ █▀█
█▀█ █▄▄ █▄█ █▀▄ ██▄ █▄▄ █▄█
''')

def fim_de_jogo():
    os.system('clear')
    print('''
    ▒█▀▀▀ ▀█▀ █▀▄▀█ 　 █▀▀▄ █▀▀ 　 ░░▀ █▀▀█ █▀▀▀ █▀▀█ 
    ▒█▀▀▀ ▒█░ █░▀░█ 　 █░░█ █▀▀ 　 ░░█ █░░█ █░▀█ █░░█ 
    ▒█░░░ ▄█▄ ▀░░░▀ 　 ▀▀▀░ ▀▀▀ 　 █▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀
    ''')
    print(f'A palavra secreta era ► {cor_fundo_verde}{palavra_secretra}{reset_cor}\n')

palavra_secretra = 'esalq'
palavra_adivinhada = ['_'] * len(palavra_secretra)
letras_palavra_lista = list(palavra_secretra)
palavras_de_cada_tentativa = {}
numero_de_tentativas = 1

letras_certa_na_posicao_errada = []
letras_erradas = []
letras_corretas = []

cor_fundo_verde = "\033[42m"
cor_fundo_vermelho = "\033[41m"
reset_cor = "\033[0m"

def solicitar_chute():
    chute = input(f'\n{numero_de_tentativas}ª tentativa: ')
    if len(chute) == len(palavra_secretra):
        palavras_de_cada_tentativa[numero_de_tentativas] = chute
        return chute
    else:
        exibir_tela_principal()
        print('CHUTE INVÁLIDO: deve ter 5 letras!\n')
        return solicitar_chute()

def exibir_tela_principal():
    os.system('clear')
    exibir_nome_do_jogo()
    print(f'Tem a letra: {cor_fundo_verde}{letras_certa_na_posicao_errada}{reset_cor}')
    print(f'Não tem a letra: {cor_fundo_vermelho}{letras_erradas}{reset_cor}\n')
    
    print(' '.join(palavra_adivinhada), '\n')
    for chave, valor in palavras_de_cada_tentativa.items():
         print(f"Tentativa {chave}: {valor}")


while numero_de_tentativas < 6:
    exibir_tela_principal()
    chute = solicitar_chute()

    if chute == palavra_secretra:
        fim_de_jogo()
        break
    else:
        numero_de_tentativas +=  1        
        chute_lista = list(chute)

        for i in range(len(chute_lista)):
            if chute_lista[i] == letras_palavra_lista[i]:
                letras_corretas.append(chute_lista[i])
                palavra_adivinhada[i] = chute_lista[i]
            elif chute_lista[i] in letras_palavra_lista:
                letras_certa_na_posicao_errada.append(chute_lista[i])
            else:
                letras_erradas.append(chute_lista[i])

        letras_certa_na_posicao_errada = list(set(letras_certa_na_posicao_errada))
        letras_erradas = list(set(letras_erradas))

if numero_de_tentativas == 6:
    fim_de_jogo()