import config as config
import controllers.vendedorController as vendedorController
session = config.connCassandra()

def listProdutos():
    print("\n===========================")
    print("========= PRODUTOS =========")
    print("===========================\n")

    session.execute("USE mercadolivre")
    result_set = session.execute("SELECT * FROM produto")

    for row in result_set:
        print("===========================")
        print(f"Código: {row.codigo}, Nome: {row.nome}, Preço: R$ {row.preco}, Vendedor: {row.vendedor}")
        print("===========================")

def findProduto():
    print("\n===========================")
    print("========= BUSCAR POR =========")
    print("========= 1 - codigo =========")
    print("========= 2 - nome =========")
    print("===========================\n")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        alvo = input("Digite o codigo do produto: ")
        where = 'codigo'
    elif(select == "2"):
        alvo = input("Digite o nome do produto: ")
        where = 'nome'
    else:
        print("Opção invalida")
        findProduto()
    
    session.execute("USE mercadolivre")
    result_set = session.execute(f"SELECT * FROM produto WHERE {where} = '{alvo}' ALLOW FILTERING")

    print("\n===========================")
    print("========= PRODUTO =========")
    print("===========================\n")

    for row in result_set:
       print(f"Código: {row.codigo}, Nome: {row.nome}, Preço: R$ {row.preco}, Vendedor: {row.vendedor}")


def insertProduto():
    print("\n===========================")
    print("========= CADASTRAR PRODUTO =========")
    print("===========================\n")
    
    codigo = input('codigo: ')
    nome = input('nome: ')
    preco = input('preco: ')

    vendedorController.listVendedores()
    
    cnpjVendedor = input('cnpj do vendedor: ')

    session.execute("USE mercadolivre")

    vendedorObj = session.execute(f"SELECT * FROM vendedor WHERE cnpj = '{cnpjVendedor}'").one()
    vendedor = f"{vendedorObj.nome} - CNPJ: {vendedorObj.cnpj}"

    result = session.execute(f"SELECT * FROM produto WHERE codigo = '{codigo}'")
    if result.one() is not None:
        print("O codigo já esta vinculado a um produto!")
        insertProduto()
    else:
        result_set = session.execute(f"INSERT INTO produto (codigo, nome, preco, vendedor) VALUES ('{codigo}', '{nome}', '{preco}', '{vendedor}')")
        print("produto cadastrado com sucesso!")

def updateProduto():
    alvo = input("Código do produto que deseja editar: ")

    session.execute("USE mercadolivre")
    result = session.execute(f"SELECT * FROM produto WHERE codigo = '{alvo}'")
    if result.one() is not None:
        print()
    else:
        print("Código Invalido")
        updateProduto()

    print("\n===========================")
    print("========= EDITAR =========")
    print("========= 1 - nome =========")
    print("========= 2 - preco =========")
    print("========= 3 - ambos =========")
    print("===========================\n")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        novoNome = input("Digite o novo nome do produto: ")
        update = f"nome = '{novoNome}'"
    elif(select == "2"):
        novoPreco= input("Digite o novo preço do produto: ")
        update = f"preco = '{novoPreco}'"
    elif(select == "3"):
        novoNome = input("Digite o novo nome do produto: ")
        novoPreco= input("Digite o novo preço do produto: ")
        update = f"nome = '{novoNome}', preco = '{novoPreco}'"
    else:
        print("Opção invalida")
        updateProduto()

    result_set = session.execute(f"UPDATE produto SET {update} WHERE codigo = '{alvo}'")
    print("Produto editado com sucesso!")

def deleteProduto():
    print("\n===========================")
    print("========= DELETAR PRODUTO =========")
    print("===========================\n")

    alvo = input("codigo do produto que deseja deletar: ")

    print("========= TEM CERTEZA? =========")
    print("========= 1- SIM / 2- NÃO =========")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        session.execute("USE mercadolivre")
        result = session.execute(f"SELECT * FROM produto WHERE codigo = '{alvo}'")
        if result.one() is not None:
            result_set = session.execute(f"DELETE FROM produto WHERE codigo = '{alvo}'")
            print("Produto deletado com sucesso!")
        else:
            print('Código não esta vinculado a nenhum produto')
    elif(select == "2"):
        print("")
    else:
        print("Opção invalida")
        deleteProduto()

