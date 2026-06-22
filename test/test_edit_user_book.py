from selenium.webdriver.common.by import By
from pages.users_page import UserPage
from test.data.test_cases import EDIT_USERS_PARAMETRIZE
import pytest



@pytest.mark.parametrize('user_param',EDIT_USERS_PARAMETRIZE)
def test_edit_user(authorized_browser, user_param):
    user_page = UserPage(authorized_browser)
    user_page.select_edit_address_book_entry()
    user_page.add_address_book_entry(user_param)
    user_page.button_click_edit_update_address_book_entry()