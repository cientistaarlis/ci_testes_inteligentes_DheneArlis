"""
TESTE MANUAL 2 — Cadastro de novo usuário
Escrito manualmente, sem auxílio de IA.

O que este teste faz:
1. Abre o site automationexercise.com
2. Navega para a página de Signup
3. Preenche nome e e-mail
4. Preenche o formulário completo de cadastro
5. Verifica a mensagem de conta criada com sucesso
"""

import pytest
import time
from playwright.sync_api import Page, expect
from tests.conftest import BASE_URL

# Gera um e-mail único usando timestamp para não conflitar com cadastros anteriores
NOVO_EMAIL = f"teste_{int(time.time())}@exemplo.com"
NOVO_NOME = "Joao Silva Teste"


def test_cadastro_novo_usuario(page: Page):
    """
    Testa o fluxo completo de cadastro de um novo usuário.
    Resultado esperado: conta criada com sucesso.
    """

    # Passo 1: Abre a página inicial
    page.goto(BASE_URL)

    # Passo 2: Navega para Login/Signup
    page.get_by_role("link", name="Signup / Login").click()

    # Passo 3: Verifica a seção "New User Signup"
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # Passo 4: Preenche nome e e-mail no formulário de signup
    page.locator('input[data-qa="signup-name"]').fill(NOVO_NOME)
    page.locator('input[data-qa="signup-email"]').fill(NOVO_EMAIL)

    # Passo 5: Clica no botão Signup
    page.locator('button[data-qa="signup-button"]').click()

    # Passo 6: Verifica que chegou no formulário detalhado de cadastro
    expect(page.get_by_text("Enter Account Information")).to_be_visible()

    # Passo 7: Preenche os campos obrigatórios do formulário
    page.locator('#id_gender1').check()  # Seleciona "Mr."
    page.locator('input[data-qa="password"]').fill("Senha@Teste123")
    page.locator('select[data-qa="days"]').select_option("15")
    page.locator('select[data-qa="months"]').select_option("6")
    page.locator('select[data-qa="years"]').select_option("1990")

    # Passo 8: Preenche endereço
    page.locator('input[data-qa="first_name"]').fill("Joao")
    page.locator('input[data-qa="last_name"]').fill("Silva")
    page.locator('input[data-qa="address"]').fill("Rua Teste, 123")
    page.locator('select[data-qa="country"]').select_option("India")
    page.locator('input[data-qa="state"]').fill("Bahia")
    page.locator('input[data-qa="city"]').fill("Salvador")
    page.locator('input[data-qa="zipcode"]').fill("40000-000")
    page.locator('input[data-qa="mobile_number"]').fill("71999999999")

    # Passo 9: Submete o formulário
    page.locator('button[data-qa="create-account"]').click()

    # Passo 10: Verifica mensagem de sucesso
    expect(page.get_by_text("Account Created!")).to_be_visible()
    expect(page.locator('h2[data-qa="account-created"]')).to_be_visible()
