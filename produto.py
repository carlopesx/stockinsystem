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
     def editar_produto(estoque):
      id_busca = input("Digite o ID do produto que deseja editar: ")

      for produto in estoque:
        if str(produto.id) == id_busca:

            print("Deixe em branco para manter o valor atual.")
            novo_nome  = input(f"Nome [{produto.nome}]: ")
            novo_tipo  = input(f"Tipo [{produto.tipo}]: ")
            nova_qtd   = input(f"Quantidade [{produto.quantidade}]: ")
            novo_preco = input(f"Preço [{produto.preco}]: ")

            produto.atualizar(
                nome       = novo_nome         or None,
                tipo       = novo_tipo         or None,
                quantidade = int(nova_qtd)     if nova_qtd   else None,
                preco      = float(novo_preco) if novo_preco else None,
            )

            print("Produto atualizado com sucesso!")
            return

      print(f"Produto com ID '{id_busca}' não encontrado.")