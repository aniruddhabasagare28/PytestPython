import json
import time

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import new_context

from page_objects.login import LoginPage
from page_objects.dashboard import dashboard
from utils.apiBase import APIUtils

with open('playwright/data/credentials.json') as f:
    credentials = json.load(f)
    print(credentials)
    user_credentials_list = credentials['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, user_credentials):
    user_name = user_credentials["username"]
    user_password = user_credentials["password"]

    browse = playwright.chromium.launch(headless=False)
    context = browse.new_context()
    page = context.new_page()

    # Orders page -> order is present
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    loginpage = LoginPage(page)

    # login
    loginpage.navigate_to_login_page()
    dashboard_page = loginpage.login_page(user_name, user_password)

    orderHistoryPage = dashboard_page.navigate_to_order()
    orderDetailsPage = orderHistoryPage.selectOrder(order_id)

    orderDetailsPage.verifyOrderMessage()
    context.close()

