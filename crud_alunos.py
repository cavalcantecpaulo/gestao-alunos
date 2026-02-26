lista_alunos = []

opcao = -1
while (opcao!=0) :
    print("--- Menu Inicial do CRUD em Python ---")
    print("--- Seja bem-vindo ---")
    print("   1 - Inserir Aluno")
    print("   2 - Atualizar Aluno")
    print("   3 - Excluir Aluno")
    print("   4 - Exibir Aluno")
    print("   0 - Encerrar Programa")
    opcao = int(input("Selecione uma opção: "))
    if(opcao>0 and opcao<=4) :
        match opcao:
        # Inserir aluno
            case 1:
                nome = input("Digite o nome do novo aluno: ")
                rm = input(f"Digite o RM do aluno ({nome}): ")
                curso = input(f"Digite o curso do aluno ({nome}): ")
                mensalidade = float(input(f"Digite a mensalidade do aluno ({nome}): "))

                dados_aluno = {
                    "nome" :  nome,
                    "rm" : rm,
                    "curso" :  curso,
                    "mensalidade" : mensalidade
                }

                lista_alunos.append(dados_aluno)
        # Alterar aluno
            case 2:
                rm_alteracao = input("Digite o RM do aluno que deseja alterar: ")
                indice = -1
                for i in range( len(lista_alunos) ):
                    if(lista_alunos[i]["rm"] == rm_alteracao):
                        print(f"Nome: {lista_alunos[indice]["nome"]}")
                        nome = input("Digite o novo nome do aluno: ")

                        print(f"Curso: {lista_alunos[indice]["curso"]}")
                        curso = input("Digite o novo curso do aluno: ")

                        print(f"Mensalidade: {lista_alunos[indice]["mensalidade"]}")
                        mensalidade = input("Digite a nova msenalidade do aluno: ")

                        lista_alunos[indice["nome"]] = nome
                        lista_alunos[indice["curso"]] = curso
                        lista_alunos[indice["mensalidade"]] = mensalidade
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
                indice = -1
                if(indice!=-1) :
                    for chave, valor in lista_alunos[indice]["rm_exibir"].items():
                        print(f"{chave}: {valor}")
                else:
                    print("RM não encontrado!!!!")
print("Opção inválida!!")