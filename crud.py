from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
from schemas import EmpresaCreate, ObrigacaoAcessoriaCreate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_empresas(db: Session, skip: int = 0, limit: int = 10):
    """Retorna uma lista de empresas com paginação."""
    return db.query(Empresa).offset(skip).limit(limit).all()


def get_empresa_by_id(db: Session, empresa_id: int):
    """Retorna uma empresa específica pelo ID."""
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()


def create_empresa(db: Session, empresa: EmpresaCreate):
    """Cria uma nova empresa no banco de dados."""
    db_empresa = Empresa(**empresa.dict())
    try:
        db.add(db_empresa)
        db.commit()
        db.refresh(db_empresa)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")
    return db_empresa


def update_empresa(db: Session, empresa_id: int, empresa_update: EmpresaCreate):
    """Atualiza os dados de uma empresa existente."""
    db_empresa = get_empresa_by_id(db, empresa_id)
    if not db_empresa:
        return None
    for key, value in empresa_update.dict().items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa


def delete_empresa(db: Session, empresa_id: int):
    """Remove uma empresa pelo ID."""
    db_empresa = get_empresa_by_id(db, empresa_id)
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
    return db_empresa


def create_obrigacao_acessoria(db: Session, obrigacao: ObrigacaoAcessoriaCreate, empresa_id: int):
    """Cria uma nova obrigação acessória para uma empresa específica."""
    db_obrigacao = ObrigacaoAcessoria(**obrigacao.dict(), empresa_id=empresa_id)
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao


def update_obrigacao(db: Session, obrigacao_id: int, obrigacao_update: ObrigacaoAcessoriaCreate):
    """Atualiza uma obrigação acessória existente."""
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        return None
    for key, value in obrigacao_update.dict().items():
        setattr(db_obrigacao, key, value)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao


def delete_obrigacao(db: Session, obrigacao_id: int):
    """Remove uma obrigação acessória pelo ID."""
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao:
        db.delete(db_obrigacao)
        db.commit()
    return db_obrigacao
