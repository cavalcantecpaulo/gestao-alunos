# 🚀 Roadmap de Refatoração - CRUD Gestão de Alunos v1.4.4 → v1.4.5

## 🔍 DIAGNÓSTICO ATUAL (2026-03-06 - Estado Real v1.4.4)

**Versao:** v1.4.4  
**Status:** CRUD funcional 65-70% completo  
**Bloqueio principal:** Handlers restantes + menu sem loop

### ✅ O que REALMENTE FUNCIONA (parabens!):

✅ Arquitetura em camadas completa (models, views, services, repositories, controllers)  
✅ Entidade `Aluno` com dataclass e `exibir_informacoes()`  
✅ Repository com `lista_alunos`, `busca_aluno_rm()`, `salvando_lista_json()`  
✅ View com coleta de dados e validacoes com retry (input_aluno, validacao_*)  
✅ Service com validadores puros funcionando (validar_nome, validar_rm, validar_curso, validar_mensalidade)  
✅ Controller com `adicionar_aluno()` completo e funcional!  
✅ Fluxo CRUD para ADICIONAR: view coleta → service valida → repository persiste  
✅ Match/case no controller roteando opcoes  
✅ Menu exibindo opcoes (menu_inicial_tela)  
✅ Sem imports circulares!  

**Teste:** `python Codigos/main.py` → selecione 1 → adicione aluno → funciona!

### ❌ O que AINDA FALTA (30-35% do trabalho):

#### 1. **Handlers Não Implementados (60% do trabalho pendente)**
- `atualizar_aluno()` - skeleton vazio (linhas 71-77)
- `excluir_aluno()` - skeleton vazio (linhas 79-83)
- Faltam: `exibir_aluno()`, `exibir_alunos()`, conectar `salvando_lista_json()`

#### 2. **Menu Sem Loop (10% do trabalho)**
- `menu_inicial()` em menu_view.py (linha 17) - skeleton vazio
- Precisa: while opcao != 0 + try/except para ValueError em escolha_usuario()

#### 3. **Validacoes Incompletas (15% do trabalho)**
- `validar_rm()` - so verifica tipo int, nao valida negativos/max 6 digitos/duplicidade
- `validacao_mensalidade()` - loop confuso (funciona mas pode simplificar)

#### 4. **Repository Sem Helpers (10% do trabalho)**
- Faltam: `adicionar_aluno_repo()`, `atualizar_aluno_repo()`, `remover_aluno_repo()`
- Falta: `carregar_lista_json()` - ler ao iniciar

#### 5. **Sem Try/Except em `escolha_usuario()` (5% do trabalho)**
- Usuario digita "abc" em vez de numero → ValueError nao tratado

### 📊 Progresso Atual:
```
[████████████████████████░░░░] 67-70% completo

IMPLEMENTADO:
- Estrutura de pastas ✅
- Dataclass Aluno ✅
- View com inputs ✅
- Service com validadores ✅
- Repository basico ✅
- Controller adicionar_aluno ✅
- Menu display ✅

FALTANDO:
- 4 handlers do controller ❌
- Menu loop ❌
- Validacoes completas ❌
- Repository helpers ❌
- Try/except inputs numericos ❌
```

**Tempo para completar v1.4.5:** 2-3 horas de trabalho focado


---

## 📐 ARQUITETURA ALVO (após v1.3.7)

```
FLUXO CORRETO (sem ciclos):

main.py (entrypoint único)
  ↓
menu_view.py (I/O puro: exibe menu, captura opção)
  ↓
menu_controller.py (orquestrador: roteia opção → handlers)
  ↓
handler_aluno() [criar/atualizar/excluir/buscar] 
  ├→ aluno_view.py (coleta dados: input() + .upper() + conversão)
  ├→ aluno_service.py (valida lógica de negócio: sem input/print)
  └→ aluno_repository.py (persiste: salva/carrega/busca em JSON)
  ↓
aluno_model.py (Aluno: entidade, método exibir_informacoes())
```

### Responsabilidades Finais (regra de ouro: cada arquivo sabe apenas o que precisa)

| Arquivo | O que FAZ | O que NÃO faz | Quem importa dele |
|---------|-----------|--------------|------------------|
| `main.py` | Entrypoint único | Lógica; I/O; regra | ninguém |
| `menu_view.py` | Exibir menu; capturar opção | Processamento | main.py |
| `menu_controller.py` | Rotear opção para handlers | I/O direto; persistência | menu_view.py |
| `aluno_view.py` | Coletar input; exibir dados | Validar regra; persistir | menu_controller.py |
| `aluno_service.py` | Validar dados (bool); criar Aluno | input/print; buscar; salvar | menu_controller.py |
| `aluno_repository.py` | Acesso a dados (lista + JSON) | Validação; interface UI | aluno_service.py + menu_controller.py |
| `aluno_model.py` | Entidade Aluno + método exibir | Persistência; validação | aluno_service.py |

