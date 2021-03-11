from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Testwait:

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(3)
    def test_wait(self):
        self.driver.find_element(By.ID,'kw').send_keys("你好啊然")
        self.driver.find_element(By.ID,'su').click()
