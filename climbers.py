from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    page.goto('https://www.reddit.com/r/climbing/')
    locate = page.locator('a[href="/r/climbing/top/"]').nth(1)
    locate.click()

    locate1= page.locator('button[role="menuitem"]').nth(1)
    locate1.click()

    locate2 = page.locator('a[href="/r/climbing/top/?t=all"]')
    locate2.click()

    with page.expect_popup() as popup_info:
        locate3 = page.locator('a[href="https://www.battleforthenet.com/"]').nth(1)
        locate3.click()

        popup = popup_info.value

        page.bring_to_front()
        popup.wait_for_load_state()
        print(popup.title())

        popup.bring_to_front()

    page.wait_for_timeout(2000)
    print(page.url)
    browser.close()
