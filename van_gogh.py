from playwright.sync_api import sync_playwright
from reddit_helpers import element_text
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://en.wikipedia.org/wiki/Vincent_van_Gogh")
    #locator= page.locator('a[href="/wiki/Van_Gogh_(disambiguation)"]')

    for i in range(0,28):
        locator = page.locator('a').nth(i+0)
        element_text(locator)

    '''for i in range(0,2):
        locator=page.locator('.mw-jump-link').nth(i+0)
        element_text(locator)

    for i in range(0,2):
        locator = page.locator('.mw-disambig').nth(i+0)
        #locator.click()
        element_text(locator)

    curr_link = page.locator('a[title$="name"]')
    tot= curr_link.count()

    for i in range(0,tot):
        locator= page.locator('a[title$="name"]').nth(i+0)
        element_text(locator)

    new_link = page.locator('div[style="display:inline"]')
    total= new_link.count()
    #print(total)
    for i in range(0,total):
        locator= page.locator('div[style="display:inline"]').nth(i+0)
        element_text(locator)

    links = page.locator('.infobox-data')
    numbers= links.count()

    for i in range(0,numbers):
        locator=page.locator('.infobox-data').nth(i+0)
        element_text(locator)'''

    page.locator('a[href="/wiki/Self-Portrait"]', has_text='Self-Portrait').hover()
    page.wait_for_timeout(2000)
    browser.close()