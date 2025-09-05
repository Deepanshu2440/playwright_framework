import time

from playwright.async_api import Page
from playwright.sync_api import expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.udemy.com/course/playwright-python-automation-testing-pytest/learn/lecture/46551437#overview')


# chrominum headless mode , 1 single context can be chnaged in configuration
def test_playwrightBasicsCut(page):
    page.goto('https://www.udemy.com/course/playwright-python-automation-testing-pytest')

def test_getLocators(page:Page):
    page.goto('https://www.saucedemo.com/v1/')
    # page.get_by_placeholder('Username').fill('standard_user')
    page.locator('#user-name').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_role('button').click()


def test_getLocators_dummy_site(page:Page):
    page.goto('https://rahulshettyacademy.com/client/#/auth/login')
    page.get_by_placeholder('email@example.com').fill('deep1@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('Deep@1234')
    page.get_by_role('button').click()

    # expect(page.get_by_text('Incorrect email or password.')).to_be_visible()
    add_cart1 = page.locator('.card').filter(has_text='ZARA COAT 3')
    add_cart2 = page.locator('.card').filter(has_text='ADIDAS ORIGINAL')
    add_cart1.get_by_text(' Add To Cart').click()
    add_cart2.get_by_text(' Add To Cart').click()
    page.get_by_role('button',name='  Cart ').nth(0).click()

    expect(page.get_by_role('button',name='Buy Now')).to_have_count(2)
    time.sleep(2)

