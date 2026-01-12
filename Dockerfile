FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /code

# Copia primeiro apenas os requisitos para ganhar velocidade no build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da sua pasta local para dentro de /code
COPY . .

# Comando para rodar garantindo que o caminho atual (.) está no PYTHONPATH
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]