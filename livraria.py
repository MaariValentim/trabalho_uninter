print ('Bem Vindo(a) a Livraria da Mariana Valentim!! ')
print('-' *40)
print('-' * 13 + 'MENU PRINCIPAL' + '-' * 13)

lista_livro = []
id_global = 0


# EXIGÊNCIA C: Função para cadastrar livro
def cadastrar_livro(id_livro):
    """
    Cadastra um novo livro na lista de livros.
    :param id_livro: ID único do livro a ser cadastrado
    """
    print("\n--- Cadastro de Livro ---")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")

    # EXIGÊNCIA G: Criando dicionário para o livro
    livro = {
        'id': id_livro,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    # Adicionando o livro à lista
    lista_livro.append(livro)
    print(f"Livro '{nome}' cadastrado com sucesso! (ID: {id_livro})")


# EXIGÊNCIA D: Função para consultar livros
def consultar_livro():
    """
    Exibe opções de consulta e mostra os livros conforme a opção selecionada.
    """
    while True:
        print("\n--- Consulta de Livros ---")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':  # Consultar Todos
            print("\n--- Todos os Livros Cadastrados ---")
            if not lista_livro:
                print("Nenhum livro cadastrado.")
            else:
                for livro in lista_livro:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("---------------------")

        elif opcao == '2':  # Consultar por ID
            id_busca = input("\nDigite o ID do livro: ")
            encontrado = False
            for livro in lista_livro:
                if str(livro['id']) == id_busca:
                    print("\n--- Livro Encontrado ---")
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado com o ID informado.")

        elif opcao == '3':  # Consultar por Autor
            autor_busca = input("\nDigite o nome do autor: ")
            livros_autor = [livro for livro in lista_livro if livro['autor'].lower() == autor_busca.lower()]

            if not livros_autor:
                print(f"Nenhum livro encontrado para o autor '{autor_busca}'.")
            else:
                print(f"\n--- Livros do Autor {autor_busca} ---")
                for livro in livros_autor:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Editora: {livro['editora']}")
                    print("---------------------")

        elif opcao == '4':  # Retornar ao menu
            break

        else:  # Opção inválida
            print("Opção inválida. Tente novamente.")


# EXIGÊNCIA E: Função para remover livro
def remover_livro():
    """
    Remove um livro da lista com base no ID fornecido.
    """
    while True:
        print("\n--- Remover Livro ---")
        if not lista_livro:
            print("Nenhum livro cadastrado para remover.")
            return

        id_remover = input("Digite o ID do livro a ser removido (ou 'sair' para cancelar): ")

        if id_remover.lower() == 'sair':
            return

        encontrado = False
        for i, livro in enumerate(lista_livro):
            if str(livro['id']) == id_remover:
                livro_removido = lista_livro.pop(i)
                print(f"Livro '{livro_removido['nome']}' removido com sucesso!")
                encontrado = True
                return

        if not encontrado:
            print("ID inválido. Tente novamente.")




def main():
    global id_global

    livros_iniciais = []

    for livro in livros_iniciais:
        lista_livro.append(livro)
        id_global = livro['id']  # Atualiza


    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':  # Cadastrar Livro
            id_global += 1
            cadastrar_livro(id_global)

        elif opcao == '2':  # Consultar Livro
            consultar_livro()

        elif opcao == '3':
            remover_livro()

        elif opcao == '4':
            print("\nEncerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()