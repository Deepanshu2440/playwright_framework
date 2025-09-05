import pytest
from playwright.sync_api import Playwright


# //these is used for pytest parameterize thing , passing the parameters like a fixture in test fn
@pytest.fixture(scope='session')
def credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser: chrome/firefox"
    )

@pytest.fixture
def page(playwright : Playwright, request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    else:
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()