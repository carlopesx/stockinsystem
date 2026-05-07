#Menu onde irá ocorrer a navegação do sistema

user = "carlos"
opc = 1

while opc != 0:
    print(f"--- BEM VINDO {user.upper()} ---\n")
    print("----- MENU DO ESTOQUE -----\n"
      "1 - CADASTRAR PRODUTOS\n"
      "2 - CONSULTAR PRODUTOS CADASTRADOS\n" 
      "3 - EDITAR PRODUTOS\n"
      "0 - SAIR")
    opc = int(input(""))

    if opc == 1:
        print("")
    elif opc == 2:
        print("")
    elif opc == 3:
        print("")
    elif opc == 0:
        print("")
    else:
        print("OPÇÃO INEXISTENTE! DIGITE NOVAMENTE")