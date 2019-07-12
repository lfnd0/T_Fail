# Texley

## Configurações necessárias para executar o projeto:

  ### Instalação do ambiente virtual:
    python -m venv env
  ### Ativação do ambiente virtual:
    env\Scripts\activate
  ### Instalação do requisitos do projeto:
    pip install -r requirements.txt
  ### Criação das entidades no banco de dados:
    python manage.py migrate
  ### Executar o projeto no servidor local:
    python manage.py runserver