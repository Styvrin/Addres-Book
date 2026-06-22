import pytest
from selenium import webdriver
from pages.base_page import BasePage
import allure

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture()
def authorized_browser(browser):
    URL='http://localhost/addressbook/'
    Admin = "admin"
    Login = "secret"
    with allure.step("Open and authorization"):
        base_page = BasePage(browser)
        base_page.open_browser(URL)
        base_page.authorization(Admin,Login)
        base_page.check_authorization()
    return browser
