from src.configs.db import engine
from src.model.produtoModel import Produtos
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


class ProdutoControll:
    
    def findAll():
        result = []
        data = session.query(Produtos).all()
        for produto in data:
            result.append({
                "id": produto.id,
                "marca": produto.marca,
                "tamanho": produto.tamanho,
                "cor": produto.cor,
                "quantidade": produto.quantidade
            })
        return result
        
        
    def findById(id):
        result = []
        data = session.query(Produtos).filter(Produtos.id == id)
        if data == []:
            return None
        for produto in data:
            result.append({
                "id": produto.id,
                "marca": produto.marca,
                "tamanho": produto.tamanho,
                "cor": produto.cor,
                "quantidade": produto.quantidade
            })
        return result

    def findByName(name):
        result = []
        data = session.query(Produtos).filter(Produtos.name == name)
        if data == None:
            return None
        for produto in data:
            result.append({
                "id": produto.id,
                "name": produto.name,
                "price": produto.price,
                "color": produto.color
            })
        return result

    def create(produto):
        
        marca = produto['marca']
        tamanho = produto['tamanho']
        cor = produto['cor']    
        quantidade = None
        categoria_id = produto['categoria_id']
        data_insert = Produtos(marca=marca, tamanho=tamanho, cor=cor, quantidade=quantidade, categoria_id=categoria_id)
        session.add(data_insert)
        session.commit()

    def thereIsProduct(produto):
        result = []
        data = ProdutoControll.findByName(produto.name)
        if data != []:
            for produto in data:
                result.append({
                    "id": produto.id,
                    "name": produto.name,
                    "price": produto.price,
                    "color": produto.color
                })
            return result
        return data