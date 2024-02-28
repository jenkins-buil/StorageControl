from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger, DATE
from sqlalchemy.orm import relationship

from src.configs.base import Base
from src.configs.db import engine

class Categorias(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(255), nullable=False, unique=True)
    produto = relationship("Produtos", backref='categorias', lazy=True)

    

    def __repr__(self):
        return f'Categoria (id={self.id}, name={self.categoria}'
Base.metadata.create_all(engine)

class Produtos(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(30))
    tamanho = Column(String(5), nullable=False)
    cor = Column(String(30), nullable=False)
    quantidade = Column(BigInteger, default=0)
    entrada = relationship("Entradas", backref='produtos', lazy=True)
    saida = relationship("Saidas", backref='produtos', lazy=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    def __repr__(self):
        return f'Produto (id={self.id}, marca={self.marca}, tamanho={self.tamanho}, cor={self.cor}), quantidade={self.quantidade}'
Base.metadata.create_all(engine)

class Entradas(Base):
    __tablename__='entradas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DATE)
    quantidade = Column(BigInteger)
    produto_id = Column(Integer, ForeignKey('produtos.id'))

    def __repr__(self):
        return f'Entrada (id={self.id}, data={self.data}, quantidade={self.quantidade}'
Base.metadata.create_all(engine)

class Saidas(Base):
    __tablename__='saidas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DATE)
    quantidade = Column(BigInteger)
    produto_id = Column(Integer, ForeignKey('produtos.id'))

    def __repr__(self):
        return f'Entrada (id={self.id}, data={self.data}, quantidade={self.quantidade}'
Base.metadata.create_all(engine)