from rahuleshettu.page_objects.login_practice_page import LoginPracticePage


def test_loginpage_practice_sign_in(driver):
    login_page = LoginPracticePage(driver)

    login_page.navigate_to_login_page()
    login_page.login_with_terms(
        "rahulshettyacademy",
        "Learning@830$3mK2",
    )

    assert "shop" in driver.url