### Regra de Ouro para Cortar o Circular:
- **view** nunca importa **service** (view coleta input, service valida dados prontos)
- **service** nunca importa **view** (service recebe dados, view mostra resultado)
- **controller** é o intermediário que liga view → service → repository

---

## ✅ ETAPAS DE REFATORAÇÃO (Baixo Risco)

## ✅ ETAPA 1: Completar CRUD Funcional para v1.4.5 (PROXIMO PASSO)

**Objetivo:** CRUD 100% funcional (todas as 6 opcoes do menu)

### 🎯 5 Tarefas Principais (Prioridade)

---

#### TAREFA 1: Implementar Menu Loop (15 minutos)
**Arquivo:** `Codigos/views/menu_view.py` linha 17

**O que fazer:**
A funcao `menu_inicial(opcao)` precisa ter um loop que:
1. Chama `menu_inicial_tela()` (ja existe)
2. Captura opcao com `escolha_usuario()` (precisa try/except)
3. Repete ate usuario escolher 0

**Por que:** Sem loop, programa executa uma vez e encerra. Menu precisa ficar rodando.

**Código necessário (7 linhas):**
```python
def menu_inicial(opcao):
    while opcao != 0:
        menu_inicial_tela()
        try:
            opcao = escolha_usuario()
        except ValueError:
            exibicao_erro("Digite numero valido!")
```

**Teste:** `python Codigos/main.py` → escolha 1 → depois escolha 0 → encerra

---

#### TAREFA 2: Implementar 4 Handlers do Controller (60-80 minutos)
**Arquivo:** `Codigos/controllers/menu_controller.py` linhas 71-83

**O que fazer:**

##### 2.1: `atualizar_aluno()` (20 minutos)
```
1. Chama input_rm() [view]
2. Busca aluno no repository
3. Se nao existe → erro e retorna
4. Se existe → exibe aluno + coleta novos dados
5. Valida novos dados
6. Atualiza na lista
7. Exibe sucesso
```

##### 2.2: `excluir_aluno()` (20 minutos)
```
1. Chama input_rm() [view]
2. Busca aluno no repository
3. Se nao existe → erro e retorna
4. Se existe → exibe aluno + pede confirmacao (S/N)
5. Se confirmado → remove da lista
6. Exibe sucesso
```

##### 2.3: `exibir_aluno()` (15 minutos)
```
1. Chama input_rm() [view]
2. Busca aluno no repository
3. Se existe → chama aluno.exibir_informacoes()
4. Se nao → erro
```

##### 2.4: `exibir_alunos()` (15 minutos)
```
1. Valida se lista nao vazia
2. Se vazia → exibe "Nenhum aluno"
3. Se tem → loop exibindo todos com aluno.exibir_informacoes()
```

**Padrão:** Todos seguem fluxo similar ao `adicionar_aluno()` que JA FUNCIONA!

---

#### TAREFA 3: Melhorar Validacoes (30-40 minutos)
**Arquivo:** `Codigos/services/aluno_service.py`

**O que fazer:**

##### 3.1: `validar_rm()` - adicionar validacoes completas
```python
def validar_rm(rm: int) -> bool:
    # Verificar tipo
    if not isinstance(rm, int):
        return False
    # Verificar positivo
    if rm <= 0:
        return False
    # Verificar max 6 digitos
    if len(str(rm)) > 6:
        return False
    # Verificar duplicidade (buscar em repository)
    if busca_aluno_rm(rm) is not None:
        return False  # RM ja existe!
    return True
```

**Impacto:** Rejeitara RM negativo, > 6 digitos, duplicado

##### 3.2: `validacao_mensalidade()` - simplificar loop
**Arquivo:** `Codigos/views/aluno_view.py` linha 90-98

Mudar de:
```python
condicao = mensalidade < 0
while condicao:
    mensalidade = float(input(...))
    condicao = mensalidade < 0
    if not condicao:
        return mensalidade
```

Para:
```python
while True:
    try:
        valor = float(input("Digite mensalidade: "))
        if valor >= 0:
            return valor
        exibicao_erro("Valor negativo!")
    except ValueError:
        exibicao_erro("Digite numero valido!")
```

**Beneficio:** Codigo mais claro, tratamento de erro melhorado

---

#### TAREFA 4: Adicionar Try/Except em `escolha_usuario()` (10 minutos)
**Arquivo:** `Codigos/controllers/menu_controller.py` linha 31

**O que fazer:**
```python
def escolha_usuario():
    while True:  # ← adicionar loop
        try:
            opcao = int(input("Selecione opcao: "))
            match opcao:
                case 1: adicionar_aluno()
                # ... resto do match
            return opcao
        except ValueError:
            exibicao_erro("Digite numero valido!")
```

