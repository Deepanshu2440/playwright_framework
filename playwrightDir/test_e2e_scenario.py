import time

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from pageObjects.orderDashboard import OrderDashboard
from pageObjects.orderHistotyPage import OrderHistoryPage
from pageObjects.orderDetailPage import OrderDetailPage
from utils.readJSON import read_json
from utils.apiBase import ApiUtils

credentials = read_json('credentials.json', "user_credentials")

# now lets say we have many login to do so we can make our dunction run in parameterize way so that it will run with different id one by one
@pytest.mark.parametrize('credentials', credentials)
@pytest.mark.smoke
def test_ui_validation(playwright: Playwright, page, credentials):
    # creating order via api
    order = ApiUtils().apiCreateOrder(playwright, credentials)

    # //login via ui
    LoginPage(page).login(credentials)
    # page.goto('https://rahulshettyacademy.com/client/')
    # page.get_by_placeholder('email@example.com').fill(credentials['username'])
    # page.get_by_placeholder('enter your passsword').fill(credentials['password'])
    # page.get_by_role('button').click()
    # //check if order placed via api
    OrderDashboard(page).dashboard(order)
    # page.get_by_role('button', name='  ORDERS').click()
    # expect(page.get_by_text(order)).to_be_visible()
    OrderHistoryPage(page).history(order)
    # page.locator(".tr").filter(has_text=order)
    # page.get_by_role('button', name='VIEW').nth(0).click()
    OrderDetailPage(page).verify()
    # expect(page.get_by_text('Thank you for Shopping With Us')).to_be_visible()



# //to run all tests via cli
#  pytest - for all
#  pystest -s - with logs
#  pystes -m smoke - with markers
#  pyetst -k  web_ui -- with matching keyword

# PARALELL EXECUTION
  # pyetst -n 3 - parallel execution -- pip install pytest-xdist
