'''from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #page.goto("https://www.wikipedia.org/")'''

def test_hover(page):
    page.goto("https://playwright.dev/")
    page.locator(".navbar__item", has_text='Node.js').hover()
    page.click('text="Python"')