**Impacto:** Usuario digita "abc" → pede de novo em vez de quebrar

---

#### TAREFA 5: Adicionar Repository Helpers (10 minutos)
**Arquivo:** `Codigos/repositories/aluno_repository.py`

**O que fazer:**
```python
def adicionar_aluno_repo(aluno) -> None:
    """Adiciona aluno na lista."""
    lista_alunos.append(aluno)

def atualizar_aluno_repo(rm: int, novos_dados: dict) -> None:
    """Atualiza dados de aluno por RM."""
    aluno = busca_aluno_rm(rm)
    if aluno:
        aluno.update(novos_dados)

def remover_aluno_repo(rm: int) -> None:
    """Remove aluno da lista por RM."""
    aluno = busca_aluno_rm(rm)
    if aluno:
        lista_alunos.remove(aluno)
```

**Impacto:** Simplifica controlador (ja tem funcoes prontas)

---

### 📋 Checklist TAREFAS para v1.4.5:
- [ ] TAREFA 1: Menu loop (15 min) - `menu_inicial()` com while
- [ ] TAREFA 2: Handlers (80 min) - atualizar, excluir, exibir, listar
- [ ] TAREFA 3: Validacoes (40 min) - validar_rm() + simplificar mensalidade
- [ ] TAREFA 4: Try/except (10 min) - escolha_usuario() sem quebrar
- [ ] TAREFA 5: Repository helpers (10 min) - adicionar, atualizar, remover

**Total:** ~150 minutos (2-3 horas)

---

### ✅ Criterio de Pronto para v1.4.5:

- [ ] `python Codigos/main.py` roda sem erro
- [ ] Adicionar aluno → funciona completamente
- [ ] Atualizar aluno → busca + altera + persiste
- [ ] Excluir aluno → pede confirmacao → deleta
- [ ] Exibir aluno → busca por RM → mostra dados
- [ ] Exibir todos → lista completa
- [ ] Salvar JSON → arquivo criado com dados
- [ ] Usuario digita "abc" em numero → pede de novo
- [ ] Usuario tenta RM negativo → rejeita
- [ ] Usuario tenta RM duplicado → rejeita

---

## 💡 APRENDIZADOS-CHAVE DA REFATORAÇÃO v1.4.3 → v1.4.4

### 1. Validadores Puros Funcionam! ✅
Em v1.4.3, havia bug: `isinstance(nome, str) is None` sempre retornava False.  
Em v1.4.4, corrigido para: `if not isinstance(nome, str) or nome == ""`

**Aprendizado:** Validadores agora sao testáveis isoladamente!
```python
# Testar sem digitar nada:
assert validar_nome("Joao") == True
assert validar_nome("") == False
```

### 2. Fluxo CRUD Funcional (Adicionar) ✅
View coleta → Service valida → Repository persiste. Funciona do começo ao fim!

### 3. Match/Case Roteando Handlers ✅
Usando match/case no controller para rotear opcões. Clean e eficiente!

### 4. Sem Imports Circulares ✅
View NAO importa Service. Service NAO importa View. Controller importa ambos.

---

## 📊 STATUS ATUAL E PROXIMOS PASSOS

### Progresso v1.4.4 → v1.4.5
```
[████████████████████████░░░░] 67-70% pronto para commit v1.4.4

Feito:
- Estrutura de pastas ✅
- Dataclass Aluno ✅
- View com inputs ✅
- Service com validadores ✅
- Repository basico ✅
- Controller adicionar_aluno ✅
- Menu display ✅
- Sem circular imports ✅

Faltando:
- 4 handlers do controller ❌
- Menu loop ❌
- Validacoes completas ❌
- Repository helpers ❌
- Try/except inputs ❌
```

### Tempo Estimado para v1.4.5
- Implementar handlers: 80 minutos
- Melhorar validacoes: 40 minutos
- Menu loop + try/except: 25 minutos
- Repository helpers: 10 minutos
- Testar tudo: 20 minutos

**Total:** 2-3 horas de trabalho focado

---

## 🎯 PLANO DE ACAO (v1.4.5 - Proxima Sessao)

### Sessao 1 (90 min): Implementar 4 Handlers
1. Abrir `menu_controller.py`
2. Implementar `atualizar_aluno()` (20 min) - busca + altera + persiste
3. Implementar `excluir_aluno()` (20 min) - busca + confirmacao + deleta
4. Implementar `exibir_aluno()` (15 min) - busca + exibe com Aluno.exibir_informacoes()
5. Implementar `exibir_alunos()` (15 min) - lista todos
6. Testar cada um: `python main.py` → escolha opcao

