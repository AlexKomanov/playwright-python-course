from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])

    page = browser.new_page(no_viewport=True)

    page.goto("https://playwright.dev/python/")

    # page.get_by_text("GET STARTED").click(timeout=3000)
    page.locator('[class="getStarted_Sjon"]').click(timeout=3000)

    page.screenshot(path="screenshot.jpg")
    page.screenshot(path="full_screenshot.jpg", full_page=True)

    print(f"{page.title() = }")
    print(f"{page.url = }")

    expect(page).to_have_url('https://playwright.dev/python/docs/intro', timeout=20000)
    expect(page).not_to_have_url('https://playwright.dev/python')
    expect(page).to_have_title('Installation | Playwright Python') # async with waiting mechanism
    # assert page.title() == 'Installation | Playwright Python' # sync without waiting mechanism
    browser.close()
