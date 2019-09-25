# Texley

## Configurações necessárias para executar o projeto:

  ### Instalação do ambiente virtual:
    python -m venv env
  ### Ativação do ambiente virtual:
    env\Scripts\activate
  ### Instalação dos requisitos do projeto:
    pip install -r requirements.txt
  ### Adição das entidades no banco de dados:
    python manage.py migrate
  ### Execução do projeto no servidor local:
    python manage.py runserver