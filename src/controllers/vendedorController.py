import config as config

session = config.connCassandra()

def listVendedores():
    print("\n===========================")
    print("========= VENDEDORES =========")
    print("===========================\n")

    session.execute("USE mercadolivre")
    result_set = session.execute("SELECT * FROM vendedor")

    for row in result_set:
        print("===========================")
        print(f"Nome: {row.nome}, Email: {row.email}, CNPJ: {row.cnpj}")
        print("===========================")

def findVendedor():
    print("\n===========================")
    print("========= BUSCAR POR =========")
    print("========= 1 - nome =========")
    print("========= 2 - email =========")
    print("========= 3 - cnpj =========")
    print("===========================\n")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        alvo = input("Digite o nome do vendedor: ")
        where = 'nome'
    elif(select == "2"):
        alvo = input("Digite o email do vendedor: ")
        where = 'email'
    elif(select == "3"):
        alvo = input("Digite o cnpj do vendedor: ")
        where = 'cnpj'
    else:
        print("Opção invalida")
        findVendedor()
    
    session.execute("USE mercadolivre")
    result_set = session.execute(f"SELECT * FROM vendedor WHERE {where} = '{alvo}' ALLOW FILTERING")

    print("\n===========================")
    print("========= VENDEDOR =========")
    print("===========================\n")

    for row in result_set:
        print(f"Nome: {row.nome}, Email: {row.email}, CNPJ: {row.cnpj}")

def insertVendedor():
    print("\n===========================")
    print("========= CADASTRAR VENDEDOR =========")
    print("===========================\n")
    
    cnpj = input('cnpj: ')
    nome = input('nome: ')
    email = input('email: ')

    session.execute("USE mercadolivre")
    result = session.execute(f"SELECT * FROM vendedor WHERE cnpj = '{cnpj}'")
    if result.one() is not None:
        print("O cnpj já esta vinculado a um vendedor!")
        insertVendedor()
    else:
        result_set = session.execute(f"INSERT INTO vendedor (cnpj, nome, email) VALUES ('{cnpj}','{nome}','{email}')")
        print("Vendedor criado com sucesso!")

def updateVendedor():
    alvo = input("cnpj do vendedor que deseja editar: ")

    session.execute("USE mercadolivre")
    result = session.execute(f"SELECT * FROM vendedor WHERE cnpj = '{alvo}'")
    if result.one() is not None:
        print()
    else:
        print("Cnpj Invalido")
        updateVendedor()

    print("\n===========================")
    print("========= EDITAR =========")
    print("========= 1 - nome =========")
    print("========= 2 - email =========")
    print("========= 3 - ambos =========")
    print("===========================\n")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        novoNome = input("Digite o novo nome do vendedor: ")
        update = f"nome = '{novoNome}'"
    elif(select == "2"):
        novoEmail = input("Digite o novo email do vendedor: ")
        update = f"email = '{novoEmail}'"
    elif(select == "3"):
        novoNome = input("Digite o novo nome do vendedor: ")
        novoEmail = input("Digite o novo email do vendedor: ")
        update = f"nome = '{novoNome}', email = '{novoEmail}'"
    else:
        print("Opção invalida")
        updateVendedor()

    result_set = session.execute(f"UPDATE vendedor SET {update} WHERE cnpj = '{alvo}'")
    print("Vendedor editado com sucesso!")

def deleteVendedor():
    print("\n===========================")
    print("========= DELETAR VENDEDOR =========")
    print("===========================\n")

    alvo = input("cnpj do vendedor que deseja deletar: ")

    print("========= TEM CERTEZA? =========")
    print("========= 1- SIM / 2- NÃO =========")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        session.execute("USE mercadolivre")
        result = session.execute(f"SELECT * FROM vendedor WHERE cnpj = '{alvo}'")
        if result.one() is not None:
            result_set = session.execute(f"DELETE FROM vendedor WHERE cnpj = '{alvo}'")
            print("Vendedor deletado com sucesso!")
        else:
            print('CPF não esta vinculado a nenhum usuario')
    elif(select == "2"):
        print("")
    else:
        print("Opção invalida")
        deleteVendedor()
