# Criando um dicionário com informações de uma pessoa
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores usando chaves
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando um novo par chave-valor
pessoa["profissão"] = "Engenheiro"
print("Profissão:", pessoa["profissão"])

# Modificando um valor existente
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["cidade"]
print("Informações restantes:", pessoa)


lista_de_pessoas = [
    {"nome": "Alice", "idade": 25},
    {"nome": "Bob", "idade": 30}
]

# Acessando informações das pessoas na lista
print("Nome da primeira pessoa:", lista_de_pessoas[0]["nome"])
print("Idade da segunda pessoa:", lista_de_pessoas[1]["idade"])