from Codigos.repositories.aluno_repository import busca_aluno_rm


def informacoes_aluno() -> None:
    """Lista dados de aluno, com um padrão de formatação.
    Parâmetro: aluno - dicionário com os dados do aluno, para exibição organizada.
    """
    exibir_informacoes()

def input_rm() -> int:
    """Input específico para o RM, que reduz código repetido, e serve para validar o tipo do input,
    que deve ser inteiro, e não pode ser negativo ou ter mais de 6 dígitos.

    Retorna: Em caso de sucesso, o RM digitado.
    """
    rm_valido = False
    while rm_valido is False:
        try:
            rm = int(input(f"\nDigite o RM do aluno: "))
            if rm>0 and len(str(rm)) < 7:
                rm_valido = True
                return rm
            else:
                exibicao_erro("RM inválido!!!")
        except ValueError:
            exibicao_erro("\nDigite um valor inteiro no RM!!!")

def input_aluno():
    """Une os inputs de alunos, e retorna os campos."""
    nome = validacao_nome()
    rm = validacao_rm()
    curso = validacao_curso()
    valor_mensalidade = validacao_mensalidade()
    aluno = {
        "nome_aluno": nome,
        "rm": rm,
        "curso": curso,
        "mensalidade": valor_mensalidade
    }
    return aluno

def validacao_nome() -> str:
    """Validação do nome do aluno, que deve ser preenchido, e não pode conter números ou caracteres especiais.

    Retorna: Em caso de sucesso, retorna o nome do aluno em letras maiúsculas.
    """
    nome_valido = False
    while nome_valido is False:
        nome = input("\nDigite o nome do aluno: ")
        condicao = nome == ""
        if not condicao:
            return nome.upper()
        else:
            exibicao_erro("Nome inválido!!! Digite apenas letras e não deixe o campo vazio!!!")

def validacao_rm() -> int:
    """Validação do RM do aluno, que deve ser um número inteiro,
     positivo, com no máximo 6 dígitos, e não pode ser repetido.

    Retorna: Em caso de sucesso, o RM digitado.
    """
    rm_digitado = input_rm()
    aluno_encontrado = busca_aluno_rm(rm_digitado)
    while aluno_encontrado is not None:
        exibicao_erro("RM existente!!!")
        rm_digitado = input_rm()
        aluno_encontrado = busca_aluno_rm(rm_digitado)
        if aluno_encontrado is None:
            return rm_digitado
    return rm_digitado

def validacao_curso() -> str:
    """Validação do curso que o aluno faz parte, que deve ser preenchido, e não pode ser vazio.

    Retorna: Em caso de sucesso, o nome do curso, em letras maiúsculas.
    """
    curso_valido = False
    while curso_valido is False:
        curso = input("\nDigite o novo curso do aluno: ")
        condicao = curso == ""
        if not condicao:
            return curso.upper()
        else:
            exibicao_erro("Curso inválido!!! Digite novamente!!!")

def validacao_mensalidade() -> float:
    """Validação do valor da mensalidade, que deve ser um número positivo, e não pode ser negativo.

    Retorna: Em caso de sucesso, o valor da mensalidade.
    """
    mensalidade = float(input(f"\nDigite o valor da mensalidade do aluno: "))
    condicao = mensalidade < 0
    while condicao:
        exibicao_erro("Valor de mensalidade inválido!!!")
        mensalidade = float(input(f"\nDigite o valor da mensalidade do aluno: "))
        condicao = mensalidade<0
        if not condicao:
                return mensalidade
    return mensalidade

