from playwright.sync_api import sync_playwright
from reddit_helpers import web_page, pop_up
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    web_page(page,'https:reddit.com/r/soccer')
    #page.goto('https:reddit.com/r/soccer')
    #page.locator('button[aria-label="Play"]').nth(0).click()
    #page.wait_for_load_state()
    with page.expect_popup() as popup_info:
        g = page.locator('text="The laws of the game"')
        pop_up(g)
        #page.click('text="The laws of the game"')
    popup = popup_info.value

    popup.wait_for_load_state()
    print(popup.title())

    page.bring_to_front()
    #with page.expect_navigation(url="https:reddit.com/r/soccer"):
    page.locator('a[href="/t/sports/"]').click()
    with page.expect_popup() as new_popup_info:
        g = page.locator('.styled-outbound-link').nth(0)
        pop_up(g)
        #pop_up(page, '.styled-outbound-link'.nth(0))


        new_popup = new_popup_info.value
        new_popup.wait_for_load_state()
        print(new_popup.title())
        print(page.url)
    browser.close()