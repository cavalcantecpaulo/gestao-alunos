lista_alunos = []
opcao = -1

def menu_inicial():
    print("\n--- Menu Inicial do CRUD em Python ---")
    print("--- Seja bem-vindo ao Mini-Crud em Python ---")
    print("   1 - Adicionar aluno")
    print("   2 - Atualizar aluno")
    print("   3 - Excluir aluno")
    print("   4 - Exibir aluno")
    print("   5 - Exibir todos os alunos")
    print("   0 - Encerrar Programa")

def exibir_aluno():
    print("\n------------------------------------")
    print(f"Nome: {aluno["nome_aluno"]}")
    print(f"RM do aluno: {aluno["rm"]}")
    print(f"Curso: {aluno["curso"]}")
    print(f"Valor da Mensalidade: {aluno["mensalidade"]}")
    print("------------------------------------")

def adicionar_aluno():
    nome = input("Digite o nome do novo aluno: ")
    rm = input(f"Digite o RM do aluno ({nome}): ")
    curso = input(f"Digite o curso do aluno ({nome}): ")
    valor_mensalidade = float(input(f"Digite a mensalidade do aluno ({nome}): "))

    aluno = {
                "nome_aluno":  nome,
                "rm" : rm,
                "curso" :  curso,
                "mensalidade" : valor_mensalidade
            }
    lista_alunos.append(aluno)

## Inicio de refatoração de código
# def msg_opcao_escolhida(acao):
#     rm = input(f"Digite o RM do aluno que deseja {acao}: ")

while (opcao!=0) :
    menu_inicial()
    opcao = int(input("Selecione uma opção: "))
    match opcao:
        # Inserir aluno
        case 1:
            adicionar_aluno()

        # Alterar aluno
        case 2:
            # msg_opcao_escolhida("Alterar")
            rm_alteracao = input("Digite o RM do aluno que deseja alterar: ")

            indice = -1
            for i in range(len(lista_alunos)):
                if (lista_alunos[i]["rm"] == rm_alteracao):
                    print(f"Nome: {lista_alunos[indice]["nome_aluno"]}")
                    nome = input("Digite o novo nome do aluno: ")

                    print(f"Curso: {lista_alunos[indice]["curso"]}")
                    curso = input("Digite o novo curso do aluno: ")

                    print(f"Mensalidade: {lista_alunos[indice]["mensalidade"]}")
                    valor_mensalidade = input("Digite a nova mensalidade do aluno: ")

                    lista_alunos[indice["nome_aluno"]] = nome
                    lista_alunos[indice["curso"]] = curso
                    lista_alunos[indice["mensalidade"]] = valor_mensalidade
                else:
                    print("RM não encontrado!!!!")

        # Excluir aluno
        case 3:
            rm_excluir = input("Digite o RM do aluno que deseja excluir: ")
            indice = -1
            for i in range(len(lista_alunos)):
                if (lista_alunos[i]["rm"] == rm_excluir):
                    lista_alunos.pop(lista_alunos[indice])
                else:
                    print("RM não encontrado!!!!")

        # Exibir Aluno
        case 4:
            rm_exibir = input("Digite o RM do aluno que deseja exibir: ")

            for aluno in lista_alunos:
                if (aluno["rm"] == rm_exibir):
                    exibir_aluno()
                else:
                    print("RM não encontrado!!!!")

        # Exibir todos os alunos
        case 5:
            if (len(lista_alunos) == 0):
                print("\nNenhum aluno encontrado!!!!")
            else:
                print("Exibindo alunos: ")
            for aluno in lista_alunos:
                exibir_aluno()

        case 0:
            print("\nEncerrando programa...")
            break

        case _:
            print("Opção inválida!!")