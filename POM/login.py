import pytest
from selenium import webdriver

class Login():

        _username="username"
        _password="password"
        _login_button="//input[@type='submit']"
        _your_project="//*[contains(text(), 'Your project (O)')]"

        def __init__(self):
            global driver
            driver=webdriver.Firefox()


        def login_to_account(self):
            driver.get("https://pypi.org/account/login/")
            driver.find_element_by_id(self._username).send_keys("govind3011")
            driver.find_element_by_id(self._password).send_keys("goving@3011")
            driver.find_element_by_xpath(self._login_button).click()
            print("login sucessfull")

        def verify_login(self):
            return driver.find_element_by_xpath(self._your_project).is_displayed()