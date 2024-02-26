# Projeto Modelo Íris com Docker

Este projeto demonstra a classificação do conjunto de dados Íris usando regressão logística em Python. Os resultados do modelo são armazenados em um banco de dados MongoDB. O projeto é containerizado usando Docker e docker-compose.

## Pré-requisitos

Para executar este projeto, você precisará de:
- Docker
- docker-compose

## Configuração

Clone o repositório e navegue até o diretório do projeto para iniciar.

## Execução

Execute o seguinte comando no terminal para iniciar o projeto:

```bash
docker-compose up --build
```

Este comando construirá a imagem do container para o aplicativo Python, iniciará o serviço MongoDB, e executará o script `modelo.py`. O script treina um modelo de regressão logística no conjunto de dados Íris e salva a acurácia no MongoDB.

## Criação da Imagem Docker

Para criar a imagem Docker do projeto:

1. **Construir a Imagem Docker**

   No diretório do projeto, construa a imagem Docker com o seguinte comando:

   ```bash
   docker build -t modelo .
   ```

   Este comando cria uma imagem Docker.

2. **Verificar a Imagem Criada**

   ```bash
   docker images
   ```

   A imagem `modelo` deve aparecer na lista de imagens disponíveis.

## Estrutura do Projeto

- `modelo.py`: Script que carrega o conjunto de dados Íris, treina um modelo de regressão logística, faz previsões e salva os resultados no MongoDB.
- `Dockerfile`: Define a imagem Docker para o aplicativo Python.
- `docker-compose.yml`: Configura os serviços necessários para o projeto.
- `requirements.txt`: Lista as dependências python do projeto.

# Link da Imagem no DockerHub
[Link](https://hub.docker.com/repository/docker/luanans/python-modelo/general)
