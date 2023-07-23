FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o contêiner
COPY ./ .

# Instale as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da API Flask para o contêiner
COPY app.py .

# Exponha a porta em que a API Flask está escutando
EXPOSE 5000

# Defina o comando para iniciar a aplicação Flask
CMD ["python", "app.py"]