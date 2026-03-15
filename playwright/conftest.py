import pytest
import os


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
    browser_name = (browser_name or "").strip()
    if browser_name in {"", "$browser_name", "${browser_name}", "%browser_name%"}:
        browser_name = (
            os.getenv("browser_name")
            or os.getenv("BROWSER_NAME")
            or "chrome"
        )

    browser_name = browser_name.lower()
    headless = bool(os.getenv("CI") or os.getenv("JENKINS_URL"))

    if browser_name in {"chrome", "chromium", "edge"}:
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    else:
        raise pytest.UsageError(
            f"Unsupported --browser_name value '{browser_name}'. Use chrome or firefox."
        )

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
