# AVASUS
Repositório destinado ao armazenamento e versionamento do desafio/fase 2 da seleção para pesquisador no Projeto “PESQUISA APLICADA A IMPLEMENTAÇÃO DE PROCESSOS EDUCACIONAIS EM SISTEMAS INTEGRADOS DE INFORMAÇÃO E COMUNICAÇÃO EM SAÚDE”. Edital 018/2022 LAIS/HUOL/UFRN.

Candidato: Daniel Teodolino Barbosa Torres
Vaga: Pesquisador Back-End Python


-----

##Comandos e Configurações

Criando o Ambiente Virtual&nbsp
 - mkvirtualenv env_lais

Ativar o ambiente virtual
 - workon env_lais

Desativar o Ambiente Virtual
 - deactivate

 Criar tabelas conforme modelo
  - python manage.py makemigrations

  '''python manage.py makemigrations 
     Migrations for 'cadastros':
     cadastros\migrations\0001_initial.py
          - Create model Modulo
          - Create model Curso
          - Create model Atividade