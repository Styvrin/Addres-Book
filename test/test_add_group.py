from selenium.webdriver.common.by import By
from pages.group_page import AddGroupPage
from test.data.test_cases import ADD_GROUP_PARAMETRIZE
import pytest


@pytest.mark.parametrize('cread_group',ADD_GROUP_PARAMETRIZE)
def test_add_group(authorized_browser, cread_group):
    group_page = AddGroupPage(authorized_browser)
    group_page.open_group_page()
    group_page.click_new_group_button()
    group_page.input_parameters_groups(cread_group)
    group_page.click_add_button()
    
    
  
