from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(14), unique=True, nullable=False, index=True) 
    endereco = Column(String(255))
    email = Column(String(100))
    telefone = Column(String(15))

    obrigacoes = relationship(
        "ObrigacaoAcessoria", 
        back_populates="empresa", 
        cascade="all, delete-orphan"
    )

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    periodicidade = Column(String(20), nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

    empresa = relationship("Empresa", back_populates="obrigacoes")
