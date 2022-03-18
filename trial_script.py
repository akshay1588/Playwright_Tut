from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://danube-webshop.herokuapp.com/")
    page.screenshot(path="example.png")
    #page.click('text=Sign Up')
    #page.type('[placeholder="Name"]', 'John')
    #page.fill('#s-surname', 'May')
    #page.fill("#s-email", "user@email.com")
    #page.fill('#s-password2', 'test1234')
    #page.click('#myself')
    #page.click('#privacy-policy')

    #page.click('text=REGISTER')

    #page.type()
    page.click(('#login'))
    page.type('[placeholder="Email"]',"user@email.com")
    if page.locator('[placeholder="Email"]')== "user@email.com":
        print('Continue')
    else:
        print('Wrong email address entered')

    page.type('#n-password2', 'test1234')
    page.click('#goto-signin-btn')

    #page.click('//*[@id="goto-signin-btn"]')
    #page.click('text=Sign In')
    #page.cl
    #page.pause()
    locator = page.locator('text="Sci-Fi"').nth(0)
    locator.click()
    page.wait_for_timeout(1000)
    print(page.url)
    browser.close()