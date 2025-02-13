from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
from schemas import EmpresaCreate, ObrigacaoAcessoriaCreate

def get_empresas(db: Session):
  return db.query(Empresa).all()

def create_empresa(db: Session, empresa: EmpresaCreate):
  db_empresa = Empresa(**empresa.dict())
  db.add(db_empresa)
  db.commit()
  db.refresh(db_empresa)
  return db_empresa

def create_obrigacao_acessoria(db: Session, obrigacao: ObrigacaoAcessoriaCreate, empresa_id: int):
  db_obrigacao = ObrigacaoAcessoria(**obrigacao.dict(), empresa_id=empresa_id)
  db.add(db_obrigacao)
  db.commit()
  db.refresh(db_obrigacao)
  return db_obrigacao
  