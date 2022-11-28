import pytest
import unittest
from selenium import webdriver
import socket
from pageobjects.loginpage import Loginpage
from selenium.common.exceptions import InvalidSessionIdException

class Test_001_loginpage:
    baseURL ="https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password ="admin"

    def test_homePageTitle(self,setup):
        self.driver =setup
        print("Current session is {}".format(setup.session_id))
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        # if act_title=="Your store. Login":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot("C:\\Users\\hp\\PycharmProjects\\pythonProjectnopcommerceapp\\screenshots.py" + "test_homePageTitle.png")
        #     self.driver.close()
        #     assert False

        def test_login(self, setup):
            self.driver = setup
            print("Current session is {}".format(setup.session_id))
            self.driver.get(self.baseURL)
            self.lp.loginpage(self.driver)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.ClickLogin()
            act_title = self.driver.title
        self.driver.close()
        if act_title =="Dashboard //nopcommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\hp\\PycharmProjects\\pythonProjectnopcommerceapp\\screenshots.py" + "test_login.png")
            self.driver.close()
            assert False
