from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])

    page = browser.new_page(no_viewport=True)

    page.goto("https://playwright.dev/python/")

    list_of_locators = page.locator('[class="navbar__item navbar__link"]').all()
    print(page.locator('[class="navbar__item navbar__link"]').count())
    print(len(list_of_locators))

    # page.locator('[class="navbar__item navbar__link"]').click()  # Error: strict mode violation
    # list_of_locators[1].click()  # Python solution
    # page.locator('[class="navbar__item navbar__link"]').nth(1).click()
    page.get_by_role(role="link", name="API").click()
    # data-uitestingname="loginbutton"

    page.wait_for_timeout(2000)




    page.screenshot(path="screenshot.jpg")
    page.screenshot(path="full_screenshot.jpg", full_page=True)

    print(f"{page.title() = }")
    print(f"{page.url = }")

    # expect(page).to_have_url('https://playwright.dev/python/docs/intro', timeout=20000)
    # expect(page).not_to_have_url('https://playwright.dev/python')
    # expect(page).to_have_title('Installation | Playwright Python') # async with waiting mechanism
    # # assert page.title() == 'Installation | Playwright Python' # sync without waiting mechanism
    # browser.close()
