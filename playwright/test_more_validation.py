import time

from playwright.sync_api import Page, expect


def test_ui_cheks(page:Page):
    #Hide / display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()



def test_handle_alert(page: Page):

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator("#confirmbtn").click()

def test_handle_frame(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers!")

def test_handle_table(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            column_value = index
            break
    row_value = page.locator("tr").filter(has_text="Rice")
    expect(row_value.locator("td").nth(column_value)).to_have_text("37")