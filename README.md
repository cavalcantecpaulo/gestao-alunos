# Gestao de Alunos - Projeto em Python

Projeto educacional para gerenciamento de alunos em Python com interface de linha de comando (CLI), utilizando operacoes CRUD e persistencia em JSON, com arquitetura em camadas (view-service-repository-controller-model).

## Sobre o Projeto

Este projeto nasceu de uma atividade da disciplina Computational Thinking Using Python e evoluiu para consolidar fundamentos de programacao, engenharia de software e arquitetura em camadas bem definidas.

**Evolucao do projeto:**
- **v1.0-1.4.2:** CRUD funcional em arquivo unico (`crud_alunos.py`)
- **v1.4.3:** Refatoracao para arquitetura em camadas (em andamento)

Objetivos alcancados ate v1.4.3:
- Estruturar projeto com separacao de responsabilidades (camadas)
- Criar validadores puros em service (sem input/print, testaveis)
- Quebrar dependencias circulares entre modulos
- Implementar entidade Aluno com dataclass
- Isolar persistencia em repository
- Iniciar controller para orquestrar fluxo
- Estruturar projeto com separacao de responsabilidades (camadas)
- Criar validadores puros em service (sem input/print, testaveis)
- Quebrar dependencias circulares entre modulos
- Implementar entidade Aluno com dataclass
- Isolar persistencia em repository
- Iniciar controller para orquestrar fluxo

## Estado Atual (v1.4.3)

- **Versao atual do codigo:** `v1.4.3`
- **Status:** Refatoracao em camadas (ETAPA 1 - 70% completa)
- **Status:** Refatoracao em camadas (ETAPA 1 - 70% completa)
- **Arquivo principal:** `Codigos/main.py` (entrypoint unico)
- **Proxima meta:** Completar menu_controller e eliminar circular imports

## Arquitetura Implementada (v1.4.3)

### Estrutura de Camadas
Projeto reorganizado para separar responsabilidades:
Projeto reorganizado para separar responsabilidades:

```
Codigos/
├── main.py                    # Entrypoint (chama menu_view)
├── models/
│   └── aluno_model.py        # Entidade Aluno (dataclass)
├── views/
│   ├── menu_view.py          # Exibir menu e titulo
│   └── aluno_view.py         # Coleta de dados (input) + validacoes com retry
│   └── aluno_view.py         # Coleta de dados (input) + validacoes com retry
├── services/
│   └── aluno_service.py      # Validadores puros (sem I/O)
├── repositories/
│   └── aluno_repository.py   # Gerenciar lista_alunos + persistencia JSON
└── controllers/
    └── menu_controller.py    # Orquestrar fluxo (em construcao)
    └── menu_controller.py    # Orquestrar fluxo (em construcao)
```

### Responsabilidades por Camada (v1.4.3)

| Camada | Arquivo | O que faz | Nao faz |
|--------|---------|-----------|---------|
| **Model** | `aluno_model.py` | Define entidade Aluno com dataclass; metodo `exibir_informacoes()` | Persistencia, validacao |
| **View** | `aluno_view.py` | Coleta dados usuario (`input_aluno`, `validacao_*`); exibe erros | Logica de negocio, acesso a dados |
| **View** | `menu_view.py` | Exibe menu e titulo; funcao `exibicao_erro()` padronizada | Processamento de opcoes |
| **Service** | `aluno_service.py` | Validadores puros (`validar_nome`, `validar_rm`, etc); cria objeto Aluno | `input()` ou `print()` |
| **Repository** | `aluno_repository.py` | Gerencia `lista_alunos`; funcoes `busca_aluno_rm()`, `salvando_lista_json()` | Validacoes, interface usuario |
| **Controller** | `menu_controller.py` | Orquestra: view coleta → service valida → repository persiste | I/O direto |
|--------|---------|-----------|---------|
| **Model** | `aluno_model.py` | Define entidade Aluno com dataclass; metodo `exibir_informacoes()` | Persistencia, validacao |
| **View** | `aluno_view.py` | Coleta dados usuario (`input_aluno`, `validacao_*`); exibe erros | Logica de negocio, acesso a dados |
| **View** | `menu_view.py` | Exibe menu e titulo; funcao `exibicao_erro()` padronizada | Processamento de opcoes |
| **Service** | `aluno_service.py` | Validadores puros (`validar_nome`, `validar_rm`, etc); cria objeto Aluno | `input()` ou `print()` |
| **Repository** | `aluno_repository.py` | Gerencia `lista_alunos`; funcoes `busca_aluno_rm()`, `salvando_lista_json()` | Validacoes, interface usuario |
| **Controller** | `menu_controller.py` | Orquestra: view coleta → service valida → repository persiste | I/O direto |