### Sessao 2 (40 min): Validacoes Completas
1. Melhorar `validar_rm()` em `aluno_service.py` - adicionar positivo + max 6 digitos + duplicidade
2. Simplificar `validacao_mensalidade()` em `aluno_view.py` - usar `while True` padrao
3. Testar: RM negativo → rejeita, RM > 6 digitos → rejeita, RM duplicado → rejeita

### Sessao 3 (25 min): Menu Loop e Try/Except
1. Implementar `menu_inicial()` em `menu_view.py` - while loop
2. Adicionar try/except em `escolha_usuario()` - ValueError tratado
3. Testar: usuario digita "abc" → pede de novo

### Sessao 4 (15 min): Repository Helpers
1. Adicionar `adicionar_aluno_repo()`, `atualizar_aluno_repo()`, `remover_aluno_repo()`
2. Simplificar chamadas no controller

### Sessao 5 (20 min): Teste Completo + Commit
1. `python main.py`
2. Testar fluxo: adicionar → atualizar → excluir → exibir → listar → salvar
3. Verificar JSON foi criado com dados
4. Commit: `feat(v1.4.5): implementa CRUD 100% completo`

---

**Próxima atualização:** Apos completar v1.4.5, atualizar para v1.4.6 (testes + carregamento JSON)

**Status:** 🟢 PRONTO PARA COMMIT v1.4.4 (funcional 67-70%) → Próximo: v1.4.5 (CRUD 100%)


##### Ação 1: Revisar o que `aluno_service.py` precisa de `aluno_view.py`
**Entender o problema:**
- `aluno_service.py` importa `validacao_nome, validacao_rm, etc` de `aluno_view.py`
- Mas essas funções em `aluno_view.py` têm `input()` dentro (coleta do usuário)
- Service **não deveria chamar `input()`**
- Responsabilidade: view coleta com input(), service valida dados prontos

**Solução:**
- Em `aluno_service.py`: reescrever `validar_nome()` para **receber `nome` já coletado**
- Em vez de chamar função com input(), validar valor que já chegou

**Exemplo da mudança:**
```python
# ❌ ERRADO (atual) - service chama função com input():
def validar_nome(nome: str) -> bool:
    if validacao_nome() is None:  # ← chama função que tem input()
        return False
    return True

# ✅ CORRETO (alvo) - service valida dados prontos:
def validar_nome(nome: str) -> bool:
    """Recebe nome JÁ coletado, retorna True/False."""
    if isinstance(nome, str) and nome.strip() != "":
        return True
    return False
```

##### Ação 2: Revisar o que `aluno_view.py` precisa de `aluno_service.py`
**Entender o problema:**
- `aluno_view.py` importa `criar_objeto_aluno` de `aluno_service.py`
- View apenas coleta dados com `input()` e exibe com `print()`
- View não deveria processar lógica de negócio

**Solução:**
- Em `aluno_view.py`: funções devem apenas coletar dados e retornar (sem processar)
- Retornar `dict` simples com os dados
- Deixar para controller (que virá depois) chamar service para validar

**Exemplo da mudança:**
```python
# ❌ ERRADO (atual) - view importa service:
from Codigos.services.aluno_service import criar_objeto_aluno

def input_aluno():
    dados = {...}
    aluno = criar_objeto_aluno(...)  # ← processamento
    
# ✅ CORRETO (alvo) - view apenas coleta:
def input_aluno() -> dict:
    """Coleta dados via input, retorna dict simples."""
    nome = input("\nDigite o nome: ").strip()
    rm = int(input("Digite o RM: "))
    curso = input("Digite o curso: ").strip()
    mensalidade = float(input("Digite a mensalidade: "))
    
    return {
        "nome_aluno": nome,
        "rm": rm,
        "curso": curso,
        "mensalidade": mensalidade
    }
    # Sem import de service, sem processamento aqui!
```

##### Ação 3: Criar `controllers/menu_controller.py` (o intermediário)
**Para que:**
- Precisa de alguém que não é nem view nem service
- Chama view → chama service → chama repository
- Quebra o ciclo direto entre view e service

**O que vai ter:**
- Handlers para cada opção do menu (adicionar_aluno, atualizar_aluno, etc)
- Cada handler: view coleta → service valida → repository salva
- Menu controller orquestra todo o fluxo

**Pseudocódigo (você implementa com seu código):**
```python
# controllers/menu_controller.py

def adicionar_aluno():
    """Handler para opção 1 do menu"""
    try:
        dados = input_aluno()  # View coleta
        
        # Service valida (dados já prontos)
        if not validar_nome(dados["nome_aluno"]):
            exibicao_erro("Nome inválido!")
            return
        if not validar_rm(dados["rm"]):
            exibicao_erro("RM inválido!")
            return
        # ... resto das validações
        
        # Repository salva
        adicionar_aluno_repo(dados)
        print("✅ Aluno adicionado!")
        
    except ValueError:
        exibicao_erro("Entrada inválida!")
```

