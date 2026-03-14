import json
import time
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import new_context

from page_objects.login import LoginPage
from page_objects.dashboard import dashboard
from utils.apiFrameworkBase import APIUtils

BASE_DIR = Path(__file__).resolve().parent
credentials_path = BASE_DIR / "data" / "credentials.json"

with open(credentials_path) as f:
    credentials = json.load(f)
    print(credentials)
    user_credentials_list = credentials['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):
    user_name = user_credentials["username"]
    user_password = user_credentials["password"]

    # Orders page -> order is present
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    loginpage = LoginPage(browserInstance)

    # login
    loginpage.navigate_to_login_page()
    dashboard_page = loginpage.login_page(user_name, user_password)
    orderHistoryPage = dashboard_page.navigate_to_order()
    orderDetailsPage = orderHistoryPage.selectOrder(order_id)

    orderDetailsPage.verifyOrderMessage()

