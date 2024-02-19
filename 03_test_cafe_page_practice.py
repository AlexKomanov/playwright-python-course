from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])

    page = browser.new_page(no_viewport=True)

    page.goto("https://devexpress.github.io/testcafe/example/")

    my_name = "Alex"

    input_your_name_element = page.locator("[id='developer-name']")
    input_your_name_element.clear()
    input_your_name_element.press_sequentially("alexander", delay=500)
    input_your_name_element.fill(my_name)

    support_testing_checkbox = page.get_by_test_id("remote-testing-checkbox")
    support_testing_checkbox.check()

    mac_os_radio = page.locator('[data-testid="macos-radio"]')
    mac_os_radio.click()

    i_tried_test_cafe = page.get_by_test_id('tried-testcafe-checkbox')
    i_tried_test_cafe.check()

    page.get_by_test_id('comments-area').fill("My custom comment")
    page.get_by_role(role="button", name="Submit").click()

    expect(page).to_have_title('Thank you!')
    expect(page).to_have_url('https://devexpress.github.io/testcafe/example/thank-you.html')

    thank_you_header = page.get_by_test_id('thank-you-header')
    expect(thank_you_header).to_contain_text(my_name)

    browser.close()
