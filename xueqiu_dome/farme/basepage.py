from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list=[(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    _error_num=0
    _max_num=3
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "aaaa"
            caps["appActivity"] = ".common.MainActivity"
            caps["appPackage"] = "com.xueqiu.android"
            caps["noReset"] = "True"

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver
    def find(self,by,locator=None):
        try:
            if locator is None:
                # 传递的是一个元素，只有一个by，黑名单，元组
                result= self.driver.find_element(*by)
            else:
                # 如果传入的是两个元素，by  locator
                result=self.driver.find_element(by,locator)
            self._error_num=0
            return result
        except Exception as e:
            if self._error_num>self._max_num:
                raise e
            self._error_num+=1
            for black_ele in self._black_list:
                ele=self.driver.find_elements(*black_ele)
                if len(ele)>0:
                    ele[0].click()
                    return self.find(by,locator)
            # 元素不在黑名单直接抛出异常
            raise e


