from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.amazon.com/
    page.goto("https://www.amazon.com/")
    # Click #nav-flyout-ya-signin >> text=Sign in
    page.locator("#nav-flyout-ya-signin >> text=Sign in").click()
    # assert page.url == "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
    # Click input[name="email"]
    emailInputLocator=page.locator("input[name=\"email\"]")
    emailInputLocator.wait_for(timeout=5000, state="attached")
    emailInputLocator.click()
    emailInputLocator.fill("user@email.com")
    emailInputLocator.press("Enter")


    # assert page.url == "https://www.amazon.com/ap/signin"
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("Amazon2018")
    # Press Enter
    # with page.expect_navigation(url="https://www.amazon.com/?ref_=nav_signin&"):
    with page.expect_navigation():
        page.locator("input[name=\"password\"]").press("Enter")
    # ---------------------
    context.close()
    browser.close()

    
with sync_playwright() as playwright:
    run(playwright)