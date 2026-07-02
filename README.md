# CRUD de Tarefas com Flask

## Objetivo

Desenvolver uma aplicação simples para cadastrar, listar, editar e excluir tarefas.

## Tecnologias

- Python
- Flask
- SQLite
- HTML e CSS

## Como rodar

### Opção 1: usando o projeto já baixado

1. Acesse a pasta do projeto:

```powershell
cd (COLOQUE O CAMINHO QUE SALVOU O ARQUVIO)
```

2. Ative o ambiente virtual:

### Opção 2: clonando o repositório

--- Clone o repositório:

```powershell
git clone <URL_DO_REPOSITORIO>
```

2. Entre na pasta do projeto:

```powershell
cd <NOME_DA_PASTA>
```

3. Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Entre na pasta da aplicação:

```powershell
cd Techflow
```

4. Instale as dependências:

```powershell
py -m pip install -r ..\requirements.txt
```

5. Execute a aplicação:

```powershell
py app.py
```

6. Abra no navegador:

```text
http://127.0.0.1:5000
```

## Estrutura

- app.py: rotas da aplicação
- models.py: operações com os dados
- database.py: configuração do banco SQLite
- templates/: páginas HTML
- requirements.txt: dependências do projeto

## Justificativa

Este trabalho foi feito para praticar os conceitos básicos de um CRUD e entender o fluxo de uma aplicação web simples, com backend, banco de dados e interface.
