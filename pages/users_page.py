from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import allure


class UserPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def add_address_book_entry(self, user_param):
        with allure.step("add address book entry parameters"):
            self._fill_text_fields(user_param)
            self._fill_birthday_fields(user_param)
            self._fill_anniversary_fields(user_param)

    def _fill_text_fields(self, user_param):
        text_fields = {
            'firstname': 'first_name',
            'middlename': 'middle_name',
            'lastname': 'last_name',
            'nickname': 'nickname',
            'title': 'title',
            'company': 'company',
            'address': 'address',
            'home': 'home',
            'mobile': 'mobile',
            'work': 'work',
            'email': 'email1',
            'email2': 'email2',
            'email3': 'email3',
            'homepage': 'homepage',
            'byear': 'age__birtday',
            'ayear': 'age_anniversary'
        }
        
        for field_name, attr_name in text_fields.items():
            with allure.step(field_name):
                element = self.find((By.NAME, field_name))
                element.clear()
                value = getattr(user_param, attr_name, '')
                if value:
                    element.send_keys(str(value))

    def _fill_birthday_fields(self, user_param):
        with allure.step("Birthday"):
            self._select_dropdown('bday', user_param.day_birtday)
            self._select_dropdown('bmonth', user_param.month_birtday)

    def _fill_anniversary_fields(self, user_param):
        with allure.step("Anniversary"):
            self._select_dropdown('aday', user_param.day_anniversary)
            self._select_dropdown('amonth', user_param.month_anniversary)

    def _select_dropdown(self, field_name, value):
        dropdown = Select(self.find((By.NAME, field_name)))
        if value:
            dropdown.select_by_value(value)
        else:
            dropdown.select_by_index(0)

    def select_add_user_group(self):
        with allure.step("Select group"):

            select_group = Select(self.find((By.NAME, "new_group")))
            options_count = len(select_group.options)

            if options_count > 1:
                select_group.select_by_index(1)  
            else:
                select_group.select_by_index(0)
                            
                        
             
    def button_click_add_address_book_entry(self):
        with allure.step("Click button 'Enter'"):
            self.find((By.CSS_SELECTOR, "input[value='Enter']")).click()

    def select_edit_address_book_entry(self):
        with allure.step("Click checkbox edit"):
            self.find((By.XPATH, "//img[@title='Edit']")).click()

    def button_click_edit_update_address_book_entry(self):
        with allure.step("Click button 'Enter'"):
            self.find((By.CSS_SELECTOR, "input[value='Update']")).click()
    
  