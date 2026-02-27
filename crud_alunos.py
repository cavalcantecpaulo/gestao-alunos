lista_alunos = []
opc = -1

def menu_inicial():
    print("\n--- CRUD Alunos Python ---")
    print("--- Seja bem-vindo ao Mini-Crud em Python ---")
    print("   1 - Adicionar aluno")
    print("   2 - Atualizar aluno")
    print("   3 - Excluir aluno")
    print("   4 - Exibir aluno")
    print("   5 - Exibir todos os alunos")
    print("   0 - Encerrar Programa")

def informacoes_aluno(aluno):
    print("\n------------------------------")
    print(f"Nome: {aluno["nome_aluno"]}")
    print(f"RM do aluno: {aluno["rm"]}")
    print(f"Curso: {aluno["curso"]}")
    print(f"Valor da Mensalidade: R${aluno["mensalidade"]}")
    print("------------------------------")

def adicionar_aluno():
    nome = input("Digite o nome do novo aluno: ")
    rm = input(f"Digite o RM do aluno ({nome}): ")
    curso = input(f"Digite o curso do aluno ({nome}): ")
    valor_mensalidade = float(input(f"Digite a mensalidade do aluno ({nome}): "))

    aluno = {
        "nome_aluno": nome,
        "rm": rm,
        "curso": curso,
        "mensalidade": valor_mensalidade
    }
    lista_alunos.append(aluno)
    print("Aluno foi adicionado com sucesso!")

def atualizar_aluno():
    rmDigitado = requisicao_aluno("atualizar")
    for aluno in lista_alunos:
        if (aluno["rm"] == rmDigitado):
            print(f"Nome: {aluno["nome_aluno"]}")
            nome = input("Digite o novo nome do aluno: ")

            print(f"Curso: {aluno["curso"]}")
            curso = input("Digite o novo curso do aluno: ")

            print(f"Mensalidade: R${aluno["mensalidade"]}")
            valor_mensalidade = float(input("Digite a nova mensalidade do aluno: "))

            aluno["nome_aluno"] = nome
            aluno["curso"] = curso
            aluno["mensalidade"] = valor_mensalidade

            print("Informações de aluno atualizada com sucesso!")
        else:
            print("RM não encontrado!!!!")

def excluir_aluno():
    rmDigitado = requisicao_aluno("excluir")
    for aluno in lista_alunos:
        if (aluno["rm"] == rmDigitado):
            lista_alunos.pop(aluno)
            print("Aluno excluído com sucesso!")
        else:
            print("RM não encontrado!!!!")
def exibir_aluno():
    rmDigitado = requisicao_aluno("exibir")
    for aluno in lista_alunos:
        if (aluno["rm"] == rmDigitado):
            informacoes_aluno(aluno)
        else:
            print("RM não encontrado!!!!")

def exibir_alunos():
    if (len(lista_alunos) == 0):
        print("\nNenhum aluno encontrado!!!!")
    else:
        print("Exibindo alunos: ")
    for aluno in lista_alunos:
        informacoes_aluno(aluno)

def requisicao_aluno(acao):
    rm = input(f"Digite o RM do aluno que deseja {acao}: ")
    return rm

while (opc != 0):
    menu_inicial()
    opc = int(input("Selecione uma opção: "))
    match opc:
        case 1:
            adicionar_aluno()
        case 2:
            atualizar_aluno()
        case 3:
            excluir_aluno()
        case 4:
            exibir_aluno()
        case 5:
            exibir_alunos()
        case 0:
            print("\nEncerrando programa...")
            break
        case _:
            print("Opção inválida!!")