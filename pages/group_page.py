from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure



class AddGroupPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    
    def click_new_group_button(self):
        with allure.step("Open panel group"):
            self.find((By.NAME, 'new')).click()
    
    
    def input_parameters_groups(self, cread_group):
        text_fields ={
            'group_name': 'group',
            'group_header': 'horr',
            'group_footer': 'comment'
        }

        for field_name, attr_name in text_fields.items():
            with allure.step(field_name):
                element = self.find((By.NAME, field_name))
                element.clear()
                value = getattr(cread_group, attr_name, '')
                if value:
                    element.send_keys(str(value))
            
    
    def click_add_button (self):
        with allure.step("Button click Enter"):

            self.find((By.CSS_SELECTOR, "input[value='Enter information']")).click()

    def select_group(self):
        with allure.step("Select group"):

            self.find((By.XPATH, "(//input[@name='selected[]'])[1]")).click()
        
        
    def click_delete_group_button(self):

        with allure.step("button deletr group"):

            self.find((By.NAME, 'delete')).click()

    def button_edit_group(self):

        with allure.step("Button edit group"):

            self.find((By.NAME, 'edit')).click()

    def button_update_group(self):

        with allure.step("Button update group"): 
               
            self.find((By.CSS_SELECTOR, "input[value='Update']")).click()

   