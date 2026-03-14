import pytest


@pytest.fixture(scope="session")   #Module, function , calss
def user_credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="take the argument from user to execute test case on which browser - by default it will be chrome"  # registration of command argument
    )


@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")   #request is global fixture provided by playwright , it can be used to read the command line arguments

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()