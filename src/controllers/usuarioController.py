import config as config

session = config.connCassandra()

def listUsuarios():

    print("\n===========================")
    print("========= USUARIOS =========")
    print("===========================\n")
    
    session.execute("USE mercadolivre")
    result_set = session.execute("SELECT * FROM usuario")

    for row in result_set:
        print("===========================")
        print(f"Nome: {row.nome}, Email: {row.email}, CPF: {row.cpf}, Favoritos: {row.fav}")
        print("===========================")

def findUsuario():
    print("\n===========================")
    print("========= BUSCAR POR =========")
    print("========= 1 - nome =========")
    print("========= 2 - email =========")
    print("========= 3 - cpf =========")
    print("===========================\n")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        alvo = input("Digite o nome do usuario: ")
        where = 'nome'
    elif(select == "2"):
        alvo = input("Digite o email do usuario: ")
        where = 'email'
    elif(select == "3"):
        alvo = input("Digite o cpf do usuario: ")
        where = 'cpf'
    else:
        print("Opção invalida")
        findUsuario()

    session.execute("USE mercadolivre")
    result_set = session.execute(f"SELECT * FROM usuario WHERE {where} = '{alvo}' ALLOW FILTERING")

    print("\n===========================")
    print("========= USUARIO =========")
    print("===========================\n")
  
    for row in result_set:
        print(f"Nome: {row.nome}, Email: {row.email}, CPF: {row.cpf}, Favoritos: {row.fav}")

def insertUsuario():

    print("\n===========================")
    print("========= CADASTRAR USUARIO =========")
    print("===========================\n")
    
    cpf = input('cpf: ')
    nome = input('nome: ')
    email = input('email: ')

    session.execute("USE mercadolivre")
    result = session.execute(f"SELECT * FROM usuario WHERE cpf = '{cpf}'")
    if result.one() is not None:
        print("O CPF já esta vinculado a um usuario!")
        insertUsuario()
    else:
        result_set = session.execute(f"INSERT INTO usuario (cpf, nome, email) VALUES ('{cpf}','{nome}','{email}')")
        print("Usuario criado com sucesso!")
        


def updateUsuario():
    
    alvo = input("cpf do usuario que deseja editar: ")

    print("\n===========================")
    print("========= EDITAR =========")
    print("========= 1 - nome =========")
    print("========= 2 - email =========")
    print("========= 3 - ambos =========")
    print("===========================\n")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        novoNome = input("Digite o novo nome do usuario: ")
        update = f"nome = '{novoNome}'"
    elif(select == "2"):
        novoEmail = input("Digite o novo email do usuario: ")
        update = f"email = '{novoEmail}'"
    elif(select == "3"):
        novoNome = input("Digite o novo nome do usuario: ")
        novoEmail = input("Digite o novo email do usuario: ")
        update = f"nome = '{novoNome}', email = '{novoEmail}'"
    else:
        print("Opção invalida")
        updateUsuario()
    
    session.execute("USE mercadolivre")
    result_set = session.execute(f"UPDATE usuario SET {update} WHERE cpf = '{alvo}'")

    print("Usuario editado com sucesso!")

def deleteUsuario():

    print("\n===========================")
    print("========= DELETAR USUARIO =========")
    print("===========================\n")

    alvo = input("cpf do usuario que deseja deletar: ")

    print("========= TEM CERTEZA? =========")
    print("========= 1- SIM / 2- NÃO =========")
    select = input("Selecione uma opção: ")
    if(select == "1"):
        session.execute("USE mercadolivre")
        result = session.execute(f"SELECT * FROM usuario WHERE cpf = '{alvo}'")
        if result.one() is not None:
            result_set = session.execute(f"DELETE FROM usuario WHERE cpf = '{alvo}'")
            print("Usuario deletado com sucesso!")
        else:
            print('CPF não esta vinculado a nenhum usuario')
    elif(select == "2"):
        print("")
    else:
        print("Opção invalida")
        deleteUsuario()

def insertFavorito():
    print('por enquanto não inserimos favoritos XD')