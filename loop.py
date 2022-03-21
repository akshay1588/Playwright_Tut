from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #page.goto('https://www.reddit.com/r/climbing/top/?t=all', timeout=0)
    page.goto('https://smartwebby.com/PHP/Phptips2.asp')

    locator=page.locator('input[name="chkexpert[]"]')
    locator.click().nth(2)
    #locator.check(force= True)


    '''all_links = page.locator('.styled-outbound-link')
    num_of_links = all_links.count()
    print(num_of_links)
    for i in range(0,num_of_links):
        page.wait_for_load_state(0)
        curr_link= all_links.nth(i+0)
        curr_link.wait_for()
        curr_link.click(force=True)
        #all_links.nth(i+0).wait_for().click(force=True)'''

    browser.close()