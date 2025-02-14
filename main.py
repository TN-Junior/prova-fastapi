from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import crud, schemas, models

Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    """Cria uma nova empresa."""
    return crud.create_empresa(db, empresa)


@app.post("/empresas/{empresa_id}/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def create_obrigacao(empresa_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
  return crud.create_obrigacao_acessoria(db, obrigacao, empresa_id)
  
  
@app.get("/empresas/", response_model=list[schemas.Empresa])
def read_empresas(db: Session = Depends(get_db)):
  return crud.get_empresas(db)

@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def get_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.get_empresa_by_id(db, empresa_id)
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa


@app.put("/empresas/{empresa_id}", response_model=schemas.Empresa)
def update_empresa(empresa_id: int, empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = crud.update_empresa(db, empresa_id, empresa)
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa
  
@app.put("/empresas/{empresa_id}/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def update_obrigacao(empresa_id: int, obrigacao_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = crud.update_obrigacao(db, obrigacao_id, obrigacao)
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return db_obrigacao

@app.delete("/empresas/{empresa_id}/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def delete_obrigacao(empresa_id: int, obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = crud.get_obrigacao(db, empresa_id, obrigacao_id)
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    crud.delete_obrigacao(db, obrigacao_id)
    return db_obrigacao