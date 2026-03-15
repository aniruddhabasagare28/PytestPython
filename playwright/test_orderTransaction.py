import pytest
from pytest_bdd import given, parsers, then, when, scenarios

from utils.apiFrameworkBase import APIUtils

from page_objects.login import LoginPage

scenarios("../playwright/features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("Place the item order with {username} and {password}"))
def step_impl(username, password, playwright, shared_data):
    user_credentials = {"username": username, "password": password}
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)
    shared_data["order_id"] = order_id

@given("User is on landing page")
def step_impl(browserInstance, shared_data):
    loginpage = LoginPage(browserInstance)
    loginpage.navigate_to_login_page()
    shared_data["login_page"] = loginpage

@when(parsers.parse("I login to portal with {username} and {password}"))
def step_impl(username, password, shared_data):
    loginpage = shared_data["login_page"]
    dashboard_page = loginpage.login_page(username, password)
    shared_data["dashboard_page"] = dashboard_page

@when("Navigate to order page")
def step_impl(shared_data):
    dashboard_page = shared_data["dashboard_page"]
    orderHistoryPage = dashboard_page.navigate_to_order()
    shared_data["orderHistoryPage"] = orderHistoryPage

@when("Select the order")
def step_impl(shared_data):
    orderHistoryPage = shared_data["orderHistoryPage"]
    order_id = shared_data["order_id"]
    orderDetailsPage = orderHistoryPage.selectOrder(order_id)
    shared_data["orderDetailsPage"] = orderDetailsPage


@then("Verify order message is successfully displayed")
def step_impl(shared_data):
    orderDetailsPage = shared_data["orderDetailsPage"]
    orderDetailsPage.verifyOrderMessage()