**Por que isso quebra o circular:**
- View não importa service ✅
- Service não importa view ✅
- Controller importa ambos, mas não há ciclo ✅

##### Ação 4: Deletar ou esvaziar `menu_service.py`
**Por que:**
- `menu_service.py` chama `crud_alunos.py` que importa `aluno_service.py`
- Cria ciclo de imports
- Sua responsabilidade vai para `menu_controller.py`

**Ação:** Remover ou deixar vazio

##### Ação 5: Rodar `python main.py` e ver o menu aparecer
**Teste final:** Sem `ImportError`

#### Checklist Ação-a-Ação:
- [ ] Ação 1: Reescrever `validar_*` em `aluno_service.py` para **receberem dados prontos** (sem chamar input)
- [ ] Ação 2: Revisar `input_aluno()` em `aluno_view.py` para **não importar service**
- [ ] Ação 3: Criar `controllers/menu_controller.py` com handlers (adicionar, atualizar, excluir, etc)
- [ ] Ação 4: Remover/esvaziar `menu_service.py`
- [ ] Ação 5: Rodar `python main.py` → deve exibir menu sem erro

---

### **ETAPA 2: Limpar `aluno_service.py` (remover I/O, deixar puro)**

**Objetivo:** Service é testável sem `input/print`  
**Por que:** Quando você quer testar se um aluno é válido, não quer digitar no terminal toda vez. Service precisa ser "puro".

#### O que entender:
**Duas categorias de validação:**

1. **Validação com Input** (VIEW):
   - Tem `input()` dentro
   - Pergunta ao usuário e trata erros
   - Exemplos: `validacao_nome()`, `validacao_mensalidade()`
   - Ficam em `aluno_view.py`

2. **Validação Pura** (SERVICE):
   - Recebe dados já coletados
   - Retorna `True/False` ou lança exceção
   - Sem `input()`, sem `print()`
   - Testável isoladamente
   - Ficam em `aluno_service.py`

#### Exemplo visual da diferença:

```
VIEW (aluno_view.py):
validacao_mensalidade() {
    while True:
        valor = input("Digite: ")     ← input aqui
        try:
            valor = float(valor)
        except ValueError:
            print("Inválido!")        ← tratamento aqui
            continue
        if valor >= 0:
            return valor
}

SERVICE (aluno_service.py):
validar_mensalidade(valor: float) -> bool {
    if isinstance(valor, (int, float)) and valor >= 0:
        return True                   ← só retorna bool
    return False
}
```

#### O que fazer:
1. **Em `aluno_view.py`:** funções de input continuam (têm `input()`)
2. **Em `aluno_service.py`:** reescrever validadores para receberem dados prontos
3. **Resultado:** Service não depende de ninguém; view coleta e controller orquestra

#### Checklist Etapa 2:
- [ ] `aluno_service.py` não tem mais `input()` ou `print()`
- [ ] Validadores puros recebem dados prontos e retornam `bool`
- [ ] `criar_objeto_aluno()` usa validadores puros
- [ ] Nenhuma função de service importa view
- [ ] Você consegue testar `validar_nome("João")` sem digitar nada

---

### **ETAPA 3: Completar `aluno_repository.py` (persistência completa)**

**Objetivo:** Repository gerencia tudo de acesso a dados  
**Por que:** View não deveria saber de JSON ou lista em memória. Repository cuida disso.

#### O que falta em `aluno_repository.py`:
Hoje tem:
- `lista_alunos` (memória)
- `busca_aluno_rm(rm)`
- `salvando_lista_json()`

Precisa de:
- `adicionar_aluno_repo(aluno_dict)` - adicionar à lista
- `atualizar_aluno_repo(rm, novo_aluno_dict)` - atualizar
- `remover_aluno_repo(rm)` - remover da lista
- `carregar_lista_json()` - ler JSON ao iniciar (hoje falta!)

#### Por que isso é importante:
- Menu controller não precisa saber ONDE os dados vivem (JSON? Banco? Memória?)
- Se mudar para banco de dados depois, muda só repository
- View nunca acessa dados diretamente

#### Checklist Etapa 3:
- [ ] Repository tem `adicionar_aluno_repo()`
- [ ] Repository tem `atualizar_aluno_repo()`
- [ ] Repository tem `remover_aluno_repo()`
- [ ] Função `carregar_lista_json()` carrega dados ao iniciar
- [ ] Fluxo criar → atualizar → excluir → exibir todo funciona
- [ ] JSON persiste corretamente

---

