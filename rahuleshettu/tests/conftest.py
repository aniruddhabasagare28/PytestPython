import pytest
from playwright.sync_api import Page


@pytest.fixture
def driver(page: Page) -> Page:
    return page

