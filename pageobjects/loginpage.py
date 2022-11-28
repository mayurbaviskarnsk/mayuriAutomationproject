from selenium import webdriver
class Loginpage:
    textbox_username_id ="Email"
    textbox_password_id ="Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext ="Logout"

    def _init_ (self,driver):
        self.driver = driver
    def setusernmae(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath("//button[normalize-space()='Log in']").click()

    def clicklogout(self):
        self.driver.find_element_by_linktext("Logout").click()