### **ETAPA 4: Corrigir Fluxos de Validação (especialmente mensalidade)**

**Objetivo:** Loops de validação robustos  
**Por que:** Usuário digita "abc" em mensalidade? App não deve quebrar.

#### Problema atual em `validacao_mensalidade()`:
```python
mensalidade = float(input(...))  # Se digitar "abc" → ValueError!
condicao = mensalidade < 0
while condicao:
    exibicao_erro("...")
    mensalidade = float(input(...))  # Pode quebrar aqui também!
    if not condicao:  # ❌ Lógica errada
        return mensalidade
return mensalidade
```

#### Solução (loop correto):
```python
def validacao_mensalidade() -> float:
    """Coleta mensalidade com retry automático."""
    while True:
        try:
            valor = float(input("\nDigite a mensalidade: "))
            if valor >= 0:
                return valor
            else:
                exibicao_erro("Valor não pode ser negativo!")
        except ValueError:
            exibicao_erro("Digite um número válido!")
```

#### O padrão de loop correto:
```
while True:
    try:
        valor = input/conversão
        se válido:
            return valor
        senão:
            erro e continua
    except exceção_específica:
        erro e continua
```

#### Checklist Etapa 4:
- [ ] `validacao_mensalidade()` tem try/except ValueError
- [ ] `validacao_nome()` não deixa nome vazio
- [ ] `validacao_rm()` trata ValueError
- [ ] Confirmação de exclusão não quebra com entrada textual
- [ ] Teste: digita "abc" em mensalidade → pede de novo (não quebra)

---

### **ETAPA 5: Consolidar com Testes e Documentação**

**Objetivo:** v1.3.7 pronto com testes mínimos  
**Por que:** Evita regressão; documenta comportamento esperado

#### O que testar:
1. **Service (validadores puros):**
   - `validar_nome("João")` → True
   - `validar_nome("")` → False
   - `validar_rm(123456)` → True
   - `validar_rm(-1)` → False
   - etc

2. **Repository (persistência):**
   - Adicionar aluno → appears em `lista_alunos`
   - Buscar aluno → retorna dict correto
   - Salvar JSON → arquivo criado e lido corretamente

3. **Integração (fluxo completo):**
   - Adicionar → salvar → ler JSON → aluno persiste

#### Checklist Etapa 5:
- [ ] Arquivo `test_aluno.py` com testes básicos
- [ ] Testes de service (validadores puros)
- [ ] Testes de repository (CRUD)
- [ ] README atualizado com v1.3.6 e v1.3.7
- [ ] Instruções claras de como rodar (`python main.py`)

---

## 📋 RESUMO RÁPIDO: O QUE PRECISA ACONTECER

### Arquivos que EXISTEM mas ESTÃO ERRADOS:
1. `aluno_service.py` - importa de view (circular!)
2. `aluno_view.py` - importa de service (circular!)
3. `menu_service.py` - referencia crud_alunos (quebrado)
4. `crud_alunos.py` - não deveria mais existir (código espalhado)

### Arquivos que PRECISAM SER CRIADOS:
1. `controllers/menu_controller.py` - orquestrador do fluxo
2. `controllers/__init__.py` - para Python reconhecer pasta como package

### Arquivos que PRECISAM SER ATUALIZADOS:
1. `main.py` - chamar menu_controller
2. `menu_view.py` - chamar menu_controller
3. `aluno_repository.py` - adicionar CRUD completo
4. `aluno_service.py` - fazer validadores puros (sem input)
5. `aluno_view.py` - fazer apenas I/O (sem service)

---

## 🎯 CRONOGRAMA PRÁTICO (próximos 3-5 commits)

### Commit 1 (v1.3.6 - Refatoração em Camadas):
```
feat: quebra import circular e refatoração em camadas

- [x] Criar controllers/menu_controller.py com orquestração do menu
- [x] Reescrever aluno_service.py com validadores puros (sem I/O)
- [x] Limpar aluno_view.py para apenas coleta/exibição
- [x] Completar aluno_repository.py com CRUD completo
- [x] Atualizar main.py para chamar menu_controller
- [x] Deletar ou esvaziar menu_service.py
- [x] Deletar ou esvaziar crud_alunos.py

Resultados:
- App inicia sem ImportError
- Fluxo CRUD completo funciona
- Validações robustas em loops
- Docstrings em funções críticas
```

### Commit 2 (v1.3.7 - Testes e Documentação):
```
test: adicionar testes unitários e melhorar cobertura

- [x] Testes de validadores puros (aluno_service.py)
- [x] Testes de repository (CRUD)
- [x] README atualizado com v1.3.6 e v1.3.7
- [x] Docstrings completas em aluno_service.py
- [x] Instruções de execução claras
```

