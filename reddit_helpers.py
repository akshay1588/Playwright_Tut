def web_page(p, url): # p is just a random variable for page
    p.goto(url)

def pop_up(g): #page.locator.click(), #page has a method called locator which returns a locator object, the locator object has a method called click
    g.click()

def web_url(p):
    print(p.url)

def refresh_page(p):
    p.reload()

def select_selector(p, selector):
    locator = p.locator(selector)
    locator.click()

def say_hello():
    print('Hello')

say_hello()

def two_sum(n1,n2):
    print(n1+n2)

two_sum(11,10)

def your_name(n):
    print('Your name is: ',n)

your_name('Akshay')
