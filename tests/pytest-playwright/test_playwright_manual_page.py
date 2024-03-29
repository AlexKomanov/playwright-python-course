import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture(scope='function')
def setup(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)

    page.goto("https://playwright.dev/python/")

    return page


def test_playwright_python_docs(setup):
    page = setup
    page.locator('[class="navbar__item navbar__link"]', has_text='API').click()
    page.wait_for_timeout(3000)


def test_playwright_python_api(setup):
    page = setup
    page.get_by_role(role='link', name='Docs').click()

    page.wait_for_timeout(3000)
