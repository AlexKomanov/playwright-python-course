from playwright.sync_api import Page, expect


def test_playwright_python_docs(page: Page):
    page.goto("https://playwright.dev/python/")
    page.locator('[class="navbar__item navbar__link"]', has_text='API').click()
    expect(page).to_have_url('https://playwright.dev/python/docs/api/class-playwright')
    page.wait_for_timeout(2000)


def test_playwright_python_api(page: Page):
    page.goto("https://playwright.dev/python/")
    page.get_by_role(role='link', name='Docs33333333').click(timeout=5000)
    expect(page).to_have_url('https://playwright.dev/python/docs/intro')
    page.wait_for_timeout(2000)
