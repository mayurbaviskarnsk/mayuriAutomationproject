from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\PycharmProjects\\pythonProjectnopcommerceapp\\chromedriver_win32 (1)")
    return driver