### O que Funciona (v1.4.3)
✅ Entidade Aluno criada com dataclass
✅ Validadores puros em service (recebem dados, retornam bool)
✅ Repository com busca e salvamento JSON
✅ View com coleta de dados e validacoes com retry
✅ Estrutura de pastas organizada (models, views, services, repositories, controllers)
✅ Entidade Aluno criada com dataclass
✅ Validadores puros em service (recebem dados, retornam bool)
✅ Repository com busca e salvamento JSON
✅ View com coleta de dados e validacoes com retry
✅ Estrutura de pastas organizada (models, views, services, repositories, controllers)

### O que Ainda Falta (para v1.4.4)
⏳ Completar `menu_controller.py` com handlers (adicionar, atualizar, excluir, exibir)
⏳ Conectar `main.py` → `menu_view` → `menu_controller` → fluxo completo
⏳ Corrigir bugs em `validacao_mensalidade()` (loop infinito)
⏳ Adicionar funcoes CRUD em repository (adicionar, atualizar, remover)
⏳ Testes basicos em `test_aluno.py`
⏳ Completar `menu_controller.py` com handlers (adicionar, atualizar, excluir, exibir)
⏳ Conectar `main.py` → `menu_view` → `menu_controller` → fluxo completo
⏳ Corrigir bugs em `validacao_mensalidade()` (loop infinito)
⏳ Adicionar funcoes CRUD em repository (adicionar, atualizar, remover)
⏳ Testes basicos em `test_aluno.py`

## Aprendizados e Boas Praticas Aplicadas (v1.4.3)

### 1. Separacao de Responsabilidades (SRP)
**Aprendizado:** Cada camada tem um proposito claro
- **View:** Apenas perguntar ao usuario (`input`) e mostrar resultado (`print`)
- **Service:** Apenas validar dados ja coletados e aplicar regras de negocio
- **Repository:** Apenas gerenciar onde os dados vivem (memoria, JSON, banco)
- **Controller:** Apenas conectar as tres camadas acima
**Aprendizado:** Cada camada tem um proposito claro
- **View:** Apenas perguntar ao usuario (`input`) e mostrar resultado (`print`)
- **Service:** Apenas validar dados ja coletados e aplicar regras de negocio
- **Repository:** Apenas gerenciar onde os dados vivem (memoria, JSON, banco)
- **Controller:** Apenas conectar as tres camadas acima

**Beneficio:** Quando precisar mudar JSON para banco de dados, muda so repository. View e service nao sabem onde dados estao.

### 2. Validadores Puros (Testabilidade)
**Antes (v1.4.2):**
```python
# Misturava input com validacao
def validacao_nome():
    nome = input("Digite nome: ")  # ← input dentro!
    if nome == "":
        return None
    return nome.upper()
```
**Antes (v1.4.2):**
```python
# Misturava input com validacao
def validacao_nome():
    nome = input("Digite nome: ")  # ← input dentro!
    if nome == "":
        return None
    return nome.upper()
```

**Depois (v1.4.3):**
```python
# View coleta (aluno_view.py)
def validacao_nome() -> str:
    nome = input("\nDigite o nome: ")
    if nome.strip() == "":
        exibicao_erro("Nome vazio!")
        # retry...
    return nome.upper()
    nome = input("\nDigite o nome: ")
    if nome.strip() == "":
        exibicao_erro("Nome vazio!")
        # retry...
    return nome.upper()

# Service valida dados prontos (aluno_service.py)
def validar_nome(nome: str) -> bool:
    """Recebe nome JA coletado, valida sem input."""
    if isinstance(nome, str) and nome.strip() != "":
        return True
    return False
```
    """Recebe nome JA coletado, valida sem input."""
    if isinstance(nome, str) and nome.strip() != "":
        return True
    return False
```

**Beneficio:** Agora posso testar `validar_nome("João")` sem digitar nada no terminal!
assert validar_nome("Joao") == True
assert validar_nome("") == False
```

