from flask import Flask, jsonify, request
from flask_cors import CORS
from src.controll.produtoControll import ProdutoControll 
from src.controll.categoriaControll import CategoriaControll



app = Flask(__name__)
cors = CORS(app)

@app.route('/produtos', methods=['POST'])
def inserirProdutos():
    produto = request.json
    ProdutoControll.create(produto)
    return "Produto inserido com sucesso"

@app.route('/produtos')
def buscarProdutos():
    produtos = ProdutoControll.findAll()
    return jsonify(produtos)

@app.route('/produtos/<int:id>')
def buscarProdutoPeloId(id):
    produto = ProdutoControll.findById(id)
    if produto == None:
        return "Produto não cadastrado"
    return jsonify(produto)

@app.route('/teste/<name>')
def buscarProdutoPeloNome(name):
    produto = ProdutoControll.findByName(name)
    if produto == []:
       return "Produto não cadastrado"
    return jsonify(produto) 

@app.route('/categorias')
def getCategoria():
    categoria = CategoriaControll.findAll()
    return jsonify(categoria)

if __name__ == '__main__':
    app.run(debug=True)