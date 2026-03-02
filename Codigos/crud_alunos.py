import json
lista_alunos = []
opc = -1

def menu_inicial(opc):
    while opc != 0:
        exibir_titulo_inicial()
        print("   1 - Adicionar aluno")
        print("   2 - Atualizar aluno")
        print("   3 - Excluir aluno")
        print("   4 - Exibir aluno")
        print("   5 - Exibir todos os alunos")
        print("   6 - Salvar lista em arquivo Json")
        print("   0 - Encerrar Programa")

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
            case 6:
                salvando_lista_json()
            case 0:
                print("\nEncerrando programa...")
                break
            case _:
                exibicao_erro("Opção inválida!!!")

def informacoes_aluno(aluno):
    print("\n-----------------------------------")
    print(f"    Nome: {aluno["nome_aluno"]} | RM{aluno["rm"]}")
    print(f"    Curso: {aluno["curso"]}")
    print(f"    Valor da Mensalidade: R${aluno["mensalidade"]}")
    print("-----------------------------------")

def adicionar_aluno():
    nome = input("\nDigite o nome do novo aluno: ")
    rm = verificacao_rm()
    curso = input(f"Digite o curso do aluno ({nome}): ")
    valor_mensalidade = float(input(f"Digite a mensalidade do aluno ({nome}): "))

    aluno = {
        "nome_aluno": nome,
        "rm": rm,
        "curso": curso,
        "mensalidade": valor_mensalidade
    }
    lista_alunos.append(aluno)
    print("\nAluno adicionado com sucesso!")

def atualizar_aluno():
    rmDigitado = requisicao_aluno("atualizar")
    for aluno in lista_alunos:
        if aluno["rm"] == rmDigitado:
            print(f"\nNome: {aluno["nome_aluno"]}")
            nome = input("Digite o novo nome do aluno: ")

            print(f"Curso: {aluno["curso"]}")
            curso = input("Digite o novo curso do aluno: ")

            print(f"Mensalidade: R${aluno["mensalidade"]}")
            valor_mensalidade = float(input("Digite a nova mensalidade do aluno: "))

            aluno["nome_aluno"] = nome
            aluno["curso"] = curso
            aluno["mensalidade"] = valor_mensalidade

            print("\nInformações de aluno atualizada com sucesso!")
        else:
            exibicao_erro("\nRM não encontrado!!!!")

def excluir_aluno():
    rmDigitado = requisicao_aluno("excluir")
    for aluno in lista_alunos:
        if aluno["rm"] == rmDigitado:
            lista_alunos.remove(aluno)
            print("\nAluno excluído com sucesso!")
        else:
            exibicao_erro("\nRM não encontrado!!!!")

def exibir_aluno():
    rmDigitado = requisicao_aluno("exibir")
    for aluno in lista_alunos:
        if aluno["rm"] == rmDigitado:
            informacoes_aluno(aluno)
    else:
        exibicao_erro("\nRM não encontrado!!!!")

def exibir_alunos():
    if len(lista_alunos) == 0:
        print("\nNenhum aluno encontrado!!!!")
    else:
        print("\nExibindo alunos: ")
    for aluno in lista_alunos:
        informacoes_aluno(aluno)

def requisicao_aluno(acao):
    rm = input(f"Digite o RM do aluno que deseja {acao}: ")
    return rm

def salvando_lista_json():
    with open("dados_alunos.json", "w") as dados_alunos:
        json.dump(lista_alunos, dados_alunos)
    print("\nSalvando lista de alunos em arquivo json... ")

def exibir_titulo_inicial():
    print("\n--- CRUD Alunos Python ---")
    print("--- Seja bem-vindo ao Mini-Crud em Python ---")

def exibicao_erro(erro):
    print(f"\nErro: {erro}")

def verificacao_rm():
    rm_digitado = input_rm()

    for aluno in lista_alunos:
        condicao = aluno["rm"] == rm_digitado
        if condicao:
            while condicao:
                exibicao_erro("RM existente!!!")
                rm_digitado = input_rm()
                if aluno["rm"] != rm_digitado:
                    return rm_digitado

    return rm_digitado

def input_rm():
    rm = input(f"Digite o RM do aluno: ")
    return rm

# def leitura_inicial_json():
#     arquivo_json = open("../dados_alunos.json", "r")
#     dados_alunos = json.load(arquivo_json)
#     return dados_alunos
#
# lista_alunos.append(leitura_inicial_json())
# for aluno in lista_alunos:
#     informacoes_aluno(aluno)

menu_inicial(opc)