### 3. Quebrando Imports Circulares
**Problema identificado:** `aluno_view.py` importava `aluno_service.py` E vice-versa = erro!
**Implementado em v1.4.4:**
```
usuario escolhe opcao 1
  ↓
menu_view.menu_inicial_tela() + menu_controller.escolha_usuario()
  ↓
menu_controller.adicionar_aluno()
  ↓
aluno_view.input_aluno() [coleta nome, rm, curso, mensalidade]
  ↓
service valida cada campo
  ↓
aluno_service.criar_objeto_aluno() [cria Aluno dataclass]
  ↓
lista_alunos.append(aluno) [persiste em memoria]
  ↓
"✅ Aluno adicionado!"
```

**Solucao (v1.4.3):**
- View NAO importa service
- Service NAO importa view
- Controller importa ambos e faz a ponte

**Regra de ouro:** Importacoes sempre "para baixo" (main → view → controller → service/repository → model)

### 4. Dataclass para Entidades
**Antes:** Aluno era dict `{"nome_aluno": ..., "rm": ...}`
**Depois:** Aluno é classe com `@dataclass`

**Beneficio:**
- Type hints automaticos
- Menos codigo boilerplate
**Beneficios:**
- Type hints automaticos (nome: str, rm: int, ...)
- Menos boilerplate (`@dataclass` vs `__init__` manual)
- Metodos proprios (`exibir_informacoes()`)

### 5. Docstrings Descritivas
Toda funcao tem docstring explicando:
- O que faz
- Parametros esperados
- O que retorna
- Excecoes que pode lancar (quando relevante)
Toda funcao tem docstring explicando proposito, parametros, retorno.

---

**Exemplo real do projeto:**

### 1. `validacao_mensalidade()` Ainda Tem Loop Problemático ⚠️
**Arquivo:** `aluno_view.py` linha 90-98
**Estado:** Funciona mas logica confusa
```python
condicao = mensalidade < 0
while condicao:
    mensalidade = float(input(...))
    condicao = mensalidade < 0  # ← AGORA recalcula!
    if not condicao:
        return mensalidade
```

**Para v1.4.5:** Simplificar com `while True` + `if/else`:
```python
while True:
    valor = float(input("..."))
    if valor >= 0:
        return valor
    exibicao_erro("Valor negativo!")
```

### 2. `validar_rm()` Nao Valida Completamente ⚠️
**Arquivo:** `aluno_service.py` linha 60-67
**Estado:** Apenas verifica tipo int
```python
def validar_rm(rm: int) -> bool:
    if not isinstance(rm, int):
        return False
    return True  # ← aceita negativos, > 6 digitos, etc!
```

**Para v1.4.5:** Adicionar validacoes de negocio:
```python
def busca_aluno_rm(rm: int) -> dict | None:
    """Busca aluno especifico pelo RM.

    Parametro: RM do aluno para busca.
    Retorna: Dict do aluno se encontrado, None caso contrario.
    """
    if not isinstance(rm, int) or rm <= 0 or len(str(rm)) > 6:
        return False
    # TODO: Verificar duplicidade (buscar em repository)
    return True
```

### 6. Type Hints em Todas Funcoes
Facilita entender o que entra e o que sai:
**Arquivo:** `menu_view.py` linha 17
**Estado:** Funcao declarada mas sem implementacao
**Para v1.4.5:** Implementar loop:
```python
def validar_mensalidade(valor: float) -> bool:  # recebe float, retorna bool
def input_aluno() -> dict:  # nao recebe nada, retorna dict
    while opcao != 0:
        menu_inicial_tela()
        try:
            opcao = escolha_usuario()
        except ValueError:
            exibicao_erro("Digite numero valido!")
```
### 4. Repository Sem Funcoes Auxiliares ⚠️
**Arquivo:** `aluno_repository.py`
**Faltam:**
- `adicionar_aluno_repo(aluno)` - wrapper para append
- `atualizar_aluno_repo(rm, dados)` - atualizar na lista
- `remover_aluno_repo(rm)` - remover da lista
- `carregar_lista_json()` - ler ao iniciar

### 5. Controllers Restantes Nao Implementados ⚠️
**Arquivo:** `menu_controller.py` linhas 70-83
**Faltam handlers:**
- `atualizar_aluno()` - 15 linhas de código
- `excluir_aluno()` - 20 linhas de código
- `exibir_aluno()` - 10 linhas de código
- `exibir_alunos()` - 15 linhas de código

### 6. Sem Try/Except em `escolha_usuario()` ⚠️
**Arquivo:** `menu_controller.py` linha 31
**Problema:** Usuario digita "abc" em vez de numero → ValueError nao tratado
**Para v1.4.5:** Envolver em try/except

