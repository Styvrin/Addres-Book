from selenium.webdriver.common.by import By
from pages.users_page import UserPage
from test.data.test_cases import ADD_USERS_PARAMETRIZE
import pytest
import time


@pytest.mark.parametrize('user_param',ADD_USERS_PARAMETRIZE)
def test_add_user(authorized_browser, user_param):
    user_page = UserPage(authorized_browser)
    user_page.button_add_user()
    user_page.add_address_book_entry(user_param)
    user_page.select_add_user_group()
    user_page.button_click_add_address_book_entry()
    
   
   
    
  
