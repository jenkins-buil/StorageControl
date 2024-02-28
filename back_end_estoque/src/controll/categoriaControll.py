from src.configs.db import engine
from src.model.produtoModel import Categorias
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

class CategoriaControll:

    def findAll():
            result = []
            data = session.query(Categorias).all()
            for categoria in data:
                result.append({
                    "id": categoria.id,
                    "categoria": categoria.categoria
                })
            return result