## Pontos de Atencao Identificados (v1.4.3)

### 1. Bug em `validacao_mensalidade()` (aluno_view.py)
**Problema:** Loop infinito quando valor negativo
```python
condicao = mensalidade < 0
while condicao:
    # ...
    if not condicao:  # ← condicao nunca recalculada!
        return mensalidade
```

**Correcao necessaria (v1.4.4):**
```python
while True:
    try:
        valor = float(input("..."))
        if valor >= 0:
            return valor
        else:
            exibicao_erro("Valor negativo!")
    except ValueError:
        exibicao_erro("Digite numero!")
```

### 2. Bug em `validar_*` (aluno_service.py)
**Problema:** `isinstance()` nunca retorna `None`
```python
def validar_nome(nome: str) -> bool:
    if isinstance(nome, str) is None:  # ← sempre False!
        return False
    return True
```

**Correcao necessaria (v1.4.4):**
```python
def validar_nome(nome: str) -> bool:
    if isinstance(nome, str) and nome.strip() != "":
        return True
    return False
```

### 3. `menu_controller.py` Incompleto
**Estado atual:** Funcao `adicionar_aluno()` criada mas handlers restantes comentados  
**Falta:** Implementar `atualizar_aluno()`, `excluir_aluno()`, `exibir_aluno()`, `exibir_alunos()`

### 4. Repository Incompleto
**Estado atual:** Tem `busca_aluno_rm()` e `salvando_lista_json()`  
**Falta:**
- `adicionar_aluno_repo(aluno_dict)`
- `atualizar_aluno_repo(rm, novos_dados)`
- `remover_aluno_repo(rm)`
- `carregar_lista_json()` (ler ao iniciar)

### 5. `aluno_view.py` Ainda Referencia `busca_aluno_rm`
**Problema:** `validacao_rm()` chama `busca_aluno_rm()` mas nao importa repository  
**Solucao (v1.4.4):** Adicionar `from Codigos.repositories.aluno_repository import busca_aluno_rm`

### 6. `menu_view.py` Tem Funcao `menu_inicial()` Vazia
**Estado atual:** Funcao declarada mas sem implementacao  
**Solucao (v1.4.4):** Implementar loop que chama `menu_inicial_tela()` e `escolha_usuario()`

## Melhorias Futuras (Roadmap v1.4.4+)

### Prioridade ALTA (v1.4.4 - Proxima Release)
- [ ] Corrigir bug em `validacao_mensalidade()` (loop infinito)
- [ ] Corrigir logica de `validar_*` em `aluno_service.py` (`isinstance` nunca None)
- [ ] Completar `menu_controller.py` com todos handlers (CRUD completo)
- [ ] Adicionar imports faltantes em `aluno_view.py` (`busca_aluno_rm`, `exibicao_erro`)
- [ ] Implementar `menu_inicial()` em `menu_view.py` (loop principal)
- [ ] Completar repository com funcoes CRUD (adicionar, atualizar, remover)
- [ ] Testar fluxo completo: adicionar → exibir → salvar JSON → funciona
- [ ] Corrigir bug em `validacao_mensalidade()` (loop infinito)
- [ ] Corrigir logica de `validar_*` em `aluno_service.py` (`isinstance` nunca None)
- [ ] Completar `menu_controller.py` com todos handlers (CRUD completo)
- [ ] Adicionar imports faltantes em `aluno_view.py` (`busca_aluno_rm`, `exibicao_erro`)
- [ ] Implementar `menu_inicial()` em `menu_view.py` (loop principal)
- [ ] Completar repository com funcoes CRUD (adicionar, atualizar, remover)
- [ ] Testar fluxo completo: adicionar → exibir → salvar JSON → funciona

### Prioridade MEDIA (v1.4.5)
- [ ] Carregamento automatico de JSON ao iniciar programa
- [ ] Testes basicos com `pytest` em `test_aluno.py`
- [ ] Tratamento robusto de `ValueError` em todos inputs numericos
- [ ] Confirmacao antes de excluir (com validacao de entrada)
- [ ] Mensagens de feedback mais claras (`✅ Sucesso`, `❌ Erro`)
- [ ] Carregamento automatico de JSON ao iniciar programa
- [ ] Testes basicos com `pytest` em `test_aluno.py`
- [ ] Tratamento robusto de `ValueError` em todos inputs numericos
- [ ] Confirmacao antes de excluir (com validacao de entrada)
- [ ] Mensagens de feedback mais claras (`✅ Sucesso`, `❌ Erro`)

