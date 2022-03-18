from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #page.goto("https://www.wikipedia.org/")
    #page.goto("https://playwright.dev/")
    #page.locator(".navbar__item", has_text='Node.js').hover()

    page.goto("https://www.amazon.com/Prime-Video/b?node=2676882011")

    page.locator("#nav-link-accountList", has_text='Account & Lists').hover()
    page.click('text="Find a List or Registry"')
    page.wait_for_load_state()
    #page.type('#searchInput', 'Cricket')
    #page.fill('input#searchInput', 'Cricket')
    #page.click("button[type=submit]")

    #locator=page.locator('text="bat-and-ball game"').nth(0)
    #locator.click()
    print(page.url)
    page.wait_for_timeout(1000)
    #def hoverAndClick(page,selector):



    browser.close()