from selenium.webdriver.common.by import By
from test.data.test_cases import EDIT_GROUP_PARAMETRIZE
from pages.group_page import AddGroupPage
import pytest
import time


@pytest.mark.parametrize('cread_group', EDIT_GROUP_PARAMETRIZE)
        
def test_edit_group(authorized_browser, cread_group):
    group_page = AddGroupPage(authorized_browser)
    group_page.open_group_page()
    group_page.select_group()
    group_page.button_edit_group()
    group_page.input_parameters_groups(cread_group)
    group_page.button_update_group()
       
    