from selenium.webdriver.common.by import By
from pages.group_page import AddGroupPage




def test_del_group(authorized_browser):
    group_page = AddGroupPage(authorized_browser)
    group_page.open_group_page()
    group_page.select_group()
    group_page.click_delete_group_button()
    