"""
TESTE COM IA 1 — Login: cenários válidos e inválidos
Gerado com auxílio do Claude (IA), que sugeriu:
- Usar pytest.mark.parametrize para cobrir múltiplos cenários com um único teste
- Os casos de teste negativos (e-mail inválido, senha errada, campos vazios)
- As asserções de mensagem de erro específicas para cada caso

Por que isso é melhor que o teste manual?
- Cobre 4 cenários com o mesmo código (mais cobertura)
- Testa casos de borda que humanos frequentemente esquecem
- Mais fácil de expandir: basta adicionar uma linha na lista de parâmetros
"""

import pytest
from playwright.sync_api import Page, expect
from tests.conftest import BASE_URL, TEST_EMAIL, TEST_PASSWORD


# IA sugeriu esta estrutura de dados para cobrir múltiplos cenários:
# (email, senha, deve_ter_sucesso, mensagem_esperada_no_erro)
CENARIOS_LOGIN = [
    # Caso 1: Login válido — deve funcionar
    (TEST_EMAIL, TEST_PASSWORD, True, None),

    # Caso 2: E-mail inexistente — deve mostrar erro
    ("usuario_nao_existe@fake.com", "qualquersenha", False, "Your email or password is incorrect!"),

    # Caso 3: Senha errada — deve mostrar erro
    (TEST_EMAIL, "senhaerrada123", False, "Your email or password is incorrect!"),

    # Caso 4: Campos vazios — deve mostrar erro de validação
    ("", "", False, ""),
]


@pytest.mark.parametrize("email,senha,sucesso,mensagem_erro", CENARIOS_LOGIN)
def test_login_multiplos_cenarios(page: Page, email: str, senha: str, sucesso: bool, mensagem_erro: str):
    """
    Testa o login com diferentes combinações de credenciais.
    A IA gerou os casos de teste e as asserções para cada cenário.
    """

    # Navega para a página de login
    page.goto(f"{BASE_URL}/login")

    # Preenche os campos (mesmo que vazios — testa validação)
    page.locator('input[data-qa="login-email"]').fill(email)
    page.locator('input[data-qa="login-password"]').fill(senha)
    page.locator('button[data-qa="login-button"]').click()

    if sucesso:
        # Caso de sucesso: verifica redirecionamento para home
        expect(page).to_have_url(BASE_URL + "/")
        # Verifica que o menu mostra "Logged in as"
        expect(page.get_by_text("Logged in as")).to_be_visible()
    else:
        # Caso de falha: verifica que permaneceu na página de login
        expect(page).to_have_url(f"{BASE_URL}/login")
        
        # SÓ verifica o texto se a mensagem_erro não for vazia
        if mensagem_erro:
            expect(page.get_by_text(mensagem_erro)).to_be_visible()