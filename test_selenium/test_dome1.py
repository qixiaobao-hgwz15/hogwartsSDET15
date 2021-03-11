import selenium
from selenium import webdriver


def test_driver():
    driver=webdriver.Firefox()
    driver.get("https://www.baidu.com")