### Prioridade BAIXA (v1.5.0+)
- [ ] Excecoes customizadas (`NomeInvalidoError`, `RMDuplicadoError`)
- [ ] Filtros de busca (por nome, por curso)
- [ ] Relatorio de mensalidades (total, media, etc)
- [ ] CLI com argparse (`python main.py --add`)
- [ ] Excecoes customizadas (`NomeInvalidoError`, `RMDuplicadoError`)
- [ ] Filtros de busca (por nome, por curso)
- [ ] Relatorio de mensalidades (total, media, etc)
- [ ] CLI com argparse (`python main.py --add`)
- [ ] Banco de dados SQLite em vez de JSON

## Como Executar (v1.4.3)

### Pre-requisitos
- Python 3.10 ou superior
- Nenhuma biblioteca externa (apenas stdlib)

### Execucao (Estado Atual - v1.4.3)
```powershell
cd gestao-alunos
python Codigos/main.py
```

**Nota:** Em v1.4.3, o menu ainda nao esta conectado ao controller. Programa inicia mas nao processa opcoes. Use para validar estrutura de pastas e imports.

### Execucao (Futuro - v1.4.4)
Apos completar controller, fluxo sera:
```
python Codigos/main.py
   ↓
Menu exibido
   ↓
Usuario digita opcao
   ↓
Controller processa (adicionar/atualizar/excluir/exibir)
   ↓
Resultado exibido
```

## Guia de Contribuicao

### Regras de Ouro (para manter arquitetura limpa)
1. **View nunca importa Service** (evita circular import)
2. **Service nunca importa View** (validadores sao puros, sem I/O)
3. **Controller importa View E Service** (faz a ponte entre eles)
4. **Repository e chamado por Service E Controller** (mas nao conhece View)

### Antes de Commitar
- [ ] `python Codigos/main.py` roda sem `ImportError`?
- [ ] Adicionou docstring em novas funcoes?
- [ ] Type hints em parametros e retorno?
- [ ] Atualizou README se mudanca significativa?

## Versionamento e Historico

### v1.4.3 (Atual - 2026-03-06)
**Status:** Refatoracao em camadas (70% completa)

**Mudancas:**
- ✅ Criada estrutura de pastas (models, views, services, repositories, controllers)
- ✅ Entidade Aluno com dataclass
- ✅ Validadores puros em `aluno_service.py` (sem I/O)
- ✅ Repository com `busca_aluno_rm()` e `salvando_lista_json()`
- ✅ View com coleta de dados e validacoes com retry
- ⏳ Controller com `adicionar_aluno()` (incompleto)
- ⏳ Menu principal ainda nao conectado

**Aprendizados principais:**
- Separacao de responsabilidades torna codigo mais testavel
- Validadores puros permitem testes sem mock de `input()`
- Circular imports quebram ao misturar I/O com logica de negocio
- Dataclass reduz boilerplate significativamente

### v1.4.2 (Anterior)
**Status:** CRUD funcional em arquivo unico (`crud_alunos.py`)

**Caracteristicas:**
- Todas funcoes em um arquivo
- Mistura de I/O e logica de negocio
- Funcional mas dificil de testar e manter

### Roadmap Futuro
- **v1.4.4:** CRUD completo funcional com controller
- **v1.4.5:** Testes basicos + carregamento JSON
- **v1.5.0:** Banco de dados SQLite
- **v2.0.0:** API REST (FastAPI/Flask)

## Referencias e Recursos

### Conceitos Aplicados
- **Single Responsibility Principle (SRP):** https://en.wikipedia.org/wiki/Single-responsibility_principle
- **Separation of Concerns:** https://en.wikipedia.org/wiki/Separation_of_concerns
- **Dataclasses Python:** https://docs.python.org/3/library/dataclasses.html

### Python Oficial
- Data Structures: https://docs.python.org/3/tutorial/datastructures.html
- Type Hints: https://docs.python.org/3/library/typing.html
- JSON module: https://docs.python.org/3/library/json.html
- Exception handling: https://docs.python.org/3/tutorial/errors.html

---

**Documentacao complementar:** Consulte `ROADMAP_REFACTORING.md` para entender arquitetura alvo e proximas etapas detalhadas.

**Ultima atualizacao:** 2026-03-06 (v1.4.3)
