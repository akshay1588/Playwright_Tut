from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #HW1
    #page.goto("https://www.wikipedia.org/")
    '''page.fill("#searchInput", 'Cricket')
    page.click('button[type="submit"]')
    page.click('text="Eden Gardens"')'''
    #HW2
    page.goto("https://playwright.dev/") #page1
    #print(page.title())
    #page.click('.header-github-link') #New page. page#2
    #page.context.wait_for_event(page)
    # Get popup after a specific action (e.g., click)
    with page.expect_popup() as popup_info:
        page.click('.header-github-link')
    popup = popup_info.value

    popup.wait_for_load_state()
    print(popup.title())

    #new_window=window.value
    #page.is_visible()
    #print(page.title())
    #HW3
    '''page.goto('https://danube-webshop.herokuapp.com/')
    page.click('text="Celsius 233"')
    #page.click('text="Add to cart"')
    page.screenshot(path='cart.png')
    locator=page.locator('button.call-to-action').nth(1)
    locator.click()'''
    #HW 4
    '''page.goto('https://www.google.com')
    print(page.title())
    if page.title()=='Google':
        print('True')
    else:
        print('False')'''
    #page.fill("input[name=\"q\"]", 'cats')
    #page.fill("input[title=\"Search\"]", 'cats')
    #page.locator("[aria-label=\"Search\"]").press("Enter") #Another selector
    #locator=page.locator('text="Google Search"').nth(0)

    #locator.click()

    #loc1=page.locator("a[href^='/search?q=cats&source=lnms&tbm']").nth(0)
    #loc1=page.locator('text="Images"')
    #loc1.click()
    page.wait_for_load_state()
    #page.wait_for_timeout(2000)
    '''page.screenshot(path='cats.png')
    print(page.url)
    if page.url=='https://www.google.co.in':
        print('Wrong URL')
    else:
        print('Right URL')'''
    browser.close()