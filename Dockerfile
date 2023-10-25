# Use a imagem Python 3.12
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie todos os seus arquivos Python para o contêiner
COPY . src/app