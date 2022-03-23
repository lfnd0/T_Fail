# PIBIC/UFAL 2019-2020
![](https://img.shields.io/badge/django-v.2.2.13-brightgreen)  ![](https://img.shields.io/badge/bootstrap-v.4.3.1-blueviolet)

## Texley

### Sobre o projeto
Uma ferramenta para apoiar o feedback em disciplinas de programação introdutória, através da extração de medidas de métricas de software.

### Execução da aplicação
  1. Criação e execução do banco de dados: `docker-compose up -d`. 
  2. Criação do ambiente virtual: `python -m venv .venv`.
  3. Ativação do ambiente virtual: `.venv\Scripts\activate` ou `source .venv/bin/activate`.
  4. Instalação das dependências: `pip install -r requirements.txt`.
  5. Migração dos modelos: `python manage.py migrate`.
  6. Execução: `python manage.py runserver`.
