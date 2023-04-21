import config as config
import time
import random

session = config.connCassandra()

def listCompras():
    print("\n===========================")
    print("========= COMPRAS =========")
    print("===========================\n")

    session.execute("USE mercadolivre")
    result_set = session.execute("SELECT * FROM compra")

    for row in result_set:
        print("===========================")
        print(f"Id: {row.id}, Usuario: {row.usuario}, Produto: R$ {row.produto}")
        print("===========================")

def findCompra():
    alvo = input("Digite o id da compra: ")
    
    session.execute("USE mercadolivre")
    result_set = session.execute(f"SELECT * FROM compra WHERE id = '{alvo}' ALLOW FILTERING")

    print("\n===========================")
    print("========= COMPRA =========")
    print("===========================\n")

    for row in result_set:
       print(f"Id: {row.id}, Usuario: {row.usuario}, Produto: {row.produto}")


def insertCompra():
    print("\n===========================")
    print("========= NOVA COMPRA =========")
    print("===========================\n")
    
    timestamp = int(time.time() * 1000)
    rand = random.randint(0, 9999)
    id = timestamp + rand
    cpfUsuario = input('cpf do usuario: ')
    codigoProduto = input('código do produto: ')

    session.execute("USE mercadolivre")

    usuarioObj = session.execute(f"SELECT * FROM usuario WHERE cpf = '{cpfUsuario}'").one()
    usuario = f"{usuarioObj.nome} - Email: {usuarioObj.email}"

    produtoObj = session.execute(f"SELECT * FROM produto WHERE codigo = '{codigoProduto}'").one()
    produto = f"{produtoObj.nome} - Preço: R$ {produtoObj.preco} - Código: {produtoObj.codigo}"

    result_set = session.execute(f"INSERT INTO compra (id, usuario, produto) VALUES ('{id}', '{usuario}', '{produto}')")
    print("Compra cadastrada com sucesso!")
       

def deleteCompra():
    print("\n===========================")
    print("========= DELETAR COMPRA =========")
    print("===========================\n")

    alvo = input("id da compra que deseja deletar: ")

    print("========= TEM CERTEZA? =========")
    print("========= 1- SIM / 2- NÃO =========")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        session.execute("USE mercadolivre")
        result = session.execute(f"SELECT * FROM compra WHERE id = '{alvo}'")
        if result.one() is not None:
            result_set = session.execute(f"DELETE FROM compra WHERE id = '{alvo}'")
            print("Compra deletada com sucesso!")
        else:
            print('Id não esta vinculado a nenhuma compra')
    elif(select == "2"):
        print("")
    else:
        print("Opção invalida")
        deleteCompra()
