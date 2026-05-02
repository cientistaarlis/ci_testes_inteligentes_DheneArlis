"""
TESTE COM IA 2 — Navegação completa e busca de produtos
Gerado com auxílio do Claude (IA), que sugeriu:
- Testar a navegação por categorias (Women, Men, Kids)
- Verificar que a listagem de produtos carrega corretamente
- Testar a funcionalidade de busca
- Verificar a página de detalhes de um produto
- Usar fixtures do pytest para reutilizar a página já na URL correta

Por que isso é melhor que fazer manualmente?
- A IA identificou 4 fluxos críticos de navegação que precisam ser testados
- Adicionou asserções que vão além do básico (verifica quantidade de itens, texto)
- Estruturou o código com uma fixture de setup para evitar repetição
"""

import pytest
from playwright.sync_api import Page, expect
from tests.conftest import BASE_URL


@pytest.fixture
def pagina_produtos(page: Page):
    """
    Fixture gerada pela IA: garante que cada teste começa
    já na página de produtos, sem repetir o goto em cada teste.
    """
    page.goto(f"{BASE_URL}/products")
    expect(page).to_have_url(f"{BASE_URL}/products")
    return page


def test_pagina_inicial_carrega_corretamente(page: Page):
    """
    Verifica que a home carrega com os elementos essenciais.
    IA sugeriu verificar: título, menu, produtos em destaque e rodapé.
    """
    page.goto(BASE_URL)

    # Verifica título da página
    expect(page).to_have_title("Automation Exercise")

    # Verifica itens do menu principal
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="Products")).to_be_visible()
    expect(page.get_by_role("link", name="Cart")).to_be_visible()
    expect(page.get_by_role("link", name="Signup / Login")).to_be_visible()

    # Verifica que produtos em destaque aparecem (pelo menos 1)
    produtos = page.locator(".features_items .product-image-wrapper")
    expect(produtos.first).to_be_visible()


def test_navegacao_categoria_women(page: Page):
    """
    Testa a navegação pela categoria Women > Dress.
    IA sugeriu verificar o título da página de categoria e a presença de produtos.
    """
    page.goto(BASE_URL)

    # Clica na categoria Women no menu lateral
    page.get_by_role("link", name="Women").click()

    # Expande e clica em "Dress" dentro de Women
    page.get_by_role("link", name=" Dress").first.click()

    # Verifica que chegou na página da categoria
    expect(page.get_by_text("Women - Dress Products")).to_be_visible()

    # Verifica que há produtos listados
    produtos = page.locator(".productinfo")
    assert produtos.count() > 0, "Nenhum produto encontrado na categoria Women - Dress"


def test_busca_de_produto(pagina_produtos: Page):
    """
    Testa a funcionalidade de busca de produtos.
    IA sugeriu testar tanto o campo de busca quanto a verificação dos resultados.
    """
    page = pagina_produtos

    # Preenche o campo de busca
    page.locator('input[id="search_product"]').fill("top")

    # Clica no botão de busca
    page.locator('button[id="submit_search"]').click()

    # Verifica título da página de resultados
    expect(page.get_by_text("Searched Products")).to_be_visible()

    # Verifica que retornou pelo menos um resultado
    resultados = page.locator(".productinfo")
    assert resultados.count() > 0, "A busca por 'top' não retornou produtos"


def test_detalhes_de_produto(pagina_produtos: Page):
    """
    Testa a página de detalhes de um produto específico.
    IA sugeriu verificar: nome, preço, categoria, condição e disponibilidade.
    """
    page = pagina_produtos

    # Clica em "View Product" do primeiro produto
    page.locator("a[href='/product_details/1']").click()

    # Verifica URL
    expect(page).to_have_url(f"{BASE_URL}/product_details/1")

    # Verifica que os elementos essenciais do produto estão visíveis
    expect(page.locator(".product-information h2")).to_be_visible()   # Nome
    expect(page.get_by_text("Category:")).to_be_visible()             # Categoria
    expect(page.get_by_text("Availability:")).to_be_visible()         # Disponibilidade
    expect(page.get_by_text("Condition:")).to_be_visible()            # Condição
    expect(page.get_by_text("Brand:")).to_be_visible()                # Marca
