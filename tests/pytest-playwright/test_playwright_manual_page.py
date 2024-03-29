import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture(scope='function')
def setup(playwright: Playwright) -> Page:
    # browser = playwright.chromium.launch(headless=True, slow_mo=500, args=["--start-maximized"])
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    page = browser.new_page()

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
