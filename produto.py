class Produto:
     def __init__(self, tipo, nome, quantidade, preco):
        self.tipo = tipo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

     def mostrar(self):
        print(f"Tipo: {self.tipo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço: {self.preco}\n")