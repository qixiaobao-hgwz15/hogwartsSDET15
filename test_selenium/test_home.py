from selenium import webdriver
from time import sleep

class TestHome():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_home(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_css_selector(".topic-22621 .title > a").click()

