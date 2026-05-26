#CLASSE PRODUTO
class Produto:
     
#MÉTODO ADICIONAR ----------
     def __init__(self, tipo, id, nome, quantidade, preco):
        self.tipo = tipo
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

#MÉTODO MOSTRAR ----------
     def mostrar(self):
        print(f"Tipo: {self.tipo}")
        print(f"Id: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço: {self.preco}\n")

#MÉTODO ATUALIZAR ----------
     def atualizar(self, tipo=None, id=None, nome=None, quantidade=None, preco=None):
        if tipo is not None:
            self.tipo = tipo
        if id is not None:
           self.id = id
        if nome is not None:
            self.nome = nome
        if quantidade is not None:
            self.quantidade = quantidade
        if preco is not None:
            self.preco = preco

#MÉTODO EDITAR ----------
     def editar_produto(estoque, id_busca, **novos_dados):
        for produto in estoque:
         if produto.id == id_busca:
            produto.atualizar(**novos_dados)
            print(f"Produto '{id_busca}' atualizado com sucesso!")
            return
        print(f"Produto '{id_busca}' não encontrado.")