### Commit 3+ (v1.3.8+ - Melhorias Futuras):
```
Carregamento automático de JSON ao iniciar
Exceções customizadas (NomeInvalidoError, etc)
Mais testes de integração
CLI com argparse
```

---

## 🚨 ARMADILHAS COMUNS (evite!)

- ❌ **Não deletar `crud_alunos.py` antes de ter controller pronto**
- ❌ **Não deixar `input()` em `aluno_service.py`**
- ❌ **Não importar view em service ou service em view**
- ❌ **Não usar `except:` genérico; sempre exceções específicas**
- ❌ **Não misturar dict e Aluno; escolher padrão e manter**
- ✅ **Fazer:** Testar cada etapa rodando `python main.py` inteiro
- ✅ **Fazer:** Commitar após cada etapa funcionar
- ✅ **Fazer:** Manter `lista_alunos` só em repository

---

---

## 💡 APRENDIZADOS-CHAVE DA REFATORAÇÃO (v1.4.3)

### 1. Por Que Separar em Camadas?
**Antes (v1.4.2):** Tudo em `crud_alunos.py` (~200 linhas)
- Adicionar validacao? Mexe no arquivo inteiro
- Trocar JSON por banco? Mexe em 10 funcoes
- Testar validador? Precisa simular input do usuario

**Depois (v1.4.3):** Camadas separadas
- Adicionar validacao? So mexe em `aluno_service.py`
- Trocar JSON por banco? So mexe em `aluno_repository.py`
- Testar validador? Chama `validar_nome("Joao")` direto!

**Beneficio Real:** Manutencao 3x mais rapida, menos bugs em cascata.

---

### 2. Entendendo Validadores Puros
**Pergunta:** Por que `validar_nome()` nao pode ter `input()` dentro?

**Resposta:** Porque nao consegue testar!
```python
# ❌ RUIM (v1.4.2):
def validacao_nome():
    nome = input("Digite: ")  # ← tem que digitar no terminal sempre!
    if nome == "":
        return None
    return nome.upper()

# Como testar isso? Nao da!

# ✅ BOM (v1.4.3):
def validar_nome(nome: str) -> bool:
    """Recebe nome ja coletado."""
    if isinstance(nome, str) and nome.strip() != "":
        return True
    return False

# Testar? Facil!
assert validar_nome("Joao") == True
assert validar_nome("") == False
assert validar_nome("  ") == False
```

**Aprendizado:** View coleta, service valida. Nunca misturar!

---

### 3. O Erro do `isinstance() is None`
**Erro cometido em v1.4.3:**
```python
if isinstance(nome, str) is None:  # ← SEMPRE False!
    return False
return True  # ← sempre executa
```

**Por que esta errado:**
- `isinstance()` retorna `True` ou `False` (boolean)
- Nunca retorna `None`
- Entao `isinstance(...) is None` sempre False
- Validador sempre retorna True (aceita tudo!)

**Correcao:**
```python
if isinstance(nome, str) and nome.strip() != "":
    return True  # ← so retorna True se for string E nao vazia
return False
```

**Aprendizado:** `isinstance()` retorna boolean. Checar resultado com `and`/`or`, nao com `is None`.

---

### 4. Loop de Validacao Correto
**Padrao identificado em v1.4.3 (loop infinito):**
```python
condicao = mensalidade < 0
while condicao:
    mensalidade = float(input(...))
    if not condicao:  # ← condicao NUNCA muda!
        return mensalidade
```

**Padrao correto (aprendido):**
```python
while True:
    try:
        valor = conversao(input(...))
        if condicao_valida(valor):
            return valor  # ← sai do loop
        else:
            erro("invalido")  # ← volta ao topo do while
    except TipoDeErro:
        erro("tipo errado")  # ← volta ao topo do while
```

**Aprendizado:** `while True` + validar + `return` ou `continue`. Nunca usar flag que nao recalcula.

---

### 5. Imports Precisam Estar Corretos
**Erro identificado:** Chamar funcao sem importar modulo.

**Exemplo real (v1.4.3):**
```python
# aluno_view.py linha 26
exibicao_erro("Nome invalido!")  # ← funcao nao importada!
```

**Python diz:** `NameError: name 'exibicao_erro' is not defined`

**Correcao:**
```python
# No topo do arquivo
from Codigos.views.menu_view import exibicao_erro

# Agora pode usar
exibicao_erro("Nome invalido!")  # ← funciona!
```

**Aprendizado:** Python nao adivinha onde funcao vive. Sempre importar antes de usar.

---

## 📊 STATUS ATUAL E PROXIMOS PASSOS

