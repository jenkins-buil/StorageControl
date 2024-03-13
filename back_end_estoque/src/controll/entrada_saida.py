from datetime import datetime
from src.model.produtoModel import Entradas, Quantidades, Produtos 
from src.controll.atualizaEstoque import AtualizaEstoque
from src.configs.db import session


class Entrada_Saida_Controll:

    def entradaProduto(produto):
        data_time = datetime.now()
        produto_id = produto['produto_id']
        tamanho = produto['tamanho']
        cor = produto['cor']
        qtde_entrada = produto['qtde_entrada']
        data_insert = Entradas(produto_id=produto_id, tamanho=tamanho, qtde_entrada=qtde_entrada, cor=cor,
                            dataEntrada=data_time, horaEntrada=data_time)
        session.add(data_insert)
        session.commit()
        temCadastro = AtualizaEstoque.temCadastroTabelaQuantidade(data_insert)
        if temCadastro:
            id = temCadastro["id"]
            vlr_atual = temCadastro['quantidade'] + (int(qtde_entrada))
            AtualizaEstoque.atualizandoQuantidade(id, vlr_atual)
            return
        AtualizaEstoque.cadastrarNovo(data_insert)  
        return

    def historicoEntrada(id):
        lista = []
        data = session.query(Entradas).filter(Entradas.produto_id == id).all()
        print(data)
        for entrada in data:
            lista.append({
                "id": entrada.id,
                "data_entrada": entrada.dataEntrada.strftime("%d/%m/%Y"),
                "hora_entrada": entrada.horaEntrada.strftime("%H:%M:%S"),
                "tamanho": entrada.tamanho,
                "cor": entrada.cor,
                "quantidade": entrada.qtde_entrada,
                "produto_id": entrada.produto_id

            })
        session.expire_all()
        return lista
        


