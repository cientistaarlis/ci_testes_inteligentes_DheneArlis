# ci_testes_inteligentes_[SEU-NOME]

<!-- 
  IMPORTANTE: Substitua SEU-USUARIO e SEU-REPOSITORIO abaixo
  pelo seu usuário e nome do repositório no GitHub.
  Exemplo: se seu repositório é github.com/joaosilva/ci_testes_inteligentes_joao
  substitua: SEU-USUARIO → joaosilva
              SEU-REPOSITORIO → ci_testes_inteligentes_joao
-->

[![Pipeline Manual](https://github.com/SEU-USUARIO/SEU-REPOSITORIO/actions/workflows/pipeline-manual.yml/badge.svg)](https://github.com/SEU-USUARIO/SEU-REPOSITORIO/actions/workflows/pipeline-manual.yml)
[![Pipeline com IA](https://github.com/SEU-USUARIO/SEU-REPOSITORIO/actions/workflows/pipeline-ai.yml/badge.svg)](https://github.com/SEU-USUARIO/SEU-REPOSITORIO/actions/workflows/pipeline-ai.yml)

Repositório da atividade prática de CI e automação de testes com Playwright (Python),
desenvolvida para a disciplina de Qualidade de Software.

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

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv

# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure suas credenciais

```bash
# Copie o arquivo de exemplo
cp .env.example .env
```

Abra o arquivo `.env` e preencha com:
- Um e-mail e senha de uma conta que você criar em [automationexercise.com/login](https://automationexercise.com/login)
- Seu nome exatamente como cadastrado no site

Depois, abra `tests/conftest.py` e atualize as três variáveis no topo do arquivo.

### 5. Execute os testes

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

> Remova `--headed` para rodar sem abrir o browser (modo headless).

---

## Pipelines de CI

| Pipeline | Arquivo | O que executa | Quando dispara |
|---|---|---|---|
| Pipeline 1 | `pipeline-manual.yml` | `tests/manual/` | Push em branch de feature ou PR para main |
| Pipeline 2 | `pipeline-ai.yml` | `tests/ai/` | Push em branch de feature ou PR para main |

Os artefatos (screenshots de falha + relatório HTML) ficam disponíveis por **7 dias** em cada execução.

---

## Sobre os testes

### Testes manuais (sem IA)
| Arquivo | Descrição |
|---|---|
| `test_login.py` | Login com credenciais válidas — verifica redirecionamento e nome no menu |
| `test_cadastro.py` | Cadastro completo de novo usuário — verifica mensagem de sucesso |

### Testes com IA
| Arquivo | Descrição |
|---|---|
| `test_login_ai.py` | Login parametrizado com 4 cenários: válido, e-mail errado, senha errada, campos vazios |
| `test_navegacao_ai.py` | 4 funções de teste: home, categoria Women, busca de produto, detalhes de produto |

> Os testes da pasta `ai/` foram gerados com auxílio do **Claude** (Anthropic),
> que sugeriu a estrutura parametrizada, os casos de borda e as asserções detalhadas.

---

## Uso de IA neste projeto

O Claude foi utilizado para:
- Sugerir o uso de `pytest.mark.parametrize` para cobrir múltiplos cenários de login
- Gerar os casos de teste negativos (credenciais inválidas, campos vazios)
- Propor a estrutura de fixtures reutilizáveis no `test_navegacao_ai.py`
- Identificar quais elementos verificar na página de detalhes de produto

Todo o código foi revisado, entendido e validado pelo autor.
