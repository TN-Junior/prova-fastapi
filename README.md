# API de Gestão de Empresas e Obrigações Acessórias

Esta API foi desenvolvida utilizando **FastAPI**, **SQLAlchemy** e **PostgreSQL** para gerenciar empresas e suas obrigações acessórias. O banco de dados PostgreSQL está sendo executado em um container **Docker**.

---

## Requisitos
Certifique-se de ter os seguintes softwares instalados:
- Python 3
- Docker
- Git

---

## Execute o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/TN-Junior/prova-fastapi.git
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure o Banco de Dados
```bash
docker run --name database -e POSTGRES_USER="insira o usuario" -e POSTGRES_PASSWORD="insira senha" -e POSTGRES_DB="insiro o nome" -p 2222:5432 -d "sua imagem do docker"
```
### Execute a aplicação
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
