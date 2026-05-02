"""
TESTE MANUAL 1 — Login com credenciais válidas
Escrito manualmente, sem auxílio de IA.

O que este teste faz:
1. Abre o site automationexercise.com
2. Navega para a página de Login
3. Preenche e-mail e senha de uma conta existente
4. Verifica que o login foi bem-sucedido (nome do usuário aparece no menu)
"""

import pytest
from playwright.sync_api import Page, expect
from tests.conftest import BASE_URL, TEST_EMAIL, TEST_PASSWORD, TEST_NAME


def test_login_valido(page: Page):
    """
    Testa o fluxo de login com credenciais corretas.
    Resultado esperado: usuário é redirecionado e vê seu nome no menu.
    """

    # Passo 1: Abre a página inicial
    page.goto(BASE_URL)

    # Passo 2: Clica no link "Signup / Login" do menu
    page.get_by_role("link", name="Signup / Login").click()

    # Passo 3: Verifica que chegou na página correta
    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.get_by_text("Login to your account")).to_be_visible()

    # Passo 4: Preenche o formulário de login
    page.locator('input[data-qa="login-email"]').fill(TEST_EMAIL)
    page.locator('input[data-qa="login-password"]').fill(TEST_PASSWORD)

    # Passo 5: Clica no botão Login
    page.locator('button[data-qa="login-button"]').click()

    # Passo 6: Verifica que o login funcionou — nome do usuário aparece no menu
    expect(page.get_by_text(f"Logged in as {TEST_NAME}")).to_be_visible()

    # Passo 7: Verifica que foi redirecionado para a página inicial
    expect(page).to_have_url(BASE_URL + "/")
