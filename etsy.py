from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    page.goto("https://www.etsy.com/")
    page.click('.select-signin')

    page.fill('#join_neu_email_field', 'dohod50129@nitynote.com')
    page.fill('#join_neu_password_field', 'test1234')
    page.click("label[for='persisent']")
    #page.click("button[type='submit']").nth(10)
    page.click('button[name="submit_attempt"]')
    #with page.expect_navigation():
    locator=page.locator("text='Outdoor & Garden'").nth(1) #using nth(1) because first title 'outdoor and garden' is hidden
    print(locator)
    locator.click()
    #page.click('text="Sign in"')
    print(page.url)
    page.wait_for_timeout(1000)
    browser.close()