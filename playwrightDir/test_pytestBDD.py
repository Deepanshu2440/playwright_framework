from pytest_bdd import given, when, then, scenarios, parsers
import pytest

from pageObjects.login import LoginPage
from pageObjects.orderDashboard import OrderDashboard
from pageObjects.orderDetailPage import OrderDetailPage
from pageObjects.orderHistotyPage import OrderHistoryPage
from utils.apiBase import ApiUtils
from playwright.sync_api import Playwright


@pytest.fixture(scope='function')
def shared_data():
    return {}


scenarios('feature/orderTransaction.feature')


@given(parsers.parse('place the order with {username} and {password}'))
def place_item_order(playwright: Playwright, username, password, shared_data):
    credentials = {'username': username, 'password': password}
    order = ApiUtils().apiCreateOrder(playwright, credentials)
    shared_data['orderId'] = order


@given('the user is on landing page')
def landing_page(page, shared_data):
    page.goto('https://rahulshettyacademy.com/client/')
    shared_data['page'] = page
    print(shared_data)


@when(parsers.parse('I login with {username} and {password}'))
def login(username, password, shared_data):
    page = shared_data['page']
    credentials = {'username': username, 'password': password}
    page = LoginPage(page).login(credentials)
    shared_data['page'] = page


@when('navigate to order page')
def navigate_to_dashboard(shared_data):
    order = shared_data['orderId']
    page = shared_data['page']
    page = OrderDashboard(page).dashboard(order)
    shared_data['page'] = page

@when('select orderId')
def select_order(shared_data):
    page = shared_data['page']
    order = shared_data['orderId']
    page = OrderHistoryPage(page).history(order)
    shared_data['page'] = page

@then('order message is successfully displayed')
def verify(shared_data):
    page = shared_data['page']
    OrderDetailPage(page).verify()



