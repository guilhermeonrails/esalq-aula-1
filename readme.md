# Usando o docker com Python 3.12

- Faça o donwload deste repositório

- Abra a paste de preferência no [Visual Studio Code](https://code.visualstudio.com/)

- Execute o comando `docker-compose build` para construir a imagem do Docker

- Agora, suba a imagem com `docker-compose up`

- Crie seus arquivos Python na pasta src

# Como executar os arquivos criados no Docker?

- Para executar os arquivos Python criados em **src**, execute o comando:

```
docker-compose run app python nome_do_arquivo.py
```

> Substitua o `nome_do_arquivo.py` pelo nome do arquivo que deseja executar.
