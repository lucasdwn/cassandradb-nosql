import os
import config as config
import controllers.usuarioController as usuarioController
import controllers.vendedorController as vendedorController
import controllers.produtoController as produtoController
import controllers.compraController as compraController

def clearConsole(): return os.system('cls'
                                     if os.name in ('nt', 'dos') else 'clear')


def createTables():
    session = config.connCassandra()
    session.execute("USE mercadolivre")

    session.execute("CREATE TABLE IF NOT EXISTS usuario (cpf text PRIMARY KEY, nome text, email text, fav text)")
    print('Tabela de usuario criada!')
    
    session.execute("CREATE TABLE IF NOT EXISTS vendedor (cnpj text PRIMARY KEY, nome text, email text)")
    print('Tabela de vendedor criada!')

    session.execute("CREATE TABLE IF NOT EXISTS produto (codigo text PRIMARY KEY, nome text, preco text, vendedor text)")
    print('Tabela de produto criada!')

    session.execute("CREATE TABLE IF NOT EXISTS compra (id text PRIMARY KEY, usuario text, produto text)")
    print('Tabela de compra criada!')
    

def mainStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - USUARIO ====")
        print("==== 2 - VENDEDOR ====")
        print("==== 3 - PRODUTO ====")
        print("==== 4 - COMPRA ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            usuarioStart()
        elif select == "2":
            vendedorStart()
        elif select == "3":
            produtoStart()
        elif select == "4":
            compraStart()
        elif select == "CLS":
            clearConsole()
            return mainStart()
        elif select == "X":
            on = False
        else:
            print("Opção Não entendida")

def usuarioStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - LISTAR USUARIOS ====")
        print("==== 2 - BUSCAR USUARIO ====")
        print("==== 3 - NOVO USUARIO ====")
        print("==== 4 - EDITAR USUARIO ====")
        print("==== 5 - DELETAR USUARIO ====")
        print("==== 6 - ADICIONAR FAVORITO ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            usuarioController.listUsuarios()
        elif select == "2":
            usuarioController.findUsuario()
        elif select == "3":
            usuarioController.insertUsuario()
        elif select == "4":
            usuarioController.updateUsuario()
        elif select == "5":
            usuarioController.deleteUsuario()
        elif select == "6":
            usuarioController.insertFavorito()
        elif select == "CLS":
            clearConsole()
            return usuarioStart()
        elif select == "X":
            on = False
            return mainStart()
        else:
            print("Opção Não entendida")
        
def vendedorStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - LISTAR VENDEDORES ====")
        print("==== 2 - BUSCAR VENDEDOR ====")
        print("==== 3 - NOVO VENDEDOR ====")
        print("==== 4 - EDITAR VENDEDOR ====")
        print("==== 5 - DELETAR VENDEDOR ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            vendedorController.listVendedores()
        elif select == "2":
            vendedorController.findVendedor()
        elif select == "3":
            vendedorController.insertVendedor()
        elif select == "4":
            vendedorController.updateVendedor()
        elif select == "5":
            vendedorController.deleteVendedor()
        elif select == "CLS":
            clearConsole()
            return vendedorStart()
        elif select == "X":
            on = False
            return mainStart()
        else:
            print("Opção Não entendida")

def produtoStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - LISTAR PRODUTOS ====")
        print("==== 2 - BUSCAR PRODUTO ====")
        print("==== 3 - NOVO PRODUTO ====")
        print("==== 4 - EDITAR PRODUTO ====")
        print("==== 5 - DELETAR PRODUTO ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            produtoController.listProdutos()
        elif select == "2":
            produtoController.findProduto()
        elif select == "3":
            produtoController.insertProduto()
        elif select == "4":
            produtoController.updateProduto()
        elif select == "5":
            produtoController.deleteProduto()
        elif select == "CLS":
            clearConsole()
            return produtoStart()
        elif select == "X":
            on = False
            return mainStart()
        else:
            print("Opção Não entendida")

def compraStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - LISTAR COMPRAS ====")
        print("==== 2 - BUSCAR COMPRA ====")
        print("==== 3 - NOVA COMPRA ====")
        print("==== 4 - DELETAR COMPRA ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            compraController.listCompras()
        elif select == "2":
            compraController.findCompra()
        elif select == "3":
            compraController.insertCompra()
        elif select == "4":
            compraController.deleteCompra()
        elif select == "CLS":
            clearConsole()
            return compraStart()
        elif select == "X":
            on = False
            return mainStart()
        else:
            print("Opção Não entendida")

# createTables()
mainStart()
