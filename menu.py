#Menu onde irá ocorrer a navegação do sistema

user = "carlos"
opc = 1
estoque = [] # ------

class Produto:
     def __init__(self, tipo, nome, quantidade, preco):
        self.tipo = tipo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
#------------------------------------------------------------------

while opc != 0:
    print(f"--- BEM VINDO {user.upper()} ---\n")
    print("----- MENU DO ESTOQUE -----\n",
      "1 - CADASTRAR PRODUTOS\n",
      "2 - CONSULTAR PRODUTOS CADASTRADOS\n",
      "3 - EDITAR PRODUTOS\n",
      "0 - SAIR")
    opc = (input(""))
#------------------------------------------------------------------
    if opc == "1":
        opc2 = 1
        while opc2 == 1:
            print("\n---- CADASTRAR PRODUTO ----")
            print("--- INFORME ---")
            tipo = input("Tipo/categoria: ")
            nome = input("nome: ") # ------

            quantidade = "0"
            while quantidade != quantidade.isdigit:
                quantidade = input("Quantidade: ")
                if not quantidade.isdigit():
                    print("Dado invalido!")
                else:
                    break

            preco = "0"
            while preco != preco.isdigit:
                preco = input("Preco: ")
                if not preco.isdigit():
                    print("Dado invalido!")
                else:
                    break
            print("")
            produto = Produto(tipo, nome, quantidade, preco)
            estoque.append(produto)
            print(f"PRODUTO CADASTRADO!")
            print(f"Tipo: {produto.nome},", f"Nome: {produto.tipo},", f"Quantidade: {produto.quantidade},", f"Preco: {produto.preco}")
        
            opc3 = 3
            while opc3 != 1 and opc3 != 0:
                print("\n1 - Cadastrar outro produto")
                print("0 - Voltar para o menu")
                opc3 = int(input(""))
            
                if opc3 == 0:
                    opc2 = 2
                    print("-------------------------------------------------------------")
                elif opc3 == 1:
                    opc2 = opc3
                    continue
                else:
                    print("Opção invalida")
            

    elif opc == "3":
        print("")
    elif opc == "0":
        print(f"ATÉ A PRÓXIMA, {user} ;)")
        break
    elif not opc.isdigit():
        print("OPÇÃO INEXISTENTE! DIGITE NOVAMENTE")