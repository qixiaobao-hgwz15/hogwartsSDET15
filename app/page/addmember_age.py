
# 手动输如添加
# from app.page.contacadd_page import ContacAddPage
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def contactAdd(self):
        self.find(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        from app.page.contacadd_page import ContacAddPage
        return ContacAddPage(self.driver)

    def get_toast(self):
        result=self.find(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        return result