### Progresso v1.4.3 → v1.4.4
```
[████████████████████░░░░] 80% pronto para commit

✅ Estrutura criada (pastas, arquivos)
✅ Dataclass Aluno
✅ Repository basico (busca, salvar)
✅ View com inputs
✅ Service com validadores (estrutura)
✅ Controller iniciado

❌ Bugs em validadores (BUG 1)
❌ Loop infinito mensalidade (BUG 2)
❌ Imports faltando (BUG 3)
❌ Dict com chaves erradas (BUG 4)
❌ Menu sem loop (BUG 5)
```

### Tempo Estimado para v1.4.4
- Corrigir 5 bugs: **1-2 horas**
- Testar fluxo completo: **30 minutos**
- Documentar mudancas: **15 minutos**

**Total:** 2-3 horas de trabalho focado

---

## 🎯 PLANO DE ACAO (v1.4.4 - Proxima Sessao)

### Sessao 1 (1 hora): Corrigir Validadores
1. Abrir `aluno_service.py`
2. Corrigir `validar_nome()` (usar `and nome.strip() != ""`)
3. Copiar padrao para `validar_rm()`, `validar_curso()`, `validar_mensalidade()`
4. Testar no terminal: `python -c "from Codigos.services.aluno_service import validar_nome; print(validar_nome('Joao'))"`

### Sessao 2 (30 min): Corrigir Loop e Imports
1. Abrir `aluno_view.py`
2. Adicionar imports no topo (exibicao_erro, busca_aluno_rm)
3. Corrigir `validacao_mensalidade()` com padrao `while True`
4. Testar: usuario digita "abc" → pede de novo (nao quebra!)

### Sessao 3 (30 min): Completar Controller
1. Abrir `menu_controller.py`
2. Corrigir chaves do dict (linha 22, 26, 30)
3. Adicionar criacao de Aluno e adicionar_repo
4. Implementar `menu_inicial()` com loop

### Sessao 4 (30 min): Testar Tudo
1. `python Codigos/main.py`
2. Adicionar aluno → funciona?
3. Salvar JSON → arquivo criado?
4. Commit: `git commit -m "feat(v1.4.4): corrige bugs validadores e completa fluxo adicionar"`

---

**Proxima atualizacao:** Apos corrigir bugs, atualizar este roadmap para v1.4.5 (testes + carregamento JSON)

**Status:** 🟡 PRONTO PARA COMMIT v1.4.3 (estrutura) → Proximo: corrigir bugs para v1.4.4

---

## 📞 DÚVIDAS FREQUENTES

**P: Pode deletar `crud_alunos.py`?**  
R: Só depois que `menu_controller.py` está completo e testado. Melhor ir movendo código aos poucos.

**P: Deve ser `from Codigos...` ou `from .`?**  
R: Mantenha `Codigos.` em todos para consistência. Depois migra para `.` se quiser.

**P: JSON sempre em `dados_alunos.json` na raiz?**  
R: Sim, por enquanto. Depois pode colocar em pasta `data/`.

**P: Service chama repository diretamente?**  
R: Sim! Service chama repository para validar RM único (ex: `busca_aluno_rm()`).  
Mas controller também chama repository para persistir.

**P: Por que `menu_controller.py` precisa existir?**  
R: Quebra o ciclo view ↔ service. Controller é o "cola" entre eles.

---

## ✨ VISÃO LONGA (após v1.3.7)

Depois que tudo estiver refatorado, caminho claro para:

- **v1.3.8:** Carregamento automático JSON ao iniciar (lê arquivo ao abrir app)
- **v1.3.9:** Exceções customizadas (código fica mais limpo)
- **v1.4.0:** Testes com `pytest` + fixtures
- **v1.4.1:** CLI com argparse (`python main.py --add-aluno`)
- **v1.5.0:** Banco de dados SQLite (muda só repository!)

---

## 📊 STATUS ATUAL E PROGRESSO

```
ETAPA 1 (Quebrar Circular):
[████████░░░░░░░░░░░░░░░░] 40% completa
  - Falta: menu_controller.py, revisão final de imports

ETAPA 2 (Validadores Puros):
[░░░░░░░░░░░░░░░░░░░░░░░░] 0% (depois da ETAPA 1)

ETAPA 3 (Repository Completo):
[░░░░░░░░░░░░░░░░░░░░░░░░] 10% (tem busca, faltam CRUD)

ETAPA 4 (Loops Robustos):
[░░░░░░░░░░░░░░░░░░░░░░░░] 5% (mensalidade tem bug)

ETAPA 5 (Testes + Docs):
[░░░░░░░░░░░░░░░░░░░░░░░░] 0% (roadmap)
```

**Tempo estimado:** 3-5 horas (divididas em 2-3 sessões)

---

**Última atualização:** 2026-03-06  
**Versão do roadmap:** 1.2  
**Status:** ATIVO - Bloqueado por ETAPA 1  

Para questões, consulte este documento antes de codificar! 🚀  

