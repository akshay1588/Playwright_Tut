from playwright.sync_api import sync_playwright
from reddit_helpers import element_text
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
    locator = page.frame_locator("#iframeResult").locator("#vehicle1")
    locator.click()
    page.wait_for_timeout(1000)
    browser.close()