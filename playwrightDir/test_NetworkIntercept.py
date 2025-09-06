import time

import pytest
from playwright.sync_api import Page, expect, Playwright

from utils.readJSON import read_json
from utils.apiBase import ApiUtils

data_to_mock = {"data": [], "message": "No Orders"}


def intercept_network(route):
    route.fulfill(json=data_to_mock)


def intercept_network_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=68b73ddcf669d6cb0aaf0729")


def test_NetworkIntercept(page: Page):
    page.goto('https://rahulshettyacademy.com/client/')

    # * here is used as a wild card
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*', intercept_network)
    page.get_by_placeholder('email@example.com').fill('deep1@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('Deep@1234')
    page.get_by_role('button').click()
    page.get_by_role('button', name='  ORDERS').click()
    expect(page.get_by_text(' You have No Orders to show at this time.')).to_be_visible()

# here using fullfill we intercepted the response which we getting
# now using continue we intercept the request (url) itself


def test_NetworkIntercept_response(page: Page):
    page.goto('https://rahulshettyacademy.com/client/')

    # * here is used as a wild card
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*', intercept_network_request)
    page.get_by_placeholder('email@example.com').fill('deep1@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('Deep@1234')
    page.get_by_role('button').click()
    page.get_by_role('button', name='  ORDERS').click()
    page.get_by_role('button', name='  View').first.click()
    print(page.locator(".blink_me").text_content())

credentials = read_json('credentials.json', "user_credentials_single")
# now we are directly accessing local storage via playwright in browser to overpass login
@pytest.mark.smoke
def test_NetworkIntercept_localStorage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    token = ApiUtils().apiLogin(playwright,credentials)
    print(token)
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")


    page.goto('https://rahulshettyacademy.com/client')

    # //skipping login as interacting with browser using js
    # page.get_by_placeholder('email@example.com').fill('deep1@gmail.com')
    # page.get_by_placeholder('enter your passsword').fill('Deep@1234')
    page.get_by_role('button', name='  ORDERS').click()
    page.get_by_role('button', name='  View').first.click()
