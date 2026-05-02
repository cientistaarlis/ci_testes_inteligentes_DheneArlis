# ci_testes_inteligentes_DheneArlis

[![Pipeline Manual](https://github.com/cientistaarlis/ci_testes_inteligentes_DheneArlis/actions/workflows/pipeline-manual.yml/badge.svg)](https://github.com/cientistaarlis/ci_testes_inteligentes_DheneArlis/actions/workflows/pipeline-manual.yml)
[![Pipeline com IA](https://github.com/cientistaarlis/ci_testes_inteligentes_DheneArlis/actions/workflows/pipeline-ai.yml/badge.svg)](https://github.com/cientistaarlis/ci_testes_inteligentes_DheneArlis/actions/workflows/pipeline-ai.yml)

Repositório da atividade prática de CI e automação de testes com Playwright (Python),
desenvolvida para a disciplina de Engenharia de Software-IFSP.

**Site testado:** [automationexercise.com](https://automationexercise.com)  
**Ferramenta:** Playwright + Python + pytest  
**CI:** GitHub Actions  

---

## Estrutura do projeto

```
.
├── .github/
│   └── workflows/
│       ├── pipeline-manual.yml   # Pipeline 1: testes escritos manualmente
│       └── pipeline-ai.yml       # Pipeline 2: testes gerados com IA
├── tests/
│   ├── conftest.py               # Configurações e credenciais compartilhadas
│   ├── manual/
│   │   ├── test_login.py         # Teste 1: login com credenciais válidas
│   │   └── test_cadastro.py      # Teste 2: cadastro de novo usuário
│   └── ai/
│       ├── test_login_ai.py      # Teste 3: login com múltiplos cenários (IA)
│       └── test_navegacao_ai.py  # Teste 4: navegação e produtos (IA)
├── .env.example                  # Variáveis de ambiente necessárias
├── .gitignore
├── pytest.ini                    # Configuração do pytest
├── requirements.txt              # Dependências Python
└── README.md
```

---

## Pré-requisitos

- Python 3.11 ou superior
- pip

---

## Como instalar e executar localmente

### 1. Repositório clonado

```bash
git clone https://github.com/cientistaarlis/ci_testes_inteligentes_DheneArlis.git
cd ci_testes_inteligentes_DheneArlis
```

### 2. Ambiente virtual criado

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Dependências instaladas

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Credenciais configuradas

```bash
cp .env.example .env
```

O arquivo `.env` foi preenchido com:
- E-mail e senha da conta criada em [automationexercise.com/login](https://automationexercise.com/login)
- Nome exatamente como cadastrado no site

As três variáveis no topo de `tests/conftest.py` foram atualizadas conforme o `.env`.

### 5. Testes executados

**Testes manuais** (Pipeline 1):
```bash
pytest tests/manual/ -v --headed
```

**Testes com IA** (Pipeline 2):
```bash
pytest tests/ai/ -v --headed
```

**Todos os testes juntos:**
```bash
pytest tests/ -v --headed
```

> O flag `--headed` pode ser removido para execução em modo headless (sem abrir o browser).

---

## Pipelines de CI

| Pipeline | Arquivo | O que executa | Quando dispara |
|---|---|---|---|
| Pipeline 1 | `pipeline-manual.yml` | `tests/manual/` | Push em branch de feature ou PR para main |
| Pipeline 2 | `pipeline-ai.yml` | `tests/ai/` | Push em branch de feature ou PR para main |

---

## Sobre os testes

### Testes manuais (sem IA)

| Arquivo | Descrição |
|---|---|
| `test_login.py` | Login com credenciais válidas — verificado redirecionamento e nome no menu |
| `test_cadastro.py` | Cadastro completo de novo usuário — verificada mensagem de sucesso |

### Testes com IA

| Arquivo | Descrição |
|---|---|
| `test_login_ai.py` | Login parametrizado com 4 cenários gerados com IA: válido, e-mail errado, senha errada, campos vazios |
| `test_navegacao_ai.py` | 4 funções de teste geradas com IA: home, categoria Women, busca de produto, detalhes de produto |

> Os testes da pasta `ai/` foram gerados com auxílio do **Claude** (Anthropic),
> que sugeriu a estrutura parametrizada, os casos de borda e as asserções detalhadas.

---

## Uso de IA neste projeto

O Claude foi utilizado para:
- Sugerido o uso de `pytest.mark.parametrize` para cobrir múltiplos cenários de login
- Gerados os casos de teste negativos (credenciais inválidas, campos vazios)
- Proposta a estrutura de fixtures reutilizáveis no `test_navegacao_ai.py`
- Identificados os elementos a verificar na página de detalhes de produto
