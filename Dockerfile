# Use a imagem Python 3.12
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie todos os seus arquivos Python para o contêiner
COPY . src/app

# Instale qualquer dependência se necessário
# Exemplo: RUN pip install -r requirements.txt

# O comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "app.py"]
