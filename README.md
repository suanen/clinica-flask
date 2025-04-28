# Clínica Flask 

Este projeto é uma API simples criada com Flask para gerenciar pacientes, consultas e usuários de uma clínica.

## Sobre o Projeto

O sistema permite:
- Cadastrar novos pacientes
- Listar consultas agendadas
- Agendar novas consultas
- Fazer login de usuários

O banco de dados utilizado é o `SQLite` e foi criado automaticamente na primeira execução da aplicação (`clinica.db`).

---

## Tecnologias Utilizadas

- Python 3
- Flask
- SQLAlchemy
- SQLite

---

## Como rodar o projeto

1. Instale o Flask e o SQLAlchemy:
   ```bash
   pip install flask sqlalchemy

-------------
Execute a aplicação:

python app.py
-------------
Acesse a API pelo link:

http://127.0.0.1:5000/
-------------
### Endpoints disponíveis

| Método   | Rota         | Descrição                          |
|----------|--------------|------------------------------------|
| POST     | /pacientes   | Cadastrar novo paciente            |
| GET      | /consultas   | Listar todas as consultas          |
| POST     | /consultas   | Agendar uma nova consulta          |
| POST     | /login       | Fazer login de usuário             |
