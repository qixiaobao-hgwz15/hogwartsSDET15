from selenium.webdriver.common.by import By

from xueqiu_dome.farme.basepage import BasePage
from xueqiu_dome.farme.market_page import Market


class MainPage(BasePage):

    def goto_market(self):

        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']").click()

        return Market(self.driver)
