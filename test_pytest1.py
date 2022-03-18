# test_my_application.py
def test_example_is_working(page):
    page.goto("https://www.google.com/")
    print(page.title())
    #assert page.inner_text('h1') == 'Example Domain'
    #page.click("text=More information")

#def test_sign_in():