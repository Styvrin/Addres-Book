from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import allure

class BasePage:
    def __init__(self,browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    
            
    def open_browser(self, URL):
        with allure.step("Open URL avtoriztom"):
            self.browser.get(URL)
    
    def authorization(self,Admin,Login):
        with allure.step("authorization  "):
            self.find((By.NAME, 'user')).send_keys(Admin)
            self.find((By.NAME, 'pass')).send_keys(Login)
            self.find((By.CSS_SELECTOR, "input[value='Login']")).click()
           
            
    
    def check_authorization(self):
        with allure.step("check login_name: 'admin'"):
                assert self.find((By.XPATH, "//b[contains(text(), 'admin')]"))
    

    def open_group_page(self):
        with allure.step('Open page Group'):
            self.find((By.XPATH, "//a[@href='group.php']")).click()

    def button_add_user(self):
        with allure.step("Open panel add user"):
            self.find((By.XPATH, "//a[@href='edit.php']")).click()

    