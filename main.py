from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import crud, schemas, models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db:Session = Depends(get_db)):
  return crud.create_empresa(db, empresa)

@app.post("/empresas/{empresa_id}/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def create_obrigacao(empresa_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
  return crud.create_obrigacao_acessoria(db, obrigacao, empresa_id)
  
  
@app.get("/empresas/", response_model=list[schemas.Empresa])
def read_empresas(db: Session = Depends(get_db)):
  return crud.get_empresas(db)