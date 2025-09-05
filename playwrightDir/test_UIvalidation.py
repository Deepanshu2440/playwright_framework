import os
import time

import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope='function')
def test_ui_validation(page: Page):
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
    return page

# //for new page child window use EXPECT_POPUP()
def test_ChildPage(test_ui_validation:Page):
    page = test_ui_validation
    with page.expect_popup() as child_page:
        page.get_by_text('London QA Meetup @Rahul Shetty - Limited Seats! Book Now!').click()

    child_page = child_page.value

    # for getting value from text
    text = child_page.locator('.hero_heading').text_content()
    print(text)
    name = text.split('Focused ')
    print(name[1].split(' ')[0])

    expect(child_page.get_by_text('Welcome to the Career-Focused Software Testing Meetup')).to_be_visible()

def test_UiChecks(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.get_by_role('button', name='Hide').click()
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()
    page.get_by_role('button', name='Show').click()

    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role('button', name='Alert').click()
    path = os.path.join(os.getcwd(), "screenshot.png")
    page.screenshot(path=path)
    page.get_by_role('button', name='Hide').click()
    page.get_by_role('button', name='Confirm').click()
    frame = page.frame_locator('#courses-iframe')
    frame.get_by_role('link', name='All Access plan').click()
    expect(frame.get_by_text('Happy Subscibers!')).to_be_visible()

    page.get_by_role('button', name='Mouse Hover').hover()
    page.get_by_role('link', name='Reload').click()
    time.sleep(5)
    print(111)


def test_UiChecks1(page:Page):
    page.goto('https://demo.automationtesting.in/Alerts.html')

    # page.on("dialog", lambda dialog: dialog.accept())
    page.once("dialog", lambda dialog: (print("Dialog message:", dialog.message), dialog.accept()))

    page.get_by_role('button').click()
    page.get_by_role('button').filter(has_text='click the button to display an  alert box:').click()
    time.sleep(2)
    page.get_by_text('Alert with OK & Cancel ').click()
    page.once("dialog", lambda dialog: (print("Dialog message:", dialog.message), dialog.dismiss()))
    page.get_by_role('button').filter(has_text='click the button to display a confirm box').click()
    expect(page.get_by_text('You pressed Cancel')).to_be_visible()














